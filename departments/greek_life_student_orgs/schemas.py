from typing import List
from pydantic import BaseModel

class StudentOrganizationRegistrationMetric(BaseModel):
    registered_student_orgs_count: int = 340
    active_org_members_total: int = 14200
    student_engagement_portal_adoption_pct: float = 94.8

class GreekLifeChapterComplianceAudit(BaseModel):
    greek_chapters_active: int = 38
    hazing_prevention_training_compliance_pct: float = 100.0
    greek_chapter_avg_gpa: float = 3.42

class PhilanthropyCommunityServiceMetric(BaseModel):
    philanthropy_funds_raised_usd: float = 850000.0
    community_service_hours_logged: int = 42000

class StudentOrgEventRiskManagementAudit(BaseModel):
    registered_org_events_annual: int = 1420
    event_risk_management_plans_approved: int = 1420
    zero_severe_incidents: bool = True

class StudentOrgFinancialAccountAudit(BaseModel):
    org_bank_accounts_audited: int = 340
    financial_compliance_score_pct: float = 98.8

class LeadershipAdvisorTrainingMetric(BaseModel):
    trained_faculty_advisors_count: int = 280
    advisor_satisfaction_score: float = 4.8

class DeterministicGreekLifePipelineResult(BaseModel):
    registration: StudentOrganizationRegistrationMetric
    greek_compliance: GreekLifeChapterComplianceAudit
    philanthropy: PhilanthropyCommunityServiceMetric
    risk_management: StudentOrgEventRiskManagementAudit
    finances: StudentOrgFinancialAccountAudit
    advisors: LeadershipAdvisorTrainingMetric
    org_health_score: float
    confidence_score: float

class StrategicGreekLifeNarrative(BaseModel):
    org_summary: str
    key_org_strengths: List[str]

class StudentOrgManagementPlan(BaseModel):
    management_actions: List[str]
    sample_hazing_compliance_declaration: str

class ReasoningGreekLifePipelineResult(BaseModel):
    narrative: StrategicGreekLifeNarrative
    management_plan: StudentOrgManagementPlan
    reasoning_steps: List[str]

class GreekLifeStudentOrgsOrchestratorReport(BaseModel):
    department: str = "Greek Life & Student Organizations"
    department_id: str = "dept_077"
    org_tier: str = "EXEMPLARY CAMPUS LIFE INVOLVEMENT"
    org_health_score: float
    confidence_score: float
    deterministic_analysis: DeterministicGreekLifePipelineResult
    reasoning_analysis: ReasoningGreekLifePipelineResult
    reasoning_steps: List[str]
