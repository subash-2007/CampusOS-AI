from typing import List
from pydantic import BaseModel

class ParentPortalEngagementMetric(BaseModel):
    registered_parents_count: int = 4250
    active_monthly_parents_count: int = 3120
    parent_portal_engagement_pct: float = 73.4

class FERPAAccessControlAudit(BaseModel):
    student_ferpa_waivers_signed: int = 3840
    ferpa_compliance_pct: float = 100.0
    unauthorized_data_access_attempts: int = 0

class FamilyNewsletterOpenRateMetric(BaseModel):
    newsletter_subscribers_count: int = 4800
    avg_open_rate_pct: float = 68.5
    avg_click_rate_pct: float = 24.2

class ParentOrientationAttendanceMetric(BaseModel):
    orientation_attendees_count: int = 1420
    satisfaction_rate_pct: float = 94.8

class ParentAssociationDonationAudit(BaseModel):
    family_fund_donations_usd: float = 480000.0
    parent_donor_count: int = 620

class EmergencyFamilyNotificationAudit(BaseModel):
    emergency_contact_verification_pct: float = 99.2
    avg_alert_dispatch_seconds: float = 2.4

class DeterministicParentPipelineResult(BaseModel):
    portal: ParentPortalEngagementMetric
    ferpa: FERPAAccessControlAudit
    newsletter: FamilyNewsletterOpenRateMetric
    orientation: ParentOrientationAttendanceMetric
    donations: ParentAssociationDonationAudit
    emergency: EmergencyFamilyNotificationAudit
    parent_relations_score: float
    confidence_score: float

class StrategicParentNarrative(BaseModel):
    parent_summary: str
    key_parent_strengths: List[str]

class FamilyEngagementPlan(BaseModel):
    engagement_actions: List[str]
    sample_ferpa_waiver_schema: str

class ReasoningParentPipelineResult(BaseModel):
    narrative: StrategicParentNarrative
    engagement_plan: FamilyEngagementPlan
    reasoning_steps: List[str]

class ParentGuardianRelationsOrchestratorReport(BaseModel):
    department: str = "Parent & Guardian Relations"
    department_id: str = "dept_061"
    parent_tier: str = "HIGHLY ENGAGED FAMILY NETWORK"
    parent_relations_score: float
    confidence_score: float
    deterministic_analysis: DeterministicParentPipelineResult
    reasoning_analysis: ReasoningParentPipelineResult
    reasoning_steps: List[str]
