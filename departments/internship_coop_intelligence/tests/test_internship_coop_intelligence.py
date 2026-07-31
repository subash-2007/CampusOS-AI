import pytest, asyncio
from departments.internship_coop_intelligence.deterministic import (
    InternshipPlacementRateMeterAgent, InternshipConversionRateMeterAgent, StipendCompensationMeterAgent,
    EmployerSatisfactionAuditorAgent, AcademicCreditComplianceAuditorAgent, SkillGrowthMeterAgent, InternshipProgramScorerAgent
)
from departments.internship_coop_intelligence.orchestrator import InternshipCoopOrchestratorAgent

def test_internship_placement_rate_meter():
    res = InternshipPlacementRateMeterAgent().run(1850)
    assert res.placement_rate_pct >= 80.0
    assert res.placed_students_count > 1000

def test_internship_conversion_rate_meter():
    res = InternshipConversionRateMeterAgent().run()
    assert res.intern_to_fulltime_offer_pct >= 40.0

def test_stipend_compensation_meter():
    res = StipendCompensationMeterAgent().run()
    assert res.avg_hourly_stipend_usd > 15.0
    assert res.paid_internships_pct >= 80.0

def test_employer_satisfaction_auditor():
    res = EmployerSatisfactionAuditorAgent().run()
    assert res.employer_csat_pct >= 90.0

def test_academic_credit_compliance_auditor():
    res = AcademicCreditComplianceAuditorAgent().run()
    assert res.university_credit_approved_pct >= 90.0

def test_skill_growth_meter():
    res = SkillGrowthMeterAgent().run()
    assert res.avg_skill_score_increase_pct > 0.0

def test_internship_program_scorer():
    res = InternshipProgramScorerAgent().run(1850)
    assert res.internship_program_score >= 80.0
    assert res.confidence_score >= 0.5

def test_internship_coop_orchestrator():
    report = asyncio.run(InternshipCoopOrchestratorAgent().run_pipeline(1850))
    assert report.department == "Internship & Co-op Intelligence"
    assert report.department_id == "dept_052"
    assert report.internship_tier == "TOP TIER CO-OP PROGRAM"
    assert len(report.reasoning_steps) == 4
