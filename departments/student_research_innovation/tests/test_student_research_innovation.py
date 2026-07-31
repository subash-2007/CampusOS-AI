import pytest, asyncio
from departments.student_research_innovation.deterministic import (
    UndergraduateResearchProgramMeterAgent, StartupIncubatorVentureMeterAgent, PatentTechTransferAuditorAgent,
    MakerspaceFabLabUsageMeterAgent, InnovationChallengeGrantMeterAgent, IndustryPartnershipResearchAgreementAuditorAgent, StudentResearchInnovationScorerAgent
)
from departments.student_research_innovation.orchestrator import StudentResearchInnovationOrchestratorAgent

def test_undergraduate_research_program_meter():
    res = UndergraduateResearchProgramMeterAgent().run()
    assert res.undergraduate_researchers_active >= 100

def test_startup_incubator_venture_meter():
    res = StartupIncubatorVentureMeterAgent().run()
    assert res.student_startups_in_incubator >= 5
    assert res.seed_funding_awarded_total_usd > 0

def test_patent_tech_transfer_auditor():
    res = PatentTechTransferAuditorAgent().run()
    assert res.patents_filed_annual >= 10
    assert res.tech_transfer_royalties_usd > 0

def test_makerspace_fab_lab_usage_meter():
    res = MakerspaceFabLabUsageMeterAgent().run()
    assert res.makerspace_student_active_users >= 100
    assert res.makerspace_equipment_utilization_pct >= 40.0

def test_innovation_challenge_grant_meter():
    res = InnovationChallengeGrantMeterAgent().run()
    assert res.innovation_grants_awarded >= 10

def test_industry_partnership_research_agreement_auditor():
    res = IndustryPartnershipResearchAgreementAuditorAgent().run()
    assert res.sponsored_research_revenue_millions > 0

def test_student_research_innovation_scorer():
    res = StudentResearchInnovationScorerAgent().run()
    assert res.innovation_score >= 80.0
    assert res.confidence_score >= 0.5

def test_student_research_innovation_orchestrator():
    report = asyncio.run(StudentResearchInnovationOrchestratorAgent().run_pipeline())
    assert report.department == "Student Research & Innovation Incubator"
    assert report.department_id == "dept_100"
    assert report.innovation_tier == "NATIONALLY RANKED STUDENT INNOVATION ECOSYSTEM"
    assert len(report.reasoning_steps) == 4
