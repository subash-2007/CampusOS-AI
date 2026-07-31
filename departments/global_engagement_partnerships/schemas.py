from typing import List
from pydantic import BaseModel

class InternationalStudentEnrollmentMetric(BaseModel):
    students_enrolled_from_international_countries: int = 3840
    visa_sponsorship_active_count: int = 3680
    international_student_avg_gpa: float = 3.62

class StudyAbroadParticipationMetric(BaseModel):
    students_studying_abroad_annual: int = 1840
    semester_programs_pct: float = 58.4
    stem_study_abroad_participants: int = 480

class GlobalMOUPartnershipAgreementAudit(BaseModel):
    active_bilateral_mou_agreements: int = 184
    joint_degree_programs_operational: int = 12
    dual_diploma_enrollments: int = 84

class ELIProgramEnglishLanguageAudit(BaseModel):
    eli_program_enrollment: int = 480
    toefl_ielts_success_rate_pct: float = 92.4
    eli_graduate_persistence_pct: float = 88.6

class InternationalFacultyExchangeMetric(BaseModel):
    visiting_international_scholars_hosted: int = 84
    outbound_faculty_sabbaticals: int = 28
    joint_research_publications: int = 184

class CulturalExchangeLanguageProgramMetric(BaseModel):
    international_cultural_events_annual: int = 124
    language_exchange_pairs_active: int = 380
    global_festival_attendance: int = 8400

class DeterministicGlobalEngagementPipelineResult(BaseModel):
    intl_students: InternationalStudentEnrollmentMetric
    study_abroad: StudyAbroadParticipationMetric
    mou: GlobalMOUPartnershipAgreementAudit
    eli: ELIProgramEnglishLanguageAudit
    faculty_exchange: InternationalFacultyExchangeMetric
    cultural: CulturalExchangeLanguageProgramMetric
    global_score: float
    confidence_score: float

class StrategicGlobalEngagementNarrative(BaseModel):
    global_summary: str
    key_global_strengths: List[str]

class GlobalEngagementPlan(BaseModel):
    global_actions: List[str]
    sample_study_abroad_program_schema: str

class ReasoningGlobalEngagementPipelineResult(BaseModel):
    narrative: StrategicGlobalEngagementNarrative
    global_plan: GlobalEngagementPlan
    reasoning_steps: List[str]

class GlobalEngagementPartnershipsOrchestratorReport(BaseModel):
    department: str = "Global Engagement & International Partnerships"
    department_id: str = "dept_101"
    global_tier: str = "WORLD-CLASS GLOBAL ENGAGEMENT INSTITUTION"
    global_score: float
    confidence_score: float
    deterministic_analysis: DeterministicGlobalEngagementPipelineResult
    reasoning_analysis: ReasoningGlobalEngagementPipelineResult
    reasoning_steps: List[str]
