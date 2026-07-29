from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from app.nlp import compute_ats_optimization

class ATSOptimizationAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="ats_optimization",
            name="ATS Optimization Agent",
            description="Compares candidate resume against job description using AI semantic matching to determine ATS score, matched keywords, and missing keywords.",
            icon="CheckCircle"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[Any] = None) -> Dict[str, Any]:
        resume_text = inputs.get("resume_text", "") or (memory.resume_text if memory else "")
        jd_text = inputs.get("job_description_text", "") or (memory.job_description_text if memory else "")
        user_profile = inputs.get("user_profile", {})

        reasoning_steps = [
            "Extracted target job requirements and candidate skill vectors",
            "Executed AI-powered semantic similarity analysis against job description",
            "Identified exact matched vs missing domain keywords and ATS formatting suggestions"
        ]

        dynamic_fallback = compute_ats_optimization(resume_text, jd_text)
        
        system_prompt = (
            "You are a Senior ATS System Architect & Technical Screener. Perform an AI-powered semantic comparison between "
            "the candidate's resume and the target job description. Return JSON ONLY with keys:\n"
            "- 'ats_score': int (0-100 match percentage)\n"
            "- 'matched_keywords': list of strings (skills/tools in BOTH resume and JD)\n"
            "- 'missing_keywords': list of strings (critical skills in JD but MISSING from resume)\n"
            "- 'suggestions': list of 3 specific bullet point rewrites to increase ATS score"
        )

        user_prompt = (
            f"User Profile: {user_profile}\n"
            f"Resume Content:\n{resume_text}\n\n"
            f"Job Description Content:\n{jd_text}\n\n"
            f"Calculated Dynamic Benchmark:\n{dynamic_fallback}"
        )

        llm_response = await self.call_llm(system_prompt, user_prompt)
        output = self.parse_json_safely(llm_response, dynamic_fallback)

        # Standardize keys
        match_score = output.get("ats_score", output.get("match_score", dynamic_fallback.get("match_score", 78)))
        output["ats_score"] = match_score
        output["match_score"] = match_score

        if memory:
            memory.ats_optimization = output
            memory.matched_keywords = output.get("matched_keywords", [])
            memory.missing_keywords = output.get("missing_keywords", [])

        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
