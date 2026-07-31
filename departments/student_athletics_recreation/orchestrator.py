from app.agents.base_agent import BaseAgent
from departments.student_athletics_recreation.deterministic import StudentAthleticsRecreationScorerAgent
from departments.student_athletics_recreation.reasoning import StrategicAthleticsNarrativeAgent, CampusAthleticsPlannerAgent
from departments.student_athletics_recreation.schemas import StudentAthleticsRecreationOrchestratorReport, ReasoningAthleticsPipelineResult

class StudentAthleticsRecreationOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Student Athletics & Recreation Department."""
    def __init__(self):
        super().__init__(agent_id="student_athletics_recreation_orchestrator", name="Student Athletics & Recreation Master Orchestrator",
                         description="Coordinates all 9 student athletics & recreation sub-agents.", icon="Activity")
        self.scorer = StudentAthleticsRecreationScorerAgent()
        self.narrative_agent = StrategicAthleticsNarrativeAgent()
        self.athletics_planner = CampusAthleticsPlannerAgent()

    async def run_pipeline(self, athletes: int = 540) -> StudentAthleticsRecreationOrchestratorReport:
        steps = ["Step 1: Running deterministic Athletics pipeline (headcount, NCAA APR, rec center, scholarships & NIL, sports medicine, intramurals)."]
        det = self.scorer.run(athletes)
        steps.append("Step 2: Executing Strategic Athletics Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Campus Athletics Planner Agent.")
        athletics_plan = await self.athletics_planner.plan_athletics(det)
        steps.append("Step 4: Compiling Student Athletics & Recreation Master Report.")
        tier = "NCAA CHAMPIONSHIP EXCELLENCE PROGRAM" if det.athletics_score >= 90 else "STANDARD ATHLETICS PROGRAM"
        return StudentAthleticsRecreationOrchestratorReport(
            athletics_tier=tier, athletics_score=det.athletics_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningAthleticsPipelineResult(narrative=narrative, athletics_plan=athletics_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
