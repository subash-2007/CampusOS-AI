from departments.shared.scoring import ScoringEngine
from departments.auxiliary_enterprises_housing.schemas import (CampusHousingOccupancyRateMetric, CampusDiningMealPlanRevenueAudit, CampusBookstoreRetailOperationsAudit, ConferenceEventServicesRevenueMetric, CampusVendingLaundryConcessionAudit, FacilityMaintenanceWorkOrderTurnaroundMetric, DeterministicAuxiliaryEnterprisesHousingPipelineResult)

class CampusHousingOccupancyRateMeterAgent:
    """Agent 1: Evaluates CampusHousingOccupancyRateMetric."""
    def run(self) -> CampusHousingOccupancyRateMetric:
        return CampusHousingOccupancyRateMetric()

class CampusDiningMealPlanRevenueAuditorAgent:
    """Agent 2: Evaluates CampusDiningMealPlanRevenueAudit."""
    def run(self) -> CampusDiningMealPlanRevenueAudit:
        return CampusDiningMealPlanRevenueAudit()

class CampusBookstoreRetailOperationsAuditorAgent:
    """Agent 3: Evaluates CampusBookstoreRetailOperationsAudit."""
    def run(self) -> CampusBookstoreRetailOperationsAudit:
        return CampusBookstoreRetailOperationsAudit()

class ConferenceEventServicesRevenueMeterAgent:
    """Agent 4: Evaluates ConferenceEventServicesRevenueMetric."""
    def run(self) -> ConferenceEventServicesRevenueMetric:
        return ConferenceEventServicesRevenueMetric()

class CampusVendingLaundryConcessionAuditorAgent:
    """Agent 5: Evaluates CampusVendingLaundryConcessionAudit."""
    def run(self) -> CampusVendingLaundryConcessionAudit:
        return CampusVendingLaundryConcessionAudit()

class FacilityMaintenanceWorkOrderTurnaroundMeterAgent:
    """Agent 6: Evaluates FacilityMaintenanceWorkOrderTurnaroundMetric."""
    def run(self) -> FacilityMaintenanceWorkOrderTurnaroundMetric:
        return FacilityMaintenanceWorkOrderTurnaroundMetric()

class AuxiliaryEnterprisesHousingScorerAgent:
    """Agent 7: Master deterministic aggregator for Auxiliary Enterprises and Housing Operations."""
    def __init__(self):
        self.housing_agent = CampusHousingOccupancyRateMeterAgent()
        self.dining_agent = CampusDiningMealPlanRevenueAuditorAgent()
        self.bookstore_agent = CampusBookstoreRetailOperationsAuditorAgent()
        self.conference_agent = ConferenceEventServicesRevenueMeterAgent()
        self.vending_agent = CampusVendingLaundryConcessionAuditorAgent()
        self.work_orders_agent = FacilityMaintenanceWorkOrderTurnaroundMeterAgent()

    def run(self) -> DeterministicAuxiliaryEnterprisesHousingPipelineResult:
        housing = self.housing_agent.run()
        dining = self.dining_agent.run()
        bookstore = self.bookstore_agent.run()
        conference = self.conference_agent.run()
        vending = self.vending_agent.run()
        work_orders = self.work_orders_agent.run()
        metrics = {
            "housing_occupancy": housing.housing_occupancy_rate_pct,
            "dining_satisfaction": (dining.dining_satisfaction_score / 5.0) * 100,
            "inclusive_access": bookstore.course_materials_digital_inclusive_access_pct,
            "work_order_speed": max(0.0, 100.0 - (work_orders.avg_work_order_resolution_hours * 5))
        }
        weights = {"housing_occupancy": 0.35, "dining_satisfaction": 0.25, "inclusive_access": 0.20, "work_order_speed": 0.20}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(housing.residence_hall_beds_capacity, 10)
        return DeterministicAuxiliaryEnterprisesHousingPipelineResult(
            housing=housing,
            dining=dining,
            bookstore=bookstore,
            conference=conference,
            vending=vending,
            work_orders=work_orders,
            auxiliary_score=score, confidence_score=confidence
        )
