import pytest, asyncio
from departments.event_conference_management.deterministic import (
    VenueBookingSpaceUtilizationMeterAgent, ConferenceExternalEventRevenueAuditorAgent, EventAVTechSupportMeterAgent,
    EventCateringPermitSafetyAuditorAgent, EventAttendeeCheckinRegistrationMeterAgent, EventFeedbackCSATAuditorAgent, EventConferenceManagementScorerAgent
)
from departments.event_conference_management.orchestrator import EventConferenceManagementOrchestratorAgent

def test_venue_booking_space_utilization_meter():
    res = VenueBookingSpaceUtilizationMeterAgent().run(4850)
    assert res.annual_event_reservations == 4850
    assert res.online_reservation_portal_adoption_pct >= 90.0

def test_conference_external_event_revenue_auditor():
    res = ConferenceExternalEventRevenueAuditorAgent().run()
    assert res.external_conference_revenue_usd > 500000.0

def test_event_av_tech_support_meter():
    res = EventAVTechSupportMeterAgent().run()
    assert res.av_technical_glitch_rate_pct < 2.0

def test_event_catering_permit_safety_auditor():
    res = EventCateringPermitSafetyAuditorAgent().run()
    assert res.food_permit_compliance_pct == 100.0

def test_event_attendee_checkin_registration_meter():
    res = EventAttendeeCheckinRegistrationMeterAgent().run()
    assert res.event_attendees_scanned_total >= 50000
    assert res.avg_checkin_seconds_per_attendee <= 10.0

def test_event_feedback_csat_auditor():
    res = EventFeedbackCSATAuditorAgent().run()
    assert res.event_planner_csat_score >= 4.0

def test_event_conference_management_scorer():
    res = EventConferenceManagementScorerAgent().run(4850)
    assert res.event_management_score >= 90.0
    assert res.confidence_score >= 0.5

def test_event_conference_management_orchestrator():
    report = asyncio.run(EventConferenceManagementOrchestratorAgent().run_pipeline(4850))
    assert report.department == "Campus Event & Conference Management"
    assert report.department_id == "dept_078"
    assert report.event_tier == "PREMIER CAMPUS CONFERENCE & EVENT CENTER"
    assert len(report.reasoning_steps) == 4
