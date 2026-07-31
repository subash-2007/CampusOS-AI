from app.agents.base_agent import BaseAgent
from departments.student_research_innovation.deterministic import StudentResearchInnovationScorerAgent
from departments.student_research_innovation.reasoning import StrategicInnovationNarrativeAgent, InnovationIncubatorPlannerAgent
from departments.student_research_innovation.schemas import StudentResearchInnovationOrchestratorReport, ReasoningInnovationPipelineResult

class StudentResearchInnovationOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Student Research & Innovation Incubator Department (Dept 100)."""
    def __init__(self):
        super().__init__(agent_id="student_research_innovation_orchestrator", name="Student Research & Innovation Incubator Master Orchestrator",
                         description="Coordinates all 9 student research & innovation incubator sub-agents.", icon="Zap")
        self.scorer = StudentResearchInnovationScorerAgent()
        self.narrative_agent = StrategicInnovationNarrativeAgent()
        self.innovation_planner = InnovationIncubatorPlannerAgent()

    async def run_pipeline(self) -> StudentResearchInnovationOrchestratorReport:
        steps = ["Step 1: Running deterministic Innovation pipeline (undergrad research, startup incubator, patents/tech transfer, makerspace, innovation grants, industry partnerships)."]
        det = self.scorer.run()
        steps.append("Step 2: Executing Strategic Innovation Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Innovation Incubator Planner Agent.")
        innovation_plan = await self.innovation_planner.plan_innovation(det)
        steps.append("Step 4: Compiling Student Research & Innovation Incubator Master Report.")
        tier = "NATIONALLY RANKED STUDENT INNOVATION ECOSYSTEM" if det.innovation_score >= 80 else "DEVELOPING STUDENT INNOVATION PROGRAM"
        return StudentResearchInnovationOrchestratorReport(
            innovation_tier=tier, innovation_score=det.innovation_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningInnovationPipelineResult(narrative=narrative, innovation_plan=innovation_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
