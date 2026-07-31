from app.agents.base_agent import BaseAgent
from departments.registrar_academic_records.deterministic import RegistrarAcademicRecordsScorerAgent
from departments.registrar_academic_records.reasoning import StrategicRegistrarNarrativeAgent, RegistrarOperationsPlannerAgent
from departments.registrar_academic_records.schemas import RegistrarAcademicRecordsOrchestratorReport, ReasoningRegistrarPipelineResult

class RegistrarAcademicRecordsOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Registrar & Academic Records Department."""
    def __init__(self):
        super().__init__(agent_id="registrar_academic_records_orchestrator", name="Registrar & Academic Records Master Orchestrator",
                         description="Coordinates all 9 registrar & academic records sub-agents.", icon="FileText")
        self.scorer = RegistrarAcademicRecordsScorerAgent()
        self.narrative_agent = StrategicRegistrarNarrativeAgent()
        self.registrar_planner = RegistrarOperationsPlannerAgent()

    async def run_pipeline(self, peak_users: int = 8500) -> RegistrarAcademicRecordsOrchestratorReport:
        steps = ["Step 1: Running deterministic Registrar pipeline (registration uptime, Parchment transcripts, degree clearance, room scheduling, transfer credits, FERPA privacy)."]
        det = self.scorer.run(peak_users)
        steps.append("Step 2: Executing Strategic Registrar Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Registrar Operations Planner Agent.")
        registrar_plan = await self.registrar_planner.plan_registrar_operations(det)
        steps.append("Step 4: Compiling Registrar & Academic Records Master Report.")
        tier = "PREMIER DIGITAL REGISTRAR ENTERPRISE" if det.registrar_score >= 90 else "STANDARD REGISTRAR OFFICE"
        return RegistrarAcademicRecordsOrchestratorReport(
            registrar_tier=tier, registrar_score=det.registrar_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningRegistrarPipelineResult(narrative=narrative, registrar_plan=registrar_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
