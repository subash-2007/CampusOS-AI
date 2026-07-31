from app.agents.base_agent import BaseAgent
from departments.procurement_vendor_contracts.deterministic import ProcurementVendorContractsScorerAgent
from departments.procurement_vendor_contracts.reasoning import StrategicProcurementNarrativeAgent, ProcurementOperationsPlannerAgent
from departments.procurement_vendor_contracts.schemas import ProcurementVendorContractsOrchestratorReport, ReasoningProcurementPipelineResult

class ProcurementVendorContractsOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Procurement Purchasing and Vendor Contracts Department."""
    def __init__(self):
        super().__init__(agent_id="procurement_vendor_contracts_orchestrator", name="Procurement Purchasing and Vendor Contracts Master Orchestrator",
                         description="Coordinates all 9 sub-agents for Procurement Purchasing and Vendor Contracts.", icon="Cpu")
        self.scorer = ProcurementVendorContractsScorerAgent()
        self.narrative_agent = StrategicProcurementNarrativeAgent()
        self.planner = ProcurementOperationsPlannerAgent()

    async def run_pipeline(self) -> ProcurementVendorContractsOrchestratorReport:
        steps = ["Step 1: Running deterministic pipeline."]
        det = self.scorer.run()
        steps.append("Step 2: Executing Strategic Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Operations Planner Agent.")
        plan = await self.planner.plan_operations(det)
        steps.append("Step 4: Compiling Master Orchestrator Report.")
        return ProcurementVendorContractsOrchestratorReport(
            tier="NATIONAL MODEL FOR STRATEGIC PROCUREMENT AND VENDOR DIVERSITY", procurement_score=det.procurement_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningProcurementPipelineResult(narrative=narrative, plan=plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
