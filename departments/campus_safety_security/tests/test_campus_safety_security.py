import pytest, asyncio
from departments.campus_safety_security.deterministic import (
    CampusPolicePatrolResponseMeterAgent, CrimePreventionAwarenessProgramMeterAgent, CampusCCTVAccessControlAuditorAgent,
    EmergencyMassNotificationAuditorAgent, CampusParkingCitationEnforcementMeterAgent, SafetyEscortNightRideServiceMeterAgent, CampusSafetySecurityScorerAgent
)
from departments.campus_safety_security.orchestrator import CampusSafetySecurityOrchestratorAgent

def test_campus_police_patrol_response_meter():
    res = CampusPolicePatrolResponseMeterAgent().run()
    assert res.avg_emergency_response_time_minutes <= 10.0

def test_crime_prevention_awareness_program_meter():
    res = CrimePreventionAwarenessProgramMeterAgent().run()
    assert res.bystander_intervention_completions >= 100

def test_campus_cctv_access_control_auditor():
    res = CampusCCTVAccessControlAuditorAgent().run()
    assert res.blue_light_station_uptime_pct >= 99.0

def test_emergency_mass_notification_auditor():
    res = EmergencyMassNotificationAuditorAgent().run()
    assert res.opt_in_enrollment_rate_pct >= 80.0

def test_campus_parking_citation_enforcement_meter():
    res = CampusParkingCitationEnforcementMeterAgent().run()
    assert res.registered_parking_permits_issued >= 100

def test_safety_escort_night_ride_service_meter():
    res = SafetyEscortNightRideServiceMeterAgent().run()
    assert res.escort_service_satisfaction_score >= 4.0

def test_campus_safety_security_scorer():
    res = CampusSafetySecurityScorerAgent().run()
    assert res.safety_score >= 90.0
    assert res.confidence_score >= 0.5

def test_campus_safety_security_orchestrator():
    report = asyncio.run(CampusSafetySecurityOrchestratorAgent().run_pipeline())
    assert report.department == "Campus Safety and Security Operations"
    assert report.department_id == "dept_102"
    assert report.safety_tier == "NATIONALLY ACCREDITED CAMPUS PUBLIC SAFETY DEPARTMENT"
    assert len(report.reasoning_steps) == 4
