from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class VulnerabilityScanScore(BaseModel):
    critical_vulnerabilities_count: int = 0
    high_vulnerabilities_count: int = 1
    vulnerability_security_score: float = 94.0

class SOC2ComplianceStatus(BaseModel):
    soc2_type2_certified: bool = True
    audited_controls_count: int = 64

class EncryptionStrengthAudit(BaseModel):
    at_rest_encryption: str = "AES-256-GCM"
    in_transit_encryption: str = "TLS 1.3"
    encryption_compliance_score: float = 100.0

class IAMRolePermissionMetric(BaseModel):
    least_privilege_score: float = 92.0
    overprivileged_roles_count: int = 0

class IncidentResponseSpeedMetric(BaseModel):
    mean_time_to_detect_minutes: int = 4
    mean_time_to_respond_minutes: int = 12

class GDPRPrivacyComplianceAudit(BaseModel):
    gdpr_compliant: bool = True
    data_retention_policy_enforced: bool = True

class DeterministicSecurityPipelineResult(BaseModel):
    vulnerability: VulnerabilityScanScore
    soc2: SOC2ComplianceStatus
    encryption: EncryptionStrengthAudit
    iam: IAMRolePermissionMetric
    incident: IncidentResponseSpeedMetric
    gdpr: GDPRPrivacyComplianceAudit
    cybersecurity_posture_score: float
    confidence_score: float

class StrategicSecurityNarrative(BaseModel):
    security_architecture_summary: str
    key_compliance_highlights: List[str]

class ThreatMitigationPlan(BaseModel):
    zero_trust_action_items: List[str]
    sample_incident_response_playbook: str

class ReasoningSecurityPipelineResult(BaseModel):
    narrative: StrategicSecurityNarrative
    mitigation_plan: ThreatMitigationPlan
    reasoning_steps: List[str]

class CybersecurityComplianceOrchestratorReport(BaseModel):
    department: str = "Cybersecurity & Compliance"
    department_id: str = "dept_026"
    security_tier: str = "ENTERPRISE HARDENED"
    cybersecurity_posture_score: float
    confidence_score: float
    deterministic_analysis: DeterministicSecurityPipelineResult
    reasoning_analysis: ReasoningSecurityPipelineResult
    reasoning_steps: List[str]
