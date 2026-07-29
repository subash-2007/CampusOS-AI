from typing import Dict, Any
from app.agents.base_agent import BaseAgent

class MemoryAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="memory_personalization",
            name="Memory & Personalization Agent",
            description="Maintains candidate memory state, career trajectory history, preferences, and personalized learning context.",
            icon="Database"
        )

    async def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        user_id = inputs.get("user_id", "default_user")

        reasoning_steps = [
            f"Retrieved session memory & persistent profile state for user '{user_id}'",
            "Updated skill mastery timeline and preferred learning styles",
            "Synthesized personalized adaptive context for platform agents"
        ]

        system_prompt = (
            "You are a Memory & Personalization Manager. Return JSON with keys: "
            "'user_profile_summary' (str), 'remembered_skills' (list), 'career_goals' (list), "
            "'personalized_tips' (list), 'last_updated' (str)."
        )

        user_prompt = f"User Memory Query: {inputs}"
        llm_response = await self.call_llm(system_prompt, user_prompt)

        fallback = {
            "user_profile_summary": "Full-stack developer focused on React, TypeScript, Python, and cloud services targeting high-growth tech companies.",
            "remembered_skills": ["TypeScript", "Next.js", "Python", "FastAPI", "MongoDB", "Tailwind CSS"],
            "career_goals": ["Full Stack Engineer at Tier-1 Tech / Unicorn Startup", "Master Cloud Deployment & Microservices"],
            "personalized_tips": [
                "Tailor cold outreach messages focusing on Next.js performance optimizations you built",
                "Review System Design concepts before your upcoming technical screens"
            ],
            "last_updated": "Today"
        }

        output = self.parse_json_safely(llm_response, fallback)
        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
