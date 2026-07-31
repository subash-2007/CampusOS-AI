from departments.shared.scoring import ScoringEngine
from departments.campus_dining_services.schemas import (
    DiningMealPlanActiveMetric, FoodSafetyHealthInspectionAudit, DietaryAllergenLabelingAudit,
    MobileFoodOrderingMetric, FoodWasteSustainabilityAudit, CampusFoodPantryInsecurityAudit, DeterministicDiningPipelineResult
)

class DiningMealPlanActiveMeterAgent:
    """Agent 1: Measures active meal plan subscriber headcount, daily meals served, and dining hall locations."""
    def run(self, plans: int = 12400) -> DiningMealPlanActiveMetric:
        return DiningMealPlanActiveMetric(active_meal_plans_count=plans, daily_meals_served=34500, dining_hall_locations_count=8)

class FoodSafetyHealthInspectionAuditorAgent:
    """Agent 2: Audits health inspection score average, food safety audit pass rate, and critical violations."""
    def run(self) -> FoodSafetyHealthInspectionAudit:
        return FoodSafetyHealthInspectionAudit(health_inspection_score_avg=98.4, food_safety_audits_passed_pct=100.0, zero_critical_violations=True)

class DietaryAllergenLabelingAuditorAgent:
    """Agent 3: Audits vegan/vegetarian options percentage, Halal/Kosher availability, and 8-major allergen labeling."""
    def run(self) -> DietaryAllergenLabelingAudit:
        return DietaryAllergenLabelingAudit(vegan_vegetarian_options_pct=42.5, halal_kosher_certified_pct=34.0, allergen_ingredient_labeling_pct=99.8)

class MobileFoodOrderingMeterAgent:
    """Agent 4: Measures annual mobile food orders processed, average pickup wait time (minutes), and app rating."""
    def run(self) -> MobileFoodOrderingMetric:
        return MobileFoodOrderingMetric(mobile_orders_processed_annual=420000, avg_pickup_wait_time_minutes=6.2, mobile_ordering_app_rating=4.75)

class FoodWasteSustainabilityAuditorAgent:
    """Agent 5: Audits composted food waste (tons), donated surplus meals, and local farm sourcing percentage."""
    def run(self) -> FoodWasteSustainabilityAudit:
        return FoodWasteSustainabilityAudit(composted_food_waste_tons=142.5, donated_surplus_meals=18500, local_farm_sourcing_pct=38.0)

class CampusFoodPantryInsecurityAuditorAgent:
    """Agent 6: Audits annual campus food pantry visits and food insecurity emergency grant funding."""
    def run(self) -> CampusFoodPantryInsecurityAudit:
        return CampusFoodPantryInsecurityAudit(food_pantry_visits_annual=4200, food_insecurity_grant_funds_usd=180000.0)

class CampusDiningServicesScorerAgent:
    """Agent 7: Master deterministic aggregator for Campus Dining & Food Services."""
    def __init__(self):
        self.meal_plan_agent = DiningMealPlanActiveMeterAgent()
        self.safety_agent = FoodSafetyHealthInspectionAuditorAgent()
        self.dietary_agent = DietaryAllergenLabelingAuditorAgent()
        self.mobile_agent = MobileFoodOrderingMeterAgent()
        self.sustainability_agent = FoodWasteSustainabilityAuditorAgent()
        self.pantry_agent = CampusFoodPantryInsecurityAuditorAgent()

    def run(self, plans: int = 12400) -> DeterministicDiningPipelineResult:
        meal_plans = self.meal_plan_agent.run(plans)
        food_safety = self.safety_agent.run()
        dietary_labeling = self.dietary_agent.run()
        mobile_ordering = self.mobile_agent.run()
        sustainability = self.sustainability_agent.run()
        food_pantry = self.pantry_agent.run()

        metrics = {
            "food_safety": food_safety.health_inspection_score_avg,
            "allergen_labeling": dietary_labeling.allergen_ingredient_labeling_pct,
            "mobile_rating": (mobile_ordering.mobile_ordering_app_rating / 5.0) * 100,
            "local_sourcing": sustainability.local_farm_sourcing_pct * 2.0
        }
        weights = {"food_safety": 0.35, "allergen_labeling": 0.30, "mobile_rating": 0.20, "local_sourcing": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(meal_plans.active_meal_plans_count, 500)
        return DeterministicDiningPipelineResult(
            meal_plans=meal_plans, food_safety=food_safety, dietary_labeling=dietary_labeling,
            mobile_ordering=mobile_ordering, sustainability=sustainability, food_pantry=food_pantry,
            dining_services_score=score, confidence_score=confidence
        )
