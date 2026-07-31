from departments.shared.scoring import ScoringEngine
from departments.sustainability_green_campus.schemas import (
    SolarRenewableEnergyGenMetric, CampusWasteDiversionRecyclingAudit, LEEDCertifiedBuildingAudit,
    WaterConservationRainwaterMetric, GreenSustainabilityCurriculumAudit, STARSScoringAASHEAudit, DeterministicSustainabilityPipelineResult
)

class SolarRenewableEnergyGenMeterAgent:
    """Agent 1: Measures solar generation (kWh), renewable energy percentage, and carbon offset tons."""
    def run(self, generation_kwh: float = 4850000.0) -> SolarRenewableEnergyGenMetric:
        return SolarRenewableEnergyGenMetric(solar_panels_installed_kwh=generation_kwh, renewable_energy_share_pct=64.5, carbon_emissions_offset_tons=3400.0)

class CampusWasteDiversionRecyclingAuditorAgent:
    """Agent 2: Audits campus waste diversion rate percentage, recycling/compost tons, and zero-waste buildings."""
    def run(self) -> CampusWasteDiversionRecyclingAudit:
        return CampusWasteDiversionRecyclingAudit(waste_diversion_rate_pct=72.4, recycling_compost_tons_annual=1250.0, zero_waste_certified_buildings=14)

class LEEDCertifiedBuildingAuditorAgent:
    """Agent 3: Audits LEED certified building counts, LEED Gold/Platinum buildings, and EUI reduction percentage."""
    def run(self) -> LEEDCertifiedBuildingAudit:
        return LEEDCertifiedBuildingAudit(leed_certified_buildings_count=24, leed_platinum_gold_buildings=18, energy_use_intensity_eui_reduction_pct=38.2)

class WaterConservationRainwaterMeterAgent:
    """Agent 4: Measures rainwater harvesting volume, low-flow plumbing coverage, and reclaimed irrigation percentage."""
    def run(self) -> WaterConservationRainwaterMetric:
        return WaterConservationRainwaterMetric(rainwater_harvesting_gallons=850000, low_flow_plumbing_coverage_pct=98.4, campus_irrigation_reclaimed_water_pct=88.0)

class GreenSustainabilityCurriculumAuditorAgent:
    """Agent 5: Audits sustainability course offerings and student green eco-reps headcount."""
    def run(self) -> GreenSustainabilityCurriculumAudit:
        return GreenSustainabilityCurriculumAudit(sustainability_courses_offered=210, student_green_eco_reps_count=140)

class STARSScoringAASHEAuditorAgent:
    """Agent 6: Audits AASHE STARS rating (Gold/Platinum) and STARS total score points."""
    def run(self) -> STARSScoringAASHEAudit:
        return STARSScoringAASHEAudit(aashe_stars_rating="STARS Gold", stars_total_score_points=78.5)

class SustainabilityGreenCampusScorerAgent:
    """Agent 7: Master deterministic aggregator for Sustainability & Green Campus."""
    def __init__(self):
        self.energy_agent = SolarRenewableEnergyGenMeterAgent()
        self.waste_agent = CampusWasteDiversionRecyclingAuditorAgent()
        self.leed_agent = LEEDCertifiedBuildingAuditorAgent()
        self.water_agent = WaterConservationRainwaterMeterAgent()
        self.curriculum_agent = GreenSustainabilityCurriculumAuditorAgent()
        self.stars_agent = STARSScoringAASHEAuditorAgent()

    def run(self, generation_kwh: float = 4850000.0) -> DeterministicSustainabilityPipelineResult:
        renewable_energy = self.energy_agent.run(generation_kwh)
        waste_diversion = self.waste_agent.run()
        leed_buildings = self.leed_agent.run()
        water_conservation = self.water_agent.run()
        green_curriculum = self.curriculum_agent.run()
        stars_rating = self.stars_agent.run()

        metrics = {
            "stars_points": stars_rating.stars_total_score_points,
            "waste_diversion": waste_diversion.waste_diversion_rate_pct,
            "renewable_share": renewable_energy.renewable_energy_share_pct,
            "low_flow_plumbing": water_conservation.low_flow_plumbing_coverage_pct
        }
        weights = {"stars_points": 0.35, "waste_diversion": 0.30, "renewable_share": 0.20, "low_flow_plumbing": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(int(renewable_energy.solar_panels_installed_kwh / 1000.0), 100)
        return DeterministicSustainabilityPipelineResult(
            renewable_energy=renewable_energy, waste_diversion=waste_diversion,
            leed_buildings=leed_buildings, water_conservation=water_conservation,
            green_curriculum=green_curriculum, stars_rating=stars_rating,
            sustainability_score=score, confidence_score=confidence
        )
