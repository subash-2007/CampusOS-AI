from typing import List
from pydantic import BaseModel

class CulinaryMenuRecipeRotationMetric(BaseModel):
    unique_recipes_served_per_semester: int = 1450
    seasonal_menu_rotations_count: int = 4
    culinary_diversity_score_pct: float = 94.8

class ExecutiveChefStaffingCertAudit(BaseModel):
    certified_executive_chefs_count: int = 18
    servsafe_manager_certification_pct: float = 100.0
    culinary_staff_training_hours_annual: int = 4200

class FarmToTableLocalSourcingMetric(BaseModel):
    local_farm_partnerships_count: int = 38
    sustainable_seafood_procurement_pct: float = 88.5
    organic_produce_spend_pct: float = 32.4

class SpecialtyDietaryStationAudit(BaseModel):
    gluten_free_dedicated_kitchens: int = 4
    top_9_allergen_free_stations: int = 6
    dietitian_approved_recipe_pct: float = 98.2

class CulinaryTasteTestCSATAudit(BaseModel):
    student_culinary_taste_csat_score: float = 4.78
    dining_hall_feedback_submissions_annual: int = 14200

class CulinaryEventThemeNightMetric(BaseModel):
    theme_night_culinary_events_annual: int = 48
    theme_night_attendees_average: int = 3200

class DeterministicCulinaryPipelineResult(BaseModel):
    menus: CulinaryMenuRecipeRotationMetric
    chefs: ExecutiveChefStaffingCertAudit
    farm_to_table: FarmToTableLocalSourcingMetric
    dietary: SpecialtyDietaryStationAudit
    csat: CulinaryTasteTestCSATAudit
    events: CulinaryEventThemeNightMetric
    culinary_score: float
    confidence_score: float

class StrategicCulinaryNarrative(BaseModel):
    culinary_summary: str
    key_culinary_strengths: List[str]

class CulinaryOperationsPlan(BaseModel):
    culinary_actions: List[str]
    sample_farm_to_table_menu_schema: str

class ReasoningCulinaryPipelineResult(BaseModel):
    narrative: StrategicCulinaryNarrative
    culinary_plan: CulinaryOperationsPlan
    reasoning_steps: List[str]

class DiningCulinaryServicesOrchestratorReport(BaseModel):
    department: str = "Campus Dining Culinary Services"
    department_id: str = "dept_092"
    culinary_tier: str = "AWARD-WINNING CAMPUS CULINARY EXCELLENCE"
    culinary_score: float
    confidence_score: float
    deterministic_analysis: DeterministicCulinaryPipelineResult
    reasoning_analysis: ReasoningCulinaryPipelineResult
    reasoning_steps: List[str]
