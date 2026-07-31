from app.agents.base_agent import BaseAgent
from departments.admissions_enrollment_management.deterministic import AdmissionsEnrollmentManagementScorerAgent
from departments.admissions_enrollment_management.reasoning import StrategicAdmissionsNarrativeAgent, EnrollmentStrategyPlannerAgent
from departments.admissions_enrollment_management.schemas import AdmissionsEnrollmentManagementOrchestratorReport, ReasoningAdmissionsPipelineResult

class AdmissionsEnrollmentManagementOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Admissions & Enrollment Management Department."""
    def __init__(self):
        super().__init__(agent_id="admissions_enrollment_management_orchestrator", name="Admissions & Enrollment Management Master Orchestrator",
                         description="Coordinates all 9 admissions & enrollment management sub-agents.", icon="UserCheck")
        self.scorer = AdmissionsEnrollmentManagementScorerAgent()
        self.narrative_agent = StrategicAdmissionsNarrativeAgent()
        self.enrollment_planner = EnrollmentStrategyPlannerAgent()

    async def run_pipeline(self, apps: int = 38500) -> AdmissionsEnrollmentManagementOrchestratorReport:
        steps = ["Step 1: Running deterministic Admissions pipeline (application volume, yield deposits, holistic file review, campus tours, Slate CRM, academic profiles)."]
        det = self.scorer.run(apps)
        steps.append("Step 2: Executing Strategic Admissions Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Enrollment Strategy Planner Agent.")
        enrollment_plan = await self.enrollment_planner.plan_enrollment(det)
        steps.append("Step 4: Compiling Admissions & Enrollment Management Master Report.")
        tier = "PREMIER SELECTIVE ENROLLMENT ENTERPRISE" if det.admissions_score >= 90 else "STANDARD ADMISSIONS OFFICE"
        return AdmissionsEnrollmentManagementOrchestratorReport(
            admissions_tier=tier, admissions_score=det.admissions_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningAdmissionsPipelineResult(narrative=narrative, enrollment_plan=enrollment_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
