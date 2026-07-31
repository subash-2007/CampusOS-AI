from app.agents.base_agent import BaseAgent
from departments.alumni_mentorship_engagement.deterministic import AlumniEngagementScorerAgent
from departments.alumni_mentorship_engagement.reasoning import StrategicAlumniNarrativeAgent, AlumniEngagementPlannerAgent
from departments.alumni_mentorship_engagement.schemas import AlumniMentorshipOrchestratorReport, ReasoningAlumniPipelineResult

class AlumniMentorshipOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Alumni Mentorship & Engagement Department."""
    def __init__(self):
        super().__init__(agent_id="alumni_mentorship_orchestrator", name="Alumni Mentorship & Engagement Master Orchestrator",
                         description="Coordinates all 9 alumni mentorship and engagement sub-agents.", icon="Users")
        self.scorer = AlumniEngagementScorerAgent()
        self.narrative_agent = StrategicAlumniNarrativeAgent()
        self.engagement_planner = AlumniEngagementPlannerAgent()

    async def run_pipeline(self, registered: int = 18400) -> AlumniMentorshipOrchestratorReport:
        steps = ["Step 1: Running deterministic Alumni pipeline (network size, mentorship pairing, annual giving, events, career transitions, chapters)."]
        det = self.scorer.run(registered)
        steps.append("Step 2: Executing Strategic Alumni Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Alumni Engagement Planner Agent.")
        engagement = await self.engagement_planner.plan_engagement(det)
        steps.append("Step 4: Compiling Alumni Mentorship & Engagement Master Report.")
        tier = "HIGHLY ENGAGED ALUMNI NETWORK" if det.alumni_engagement_score >= 80 else "STANDARD ALUMNI NETWORK"
        return AlumniMentorshipOrchestratorReport(
            alumni_tier=tier, alumni_engagement_score=det.alumni_engagement_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningAlumniPipelineResult(narrative=narrative, engagement_plan=engagement, reasoning_steps=steps),
            reasoning_steps=steps
        )
