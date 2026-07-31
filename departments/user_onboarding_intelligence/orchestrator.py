from app.agents.base_agent import BaseAgent
from departments.user_onboarding_intelligence.deterministic import OnboardingQualityScorerAgent
from departments.user_onboarding_intelligence.reasoning import StrategicOnboardingNarrativeAgent, OnboardingImprovementPlannerAgent
from departments.user_onboarding_intelligence.schemas import UserOnboardingOrchestratorReport, ReasoningOnboardingPipelineResult

class UserOnboardingOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for User Onboarding Intelligence Department."""
    def __init__(self):
        super().__init__(agent_id="user_onboarding_orchestrator", name="User Onboarding Intelligence Master Orchestrator",
                         description="Coordinates all 9 onboarding intelligence sub-agents.", icon="UserPlus")
        self.scorer = OnboardingQualityScorerAgent()
        self.narrative_agent = StrategicOnboardingNarrativeAgent()
        self.improvement_planner = OnboardingImprovementPlannerAgent()

    async def run_pipeline(self, completion_pct: float = 76.0) -> UserOnboardingOrchestratorReport:
        steps = ["Step 1: Running deterministic Onboarding pipeline (completion, dropoff, first value, guided tour, personalization, NPS)."]
        det = self.scorer.run(completion_pct)
        steps.append("Step 2: Executing Strategic Onboarding Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Onboarding Improvement Planner Agent.")
        improvement = await self.improvement_planner.plan_improvement(det)
        steps.append("Step 4: Compiling User Onboarding Intelligence Master Report.")
        tier = "WORLD-CLASS ONBOARDING" if det.onboarding_quality_score >= 65 else "STANDARD ONBOARDING"
        return UserOnboardingOrchestratorReport(
            onboarding_tier=tier, onboarding_quality_score=det.onboarding_quality_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningOnboardingPipelineResult(narrative=narrative, improvement_plan=improvement, reasoning_steps=steps),
            reasoning_steps=steps
        )
