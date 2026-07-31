from typing import List
from pydantic import BaseModel

class SolarRenewableEnergyGenMetric(BaseModel):
    solar_panels_installed_kwh: float = 4850000.0
    renewable_energy_share_pct: float = 64.5
    carbon_emissions_offset_tons: float = 3400.0

class CampusWasteDiversionRecyclingAudit(BaseModel):
    waste_diversion_rate_pct: float = 72.4
    recycling_compost_tons_annual: float = 1250.0
    zero_waste_certified_buildings: int = 14

class LEEDCertifiedBuildingAudit(BaseModel):
    leed_certified_buildings_count: int = 24
    leed_platinum_gold_buildings: int = 18
    energy_use_intensity_eui_reduction_pct: float = 38.2

class WaterConservationRainwaterMetric(BaseModel):
    rainwater_harvesting_gallons: int = 850000
    low_flow_plumbing_coverage_pct: float = 98.4
    campus_irrigation_reclaimed_water_pct: float = 88.0

class GreenSustainabilityCurriculumAudit(BaseModel):
    sustainability_courses_offered: int = 210
    student_green_eco_reps_count: int = 140

class STARSScoringAASHEAudit(BaseModel):
    aashe_stars_rating: str = "STARS Gold"
    stars_total_score_points: float = 78.5

class DeterministicSustainabilityPipelineResult(BaseModel):
    renewable_energy: SolarRenewableEnergyGenMetric
    waste_diversion: CampusWasteDiversionRecyclingAudit
    leed_buildings: LEEDCertifiedBuildingAudit
    water_conservation: WaterConservationRainwaterMetric
    green_curriculum: GreenSustainabilityCurriculumAudit
    stars_rating: STARSScoringAASHEAudit
    sustainability_score: float
    confidence_score: float

class StrategicSustainabilityNarrative(BaseModel):
    sustainability_summary: str
    key_green_strengths: List[str]

class ClimateActionPlan(BaseModel):
    climate_actions: List[str]
    sample_decarbonization_roadmap_schema: str

class ReasoningSustainabilityPipelineResult(BaseModel):
    narrative: StrategicSustainabilityNarrative
    climate_plan: ClimateActionPlan
    reasoning_steps: List[str]

class SustainabilityGreenCampusOrchestratorReport(BaseModel):
    department: str = "Sustainability & Green Campus"
    department_id: str = "dept_079"
    sustainability_tier: str = "STARS GOLD CLIMATE LEADER"
    sustainability_score: float
    confidence_score: float
    deterministic_analysis: DeterministicSustainabilityPipelineResult
    reasoning_analysis: ReasoningSustainabilityPipelineResult
    reasoning_steps: List[str]
