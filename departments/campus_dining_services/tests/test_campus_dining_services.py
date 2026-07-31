import pytest, asyncio
from departments.campus_dining_services.deterministic import (
    DiningMealPlanActiveMeterAgent, FoodSafetyHealthInspectionAuditorAgent, DietaryAllergenLabelingAuditorAgent,
    MobileFoodOrderingMeterAgent, FoodWasteSustainabilityAuditorAgent, CampusFoodPantryInsecurityAuditorAgent, CampusDiningServicesScorerAgent
)
from departments.campus_dining_services.orchestrator import CampusDiningServicesOrchestratorAgent

def test_dining_meal_plan_active_meter():
    res = DiningMealPlanActiveMeterAgent().run(12400)
    assert res.active_meal_plans_count == 12400
    assert res.daily_meals_served >= 20000

def test_food_safety_health_inspection_auditor():
    res = FoodSafetyHealthInspectionAuditorAgent().run()
    assert res.health_inspection_score_avg >= 95.0
    assert res.zero_critical_violations is True

def test_dietary_allergen_labeling_auditor():
    res = DietaryAllergenLabelingAuditorAgent().run()
    assert res.allergen_ingredient_labeling_pct >= 95.0
    assert res.vegan_vegetarian_options_pct >= 30.0

def test_mobile_food_ordering_meter():
    res = MobileFoodOrderingMeterAgent().run()
    assert res.avg_pickup_wait_time_minutes <= 10.0
    assert res.mobile_ordering_app_rating >= 4.0

def test_food_waste_sustainability_auditor():
    res = FoodWasteSustainabilityAuditorAgent().run()
    assert res.composted_food_waste_tons > 50.0
    assert res.donated_surplus_meals >= 10000

def test_campus_food_pantry_insecurity_auditor():
    res = CampusFoodPantryInsecurityAuditorAgent().run()
    assert res.food_pantry_visits_annual >= 2000

def test_campus_dining_services_scorer():
    res = CampusDiningServicesScorerAgent().run(12400)
    assert res.dining_services_score >= 88.0
    assert res.confidence_score >= 0.5

def test_campus_dining_services_orchestrator():
    report = asyncio.run(CampusDiningServicesOrchestratorAgent().run_pipeline(12400))
    assert report.department == "Campus Dining & Food Services"
    assert report.department_id == "dept_069"
    assert report.dining_tier == "PREMIER SUSTAINABLE DINING NETWORK"
    assert len(report.reasoning_steps) == 4
