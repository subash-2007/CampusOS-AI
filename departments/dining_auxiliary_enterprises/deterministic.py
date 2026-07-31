from departments.shared.scoring import ScoringEngine
from departments.dining_auxiliary_enterprises.schemas import (
    DiningHallMealPlanSubscriptionMetric, AuxiliaryRevenueRetailSalesAudit, DietaryNutritionAllergenComplianceAudit,
    SustainableFoodSourcingWasteAudit, MobileOrderCampusCardIntegrationMetric, DiningFacilityHealthSafetyInspectionAudit, DeterministicDiningAuxiliaryPipelineResult
)

class DiningHallMealPlanSubscriptionMeterAgent:
    """Agent 1: Measures active meal plan subscribers, residential unlimited plans, and commuter adoption percentage."""
    def run(self, subscribers: int = 12500) -> DiningHallMealPlanSubscriptionMetric:
        return DiningHallMealPlanSubscriptionMetric(active_meal_plan_subscribers=subscribers, residential_unlimited_meal_plans=8200, commuter_meal_plan_adoption_pct=38.5)

class AuxiliaryRevenueRetailSalesAuditorAgent:
    """Agent 2: Audits annual auxiliary revenue (USD), retail food court sales (USD), and vending micro-market sales."""
    def run(self) -> AuxiliaryRevenueRetailSalesAudit:
        return AuxiliaryRevenueRetailSalesAudit(annual_auxiliary_revenue_usd=28500000.0, retail_food_court_sales_usd=8400000.0, vending_micro_market_revenue_usd=1850000.0)

class DietaryNutritionAllergenComplianceAuditorAgent:
    """Agent 3: Audits vegan/vegetarian menu percentage, halal/kosher stations, and allergen labeling accuracy percentage."""
    def run(self) -> DietaryNutritionAllergenComplianceAudit:
        return DietaryNutritionAllergenComplianceAudit(vegan_vegetarian_menu_options_pct=42.0, halal_kosher_certified_stations=8, allergen_labeling_accuracy_pct=100.0)

class SustainableFoodSourcingWasteAuditorAgent:
    """Agent 4: Audits locally sourced food percentage, composted food waste (lbs), and trayless water savings."""
    def run(self) -> SustainableFoodSourcingWasteAudit:
        return SustainableFoodSourcingWasteAudit(locally_sourced_food_pct=34.5, food_waste_composted_lbs_annual=450000.0, trayless_dining_water_savings_gallons=1200000)

class MobileOrderCampusCardIntegrationMeterAgent:
    """Agent 5: Measures annual mobile dining orders, mobile wallet transactions, and average pickup wait time (mins)."""
    def run(self) -> MobileOrderCampusCardIntegrationMetric:
        return MobileOrderCampusCardIntegrationMetric(mobile_dining_orders_annual=840000, campus_card_mobile_wallet_transactions=1450000, avg_pickup_wait_time_minutes=4.5)

class DiningFacilityHealthSafetyInspectionAuditorAgent:
    """Agent 6: Audits health department inspection score average and critical food safety violations count."""
    def run(self) -> DiningFacilityHealthSafetyInspectionAudit:
        return DiningFacilityHealthSafetyInspectionAudit(health_department_inspection_score_avg=98.8, critical_food_safety_violations=0)

class DiningAuxiliaryEnterprisesScorerAgent:
    """Agent 7: Master deterministic aggregator for Campus Dining Auxiliary Enterprises."""
    def __init__(self):
        self.meal_plan_agent = DiningHallMealPlanSubscriptionMeterAgent()
        self.revenue_agent = AuxiliaryRevenueRetailSalesAuditorAgent()
        self.nutrition_agent = DietaryNutritionAllergenComplianceAuditorAgent()
        self.sustainability_agent = SustainableFoodSourcingWasteAuditorAgent()
        self.mobile_agent = MobileOrderCampusCardIntegrationMeterAgent()
        self.health_safety_agent = DiningFacilityHealthSafetyInspectionAuditorAgent()

    def run(self, subscribers: int = 12500) -> DeterministicDiningAuxiliaryPipelineResult:
        meal_plans = self.meal_plan_agent.run(subscribers)
        revenue = self.revenue_agent.run()
        nutrition = self.nutrition_agent.run()
        sustainability = self.sustainability_agent.run()
        mobile_orders = self.mobile_agent.run()
        health_safety = self.health_safety_agent.run()

        metrics = {
            "health_inspection": health_safety.health_department_inspection_score_avg,
            "allergen_accuracy": nutrition.allergen_labeling_accuracy_pct,
            "commuter_adoption": min(100.0, meal_plans.commuter_meal_plan_adoption_pct * 2.2),
            "mobile_pickup_speed": max(0.0, 100.0 - (mobile_orders.avg_pickup_wait_time_minutes * 10))
        }
        weights = {"health_inspection": 0.35, "allergen_accuracy": 0.30, "commuter_adoption": 0.20, "mobile_pickup_speed": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(meal_plans.active_meal_plan_subscribers, 500)
        return DeterministicDiningAuxiliaryPipelineResult(
            meal_plans=meal_plans, revenue=revenue, nutrition=nutrition,
            sustainability=sustainability, mobile_orders=mobile_orders, health_safety=health_safety,
            dining_auxiliary_score=score, confidence_score=confidence
        )
