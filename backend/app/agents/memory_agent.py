from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent

class MemoryAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="memory_personalization",
            name="Memory & Personalization Agent",
            description="Maintains candidate memory state, career trajectory history, preferences, and personalized learning context.",
            icon="Database"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[Any] = None) -> Dict[str, Any]:
        reasoning_steps = [
            "Retrieved session memory & persistent profile state",
            "Updated skill mastery timeline and candidate target role context",
            "Synthesized personalized adaptive context for platform agents"
        ]

        candidate_skills = memory.get_candidate_skills() if memory else ["Python", "TypeScript", "REST APIs"]
        target_role = memory.get_target_role() if memory else "Software Engineer"
        missing_skills = memory.get_missing_skills() if memory else ["Cloud Infrastructure"]

        dynamic_data = {
            "user_profile_summary": f"Candidate targeting {target_role} with active skills in {', '.join(candidate_skills[:4])}.",
            "remembered_skills": candidate_skills,
            "career_goals": [f"Target Role: {target_role}", "Build Scalable Cloud Applications"],
            "personalized_tips": [
                f"Highlight {candidate_skills[0]} projects when reaching out to recruiters",
                f"Focus learning efforts on {missing_skills[0]} to close core skill gap"
            ],
            "last_updated": "Just now"
        }

        system_prompt = (
            "You are a Memory & Personalization Manager. Return JSON with keys: "
            "'user_profile_summary' (str), 'remembered_skills' (list), 'career_goals' (list), "
            "'personalized_tips' (list), 'last_updated' (str)."
        )
        user_prompt = f"Dynamic Memory Data:\n{dynamic_data}"
        llm_response = await self.call_llm(system_prompt, user_prompt)

        output = self.parse_json_safely(llm_response, dynamic_data)
        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
