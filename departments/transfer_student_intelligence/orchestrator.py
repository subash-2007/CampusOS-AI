from app.agents.base_agent import BaseAgent
from departments.transfer_student_intelligence.deterministic import TransferStudentIntelligenceScorerAgent
from departments.transfer_student_intelligence.reasoning import StrategicTransferNarrativeAgent, TransferPathwayPlannerAgent
from departments.transfer_student_intelligence.schemas import TransferStudentIntelligenceOrchestratorReport, ReasoningTransferPipelineResult

class TransferStudentIntelligenceOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Transfer Student Intelligence Department."""
    def __init__(self):
        super().__init__(agent_id="transfer_student_intelligence_orchestrator", name="Transfer Student Intelligence Master Orchestrator",
                         description="Coordinates all 9 transfer student intelligence sub-agents.", icon="GitPullRequest")
        self.scorer = TransferStudentIntelligenceScorerAgent()
        self.narrative_agent = StrategicTransferNarrativeAgent()
        self.pathway_planner = TransferPathwayPlannerAgent()

    async def run_pipeline(self, agreements: int = 142) -> TransferStudentIntelligenceOrchestratorReport:
        steps = ["Step 1: Running deterministic Transfer Student Intelligence pipeline (articulation agreements, credit evaluation, GPA stability, orientation, housing & aid, graduation rates)."]
        det = self.scorer.run(agreements)
        steps.append("Step 2: Executing Strategic Transfer Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Transfer Pathway Planner Agent.")
        pathways = await self.pathway_planner.plan_pathways(det)
        steps.append("Step 4: Compiling Transfer Student Intelligence Master Report.")
        tier = "HIGH-EFFICIENCY ARTICULATION PATHWAY" if det.transfer_intelligence_score >= 85 else "STANDARD TRANSFER PATHWAY"
        return TransferStudentIntelligenceOrchestratorReport(
            transfer_tier=tier, transfer_intelligence_score=det.transfer_intelligence_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningTransferPipelineResult(narrative=narrative, pathway_plan=pathways, reasoning_steps=steps),
            reasoning_steps=steps
        )
