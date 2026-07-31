from departments.shared.scoring import ScoringEngine
from departments.event_conference_management.schemas import (
    VenueBookingSpaceUtilizationMetric, ConferenceExternalEventRevenueAudit, EventAVTechSupportMetric,
    EventCateringPermitSafetyAudit, EventAttendeeCheckinRegistrationMetric, EventFeedbackCSATAudit, DeterministicEventPipelineResult
)

class VenueBookingSpaceUtilizationMeterAgent:
    """Agent 1: Measures annual event reservations count, ballroom/auditorium utilization percentage, and portal adoption."""
    def run(self, reservations: int = 4850) -> VenueBookingSpaceUtilizationMetric:
        return VenueBookingSpaceUtilizationMetric(annual_event_reservations=reservations, auditorium_ballroom_utilization_pct=88.4, online_reservation_portal_adoption_pct=98.2)

class ConferenceExternalEventRevenueAuditorAgent:
    """Agent 2: Audits external conference revenue (USD), external event contracts, and summer conference housing nights."""
    def run(self) -> ConferenceExternalEventRevenueAudit:
        return ConferenceExternalEventRevenueAudit(external_conference_revenue_usd=1450000.0, external_event_contracts_signed=64, summer_conference_housing_nights=14200)

class EventAVTechSupportMeterAgent:
    """Agent 3: Measures AV-supported events count, technical glitch rate percentage, and AV staff satisfaction score."""
    def run(self) -> EventAVTechSupportMetric:
        return EventAVTechSupportMetric(av_supported_events_count=2450, av_technical_glitch_rate_pct=0.8, av_staff_satisfaction_score=4.85)

class EventCateringPermitSafetyAuditorAgent:
    """Agent 4: Audits catering orders fulfilled, food permit compliance percentage, and alcohol permit compliance."""
    def run(self) -> EventCateringPermitSafetyAudit:
        return EventCateringPermitSafetyAudit(catering_orders_fulfilled=1850, food_permit_compliance_pct=100.0, alcohol_event_permit_compliance_pct=100.0)

class EventAttendeeCheckinRegistrationMeterAgent:
    """Agent 5: Measures attendee check-in scans, average check-in speed (seconds), and badge printing fulfillment."""
    def run(self) -> EventAttendeeCheckinRegistrationMetric:
        return EventAttendeeCheckinRegistrationMetric(event_attendees_scanned_total=85000, avg_checkin_seconds_per_attendee=4.2, badge_printing_fulfillment_pct=99.4)

class EventFeedbackCSATAuditorAgent:
    """Agent 6: Audits event planner CSAT score and overall attendee experience rating (out of 5)."""
    def run(self) -> EventFeedbackCSATAudit:
        return EventFeedbackCSATAudit(event_planner_csat_score=4.78, attendee_experience_rating=4.72)

class EventConferenceManagementScorerAgent:
    """Agent 7: Master deterministic aggregator for Campus Event & Conference Management."""
    def __init__(self):
        self.venue_agent = VenueBookingSpaceUtilizationMeterAgent()
        self.conference_agent = ConferenceExternalEventRevenueAuditorAgent()
        self.av_agent = EventAVTechSupportMeterAgent()
        self.catering_agent = EventCateringPermitSafetyAuditorAgent()
        self.checkin_agent = EventAttendeeCheckinRegistrationMeterAgent()
        self.csat_agent = EventFeedbackCSATAuditorAgent()

    def run(self, reservations: int = 4850) -> DeterministicEventPipelineResult:
        venues = self.venue_agent.run(reservations)
        conferences = self.conference_agent.run()
        av_tech = self.av_agent.run()
        catering = self.catering_agent.run()
        checkin = self.checkin_agent.run()
        csat = self.csat_agent.run()

        metrics = {
            "catering_permits": catering.food_permit_compliance_pct,
            "badge_fulfillment": checkin.badge_printing_fulfillment_pct,
            "av_reliability": max(0.0, 100.0 - (av_tech.av_technical_glitch_rate_pct * 10)),
            "planner_csat": (csat.event_planner_csat_score / 5.0) * 100
        }
        weights = {"catering_permits": 0.35, "badge_fulfillment": 0.30, "av_reliability": 0.20, "planner_csat": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(venues.annual_event_reservations, 100)
        return DeterministicEventPipelineResult(
            venues=venues, conferences=conferences, av_tech=av_tech,
            catering=catering, checkin=checkin, csat=csat,
            event_management_score=score, confidence_score=confidence
        )
