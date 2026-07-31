import pytest, asyncio
from departments.sustainability_green_campus.deterministic import (
    SolarRenewableEnergyGenMeterAgent, CampusWasteDiversionRecyclingAuditorAgent, LEEDCertifiedBuildingAuditorAgent,
    WaterConservationRainwaterMeterAgent, GreenSustainabilityCurriculumAuditorAgent, STARSScoringAASHEAuditorAgent, SustainabilityGreenCampusScorerAgent
)
from departments.sustainability_green_campus.orchestrator import SustainabilityGreenCampusOrchestratorAgent

def test_solar_renewable_energy_gen_meter():
    res = SolarRenewableEnergyGenMeterAgent().run(4850000.0)
    assert res.solar_panels_installed_kwh == 4850000.0
    assert res.renewable_energy_share_pct >= 50.0

def test_campus_waste_diversion_recycling_auditor():
    res = CampusWasteDiversionRecyclingAuditorAgent().run()
    assert res.waste_diversion_rate_pct >= 60.0

def test_leed_certified_building_auditor():
    res = LEEDCertifiedBuildingAuditorAgent().run()
    assert res.leed_certified_buildings_count >= 15

def test_water_conservation_rainwater_meter():
    res = WaterConservationRainwaterMeterAgent().run()
    assert res.low_flow_plumbing_coverage_pct >= 90.0

def test_green_sustainability_curriculum_auditor():
    res = GreenSustainabilityCurriculumAuditorAgent().run()
    assert res.sustainability_courses_offered >= 100

def test_stars_scoring_aashe_auditor():
    res = STARSScoringAASHEAuditorAgent().run()
    assert "STARS" in res.aashe_stars_rating
    assert res.stars_total_score_points >= 70.0

def test_sustainability_green_campus_scorer():
    res = SustainabilityGreenCampusScorerAgent().run(4850000.0)
    assert res.sustainability_score >= 75.0
    assert res.confidence_score >= 0.5

def test_sustainability_green_campus_orchestrator():
    report = asyncio.run(SustainabilityGreenCampusOrchestratorAgent().run_pipeline(4850000.0))
    assert report.department == "Sustainability & Green Campus"
    assert report.department_id == "dept_079"
    assert report.sustainability_tier == "STARS GOLD CLIMATE LEADER"
    assert len(report.reasoning_steps) == 4
