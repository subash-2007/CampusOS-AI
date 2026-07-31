from typing import List
from pydantic import BaseModel

class GDPRComplianceAudit(BaseModel):
    gdpr_compliant: bool = True
    data_subject_rights_implemented: int = 8
    dpa_registered: bool = True

class DataRetentionPolicyAudit(BaseModel):
    retention_policies_defined: int = 24
    expired_data_auto_purged: bool = True
    avg_retention_days: int = 365

class ConsentManagementMetric(BaseModel):
    consent_capture_rate_pct: float = 98.0
    granular_consent_options_count: int = 12
    consent_withdrawal_latency_hours: float = 0.5

class DataEncryptionAudit(BaseModel):
    data_at_rest_encryption: str = "AES-256-GCM"
    data_in_transit_encryption: str = "TLS 1.3"
    key_rotation_days: int = 90

class DataBreachDetectionMetric(BaseModel):
    breach_detection_time_minutes: float = 4.5
    breach_incidents_last_12m: int = 0
    incident_response_plan_tested: bool = True

class DataLineageAudit(BaseModel):
    data_lineage_coverage_pct: float = 94.0
    undocumented_data_flows: int = 2

class DeterministicPrivacyPipelineResult(BaseModel):
    gdpr: GDPRComplianceAudit
    retention: DataRetentionPolicyAudit
    consent: ConsentManagementMetric
    encryption: DataEncryptionAudit
    breach_detection: DataBreachDetectionMetric
    lineage: DataLineageAudit
    privacy_compliance_score: float
    confidence_score: float

class StrategicPrivacyNarrative(BaseModel):
    privacy_compliance_summary: str
    key_privacy_strengths: List[str]

class PrivacyRoadmapPlan(BaseModel):
    compliance_improvement_actions: List[str]
    sample_privacy_policy_clause: str

class ReasoningPrivacyPipelineResult(BaseModel):
    narrative: StrategicPrivacyNarrative
    roadmap: PrivacyRoadmapPlan
    reasoning_steps: List[str]

class PrivacyDataGovernanceOrchestratorReport(BaseModel):
    department: str = "Privacy & Data Governance"
    department_id: str = "dept_041"
    privacy_tier: str = "FULL GDPR COMPLIANCE"
    privacy_compliance_score: float
    confidence_score: float
    deterministic_analysis: DeterministicPrivacyPipelineResult
    reasoning_analysis: ReasoningPrivacyPipelineResult
    reasoning_steps: List[str]
