from app.agents.base_agent import BaseAgent
from departments.student_judicial_conduct.deterministic import StudentJudicialConductScorerAgent
from departments.student_judicial_conduct.reasoning import StrategicJudicialNarrativeAgent, JudicialOperationsPlannerAgent
from departments.student_judicial_conduct.schemas import StudentJudicialConductOrchestratorReport, ReasoningJudicialPipelineResult

class StudentJudicialConductOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Student Judicial & Conduct Affairs Department."""
    def __init__(self):
        super().__init__(agent_id="student_judicial_conduct_orchestrator", name="Student Judicial & Conduct Affairs Master Orchestrator",
                         description="Coordinates all 9 student judicial & conduct affairs sub-agents.", icon="Shield")
        self.scorer = StudentJudicialConductScorerAgent()
        self.narrative_agent = StrategicJudicialNarrativeAgent()
        self.judicial_planner = JudicialOperationsPlannerAgent()

    async def run_pipeline(self, cases: int = 1420) -> StudentJudicialConductOrchestratorReport:
        steps = ["Step 1: Running deterministic Judicial pipeline (conduct cases, hearing resolution speed, academic integrity, restorative justice, advisor training, Title IX cross-ref)."]
        det = self.scorer.run(cases)
        steps.append("Step 2: Executing Strategic Judicial Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Judicial Operations Planner Agent.")
        judicial_plan = await self.judicial_planner.plan_judicial_operations(det)
        steps.append("Step 4: Compiling Student Judicial & Conduct Affairs Master Report.")
        tier = "MODEL FAIR DUE-PROCESS CONDUCT SYSTEM" if det.judicial_score >= 90 else "STANDARD STUDENT CONDUCT OFFICE"
        return StudentJudicialConductOrchestratorReport(
            judicial_tier=tier, judicial_score=det.judicial_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningJudicialPipelineResult(narrative=narrative, judicial_plan=judicial_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
