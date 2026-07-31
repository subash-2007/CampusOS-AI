from app.agents.base_agent import BaseAgent
from departments.student_government_leadership.deterministic import StudentGovernmentLeadershipScorerAgent
from departments.student_government_leadership.reasoning import StrategicSGANarrativeAgent, StudentGovernancePlannerAgent
from departments.student_government_leadership.schemas import StudentGovernmentLeadershipOrchestratorReport, ReasoningSGAPipelineResult

class StudentGovernmentLeadershipOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Student Government & Leadership Department."""
    def __init__(self):
        super().__init__(agent_id="student_government_leadership_orchestrator", name="Student Government & Leadership Master Orchestrator",
                         description="Coordinates all 9 student government & leadership sub-agents.", icon="Award")
        self.scorer = StudentGovernmentLeadershipScorerAgent()
        self.narrative_agent = StrategicSGANarrativeAgent()
        self.governance_planner = StudentGovernancePlannerAgent()

    async def run_pipeline(self, voters: int = 8450) -> StudentGovernmentLeadershipOrchestratorReport:
        steps = ["Step 1: Running deterministic SGA pipeline (elections, budget allocation, Student Senate legislation, leadership academy, town halls, badges)."]
        det = self.scorer.run(voters)
        steps.append("Step 2: Executing Strategic SGA Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Student Governance Planner Agent.")
        governance_plan = await self.governance_planner.plan_governance(det)
        steps.append("Step 4: Compiling Student Government & Leadership Master Report.")
        tier = "HIGH-ENGAGEMENT STUDENT DEMOCRACY" if det.sga_score >= 88 else "STANDARD STUDENT GOVERNMENT"
        return StudentGovernmentLeadershipOrchestratorReport(
            governance_tier=tier, sga_score=det.sga_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningSGAPipelineResult(narrative=narrative, governance_plan=governance_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
