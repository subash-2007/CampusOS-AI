from app.agents.base_agent import BaseAgent
from departments.event_conference_management.deterministic import EventConferenceManagementScorerAgent
from departments.event_conference_management.reasoning import StrategicEventNarrativeAgent, EventOperationsPlannerAgent
from departments.event_conference_management.schemas import EventConferenceManagementOrchestratorReport, ReasoningEventPipelineResult

class EventConferenceManagementOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Campus Event & Conference Management Department."""
    def __init__(self):
        super().__init__(agent_id="event_conference_management_orchestrator", name="Campus Event & Conference Management Master Orchestrator",
                         description="Coordinates all 9 campus event & conference management sub-agents.", icon="Calendar")
        self.scorer = EventConferenceManagementScorerAgent()
        self.narrative_agent = StrategicEventNarrativeAgent()
        self.event_planner = EventOperationsPlannerAgent()

    async def run_pipeline(self, reservations: int = 4850) -> EventConferenceManagementOrchestratorReport:
        steps = ["Step 1: Running deterministic Event pipeline (venues, conferences, AV tech, catering, checkin, CSAT)."]
        det = self.scorer.run(reservations)
        steps.append("Step 2: Executing Strategic Event Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Event Operations Planner Agent.")
        event_plan = await self.event_planner.plan_events(det)
        steps.append("Step 4: Compiling Campus Event & Conference Management Master Report.")
        tier = "PREMIER CAMPUS CONFERENCE & EVENT CENTER" if det.event_management_score >= 90 else "STANDARD EVENT MANAGEMENT FACILITY"
        return EventConferenceManagementOrchestratorReport(
            event_tier=tier, event_management_score=det.event_management_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningEventPipelineResult(narrative=narrative, event_plan=event_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
