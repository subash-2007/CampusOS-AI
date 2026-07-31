from typing import List
from pydantic import BaseModel

class CampusPolicePatrolResponseMetric(BaseModel):
    sworn_campus_officers_count: int = 84
    avg_emergency_response_time_minutes: float = 3.8
    clery_act_incidents_reported_annual: int = 284

class CrimePreventionAwarenessProgramMetric(BaseModel):
    rad_self_defense_workshop_participants: int = 1840
    crime_prevention_programs_offered: int = 48
    bystander_intervention_completions: int = 4200

class CampusCCTVAccessControlAudit(BaseModel):
    cctv_cameras_operational: int = 2840
    blue_light_station_uptime_pct: float = 99.97
    access_control_doors_managed: int = 4800

class EmergencyMassNotificationAudit(BaseModel):
    mass_notification_tests_annual: int = 4
    avg_notification_delivery_seconds: float = 28.0
    opt_in_enrollment_rate_pct: float = 94.8

class CampusParkingCitationEnforcementMetric(BaseModel):
    registered_parking_permits_issued: int = 8400
    parking_citations_issued_annual: int = 12400
    parking_appeal_success_rate_pct: float = 18.4

class SafetyEscortNightRideServiceMetric(BaseModel):
    safe_walk_escort_requests_fulfilled: int = 4200
    night_ride_shuttle_trips_annual: int = 18400
    escort_service_satisfaction_score: float = 4.82

class DeterministicCampusSafetyPipelineResult(BaseModel):
    patrol: CampusPolicePatrolResponseMetric
    crime_prevention: CrimePreventionAwarenessProgramMetric
    cctv: CampusCCTVAccessControlAudit
    notification: EmergencyMassNotificationAudit
    parking: CampusParkingCitationEnforcementMetric
    escort: SafetyEscortNightRideServiceMetric
    safety_score: float
    confidence_score: float

class StrategicCampusSafetyNarrative(BaseModel):
    safety_summary: str
    key_safety_strengths: List[str]

class CampusSafetyOperationsPlan(BaseModel):
    safety_actions: List[str]
    sample_clery_incident_schema: str

class ReasoningCampusSafetyPipelineResult(BaseModel):
    narrative: StrategicCampusSafetyNarrative
    safety_plan: CampusSafetyOperationsPlan
    reasoning_steps: List[str]

class CampusSafetySecurityOrchestratorReport(BaseModel):
    department: str = "Campus Safety and Security Operations"
    department_id: str = "dept_102"
    safety_tier: str = "NATIONALLY ACCREDITED CAMPUS PUBLIC SAFETY DEPARTMENT"
    safety_score: float
    confidence_score: float
    deterministic_analysis: DeterministicCampusSafetyPipelineResult
    reasoning_analysis: ReasoningCampusSafetyPipelineResult
    reasoning_steps: List[str]
