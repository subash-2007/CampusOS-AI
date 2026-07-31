from app.agents.base_agent import BaseAgent
from departments.customer_support_success.deterministic import CustomerSupportScorerAgent
from departments.customer_support_success.reasoning import StrategicSupportNarrativeAgent, CustomerSuccessPlannerAgent
from departments.customer_support_success.schemas import CustomerSupportSuccessOrchestratorReport, ReasoningSupportPipelineResult

class CustomerSupportSuccessOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Customer Support & Success Intelligence Department."""
    def __init__(self):
        super().__init__(agent_id="customer_support_success_orchestrator", name="Customer Support & Success Intelligence Master Orchestrator",
                         description="Coordinates all 9 support and success sub-agents.", icon="Headphones")
        self.scorer = CustomerSupportScorerAgent()
        self.narrative_agent = StrategicSupportNarrativeAgent()
        self.success_planner = CustomerSuccessPlannerAgent()

    async def run_pipeline(self, response_time: float = 14.2) -> CustomerSupportSuccessOrchestratorReport:
        steps = ["Step 1: Running deterministic Support pipeline (first response time, CSAT, AI deflection, account health, channel volume, agent performance)."]
        det = self.scorer.run(response_time)
        steps.append("Step 2: Executing Strategic Support Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Customer Success Planner Agent.")
        success = await self.success_planner.plan_success(det)
        steps.append("Step 4: Compiling Customer Support & Success Intelligence Master Report.")
        tier = "WORLD CLASS CUSTOMER SUPPORT" if det.support_excellence_score >= 85 else "STANDARD SUPPORT"
        return CustomerSupportSuccessOrchestratorReport(
            support_tier=tier, support_excellence_score=det.support_excellence_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningSupportPipelineResult(narrative=narrative, success_plan=success, reasoning_steps=steps),
            reasoning_steps=steps
        )
