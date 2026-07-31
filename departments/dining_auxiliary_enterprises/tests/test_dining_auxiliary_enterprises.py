import pytest, asyncio
from departments.dining_auxiliary_enterprises.deterministic import (
    DiningHallMealPlanSubscriptionMeterAgent, AuxiliaryRevenueRetailSalesAuditorAgent, DietaryNutritionAllergenComplianceAuditorAgent,
    SustainableFoodSourcingWasteAuditorAgent, MobileOrderCampusCardIntegrationMeterAgent, DiningFacilityHealthSafetyInspectionAuditorAgent, DiningAuxiliaryEnterprisesScorerAgent
)
from departments.dining_auxiliary_enterprises.orchestrator import DiningAuxiliaryEnterprisesOrchestratorAgent

def test_dining_hall_meal_plan_subscription_meter():
    res = DiningHallMealPlanSubscriptionMeterAgent().run(12500)
    assert res.active_meal_plan_subscribers == 12500
    assert res.commuter_meal_plan_adoption_pct >= 30.0

def test_auxiliary_revenue_retail_sales_auditor():
    res = AuxiliaryRevenueRetailSalesAuditorAgent().run()
    assert res.annual_auxiliary_revenue_usd > 10000000.0

def test_dietary_nutrition_allergen_compliance_auditor():
    res = DietaryNutritionAllergenComplianceAuditorAgent().run()
    assert res.allergen_labeling_accuracy_pct == 100.0

def test_sustainable_food_sourcing_waste_auditor():
    res = SustainableFoodSourcingWasteAuditorAgent().run()
    assert res.food_waste_composted_lbs_annual >= 100000.0

def test_mobile_order_campus_card_integration_meter():
    res = MobileOrderCampusCardIntegrationMeterAgent().run()
    assert res.mobile_dining_orders_annual >= 500000
    assert res.avg_pickup_wait_time_minutes <= 10.0

def test_dining_facility_health_safety_inspection_auditor():
    res = DiningFacilityHealthSafetyInspectionAuditorAgent().run()
    assert res.health_department_inspection_score_avg >= 95.0
    assert res.critical_food_safety_violations == 0

def test_dining_auxiliary_enterprises_scorer():
    res = DiningAuxiliaryEnterprisesScorerAgent().run(12500)
    assert res.dining_auxiliary_score >= 88.0
    assert res.confidence_score >= 0.5

def test_dining_auxiliary_enterprises_orchestrator():
    report = asyncio.run(DiningAuxiliaryEnterprisesOrchestratorAgent().run_pipeline(12500))
    assert report.department == "Campus Dining Auxiliary Enterprises"
    assert report.department_id == "dept_082"
    assert report.dining_auxiliary_tier == "PREMIER AUXILIARY DINING & RETAIL ENTERPRISE"
    assert len(report.reasoning_steps) == 4
