from typing import List
from pydantic import BaseModel

class VenueBookingSpaceUtilizationMetric(BaseModel):
    annual_event_reservations: int = 4850
    auditorium_ballroom_utilization_pct: float = 88.4
    online_reservation_portal_adoption_pct: float = 98.2

class ConferenceExternalEventRevenueAudit(BaseModel):
    external_conference_revenue_usd: float = 1450000.0
    external_event_contracts_signed: int = 64
    summer_conference_housing_nights: int = 14200

class EventAVTechSupportMetric(BaseModel):
    av_supported_events_count: int = 2450
    av_technical_glitch_rate_pct: float = 0.8
    av_staff_satisfaction_score: float = 4.85

class EventCateringPermitSafetyAudit(BaseModel):
    catering_orders_fulfilled: int = 1850
    food_permit_compliance_pct: float = 100.0
    alcohol_event_permit_compliance_pct: float = 100.0

class EventAttendeeCheckinRegistrationMetric(BaseModel):
    event_attendees_scanned_total: int = 85000
    avg_checkin_seconds_per_attendee: float = 4.2
    badge_printing_fulfillment_pct: float = 99.4

class EventFeedbackCSATAudit(BaseModel):
    event_planner_csat_score: float = 4.78
    attendee_experience_rating: float = 4.72

class DeterministicEventPipelineResult(BaseModel):
    venues: VenueBookingSpaceUtilizationMetric
    conferences: ConferenceExternalEventRevenueAudit
    av_tech: EventAVTechSupportMetric
    catering: EventCateringPermitSafetyAudit
    checkin: EventAttendeeCheckinRegistrationMetric
    csat: EventFeedbackCSATAudit
    event_management_score: float
    confidence_score: float

class StrategicEventNarrative(BaseModel):
    event_summary: str
    key_event_strengths: List[str]

class EventOperationsPlan(BaseModel):
    event_actions: List[str]
    sample_venue_reservation_contract: str

class ReasoningEventPipelineResult(BaseModel):
    narrative: StrategicEventNarrative
    event_plan: EventOperationsPlan
    reasoning_steps: List[str]

class EventConferenceManagementOrchestratorReport(BaseModel):
    department: str = "Campus Event & Conference Management"
    department_id: str = "dept_078"
    event_tier: str = "PREMIER CAMPUS CONFERENCE & EVENT CENTER"
    event_management_score: float
    confidence_score: float
    deterministic_analysis: DeterministicEventPipelineResult
    reasoning_analysis: ReasoningEventPipelineResult
    reasoning_steps: List[str]
