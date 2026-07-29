from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent

class CareerRoadmapAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="career_roadmap",
            name="Career Roadmap Agent",
            description="Generates personalized 30-60-90 day strategic career roadmaps and salary growth trajectories.",
            icon="Compass"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[Any] = None) -> Dict[str, Any]:
        target_role = memory.target_role if memory else "Software Engineer"
        missing_skills = memory.get_missing_skills() if memory else []

        reasoning_steps = [
            "Evaluated candidate readiness score and target role trajectory",
            "Synthesized 30-60-90 day milestone strategic execution plan"
        ]

        dynamic_fallback = {
            "overall_readiness": 85,
            "plan_30_days": f"Master missing core skills ({', '.join(missing_skills[:2]) if missing_skills else 'Cloud & Containerization'}) and optimize resume ATS keyword match.",
            "plan_60_days": f"Build and deploy full-stack production application to AWS/GCP and publish open-source GitHub repository.",
            "plan_90_days": f"Execute targeted recruiter cold outreach, complete technical interview loops, and negotiate job offers for {target_role}."
        }

        system_prompt = (
            "You are an Executive Career Strategist. Generate a 30-60-90 day strategic execution plan. "
            "Return JSON ONLY with keys:\n"
            "- 'overall_readiness': int (0-100)\n"
            "- 'plan_30_days': str (Focus for first 30 days)\n"
            "- 'plan_60_days': str (Focus for 31-60 days)\n"
            "- 'plan_90_days': str (Focus for 61-90 days)"
        )

        user_prompt = f"Target Role: {target_role}\nIdentified Gaps: {missing_skills}"
        llm_response = await self.call_llm(system_prompt, user_prompt)
        output = self.parse_json_safely(llm_response, dynamic_fallback)

        if memory:
            memory.career_roadmap = output

        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
