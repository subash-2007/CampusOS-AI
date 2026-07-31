from departments.shared.scoring import ScoringEngine
from departments.campus_planning_construction.schemas import (CapitalProjectBudgetCompletionAudit, LEEDGreenBuildingCertificationMetric, CampusMasterPlanMilestoneMetric, SpaceUtilizationClassroomLabAudit, DeferredMaintenanceBacklogAudit, CampusAccessibilityUniversalDesignAudit, DeterministicCampusPlanningConstructionPipelineResult)

class CapitalProjectBudgetCompletionAuditorAgent:
    """Agent 1: Evaluates CapitalProjectBudgetCompletionAudit."""
    def run(self) -> CapitalProjectBudgetCompletionAudit:
        return CapitalProjectBudgetCompletionAudit()

class LEEDGreenBuildingCertificationMeterAgent:
    """Agent 2: Evaluates LEEDGreenBuildingCertificationMetric."""
    def run(self) -> LEEDGreenBuildingCertificationMetric:
        return LEEDGreenBuildingCertificationMetric()

class CampusMasterPlanMilestoneMeterAgent:
    """Agent 3: Evaluates CampusMasterPlanMilestoneMetric."""
    def run(self) -> CampusMasterPlanMilestoneMetric:
        return CampusMasterPlanMilestoneMetric()

class SpaceUtilizationClassroomLabAuditorAgent:
    """Agent 4: Evaluates SpaceUtilizationClassroomLabAudit."""
    def run(self) -> SpaceUtilizationClassroomLabAudit:
        return SpaceUtilizationClassroomLabAudit()

class DeferredMaintenanceBacklogAuditorAgent:
    """Agent 5: Evaluates DeferredMaintenanceBacklogAudit."""
    def run(self) -> DeferredMaintenanceBacklogAudit:
        return DeferredMaintenanceBacklogAudit()

class CampusAccessibilityUniversalDesignAuditorAgent:
    """Agent 6: Evaluates CampusAccessibilityUniversalDesignAudit."""
    def run(self) -> CampusAccessibilityUniversalDesignAudit:
        return CampusAccessibilityUniversalDesignAudit()

class CampusPlanningConstructionScorerAgent:
    """Agent 7: Master deterministic aggregator for Campus Planning and Capital Construction."""
    def __init__(self):
        self.capital_agent = CapitalProjectBudgetCompletionAuditorAgent()
        self.leed_agent = LEEDGreenBuildingCertificationMeterAgent()
        self.master_plan_agent = CampusMasterPlanMilestoneMeterAgent()
        self.space_agent = SpaceUtilizationClassroomLabAuditorAgent()
        self.deferred_maint_agent = DeferredMaintenanceBacklogAuditorAgent()
        self.ada_agent = CampusAccessibilityUniversalDesignAuditorAgent()

    def run(self) -> DeterministicCampusPlanningConstructionPipelineResult:
        capital = self.capital_agent.run()
        leed = self.leed_agent.run()
        master_plan = self.master_plan_agent.run()
        space = self.space_agent.run()
        deferred_maint = self.deferred_maint_agent.run()
        ada = self.ada_agent.run()
        metrics = {
            "budget_compliance": capital.projects_on_budget_pct,
            "schedule_compliance": capital.projects_on_schedule_pct,
            "master_plan": master_plan.master_plan_completion_pct,
            "fci_score": deferred_maint.facility_condition_index_score_pct
        }
        weights = {"budget_compliance": 0.30, "schedule_compliance": 0.25, "master_plan": 0.25, "fci_score": 0.20}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(capital.capital_projects_active, 10)
        return DeterministicCampusPlanningConstructionPipelineResult(
            capital=capital,
            leed=leed,
            master_plan=master_plan,
            space=space,
            deferred_maint=deferred_maint,
            ada=ada,
            planning_score=score, confidence_score=confidence
        )
