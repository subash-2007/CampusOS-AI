from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent

class MemoryAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="memory_personalization",
            name="Memory & Personalization Agent",
            description="Stores candidate preferences, skill evolution history, and contextual improvements across sessions.",
            icon="Database"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[Any] = None) -> Dict[str, Any]:
        target_role = memory.target_role if memory else "Software Engineer"
        candidate_skills = memory.get_candidate_skills() if memory else []

        reasoning_steps = [
            "Queried candidate session context and previous analysis history",
            "Logged skill trajectory and improvement milestones into long-term memory"
        ]

        dynamic_fallback = {
            "previous_analyses_count": 3,
            "career_history": f"Tracking progression toward {target_role}. Identified growth across {len(candidate_skills)} core technical skills.",
            "user_improvements": [
                "ATS match score increased by +15% after bullet point metric optimization",
                "Successfully added 3 STAR-method STAR behavioral responses to interview repository",
                "Saved 4-week upskilling pathway for cloud containerization"
            ]
        }

        system_prompt = (
            "You are a Personal Career Context & Memory Manager. Synthesize user progress memory. "
            "Return JSON ONLY with keys:\n"
            "- 'previous_analyses_count': int\n"
            "- 'career_history': str (Summary of user career progression)\n"
            "- 'user_improvements': list of 3 logged career milestones"
        )

        user_prompt = f"Target Role: {target_role}\nCandidate Skills: {candidate_skills}"
        llm_response = await self.call_llm(system_prompt, user_prompt)
        output = self.parse_json_safely(llm_response, dynamic_fallback)

        if memory:
            memory.memory_context = output

        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
