from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from app.nlp import analyze_resume_dynamically

class ResumeIntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="resume_intelligence",
            name="Resume Intelligence Agent",
            description="Evaluates resume structure, impact metrics, action verb density, and domain appropriateness.",
            icon="FileText"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[Any] = None) -> Dict[str, Any]:
        resume_text = inputs.get("resume_text", "") or (memory.resume_text if memory else "")
        
        reasoning_steps = [
            "Parsed raw resume document text and sections",
            "Audited quantitative metrics density & action verb strength dynamically",
            "Calculated Resume Quality Score & extracted technical skills"
        ]

        # 1. Deterministic Local Dynamic Analysis
        dynamic_data = analyze_resume_dynamically(resume_text)

        # 2. LLM Optional Enhancement
        system_prompt = (
            "You are an expert Resume Intelligence Analyst. Polish the resume audit findings into JSON format with keys: "
            "'overall_score' (int), 'impact_score' (int), 'formatting_score' (int), 'strengths' (list), "
            "'weaknesses' (list), 'improvements' (list), 'action_verb_rating' (str)."
        )
        user_prompt = f"Resume Content:\n{resume_text}\nDynamic Analysis Metrics:\n{dynamic_data}"
        llm_response = await self.call_llm(system_prompt, user_prompt)

        output = self.parse_json_safely(llm_response, dynamic_data)
        
        # Enforce deterministic scores from dynamic engine
        output["overall_score"] = dynamic_data["overall_score"]
        output["impact_score"] = dynamic_data["impact_score"]
        output["formatting_score"] = dynamic_data["formatting_score"]
        output["extracted_skills"] = dynamic_data["extracted_skills"]

        if memory:
            memory.resume_analysis = output
            memory.log_step(self.agent_id, "Completed dynamic resume analysis", {"score": output["overall_score"]})

        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
