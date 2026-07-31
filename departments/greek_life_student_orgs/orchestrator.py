from app.agents.base_agent import BaseAgent
from departments.greek_life_student_orgs.deterministic import GreekLifeStudentOrgsScorerAgent
from departments.greek_life_student_orgs.reasoning import StrategicGreekLifeNarrativeAgent, StudentOrgManagementPlannerAgent
from departments.greek_life_student_orgs.schemas import GreekLifeStudentOrgsOrchestratorReport, ReasoningGreekLifePipelineResult

class GreekLifeStudentOrgsOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Greek Life & Student Organizations Department."""
    def __init__(self):
        super().__init__(agent_id="greek_life_student_orgs_orchestrator", name="Greek Life & Student Organizations Master Orchestrator",
                         description="Coordinates all 9 Greek Life & student organizations sub-agents.", icon="Users")
        self.scorer = GreekLifeStudentOrgsScorerAgent()
        self.narrative_agent = StrategicGreekLifeNarrativeAgent()
        self.management_planner = StudentOrgManagementPlannerAgent()

    async def run_pipeline(self, orgs: int = 340) -> GreekLifeStudentOrgsOrchestratorReport:
        steps = ["Step 1: Running deterministic Greek Life pipeline (registration, Greek compliance, philanthropy, risk management, finances, advisors)."]
        det = self.scorer.run(orgs)
        steps.append("Step 2: Executing Strategic Greek Life Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Student Org Management Planner Agent.")
        management_plan = await self.management_planner.plan_management(det)
        steps.append("Step 4: Compiling Greek Life & Student Organizations Master Report.")
        tier = "EXEMPLARY CAMPUS LIFE INVOLVEMENT" if det.org_health_score >= 90 else "STANDARD CAMPUS ORGANIZATIONAL SYSTEM"
        return GreekLifeStudentOrgsOrchestratorReport(
            org_tier=tier, org_health_score=det.org_health_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningGreekLifePipelineResult(narrative=narrative, management_plan=management_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
