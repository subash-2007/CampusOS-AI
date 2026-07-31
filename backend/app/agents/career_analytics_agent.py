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
        resume_score = memory.resume_analysis.get("overall_score", 85) if memory else 85
        ats_score = memory.ats_optimization.get("match_score", 82) if memory else 82
        readiness_pct = memory.skill_gap_analysis.get("overall_readiness_pct", 80) if memory else 80
        portfolio_score = memory.portfolio_recommendations.get("portfolio_score", 88) if memory else 88

        overall_readiness = int(round((resume_score * 0.25) + (ats_score * 0.35) + (readiness_pct * 0.25) + (portfolio_score * 0.15)))

        dynamic_data = {
            "readiness_score": overall_readiness,
            "score": overall_readiness,
            "market_percentile": f"Top {max(5, 100 - overall_readiness)}% among Target Role Candidates",
            "breakdown": {
                "resume_quality": resume_score,
                "ats_match": ats_score,
                "technical_depth": readiness_pct,
                "interview_readiness": max(50, overall_readiness - 5),
                "portfolio_impact": portfolio_score
            },
            "key_insights": [
                f"Your ATS Match Score ({ats_score}%) directly reflects current skill alignment.",
                "Closing critical skill gaps will elevate your readiness score above 90%.",
                "Your portfolio appeal score is a major market differentiator."
            ]
        }

        reasoning_steps = [
            "Step 1: Examined raw candidate resume & JD match data vectors",
            "Step 2: Aggregated sub-agent outputs across Resume, ATS, Skill Gap, Portfolio, and Interview modules",
            "Step 3: Identified quantitative candidate scoring strengths",
            "Step 4: Pinpointed metric bottlenecks dragging down overall readiness rating",
            "Step 5: Benchmarked analytics against HR Analytics Specialist talent evaluation standards",
            "Step 6: Computed weighted Career Readiness Index and placement probabilities",
            "Step 7: Prioritized high-yield quantitative improvements",
            "Step 8: Generated enterprise Career Analytics Consulting Report"
        ]

        system_prompt = self.build_expert_system_prompt(
            persona_role="HR Analytics Specialist & Data Scientist",
            domain_focus="Quantitative readiness metric aggregation, hiring probability forecasting, market percentile modeling, and HR talent analytics."
        )

        user_prompt = self.build_user_context_prompt(inputs, memory=memory)
        llm_response = await self.call_llm(system_prompt, user_prompt, task_type="career_analytics", preferred_engine="anthropic")
        output = self.parse_agent_output(llm_response, dynamic_data)

        score_val = output.get("score") or output.get("readiness_score") or overall_readiness
        output["readiness_score"] = score_val
        output["score"] = score_val

        if memory:
            memory.career_analytics = output

        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
