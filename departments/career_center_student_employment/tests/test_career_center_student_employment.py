import pytest, asyncio
from departments.career_center_student_employment.deterministic import (
    CampusCareerFairEmployerEngagementMeterAgent, OnCampusStudentEmploymentPayrollAuditorAgent, CareerAdvisingAppointmentVolumeMeterAgent,
    MockInterviewSkillVerificationAuditorAgent, OnCampusRecruitingOCRInterviewScheduleMeterAgent, FirstDestinationCareerOutcomeAuditorAgent, CareerCenterStudentEmploymentScorerAgent
)
from departments.career_center_student_employment.orchestrator import CareerCenterStudentEmploymentOrchestratorAgent

def test_campus_career_fair_employer_engagement_meter():
    res = CampusCareerFairEmployerEngagementMeterAgent().run(680)
    assert res.participating_employers_count == 680
    assert res.student_career_fair_attendees >= 10000

def test_on_campus_student_employment_payroll_auditor():
    res = OnCampusStudentEmploymentPayrollAuditorAgent().run()
    assert res.student_payroll_compliance_score_pct == 100.0

def test_career_advising_appointment_volume_meter():
    res = CareerAdvisingAppointmentVolumeMeterAgent().run()
    assert res.one_on_one_career_coaching_appointments >= 5000
    assert res.advising_csat_score >= 4.0

def test_mock_interview_skill_verification_auditor():
    res = MockInterviewSkillVerificationAuditorAgent().run()
    assert res.interview_readiness_score_pct >= 85.0

def test_on_campus_recruiting_ocr_interview_schedule_meter():
    res = OnCampusRecruitingOCRInterviewScheduleMeterAgent().run()
    assert res.employer_job_postings_handshake >= 10000

def test_first_destination_career_outcome_auditor():
    res = FirstDestinationCareerOutcomeAuditorAgent().run()
    assert res.employed_or_grad_school_at_6_months_pct >= 90.0
    assert res.avg_starting_salary_usd >= 50000.0

def test_career_center_student_employment_scorer():
    res = CareerCenterStudentEmploymentScorerAgent().run(680)
    assert res.career_center_score >= 90.0
    assert res.confidence_score >= 0.5

def test_career_center_student_employment_orchestrator():
    report = asyncio.run(CareerCenterStudentEmploymentOrchestratorAgent().run_pipeline(680))
    assert report.department == "Career Center & Student Employment"
    assert report.department_id == "dept_086"
    assert report.career_center_tier == "TOP-TIER NATIONAL CAREER & EMPLOYMENT CENTER"
    assert len(report.reasoning_steps) == 4
