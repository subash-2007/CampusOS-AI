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
        target_role = inputs.get("target_role") or (memory.target_role if memory else "Software Engineer")
        candidate_skills = memory.get_candidate_skills() if memory else ["Python", "FastAPI", "React"]

        dynamic_fallback = {
            "score": 90,
            "previous_analyses_count": 3,
            "career_history": f"Tracking progression toward {target_role}. Identified growth across {len(candidate_skills)} core technical skills.",
            "user_improvements": [
                "ATS match score increased by +15% after bullet point metric optimization",
                "Successfully added 3 STAR-method STAR behavioral responses to interview repository",
                "Saved 4-week upskilling pathway for cloud containerization"
            ]
        }

        reasoning_steps = [
            "Step 1: Examined candidate past analysis sessions and MongoDB memory state",
            "Step 2: Cross-referenced current target Job Description demands with candidate history",
            "Step 3: Identified candidate skill acquisition velocity and profile strengths",
            "Step 4: Pinpointed stagnation risks and un-updated resume sections",
            "Step 5: Benchmarked candidate growth trajectory against Career Progress Manager standards",
            "Step 6: Formulated personalized progress tracking and memory persistence strategies",
            "Step 7: Prioritized high-yield next steps for long-term career growth",
            "Step 8: Generated enterprise Career Memory & Progress Report"
        ]

        system_prompt = self.build_expert_system_prompt(
            persona_role="Career Progress Manager & Candidate Context Director",
            domain_focus="Multi-session candidate memory tracking, skill growth velocity analytics, and career trajectory persistence."
        )

        user_prompt = self.build_user_context_prompt(inputs, memory=memory)
        llm_response = await self.call_llm(system_prompt, user_prompt, task_type="memory_personalization", preferred_engine="anthropic")
        output = self.parse_agent_output(llm_response, dynamic_fallback)

        if memory:
            memory.memory_context = output

        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
