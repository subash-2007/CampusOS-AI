from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from app.nlp import analyze_resume_dynamically, extract_skills_from_text

class ResumeIntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="resume_intelligence",
            name="Resume Intelligence Agent",
            description="Parses resume structure, extracts technical skills, evaluates metric density, and calculates overall resume quality score.",
            icon="FileText"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[Any] = None) -> Dict[str, Any]:
        resume_text = inputs.get("resume_text", "") or (memory.resume_text if memory else "")
        user_profile = inputs.get("user_profile", {})

        reasoning_steps = [
            "Parsed document text across Education, Experience, Projects, and Skills",
            "Extracted candidate technical skills and quantitative metrics",
            "Evaluated structural impact and action verb density via LLM"
        ]

        dynamic_fallback = analyze_resume_dynamically(resume_text)
        extracted_skills = extract_skills_from_text(resume_text)
        dynamic_fallback["extracted_skills"] = extracted_skills

        system_prompt = (
            "You are an Expert Technical Recruiter & Resume Auditor. Analyze the provided resume text and user profile. "
            "Return JSON ONLY with keys:\n"
            "- 'overall_score': int (0-100)\n"
            "- 'impact_score': int (0-100)\n"
            "- 'credibility_index': int (0-100)\n"
            "- 'ats_readiness': int (0-100)\n"
            "- 'extracted_skills': list of strings\n"
            "- 'strengths': list of 3 specific strengths\n"
            "- 'weaknesses': list of 3 specific weaknesses or gaps\n"
            "- 'suggestions': list of 3 actionable bullet improvement tips"
        )

        user_prompt = (
            f"User Profile: {user_profile}\n"
            f"Resume Text:\n{resume_text}\n\n"
            f"Calculated Dynamic Benchmark:\n{dynamic_fallback}"
        )

        llm_response = await self.call_llm(system_prompt, user_prompt)
        output = self.parse_json_safely(llm_response, dynamic_fallback)

        # Standardize keys
        if "overall_score" not in output:
            output["overall_score"] = output.get("resume_score", dynamic_fallback["overall_score"])
        if "impact_score" not in output:
            output["impact_score"] = dynamic_fallback["impact_score"]
        if "credibility_index" not in output:
            output["credibility_index"] = dynamic_fallback["credibility_index"]
        if "ats_readiness" not in output:
            output["ats_readiness"] = dynamic_fallback["ats_readiness"]

        if not output.get("extracted_skills"):
            output["extracted_skills"] = extracted_skills

        if memory:
            memory.resume_analysis = output
            memory.candidate_skills = list(set(output.get("extracted_skills", []) + extracted_skills))

        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
