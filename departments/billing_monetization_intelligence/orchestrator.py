from app.agents.base_agent import BaseAgent
from departments.billing_monetization_intelligence.deterministic import BillingHealthScorerAgent
from departments.billing_monetization_intelligence.reasoning import StrategicBillingNarrativeAgent, MonetizationOptimizationPlannerAgent
from departments.billing_monetization_intelligence.schemas import BillingMonetizationOrchestratorReport, ReasoningBillingPipelineResult

class BillingMonetizationOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Billing & Monetization Intelligence Department."""
    def __init__(self):
        super().__init__(agent_id="billing_monetization_orchestrator", name="Billing & Monetization Intelligence Master Orchestrator",
                         description="Coordinates all 9 billing and monetization sub-agents.", icon="CreditCard")
        self.scorer = BillingHealthScorerAgent()
        self.narrative_agent = StrategicBillingNarrativeAgent()
        self.monetization_planner = MonetizationOptimizationPlannerAgent()

    async def run_pipeline(self, mrr: float = 48500.0) -> BillingMonetizationOrchestratorReport:
        steps = ["Step 1: Running deterministic Billing pipeline (MRR/ARR, churn, LTV/CAC, gateway webhooks, pricing tiers, invoice tax compliance)."]
        det = self.scorer.run(mrr)
        steps.append("Step 2: Executing Strategic Billing Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Monetization Optimization Planner Agent.")
        monetization = await self.monetization_planner.plan_monetization(det)
        steps.append("Step 4: Compiling Billing & Monetization Intelligence Master Report.")
        tier = "HIGH GROWTH MONETIZATION" if det.billing_health_score >= 80 else "STANDARD BILLING"
        return BillingMonetizationOrchestratorReport(
            billing_tier=tier, billing_health_score=det.billing_health_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningBillingPipelineResult(narrative=narrative, monetization_plan=monetization, reasoning_steps=steps),
            reasoning_steps=steps
        )
