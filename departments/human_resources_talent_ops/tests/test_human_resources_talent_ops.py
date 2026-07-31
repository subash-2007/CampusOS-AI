import pytest, asyncio
from departments.human_resources_talent_ops.deterministic import (FacultyStaffRecruitmentTimeFillMeterAgent, EmployeeRetentionTurnoverAuditorAgent, BenefitsCompensationAdministrationAuditorAgent, EmployeePerformanceReviewCycleMeterAgent, StaffProfessionalDevelopmentTrainingMeterAgent, TitleIXEqualOpportunityComplianceAuditorAgent, HumanResourcesTalentOpsScorerAgent)
from departments.human_resources_talent_ops.orchestrator import HumanResourcesTalentOpsOrchestratorAgent

def test_faculty_staff_recruitment_time_fill_meter_agent():
    res = FacultyStaffRecruitmentTimeFillMeterAgent().run()
    assert res is not None

def test_employee_retention_turnover_auditor_agent():
    res = EmployeeRetentionTurnoverAuditorAgent().run()
    assert res is not None

def test_benefits_compensation_administration_auditor_agent():
    res = BenefitsCompensationAdministrationAuditorAgent().run()
    assert res is not None

def test_employee_performance_review_cycle_meter_agent():
    res = EmployeePerformanceReviewCycleMeterAgent().run()
    assert res is not None

def test_staff_professional_development_training_meter_agent():
    res = StaffProfessionalDevelopmentTrainingMeterAgent().run()
    assert res is not None

def test_title_i_x_equal_opportunity_compliance_auditor_agent():
    res = TitleIXEqualOpportunityComplianceAuditorAgent().run()
    assert res is not None

def test_human_resources_talent_ops_scorer():
    res = HumanResourcesTalentOpsScorerAgent().run()
    assert res.hr_score >= 50.0
    assert res.confidence_score >= 0.5

def test_human_resources_talent_ops_orchestrator():
    report = asyncio.run(HumanResourcesTalentOpsOrchestratorAgent().run_pipeline())
    assert report.department == "Campus Human Resources and Talent Operations"
    assert report.department_id == "dept_110"
    assert report.tier == "GREAT COLLEGES TO WORK FOR HIGHER ED HR EXCELLENCE"
    assert len(report.reasoning_steps) == 4
