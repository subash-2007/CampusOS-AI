from app.agents.base_agent import BaseAgent
from departments.analytics_intelligence.deterministic import AnalyticsHealthScorerAgent
from departments.analytics_intelligence.reasoning import StrategicAnalyticsNarrativeAgent, GrowthOptimizationPlannerAgent
from departments.analytics_intelligence.schemas import AnalyticsIntelligenceOrchestratorReport, ReasoningAnalyticsPipelineResult

class AnalyticsIntelligenceOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Analytics Intelligence Department."""
    def __init__(self):
        super().__init__(agent_id="analytics_intelligence_orchestrator", name="Analytics Intelligence Master Orchestrator",
                         description="Coordinates all 9 analytics intelligence sub-agents.", icon="PieChart")
        self.scorer = AnalyticsHealthScorerAgent()
        self.narrative_agent = StrategicAnalyticsNarrativeAgent()
        self.growth_planner = GrowthOptimizationPlannerAgent()

    async def run_pipeline(self, dau_mau: float = 0.42) -> AnalyticsIntelligenceOrchestratorReport:
        steps = ["Step 1: Running deterministic Analytics pipeline (engagement, funnel, retention, event tracking, A/B tests, dashboards)."]
        det = self.scorer.run(dau_mau)
        steps.append("Step 2: Executing Strategic Analytics Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Growth Optimization Planner Agent.")
        growth = await self.growth_planner.plan_growth(det)
        steps.append("Step 4: Compiling Analytics Intelligence Master Report.")
        tier = "ENTERPRISE ANALYTICS" if det.analytics_health_score >= 55 else "BASIC ANALYTICS"
        return AnalyticsIntelligenceOrchestratorReport(
            analytics_tier=tier, analytics_health_score=det.analytics_health_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningAnalyticsPipelineResult(narrative=narrative, growth_plan=growth, reasoning_steps=steps),
            reasoning_steps=steps
        )
