from app.agents.base_agent import BaseAgent
from departments.intercollegiate_athletics_ncaa.deterministic import IntercollegiateAthleticsNCAAScorerAgent
from departments.intercollegiate_athletics_ncaa.reasoning import StrategicAthleticsNarrativeAgent, AthleticsOperationsPlannerAgent
from departments.intercollegiate_athletics_ncaa.schemas import IntercollegiateAthleticsNCAAOrchestratorReport, ReasoningAthleticsPipelineResult

class IntercollegiateAthleticsNCAAOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Intercollegiate Athletics and NCAA Compliance Department."""
    def __init__(self):
        super().__init__(agent_id="intercollegiate_athletics_ncaa_orchestrator", name="Intercollegiate Athletics and NCAA Compliance Master Orchestrator",
                         description="Coordinates all 9 sub-agents for Intercollegiate Athletics and NCAA Compliance.", icon="Cpu")
        self.scorer = IntercollegiateAthleticsNCAAScorerAgent()
        self.narrative_agent = StrategicAthleticsNarrativeAgent()
        self.planner = AthleticsOperationsPlannerAgent()

    async def run_pipeline(self) -> IntercollegiateAthleticsNCAAOrchestratorReport:
        steps = ["Step 1: Running deterministic pipeline."]
        det = self.scorer.run()
        steps.append("Step 2: Executing Strategic Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Operations Planner Agent.")
        plan = await self.planner.plan_operations(det)
        steps.append("Step 4: Compiling Master Orchestrator Report.")
        return IntercollegiateAthleticsNCAAOrchestratorReport(
            tier="NCAA DIVISION I CHAMPIONSHIP ATHLETICS PROGRAM", athletics_score=det.athletics_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningAthleticsPipelineResult(narrative=narrative, plan=plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
