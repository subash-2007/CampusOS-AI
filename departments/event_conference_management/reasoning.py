from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.event_conference_management.schemas import (
    StrategicEventNarrative, EventOperationsPlan, ReasoningEventPipelineResult, DeterministicEventPipelineResult
)

class StrategicEventNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates campus event facility utilization, external conference revenue, and AV technical execution."""
    def __init__(self):
        super().__init__(agent_id="strategic_event_narrative", name="Strategic Event Narrative Agent",
                         description="Evaluates venue booking efficiency, external conference revenue, AV technical reliability, and event planner satisfaction.", icon="Calendar")

    async def evaluate(self, det: DeterministicEventPipelineResult) -> StrategicEventNarrative:
        fallback = {
            "event_summary": f"Premier campus conference & event center ({det.event_management_score:.1f}% score). Managing {det.venues.annual_event_reservations:,} annual event reservations ({det.venues.auditorium_ballroom_utilization_pct}% ballroom utilization), ${det.conferences.external_conference_revenue_usd/1e6:.2f}M external conference revenue, {det.av_tech.av_technical_glitch_rate_pct}% AV glitch rate.",
            "key_event_strengths": [f"{det.checkin.event_attendees_scanned_total:,} attendees checked in with average {det.checkin.avg_checkin_seconds_per_attendee:.1f}-second scan speed", f"100% food & alcohol catering permit compliance across {det.catering.catering_orders_fulfilled:,} catered campus events"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Director of Campus Event Services & Conference Operations", "venue scheduling, conference hosting, AV production, catering permits, event registration"),
                                          PromptBuilder.build_user_context({"score": det.event_management_score}), task_type="event_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicEventNarrative(event_summary=parsed.get("event_summary", fallback["event_summary"]),
                                          key_event_strengths=parsed.get("key_event_strengths", fallback["key_event_strengths"]))
        except Exception:
            return StrategicEventNarrative(**fallback)

class EventOperationsPlannerAgent(BaseAgent):
    """Agent 9: Generates venue reservation workflows and event AV technical production roadmaps."""
    def __init__(self):
        super().__init__(agent_id="event_operations_planner", name="Event Operations Planner Agent",
                         description="Formulates space reservation scheduling algorithms, hybrid conference streaming setups, and catering permit review systems.", icon="Layers")

    async def plan_events(self, det: DeterministicEventPipelineResult) -> EventOperationsPlan:
        fallback = {
            "event_actions": ["Deploy AI Room Utilization Optimization Engine to eliminate double-bookings and balance setup turnarounds", "Launch Mobile QR-Code Self-Check-In Kiosks for campus conferences"],
            "sample_venue_reservation_contract": "CAMPUS EVENT VENUE & SERVICES FACILITY AGREEMENT\nEvent Name: Annual Higher Ed AI Summit 2026\nSponsor: Academic Technology Association\nVenue: Grand University Ballroom & Auditorium (Capacity: 1,200)\nDates: October 14-16, 2026\nIncluded Services:\n  1. AV Tech Support: 4K Dual Projection, Wireless Microphones, Live Webcast Recording\n  2. Catering: Full Breakfast, Lunch Buffet, Networking Reception (Permit Approved)\n  3. Housing: 250 Residence Hall Conference Rooms reserved\nTotal Contract Fee: $64,500 USD\nStatus: CONFIRMED & DEPOSIT RECEIVED"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Event Operations Specialist & Conference Producer", "venue contract, AV production, event checkin"),
                                          PromptBuilder.build_user_context({"reservations": det.venues.annual_event_reservations}), task_type="event_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return EventOperationsPlan(event_actions=parsed.get("event_actions", fallback["event_actions"]),
                                       sample_venue_reservation_contract=parsed.get("sample_venue_reservation_contract", fallback["sample_venue_reservation_contract"]))
        except Exception:
            return EventOperationsPlan(**fallback)
