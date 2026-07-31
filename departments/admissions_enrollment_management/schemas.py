from typing import List
from pydantic import BaseModel

class UndergraduateAdmissionsApplicationVolumeMetric(BaseModel):
    applications_received_count: int = 38500
    admitted_students_count: int = 14200
    admissions_selectivity_rate_pct: float = 36.8

class EnrollmentYieldDepositMetric(BaseModel):
    enrolled_freshmen_count: int = 4850
    enrollment_yield_rate_pct: float = 34.2
    tuition_deposit_fulfillment_pct: float = 98.6

class ApplicationHolisticReviewTurnaroundAudit(BaseModel):
    holistic_file_reviews_completed: int = 38500
    avg_application_review_days: float = 14.5
    holistic_rubric_audit_compliance_pct: float = 100.0

class CampusTourOpenHouseVisitorMetric(BaseModel):
    campus_tour_visitors_annual: int = 24500
    prospective_student_open_house_attendees: int = 8400
    tour_visitor_application_conversion_pct: float = 68.4

class CRMRecruitmentCampaignAudit(BaseModel):
    prospect_contacts_in_slate_crm: int = 185000
    email_campaign_open_rate_pct: float = 48.5
    inquiry_to_applicant_conversion_pct: float = 24.2

class HighSchoolGPAStandardizedTestAudit(BaseModel):
    enrolled_class_avg_gpa: float = 3.84
    test_optional_applicants_pct: float = 62.0

class DeterministicAdmissionsPipelineResult(BaseModel):
    volume: UndergraduateAdmissionsApplicationVolumeMetric
    yield_metric: EnrollmentYieldDepositMetric
    holistic_review: ApplicationHolisticReviewTurnaroundAudit
    tours: CampusTourOpenHouseVisitorMetric
    crm: CRMRecruitmentCampaignAudit
    academics: HighSchoolGPAStandardizedTestAudit
    admissions_score: float
    confidence_score: float

class StrategicAdmissionsNarrative(BaseModel):
    admissions_summary: str
    key_admissions_strengths: List[str]

class EnrollmentStrategyPlan(BaseModel):
    admissions_actions: List[str]
    sample_admissions_decision_letter_schema: str

class ReasoningAdmissionsPipelineResult(BaseModel):
    narrative: StrategicAdmissionsNarrative
    enrollment_plan: EnrollmentStrategyPlan
    reasoning_steps: List[str]

class AdmissionsEnrollmentManagementOrchestratorReport(BaseModel):
    department: str = "Admissions & Enrollment Management"
    department_id: str = "dept_089"
    admissions_tier: str = "PREMIER SELECTIVE ENROLLMENT ENTERPRISE"
    admissions_score: float
    confidence_score: float
    deterministic_analysis: DeterministicAdmissionsPipelineResult
    reasoning_analysis: ReasoningAdmissionsPipelineResult
    reasoning_steps: List[str]
