import pytest, asyncio
from departments.high_school_outreach.deterministic import (
    HighSchoolPartnerCountMeterAgent, K12STEMProgramParticipationMeterAgent, DualEnrollmentCreditAuditorAgent,
    CampusTourVisitMeterAgent, CounselorRelationshipAuditorAgent, OutreachScholarshipMeterAgent, HighSchoolOutreachScorerAgent
)
from departments.high_school_outreach.orchestrator import HighSchoolOutreachOrchestratorAgent

def test_high_school_partner_count_meter():
    res = HighSchoolPartnerCountMeterAgent().run(184)
    assert res.partner_high_schools_count == 184
    assert res.title_1_schools_supported_pct >= 30.0

def test_k12_stem_program_participation_meter():
    res = K12STEMProgramParticipationMeterAgent().run()
    assert res.stem_camps_hosted >= 10
    assert res.female_minority_stem_pct >= 50.0

def test_dual_enrollment_credit_auditor():
    res = DualEnrollmentCreditAuditorAgent().run()
    assert res.dual_enrollment_students_count >= 500
    assert res.matriculation_rate_post_hs_pct >= 40.0

def test_campus_tour_visit_meter():
    res = CampusTourVisitMeterAgent().run()
    assert res.tour_satisfaction_score >= 4.0

def test_counselor_relationship_auditor():
    res = CounselorRelationshipAuditorAgent().run()
    assert res.registered_hs_counselors >= 300

def test_outreach_scholarship_meter():
    res = OutreachScholarshipMeterAgent().run()
    assert res.k12_outreach_grants_awarded_usd > 100000.0

def test_high_school_outreach_scorer():
    res = HighSchoolOutreachScorerAgent().run(184)
    assert res.outreach_health_score >= 80.0
    assert res.confidence_score >= 0.5

def test_high_school_outreach_orchestrator():
    report = asyncio.run(HighSchoolOutreachOrchestratorAgent().run_pipeline(184))
    assert report.department == "High School & K-12 Outreach"
    assert report.department_id == "dept_062"
    assert report.outreach_tier == "STRATEGIC PIPELINE FEEDER"
    assert len(report.reasoning_steps) == 4
