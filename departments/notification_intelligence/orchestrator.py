from app.agents.base_agent import BaseAgent
from departments.notification_intelligence.deterministic import NotificationEffectivenessScorerAgent
from departments.notification_intelligence.reasoning import StrategicNotificationNarrativeAgent, NotificationOptimizationPlannerAgent
from departments.notification_intelligence.schemas import NotificationIntelligenceOrchestratorReport, ReasoningNotificationPipelineResult

class NotificationIntelligenceOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Notification Intelligence Department."""
    def __init__(self):
        super().__init__(agent_id="notification_intelligence_orchestrator", name="Notification Intelligence Master Orchestrator",
                         description="Coordinates all 9 notification intelligence sub-agents.", icon="Bell")
        self.scorer = NotificationEffectivenessScorerAgent()
        self.narrative_agent = StrategicNotificationNarrativeAgent()
        self.optimization_planner = NotificationOptimizationPlannerAgent()

    async def run_pipeline(self, open_rate: float = 34.0) -> NotificationIntelligenceOrchestratorReport:
        steps = ["Step 1: Running deterministic Notification pipeline (email, push, timing, frequency, SMS, personalization)."]
        det = self.scorer.run(open_rate)
        steps.append("Step 2: Executing Strategic Notification Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Notification Optimization Planner Agent.")
        optimization = await self.optimization_planner.plan_optimization(det)
        steps.append("Step 4: Compiling Notification Intelligence Master Report.")
        tier = "HIGH ENGAGEMENT NOTIFICATIONS" if det.notification_effectiveness_score >= 60 else "STANDARD NOTIFICATIONS"
        return NotificationIntelligenceOrchestratorReport(
            notification_tier=tier,
            notification_effectiveness_score=det.notification_effectiveness_score,
            confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningNotificationPipelineResult(narrative=narrative, optimization_plan=optimization, reasoning_steps=steps),
            reasoning_steps=steps
        )
