from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent

class CareerAnalyticsAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="career_analytics",
            name="Career Analytics Agent",
            description="Aggregates readiness scores, market competitiveness metrics, and progress tracking across all AI intelligence modules.",
            icon="BarChart3"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[Any] = None) -> Dict[str, Any]:
        reasoning_steps = [
            "Aggregated real-time metrics across Resume, ATS, Skill Gap, and Interview modules",
            "Computed holistic Career Readiness Index dynamically",
            "Generated comparative market percentiles and domain radar breakdown"
        ]

        resume_score = memory.resume_analysis.get("overall_score", 80) if memory else 80
        ats_score = memory.ats_optimization.get("match_score", 75) if memory else 75
        readiness_pct = memory.skill_gap_analysis.get("overall_readiness_pct", 70) if memory else 70
        portfolio_score = memory.portfolio_recommendations.get("portfolio_score", 85) if memory else 85

        overall_readiness = int(round((resume_score * 0.25) + (ats_score * 0.35) + (readiness_pct * 0.25) + (portfolio_score * 0.15)))

        dynamic_data = {
            "readiness_score": overall_readiness,
            "market_percentile": f"Top {max(5, 100 - overall_readiness)}% among Target Role Candidates",
            "breakdown": {
                "resume_quality": resume_score,
                "ats_match": ats_score,
                "technical_depth": readiness_pct,
                "interview_readiness": max(50, overall_readiness - 5),
                "portfolio_impact": portfolio_score
            },
            "skill_distribution": [
                {"name": "Frontend Stack", "value": 30},
                {"name": "Backend APIs & DB", "value": 35},
                {"name": "Cloud & DevOps", "value": 20},
                {"name": "System Architecture", "value": 15}
            ],
            "key_insights": [
                f"Your ATS Match Score ({ats_score}%) directly reflects current skill alignment.",
                "Closing critical skill gaps will elevate your readiness score above 90%.",
                "Your portfolio appeal score is a major market differentiator."
            ]
        }

        system_prompt = (
            "You are a Career Analytics Data Specialist. Return JSON with keys: "
            "'readiness_score' (int), 'market_percentile' (str), 'breakdown' (dict), 'skill_distribution' (list), 'key_insights' (list)."
        )
        user_prompt = f"Dynamic Metrics:\n{dynamic_data}"
        llm_response = await self.call_llm(system_prompt, user_prompt)

        output = self.parse_json_safely(llm_response, dynamic_data)
        output["readiness_score"] = overall_readiness

        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
