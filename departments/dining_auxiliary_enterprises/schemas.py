from typing import List
from pydantic import BaseModel

class DiningHallMealPlanSubscriptionMetric(BaseModel):
    active_meal_plan_subscribers: int = 12500
    residential_unlimited_meal_plans: int = 8200
    commuter_meal_plan_adoption_pct: float = 38.5

class AuxiliaryRevenueRetailSalesAudit(BaseModel):
    annual_auxiliary_revenue_usd: float = 28500000.0
    retail_food_court_sales_usd: float = 8400000.0
    vending_micro_market_revenue_usd: float = 1850000.0

class DietaryNutritionAllergenComplianceAudit(BaseModel):
    vegan_vegetarian_menu_options_pct: float = 42.0
    halal_kosher_certified_stations: int = 8
    allergen_labeling_accuracy_pct: float = 100.0

class SustainableFoodSourcingWasteAudit(BaseModel):
    locally_sourced_food_pct: float = 34.5
    food_waste_composted_lbs_annual: float = 450000.0
    trayless_dining_water_savings_gallons: int = 1200000

class MobileOrderCampusCardIntegrationMetric(BaseModel):
    mobile_dining_orders_annual: int = 840000
    campus_card_mobile_wallet_transactions: int = 1450000
    avg_pickup_wait_time_minutes: float = 4.5

class DiningFacilityHealthSafetyInspectionAudit(BaseModel):
    health_department_inspection_score_avg: float = 98.8
    critical_food_safety_violations: int = 0

class DeterministicDiningAuxiliaryPipelineResult(BaseModel):
    meal_plans: DiningHallMealPlanSubscriptionMetric
    revenue: AuxiliaryRevenueRetailSalesAudit
    nutrition: DietaryNutritionAllergenComplianceAudit
    sustainability: SustainableFoodSourcingWasteAudit
    mobile_orders: MobileOrderCampusCardIntegrationMetric
    health_safety: DiningFacilityHealthSafetyInspectionAudit
    dining_auxiliary_score: float
    confidence_score: float

class StrategicDiningAuxiliaryNarrative(BaseModel):
    dining_auxiliary_summary: str
    key_dining_auxiliary_strengths: List[str]

class DiningAuxiliaryOperationsPlan(BaseModel):
    dining_auxiliary_actions: List[str]
    sample_meal_plan_flex_dollar_schema: str

class ReasoningDiningAuxiliaryPipelineResult(BaseModel):
    narrative: StrategicDiningAuxiliaryNarrative
    operations_plan: DiningAuxiliaryOperationsPlan
    reasoning_steps: List[str]

class DiningAuxiliaryEnterprisesOrchestratorReport(BaseModel):
    department: str = "Campus Dining Auxiliary Enterprises"
    department_id: str = "dept_082"
    dining_auxiliary_tier: str = "PREMIER AUXILIARY DINING & RETAIL ENTERPRISE"
    dining_auxiliary_score: float
    confidence_score: float
    deterministic_analysis: DeterministicDiningAuxiliaryPipelineResult
    reasoning_analysis: ReasoningDiningAuxiliaryPipelineResult
    reasoning_steps: List[str]
