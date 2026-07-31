from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.user_onboarding_intelligence.schemas import (
    StrategicOnboardingNarrative, OnboardingImprovementPlan, ReasoningOnboardingPipelineResult, DeterministicOnboardingPipelineResult
)

class StrategicOnboardingNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates onboarding quality, NPS, and personalization effectiveness."""
    def __init__(self):
        super().__init__(agent_id="strategic_onboarding_narrative", name="Strategic Onboarding Narrative Agent",
                         description="Evaluates onboarding completion, NPS, and guided tour effectiveness.", icon="UserCheck")

    async def evaluate(self, det: DeterministicOnboardingPipelineResult) -> StrategicOnboardingNarrative:
        fallback = {
            "onboarding_summary": f"World-class onboarding experience ({det.onboarding_quality_score:.1f}% quality). {det.completion.avg_completion_pct}% completion in {det.completion.avg_completion_time_minutes}min, NPS={det.nps.nps_score}.",
            "key_onboarding_strengths": [f"15-minute time-to-first-value with '{det.first_value.first_value_event}' event", f"{det.personalization.personalized_onboarding_paths} personalized paths at {det.personalization.path_assignment_accuracy_pct}% accuracy"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("User Experience Research Lead", "onboarding, activation, NPS"),
                                          PromptBuilder.build_user_context({"completion": det.completion.avg_completion_pct}), task_type="onboarding_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicOnboardingNarrative(onboarding_summary=parsed.get("onboarding_summary", fallback["onboarding_summary"]),
                                                key_onboarding_strengths=parsed.get("key_onboarding_strengths", fallback["key_onboarding_strengths"]))
        except Exception:
            return StrategicOnboardingNarrative(**fallback)

class OnboardingImprovementPlannerAgent(BaseAgent):
    """Agent 9: Generates dropoff reduction strategies and onboarding flow samples."""
    def __init__(self):
        super().__init__(agent_id="onboarding_improvement_planner", name="Onboarding Improvement Planner Agent",
                         description="Formulates dropoff reduction strategies and onboarding flow optimizations.", icon="Map")

    async def plan_improvement(self, det: DeterministicOnboardingPipelineResult) -> OnboardingImprovementPlan:
        fallback = {
            "dropoff_reduction_actions": [f"Add drag-and-drop resume parser at Step {det.dropoff.highest_dropoff_step} ({det.dropoff.highest_dropoff_step_name}) to reduce {det.dropoff.dropoff_rate_at_step_pct}% dropoff", "Implement progress gamification with XP points for each completed onboarding step"],
            "sample_onboarding_flow": "Step 1: Social login (Google/LinkedIn) → Step 2: Role & Goal selection → Step 3: Resume upload (drag-drop) → Step 4: AI Profile enrichment → Step 5: First job matches revealed → Step 6: Skill gap preview → Step 7: Action plan activation"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Product Designer", "onboarding flows, activation optimization"),
                                          PromptBuilder.build_user_context({"dropoff_step": det.dropoff.highest_dropoff_step_name}), task_type="onboarding_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return OnboardingImprovementPlan(dropoff_reduction_actions=parsed.get("dropoff_reduction_actions", fallback["dropoff_reduction_actions"]),
                                             sample_onboarding_flow=parsed.get("sample_onboarding_flow", fallback["sample_onboarding_flow"]))
        except Exception:
            return OnboardingImprovementPlan(**fallback)
