from app.agents.base_agent import BaseAgent
from departments.global_study_abroad_intelligence.deterministic import GlobalStudyAbroadScorerAgent
from departments.global_study_abroad_intelligence.reasoning import StrategicStudyAbroadNarrativeAgent, GlobalMobilityPlannerAgent
from departments.global_study_abroad_intelligence.schemas import GlobalStudyAbroadOrchestratorReport, ReasoningStudyAbroadPipelineResult

class GlobalStudyAbroadOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Global Study Abroad Intelligence Department."""
    def __init__(self):
        super().__init__(agent_id="global_study_abroad_orchestrator", name="Global Study Abroad Intelligence Master Orchestrator",
                         description="Coordinates all 9 global study abroad sub-agents.", icon="Globe")
        self.scorer = GlobalStudyAbroadScorerAgent()
        self.narrative_agent = StrategicStudyAbroadNarrativeAgent()
        self.mobility_planner = GlobalMobilityPlannerAgent()

    async def run_pipeline(self, students: int = 420) -> GlobalStudyAbroadOrchestratorReport:
        steps = ["Step 1: Running deterministic Study Abroad pipeline (participation, visa compliance, credit transfer, safety risk, orientation, scholarships)."]
        det = self.scorer.run(students)
        steps.append("Step 2: Executing Strategic Study Abroad Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Global Mobility Planner Agent.")
        mobility = await self.mobility_planner.plan_mobility(det)
        steps.append("Step 4: Compiling Global Study Abroad Intelligence Master Report.")
        tier = "PREMIER GLOBAL MOBILITY PROGRAM" if det.study_abroad_score >= 85 else "STANDARD STUDY ABROAD PROGRAM"
        return GlobalStudyAbroadOrchestratorReport(
            study_abroad_tier=tier, study_abroad_score=det.study_abroad_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningStudyAbroadPipelineResult(narrative=narrative, mobility_plan=mobility, reasoning_steps=steps),
            reasoning_steps=steps
        )
