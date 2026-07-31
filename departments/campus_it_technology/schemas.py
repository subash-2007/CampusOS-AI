from typing import List
from pydantic import BaseModel

class NetworkInfrastructureUptimeMetric(BaseModel):
    campus_wifi_access_points_managed: int = 3800
    network_uptime_sla_pct: float = 99.97
    avg_campus_wifi_speed_mbps: float = 980.0

class ITHelpdeskTicketResolutionAudit(BaseModel):
    helpdesk_tickets_resolved_annual: int = 48000
    first_call_resolution_rate_pct: float = 84.6
    avg_ticket_resolution_hours: float = 3.8

class CampusCybersecuritySOCAudit(BaseModel):
    security_incidents_detected_annual: int = 2840
    mean_time_to_contain_hours: float = 1.8
    student_data_breach_incidents: int = 0

class SoftwareLicenseComplianceAudit(BaseModel):
    enterprise_software_licenses_managed: int = 145000
    microsoft_google_workspace_seats: int = 42000
    license_compliance_audit_score_pct: float = 99.2

class ClassroomAVTechnologyReadinessMetric(BaseModel):
    smart_classrooms_equipped: int = 620
    av_technology_uptime_pct: float = 99.1
    hybrid_learning_rooms_count: int = 220

class ITServiceContinuityDRPAudit(BaseModel):
    disaster_recovery_rto_minutes: float = 12.0
    backup_completion_rate_pct: float = 100.0
    drp_test_exercises_annual: int = 4

class DeterministicITPipelineResult(BaseModel):
    network: NetworkInfrastructureUptimeMetric
    helpdesk: ITHelpdeskTicketResolutionAudit
    cybersecurity: CampusCybersecuritySOCAudit
    software: SoftwareLicenseComplianceAudit
    classroom_av: ClassroomAVTechnologyReadinessMetric
    drp: ITServiceContinuityDRPAudit
    it_score: float
    confidence_score: float

class StrategicITNarrative(BaseModel):
    it_summary: str
    key_it_strengths: List[str]

class ITOperationsPlan(BaseModel):
    it_actions: List[str]
    sample_helpdesk_ticket_schema: str

class ReasoningITPipelineResult(BaseModel):
    narrative: StrategicITNarrative
    it_plan: ITOperationsPlan
    reasoning_steps: List[str]

class CampusITTechnologyOrchestratorReport(BaseModel):
    department: str = "Campus IT & Technology Services"
    department_id: str = "dept_095"
    it_tier: str = "AWARD-WINNING DIGITAL CAMPUS TECHNOLOGY INFRASTRUCTURE"
    it_score: float
    confidence_score: float
    deterministic_analysis: DeterministicITPipelineResult
    reasoning_analysis: ReasoningITPipelineResult
    reasoning_steps: List[str]
