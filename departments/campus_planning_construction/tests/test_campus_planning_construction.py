import pytest, asyncio
from departments.campus_planning_construction.deterministic import (CapitalProjectBudgetCompletionAuditorAgent, LEEDGreenBuildingCertificationMeterAgent, CampusMasterPlanMilestoneMeterAgent, SpaceUtilizationClassroomLabAuditorAgent, DeferredMaintenanceBacklogAuditorAgent, CampusAccessibilityUniversalDesignAuditorAgent, CampusPlanningConstructionScorerAgent)
from departments.campus_planning_construction.orchestrator import CampusPlanningConstructionOrchestratorAgent

def test_capital_project_budget_completion_auditor_agent():
    res = CapitalProjectBudgetCompletionAuditorAgent().run()
    assert res is not None

def test_l_e_e_d_green_building_certification_meter_agent():
    res = LEEDGreenBuildingCertificationMeterAgent().run()
    assert res is not None

def test_campus_master_plan_milestone_meter_agent():
    res = CampusMasterPlanMilestoneMeterAgent().run()
    assert res is not None

def test_space_utilization_classroom_lab_auditor_agent():
    res = SpaceUtilizationClassroomLabAuditorAgent().run()
    assert res is not None

def test_deferred_maintenance_backlog_auditor_agent():
    res = DeferredMaintenanceBacklogAuditorAgent().run()
    assert res is not None

def test_campus_accessibility_universal_design_auditor_agent():
    res = CampusAccessibilityUniversalDesignAuditorAgent().run()
    assert res is not None

def test_campus_planning_construction_scorer():
    res = CampusPlanningConstructionScorerAgent().run()
    assert res.planning_score >= 50.0
    assert res.confidence_score >= 0.5

def test_campus_planning_construction_orchestrator():
    report = asyncio.run(CampusPlanningConstructionOrchestratorAgent().run_pipeline())
    assert report.department == "Campus Planning and Capital Construction"
    assert report.department_id == "dept_104"
    assert report.tier == "LEED PLATINUM CAMPUS MASTER PLAN INSTITUTION"
    assert len(report.reasoning_steps) == 4
