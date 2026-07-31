from app.agents.base_agent import BaseAgent
from departments.alumni_advancement_endowment.deterministic import AlumniAdvancementEndowmentScorerAgent
from departments.alumni_advancement_endowment.reasoning import StrategicAdvancementNarrativeAgent, AdvancementOperationsPlannerAgent
from departments.alumni_advancement_endowment.schemas import AlumniAdvancementEndowmentOrchestratorReport, ReasoningAdvancementPipelineResult

class AlumniAdvancementEndowmentOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Alumni Advancement and Endowment Management Department."""
    def __init__(self):
        super().__init__(agent_id="alumni_advancement_endowment_orchestrator", name="Alumni Advancement and Endowment Management Master Orchestrator",
                         description="Coordinates all 9 sub-agents for Alumni Advancement and Endowment Management.", icon="Cpu")
        self.scorer = AlumniAdvancementEndowmentScorerAgent()
        self.narrative_agent = StrategicAdvancementNarrativeAgent()
        self.planner = AdvancementOperationsPlannerAgent()

    async def run_pipeline(self) -> AlumniAdvancementEndowmentOrchestratorReport:
        steps = ["Step 1: Running deterministic pipeline."]
        det = self.scorer.run()
        steps.append("Step 2: Executing Strategic Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Operations Planner Agent.")
        plan = await self.planner.plan_operations(det)
        steps.append("Step 4: Compiling Master Orchestrator Report.")
        return AlumniAdvancementEndowmentOrchestratorReport(
            tier="BILLION DOLLAR CAMPUS ENDOWMENT ADVANCEMENT EXCELLENCE", advancement_score=det.advancement_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningAdvancementPipelineResult(narrative=narrative, plan=plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
