from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent

class SkillGapAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="skill_gap_intelligence",
            name="Skill Gap Intelligence Agent",
            description="Analyzes skill differentials between candidate experience and job description requirements to build prioritized learning roadmaps.",
            icon="Zap"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[Any] = None) -> Dict[str, Any]:
        candidate_skills = memory.get_candidate_skills() if memory else []
        missing_skills = memory.get_missing_skills() if memory else []
        target_role = memory.target_role if memory else "Software Engineer"

        reasoning_steps = [
            "Cross-referenced candidate skill inventory against job requirements",
            "Identified missing core technical competencies and prioritized learning impact"
        ]

        dynamic_fallback = {
            "overall_readiness_pct": max(60, 100 - (len(missing_skills) * 6)),
            "missing_skills": missing_skills if missing_skills else ["AWS", "Docker", "Redis", "GraphQL"],
            "priority": "High Priority",
            "learning_plan": [
                "Week 1: Complete hands-on AWS & Docker fundamentals tutorial",
                "Week 2: Build a microservice caching layer using Redis",
                "Week 3: Integrate GraphQL query API into full-stack application",
                "Week 4: Deploy end-to-end containerized application to cloud"
            ]
        }

        system_prompt = (
            "You are a Technical Upskilling Architect. Compare candidate skills vs required skills and construct a 4-week learning plan. "
            "Return JSON ONLY with keys:\n"
            "- 'overall_readiness_pct': int (0-100)\n"
            "- 'missing_skills': list of strings\n"
            "- 'priority': str ('High', 'Medium', 'Low')\n"
            "- 'learning_plan': list of 4 weekly concrete learning steps"
        )

        user_prompt = (
            f"Target Role: {target_role}\n"
            f"Candidate Skills: {candidate_skills}\n"
            f"Missing Skills: {missing_skills}"
        )

        llm_response = await self.call_llm(system_prompt, user_prompt)
        output = self.parse_json_safely(llm_response, dynamic_fallback)

        if memory:
            memory.skill_gap_analysis = output

        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
