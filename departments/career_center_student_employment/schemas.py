from typing import List
from pydantic import BaseModel

class CampusCareerFairEmployerEngagementMetric(BaseModel):
    career_fairs_hosted_annual: int = 12
    participating_employers_count: int = 680
    student_career_fair_attendees: int = 14500

class OnCampusStudentEmploymentPayrollAudit(BaseModel):
    student_employees_hired_on_campus: int = 4200
    federal_work_study_fws_disbursed_usd: float = 3800000.0
    student_payroll_compliance_score_pct: float = 100.0

class CareerAdvisingAppointmentVolumeMetric(BaseModel):
    one_on_one_career_coaching_appointments: int = 9400
    resume_critique_turnaround_hours: float = 18.5
    advising_csat_score: float = 4.88

class MockInterviewSkillVerificationAudit(BaseModel):
    mock_interviews_conducted: int = 2800
    ai_interview_prep_portal_active_users: int = 6400
    interview_readiness_score_pct: float = 92.4

class OnCampusRecruitingOCRInterviewScheduleMetric(BaseModel):
    on_campus_interviews_conducted: int = 1850
    employer_job_postings_handshake: int = 24500

class FirstDestinationCareerOutcomeAudit(BaseModel):
    first_destination_knowledge_rate_pct: float = 88.5
    employed_or_grad_school_at_6_months_pct: float = 95.2
    avg_starting_salary_usd: float = 72400.0

class DeterministicCareerCenterPipelineResult(BaseModel):
    fairs: CampusCareerFairEmployerEngagementMetric
    employment: OnCampusStudentEmploymentPayrollAudit
    advising: CareerAdvisingAppointmentVolumeMetric
    mock_interviews: MockInterviewSkillVerificationAudit
    recruiting: OnCampusRecruitingOCRInterviewScheduleMetric
    outcomes: FirstDestinationCareerOutcomeAudit
    career_center_score: float
    confidence_score: float

class StrategicCareerCenterNarrative(BaseModel):
    career_center_summary: str
    key_career_center_strengths: List[str]

class CareerDevelopmentPlan(BaseModel):
    career_actions: List[str]
    sample_first_destination_survey_schema: str

class ReasoningCareerCenterPipelineResult(BaseModel):
    narrative: StrategicCareerCenterNarrative
    career_plan: CareerDevelopmentPlan
    reasoning_steps: List[str]

class CareerCenterStudentEmploymentOrchestratorReport(BaseModel):
    department: str = "Career Center & Student Employment"
    department_id: str = "dept_086"
    career_center_tier: str = "TOP-TIER NATIONAL CAREER & EMPLOYMENT CENTER"
    career_center_score: float
    confidence_score: float
    deterministic_analysis: DeterministicCareerCenterPipelineResult
    reasoning_analysis: ReasoningCareerCenterPipelineResult
    reasoning_steps: List[str]
