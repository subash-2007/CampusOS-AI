import pytest, asyncio
from departments.global_engagement_partnerships.deterministic import (
    InternationalStudentEnrollmentMeterAgent, StudyAbroadParticipationMeterAgent, GlobalMOUPartnershipAgreementAuditorAgent,
    ELIProgramEnglishLanguageAuditorAgent, InternationalFacultyExchangeMeterAgent, CulturalExchangeLanguageProgramMeterAgent, GlobalEngagementPartnershipsScorerAgent
)
from departments.global_engagement_partnerships.orchestrator import GlobalEngagementPartnershipsOrchestratorAgent

def test_international_student_enrollment_meter():
    res = InternationalStudentEnrollmentMeterAgent().run(3840)
    assert res.students_enrolled_from_international_countries == 3840

def test_study_abroad_participation_meter():
    res = StudyAbroadParticipationMeterAgent().run()
    assert res.students_studying_abroad_annual >= 100

def test_global_mou_partnership_agreement_auditor():
    res = GlobalMOUPartnershipAgreementAuditorAgent().run()
    assert res.active_bilateral_mou_agreements >= 10

def test_eli_program_english_language_auditor():
    res = ELIProgramEnglishLanguageAuditorAgent().run()
    assert res.toefl_ielts_success_rate_pct >= 80.0

def test_international_faculty_exchange_meter():
    res = InternationalFacultyExchangeMeterAgent().run()
    assert res.joint_research_publications >= 10

def test_cultural_exchange_language_program_meter():
    res = CulturalExchangeLanguageProgramMeterAgent().run()
    assert res.international_cultural_events_annual >= 10

def test_global_engagement_partnerships_scorer():
    res = GlobalEngagementPartnershipsScorerAgent().run(3840)
    assert res.global_score >= 80.0
    assert res.confidence_score >= 0.5

def test_global_engagement_partnerships_orchestrator():
    report = asyncio.run(GlobalEngagementPartnershipsOrchestratorAgent().run_pipeline(3840))
    assert report.department == "Global Engagement & International Partnerships"
    assert report.department_id == "dept_101"
    assert report.global_tier == "WORLD-CLASS GLOBAL ENGAGEMENT INSTITUTION"
    assert len(report.reasoning_steps) == 4
