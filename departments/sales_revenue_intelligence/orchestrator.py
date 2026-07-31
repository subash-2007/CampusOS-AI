from app.agents.base_agent import BaseAgent
from departments.sales_revenue_intelligence.deterministic import SalesHealthScorerAgent
from departments.sales_revenue_intelligence.reasoning import StrategicSalesNarrativeAgent, RevenueGrowthPlannerAgent
from departments.sales_revenue_intelligence.schemas import SalesRevenueOrchestratorReport, ReasoningSalesPipelineResult

class SalesRevenueOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Sales & Revenue Intelligence Department."""
    def __init__(self):
        super().__init__(agent_id="sales_revenue_orchestrator", name="Sales & Revenue Intelligence Master Orchestrator",
                         description="Coordinates all 9 sales and revenue sub-agents.", icon="DollarSign")
        self.scorer = SalesHealthScorerAgent()
        self.narrative_agent = StrategicSalesNarrativeAgent()
        self.growth_planner = RevenueGrowthPlannerAgent()

    async def run_pipeline(self, pipeline_usd: float = 1450000.0) -> SalesRevenueOrchestratorReport:
        steps = ["Step 1: Running deterministic Sales pipeline (pipeline volume, lead conversion, sales cycle, win/loss, quota attainment, revenue forecast)."]
        det = self.scorer.run(pipeline_usd)
        steps.append("Step 2: Executing Strategic Sales Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Revenue Growth Planner Agent.")
        growth = await self.growth_planner.plan_growth(det)
        steps.append("Step 4: Compiling Sales & Revenue Intelligence Master Report.")
        tier = "HIGH PERFORMING SALES PIPELINE" if det.sales_health_score >= 80 else "STANDARD SALES PIPELINE"
        return SalesRevenueOrchestratorReport(
            sales_tier=tier, sales_health_score=det.sales_health_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningSalesPipelineResult(narrative=narrative, growth_plan=growth, reasoning_steps=steps),
            reasoning_steps=steps
        )
