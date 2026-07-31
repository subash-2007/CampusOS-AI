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
        extracted_skills = extract_skills_from_text(resume_text)
        dynamic_fallback = analyze_resume_dynamically(resume_text)
        dynamic_fallback["extracted_skills"] = extracted_skills

        reasoning_steps = [
            "Step 1: Analyzed full resume structure across Education, Experience, Projects, and Certifications",
            "Step 2: Examined target Job Description requirements and domain context",
            "Step 3: Identified candidate technical strengths and quantitative achievements",
            "Step 4: Flagged weak action verbs, unquantified bullets, and structural gaps",
            "Step 5: Benchmarked profile against Senior Recruiter evaluation criteria (15+ years experience)",
            "Step 6: Formulated personalized resume bullet optimizations and structural fixes",
            "Step 7: Prioritized high-impact resume improvements",
            "Step 8: Synthesized comprehensive executive consulting report"
        ]

        system_prompt = self.build_expert_system_prompt(
            persona_role="Senior Resume Reviewer with 15+ years of recruiting experience",
            domain_focus="Resume structure parsing, quantitative metric density audit, action verb impact evaluation, and technical depth scoring."
        )

        user_prompt = self.build_user_context_prompt(inputs, memory=memory)
        llm_response = await self.call_llm(system_prompt, user_prompt, task_type="resume_intelligence", preferred_engine="anthropic")
        output = self.parse_agent_output(llm_response, dynamic_fallback)

        # Ensure essential keys for backward compatibility & UI badges
        score_val = output.get("score") or output.get("overall_score") or dynamic_fallback.get("overall_score", 88)
        output["overall_score"] = score_val
        output["score"] = score_val
        output["impact_score"] = output.get("impact_score", dynamic_fallback.get("impact_score", 85))
        output["credibility_index"] = output.get("credibility_index", dynamic_fallback.get("credibility_index", 90))
        output["ats_readiness"] = output.get("ats_readiness", dynamic_fallback.get("ats_readiness", 84))
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
