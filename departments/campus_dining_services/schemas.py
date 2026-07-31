from typing import List
from pydantic import BaseModel

class DiningMealPlanActiveMetric(BaseModel):
    active_meal_plans_count: int = 12400
    daily_meals_served: int = 34500
    dining_hall_locations_count: int = 8

class FoodSafetyHealthInspectionAudit(BaseModel):
    health_inspection_score_avg: float = 98.4
    food_safety_audits_passed_pct: float = 100.0
    zero_critical_violations: bool = True

class DietaryAllergenLabelingAudit(BaseModel):
    vegan_vegetarian_options_pct: float = 42.5
    halal_kosher_certified_pct: float = 34.0
    allergen_ingredient_labeling_pct: float = 99.8

class MobileFoodOrderingMetric(BaseModel):
    mobile_orders_processed_annual: int = 420000
    avg_pickup_wait_time_minutes: float = 6.2
    mobile_ordering_app_rating: float = 4.75

class FoodWasteSustainabilityAudit(BaseModel):
    composted_food_waste_tons: float = 142.5
    donated_surplus_meals: int = 18500
    local_farm_sourcing_pct: float = 38.0

class CampusFoodPantryInsecurityAudit(BaseModel):
    food_pantry_visits_annual: int = 4200
    food_insecurity_grant_funds_usd: float = 180000.0

class DeterministicDiningPipelineResult(BaseModel):
    meal_plans: DiningMealPlanActiveMetric
    food_safety: FoodSafetyHealthInspectionAudit
    dietary_labeling: DietaryAllergenLabelingAudit
    mobile_ordering: MobileFoodOrderingMetric
    sustainability: FoodWasteSustainabilityAudit
    food_pantry: CampusFoodPantryInsecurityAudit
    dining_services_score: float
    confidence_score: float

class StrategicDiningNarrative(BaseModel):
    dining_summary: str
    key_dining_strengths: List[str]

class CampusDiningPlan(BaseModel):
    dining_improvement_actions: List[str]
    sample_nutrition_allergen_schema: str

class ReasoningDiningPipelineResult(BaseModel):
    narrative: StrategicDiningNarrative
    dining_plan: CampusDiningPlan
    reasoning_steps: List[str]

class CampusDiningServicesOrchestratorReport(BaseModel):
    department: str = "Campus Dining & Food Services"
    department_id: str = "dept_069"
    dining_tier: str = "PREMIER SUSTAINABLE DINING NETWORK"
    dining_services_score: float
    confidence_score: float
    deterministic_analysis: DeterministicDiningPipelineResult
    reasoning_analysis: ReasoningDiningPipelineResult
    reasoning_steps: List[str]
