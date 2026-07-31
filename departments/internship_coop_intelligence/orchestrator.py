from app.agents.base_agent import BaseAgent
from departments.internship_coop_intelligence.deterministic import InternshipProgramScorerAgent
from departments.internship_coop_intelligence.reasoning import StrategicInternshipNarrativeAgent, InternshipProgramPlannerAgent
from departments.internship_coop_intelligence.schemas import InternshipCoopOrchestratorReport, ReasoningInternshipPipelineResult

class InternshipCoopOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Internship & Co-op Intelligence Department."""
    def __init__(self):
        super().__init__(agent_id="internship_coop_orchestrator", name="Internship & Co-op Intelligence Master Orchestrator",
                         description="Coordinates all 9 internship and co-op sub-agents.", icon="Briefcase")
        self.scorer = InternshipProgramScorerAgent()
        self.narrative_agent = StrategicInternshipNarrativeAgent()
        self.program_planner = InternshipProgramPlannerAgent()

    async def run_pipeline(self, total_applicants: int = 1850) -> InternshipCoopOrchestratorReport:
        steps = ["Step 1: Running deterministic Internship pipeline (placement rate, conversion rate, stipend, employer satisfaction, academic credit, skill growth)."]
        det = self.scorer.run(total_applicants)
        steps.append("Step 2: Executing Strategic Internship Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Internship Program Planner Agent.")
        program = await self.program_planner.plan_program(det)
        steps.append("Step 4: Compiling Internship & Co-op Intelligence Master Report.")
        tier = "TOP TIER CO-OP PROGRAM" if det.internship_program_score >= 80 else "STANDARD CO-OP PROGRAM"
        return InternshipCoopOrchestratorReport(
            internship_tier=tier, internship_program_score=det.internship_program_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningInternshipPipelineResult(narrative=narrative, program_plan=program, reasoning_steps=steps),
            reasoning_steps=steps
        )
