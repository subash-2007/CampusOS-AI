from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from app.nlp import compute_ats_optimization

class ATSOptimizationAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="ats_optimization",
            name="ATS Optimization Agent",
            description="Calculates ATS match percentage, extracts keyword gaps, and rewrites bullet points for maximum scanner pass rate.",
            icon="CheckCircle"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[Any] = None) -> Dict[str, Any]:
        resume_text = inputs.get("resume_text", "") or (memory.resume_text if memory else "")
        job_desc = inputs.get("job_description_text", "") or (memory.job_description_text if memory else "")

        reasoning_steps = [
            "Extracted keywords from target Job Description",
            "Executed TF-IDF Cosine Similarity & Jaccard overlap matrix",
            "Dynamically calculated ATS score and matched vs missing keyword lists"
        ]

        # 1. Deterministic Local Dynamic Matcher
        dynamic_data = compute_ats_optimization(resume_text, job_desc)

        # 2. LLM Optional Enhancement
        system_prompt = (
            "You are an ATS Scanner Expert. Refine ATS optimization findings into JSON with keys: "
            "'match_score' (int), 'ats_compatibility' (str), 'matched_keywords' (list), 'missing_keywords' (list), "
            "'formatting_warnings' (list), 'bullet_optimizations' (list of dicts with 'original' and 'optimized')."
        )
        user_prompt = f"Resume:\n{resume_text}\nJob Description:\n{job_desc}\nDynamic Match Results:\n{dynamic_data}"
        llm_response = await self.call_llm(system_prompt, user_prompt)

        output = self.parse_json_safely(llm_response, dynamic_data)

        # Enforce mathematical dynamic scores and extracted keyword sets
        output["match_score"] = dynamic_data["match_score"]
        output["matched_keywords"] = dynamic_data["matched_keywords"]
        output["missing_keywords"] = dynamic_data["missing_keywords"]

        if memory:
            memory.ats_optimization = output
            memory.log_step(self.agent_id, "Completed dynamic ATS optimization audit", {"match_score": output["match_score"]})

        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
