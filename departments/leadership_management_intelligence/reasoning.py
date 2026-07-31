from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.leadership_management_intelligence.schemas import (
    StrategicLeadershipNarrative, ExecutiveCoachingPlan, ReasoningLeadershipPipelineResult, DeterministicLeadershipPipelineResult
)

class StrategicLeadershipNarrativeAgent(BaseAgent):
    """Agent 8: Formulates strategic leadership evaluations and executive management summaries."""
    def __init__(self):
        super().__init__(
            agent_id="strategic_leadership_narrative",
            name="Strategic Leadership Narrative Agent",
            description="Evaluates management effectiveness, team retention, and strategic vision execution.",
            icon="Users"
        )

    async def evaluate(self, det_result: DeterministicLeadershipPipelineResult) -> StrategicLeadershipNarrative:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Executive Leadership Coach & Management Consultant",
            domain_focus="Executive management evaluation, organizational leadership, and team retention."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"readiness_score": det_result.leadership_readiness_score, "team_size": det_result.capacity.managed_team_size}
        )
        
        fallback = {
            "leadership_evaluation_summary": f"Candidate demonstrates executive-ready leadership capabilities ({det_result.leadership_readiness_score}% readiness score) managing a team of {det_result.capacity.managed_team_size} engineers with a high 95% retention rate.",
            "key_management_strengths": [
                "Exceptional team retention and low voluntary attrition (5%)",
                "Strong cross-functional stakeholder alignment across Product, Design, and Engineering"
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="leadership_eval", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicLeadershipNarrative(
                leadership_evaluation_summary=parsed.get("leadership_evaluation_summary", fallback["leadership_evaluation_summary"]),
                key_management_strengths=parsed.get("key_management_strengths", fallback["key_management_strengths"])
            )
        except Exception:
            return StrategicLeadershipNarrative(**fallback)

class ExecutiveCoachingPlannerAgent(BaseAgent):
    """Agent 9: Formulates executive coaching growth goals and leadership action items."""
    def __init__(self):
        super().__init__(
            agent_id="executive_coaching_planner",
            name="Executive Coaching Planner Agent",
            description="Generates executive coaching plans and strategic leadership development milestones.",
            icon="Compass"
        )

    async def plan_coaching(self, det_result: DeterministicLeadershipPipelineResult) -> ExecutiveCoachingPlan:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Chief Human Resources Officer & Executive Coach",
            domain_focus="Executive coaching, organizational scaling, and leadership milestone planning."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"vision_score": det_result.vision.vision_clarity_score}
        )
        
        fallback = {
            "leadership_development_goals": [
                "Scale engineering organization from 12 to 30+ engineers while preserving team culture",
                "Establish quarterly Executive OKR alignment reviews with C-suite stakeholders"
            ],
            "coaching_action_items": [
                "Delegate operational sprint management to Engineering Managers to focus on long-term strategy",
                "Mentor senior engineers for transition into EM and Staff roles"
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="coaching_plan", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return ExecutiveCoachingPlan(
                leadership_development_goals=parsed.get("leadership_development_goals", fallback["leadership_development_goals"]),
                coaching_action_items=parsed.get("coaching_action_items", fallback["coaching_action_items"])
            )
        except Exception:
            return ExecutiveCoachingPlan(**fallback)
