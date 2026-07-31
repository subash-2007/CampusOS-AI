from app.agents.base_agent import BaseAgent
from departments.community_civic_engagement.deterministic import CommunityCivicEngagementScorerAgent
from departments.community_civic_engagement.reasoning import StrategicCivicNarrativeAgent, CivicOperationsPlannerAgent
from departments.community_civic_engagement.schemas import CommunityCivicEngagementOrchestratorReport, ReasoningCivicPipelineResult

class CommunityCivicEngagementOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Community and Civic Engagement Department."""
    def __init__(self):
        super().__init__(agent_id="community_civic_engagement_orchestrator", name="Community and Civic Engagement Master Orchestrator",
                         description="Coordinates all 9 sub-agents for Community and Civic Engagement.", icon="Cpu")
        self.scorer = CommunityCivicEngagementScorerAgent()
        self.narrative_agent = StrategicCivicNarrativeAgent()
        self.planner = CivicOperationsPlannerAgent()

    async def run_pipeline(self) -> CommunityCivicEngagementOrchestratorReport:
        steps = ["Step 1: Running deterministic pipeline."]
        det = self.scorer.run()
        steps.append("Step 2: Executing Strategic Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Operations Planner Agent.")
        plan = await self.planner.plan_operations(det)
        steps.append("Step 4: Compiling Master Orchestrator Report.")
        return CommunityCivicEngagementOrchestratorReport(
            tier="CARNEGIE COMMUNITY ENGAGEMENT CLASSIFIED INSTITUTION", engagement_score=det.engagement_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningCivicPipelineResult(narrative=narrative, plan=plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
