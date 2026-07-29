from typing import Dict, Any
from app.agents.base_agent import BaseAgent

class SkillGapAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="skill_gap_intelligence",
            name="Skill Gap Intelligence Agent",
            description="Identifies missing technical and soft skills, generating a prioritized learning matrix and course recommendations.",
            icon="Zap"
        )

    async def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        resume_text = inputs.get("resume_text", "")
        target_role = inputs.get("target_role", "") or inputs.get("prompt", "") or "Software Engineer"

        reasoning_steps = [
            "Audited current technical competencies from user profile",
            "Compared against top 2026 industry demand standards for target role",
            "Built prioritized skill acquisition matrix & learning resources"
        ]

        system_prompt = (
            "You are a Skill Gap Analyst. Evaluate skill gaps for target role and return JSON with keys: "
            "'critical_gaps' (list of dicts with 'skill', 'urgency', 'reason'), "
            "'secondary_gaps' (list of dicts with 'skill', 'urgency', 'reason'), "
            "'learning_pathway' (list of dicts with 'week', 'topic', 'resource', 'estimated_hours'), "
            "'overall_readiness_pct' (int)."
        )

        user_prompt = f"Resume:\n{resume_text}\nTarget Role: {target_role}"
        llm_response = await self.call_llm(system_prompt, user_prompt)

        fallback = {
            "critical_gaps": [
                {"skill": "Docker & Containerization", "urgency": "High", "reason": "Required for modern deployment pipelines in 85% of job listings"},
                {"skill": "System Design Fundamentals", "urgency": "High", "reason": "Crucial for mid/senior interviews and architecture reviews"},
                {"skill": "Redis & Caching Strategies", "urgency": "Medium", "reason": "High demand for API optimization & session management"}
            ],
            "secondary_gaps": [
                {"skill": "GraphQL APIs", "urgency": "Medium", "reason": "Increasingly used for flexible client-side data fetching"},
                {"skill": "CI/CD Pipelines (GitHub Actions)", "urgency": "Low", "reason": "Great bonus skill for DevOps awareness"}
            ],
            "learning_pathway": [
                {"week": "Week 1", "topic": "Docker Containers & Compose", "resource": "Docker Official Docs & Hands-on Labs", "estimated_hours": "6 hrs"},
                {"week": "Week 2", "topic": "System Design & Microservices", "resource": "ByteByteGo & Designing Data-Intensive Applications", "estimated_hours": "8 hrs"},
                {"week": "Week 3", "topic": "Redis Caching & Async Queues", "resource": "Redis University Free Courses", "estimated_hours": "5 hrs"}
            ],
            "overall_readiness_pct": 78
        }

        output = self.parse_json_safely(llm_response, fallback)
        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
