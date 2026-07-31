from app.agents.base_agent import BaseAgent
from departments.parent_guardian_relations.deterministic import ParentGuardianRelationsScorerAgent
from departments.parent_guardian_relations.reasoning import StrategicParentNarrativeAgent, FamilyEngagementPlannerAgent
from departments.parent_guardian_relations.schemas import ParentGuardianRelationsOrchestratorReport, ReasoningParentPipelineResult

class ParentGuardianRelationsOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Parent & Guardian Relations Department."""
    def __init__(self):
        super().__init__(agent_id="parent_guardian_relations_orchestrator", name="Parent & Guardian Relations Master Orchestrator",
                         description="Coordinates all 9 parent and guardian relations sub-agents.", icon="Users")
        self.scorer = ParentGuardianRelationsScorerAgent()
        self.narrative_agent = StrategicParentNarrativeAgent()
        self.engagement_planner = FamilyEngagementPlannerAgent()

    async def run_pipeline(self, registered: int = 4250) -> ParentGuardianRelationsOrchestratorReport:
        steps = ["Step 1: Running deterministic Parent pipeline (portal engagement, FERPA access control, family newsletter, orientation, donations, emergency alerts)."]
        det = self.scorer.run(registered)
        steps.append("Step 2: Executing Strategic Parent Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Family Engagement Planner Agent.")
        engagement = await self.engagement_planner.plan_engagement(det)
        steps.append("Step 4: Compiling Parent & Guardian Relations Master Report.")
        tier = "HIGHLY ENGAGED FAMILY NETWORK" if det.parent_relations_score >= 85 else "STANDARD PARENT NETWORK"
        return ParentGuardianRelationsOrchestratorReport(
            parent_tier=tier, parent_relations_score=det.parent_relations_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningParentPipelineResult(narrative=narrative, engagement_plan=engagement, reasoning_steps=steps),
            reasoning_steps=steps
        )
