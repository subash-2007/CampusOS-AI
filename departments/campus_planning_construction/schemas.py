from typing import List
from pydantic import BaseModel

class CapitalProjectBudgetCompletionAudit(BaseModel):
    capital_projects_active: int = 28
    projects_on_budget_pct: float = 92.4
    projects_on_schedule_pct: float = 88.6

class LEEDGreenBuildingCertificationMetric(BaseModel):
    leed_certified_buildings_count: int = 48
    leed_platinum_buildings: int = 8
    energy_star_buildings: int = 24

class CampusMasterPlanMilestoneMetric(BaseModel):
    campus_master_plan_milestones_completed: int = 48
    total_master_plan_milestones: int = 52
    master_plan_completion_pct: float = 92.3

class SpaceUtilizationClassroomLabAudit(BaseModel):
    classrooms_utilization_rate_pct: float = 74.8
    research_lab_utilization_rate_pct: float = 82.4
    gross_sq_ft_campus_total: int = 4800000

class DeferredMaintenanceBacklogAudit(BaseModel):
    deferred_maintenance_backlog_millions: float = 84.0
    facility_condition_index_score_pct: float = 88.4
    pm_work_orders_completed_annual: int = 48000

class CampusAccessibilityUniversalDesignAudit(BaseModel):
    universal_design_features_installed: int = 840
    accessible_routes_pct: float = 96.4
    signage_braille_wayfinding_compliance_pct: float = 98.2

class DeterministicCampusPlanningConstructionPipelineResult(BaseModel):
    capital: CapitalProjectBudgetCompletionAudit
    leed: LEEDGreenBuildingCertificationMetric
    master_plan: CampusMasterPlanMilestoneMetric
    space: SpaceUtilizationClassroomLabAudit
    deferred_maint: DeferredMaintenanceBacklogAudit
    ada: CampusAccessibilityUniversalDesignAudit
    planning_score: float
    confidence_score: float

class StrategicPlanningNarrative(BaseModel):
    planning_summary: str
    key_planning_strengths: List[str]

class PlanningOperationsPlan(BaseModel):
    planning_actions: List[str]
    sample_schema_data: str

class ReasoningPlanningPipelineResult(BaseModel):
    narrative: StrategicPlanningNarrative
    plan: PlanningOperationsPlan
    reasoning_steps: List[str]

class CampusPlanningConstructionOrchestratorReport(BaseModel):
    department: str = "Campus Planning and Capital Construction"
    department_id: str = "dept_104"
    tier: str = "LEED PLATINUM CAMPUS MASTER PLAN INSTITUTION"
    planning_score: float
    confidence_score: float
    deterministic_analysis: DeterministicCampusPlanningConstructionPipelineResult
    reasoning_analysis: ReasoningPlanningPipelineResult
    reasoning_steps: List[str]
