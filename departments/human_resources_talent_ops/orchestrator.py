from app.agents.base_agent import BaseAgent
from departments.human_resources_talent_ops.deterministic import HumanResourcesTalentOpsScorerAgent
from departments.human_resources_talent_ops.reasoning import StrategicHRNarrativeAgent, HROperationsPlannerAgent
from departments.human_resources_talent_ops.schemas import HumanResourcesTalentOpsOrchestratorReport, ReasoningHRPipelineResult

class HumanResourcesTalentOpsOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Campus Human Resources and Talent Operations Department."""
    def __init__(self):
        super().__init__(agent_id="human_resources_talent_ops_orchestrator", name="Campus Human Resources and Talent Operations Master Orchestrator",
                         description="Coordinates all 9 sub-agents for Campus Human Resources and Talent Operations.", icon="Cpu")
        self.scorer = HumanResourcesTalentOpsScorerAgent()
        self.narrative_agent = StrategicHRNarrativeAgent()
        self.planner = HROperationsPlannerAgent()

    async def run_pipeline(self) -> HumanResourcesTalentOpsOrchestratorReport:
        steps = ["Step 1: Running deterministic pipeline."]
        det = self.scorer.run()
        steps.append("Step 2: Executing Strategic Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Operations Planner Agent.")
        plan = await self.planner.plan_operations(det)
        steps.append("Step 4: Compiling Master Orchestrator Report.")
        return HumanResourcesTalentOpsOrchestratorReport(
            tier="GREAT COLLEGES TO WORK FOR HIGHER ED HR EXCELLENCE", hr_score=det.hr_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningHRPipelineResult(narrative=narrative, plan=plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
