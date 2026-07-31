from typing import List
from pydantic import BaseModel

class EmergencyCallboxAudit(BaseModel):
    callboxes_installed_count: int = 142
    functional_callboxes_pct: float = 99.3
    avg_callbox_response_seconds: float = 14.5

class CampusSafetyAppMetric(BaseModel):
    app_downloads_count: int = 18500
    active_safety_app_users_pct: float = 84.2
    safe_walk_escorts_requested: int = 1420

class EmergencyAlertBroadcastAudit(BaseModel):
    mass_notification_channels: int = 6
    alert_delivery_time_seconds: float = 3.2
    delivery_reach_pct: float = 98.8

class CleryActComplianceAudit(BaseModel):
    clery_act_crime_statistics_logged: int = 24
    annual_security_report_published: bool = True
    clery_compliance_score_pct: float = 100.0

class SecurityCameraCoverageMetric(BaseModel):
    security_cameras_active: int = 840
    camera_uptime_pct: float = 99.6
    ai_anomaly_alerts_triggered: int = 34

class CampusDisasterDrillMetric(BaseModel):
    disaster_drills_completed_annual: int = 6
    evacuation_time_avg_minutes: float = 4.2
    first_responder_coordination_rating: float = 4.9

class DeterministicSafetyPipelineResult(BaseModel):
    callboxes: EmergencyCallboxAudit
    safety_app: CampusSafetyAppMetric
    emergency_alerts: EmergencyAlertBroadcastAudit
    clery_act: CleryActComplianceAudit
    cameras: SecurityCameraCoverageMetric
    drills: CampusDisasterDrillMetric
    campus_safety_score: float
    confidence_score: float

class StrategicSafetyNarrative(BaseModel):
    safety_summary: str
    key_safety_strengths: List[str]

class CampusEmergencyPlan(BaseModel):
    safety_protocol_actions: List[str]
    sample_clery_alert_broadcast: str

class ReasoningSafetyPipelineResult(BaseModel):
    narrative: StrategicSafetyNarrative
    emergency_plan: CampusEmergencyPlan
    reasoning_steps: List[str]

class CampusSafetyEmergencyOrchestratorReport(BaseModel):
    department: str = "Campus Safety & Emergency Response"
    department_id: str = "dept_065"
    safety_tier: str = "GOLD-STANDARD SAFE CAMPUS"
    campus_safety_score: float
    confidence_score: float
    deterministic_analysis: DeterministicSafetyPipelineResult
    reasoning_analysis: ReasoningSafetyPipelineResult
    reasoning_steps: List[str]
