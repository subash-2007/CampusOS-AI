import pytest, asyncio
from departments.dining_culinary_services.deterministic import (
    CulinaryMenuRecipeRotationMeterAgent, ExecutiveChefStaffingCertAuditorAgent, FarmToTableLocalSourcingMeterAgent,
    SpecialtyDietaryStationAuditorAgent, CulinaryTasteTestCSATAuditorAgent, CulinaryEventThemeNightMeterAgent, DiningCulinaryServicesScorerAgent
)
from departments.dining_culinary_services.orchestrator import DiningCulinaryServicesOrchestratorAgent

def test_culinary_menu_recipe_rotation_meter():
    res = CulinaryMenuRecipeRotationMeterAgent().run(1450)
    assert res.unique_recipes_served_per_semester == 1450
    assert res.culinary_diversity_score_pct >= 90.0

def test_executive_chef_staffing_cert_auditor():
    res = ExecutiveChefStaffingCertAuditorAgent().run()
    assert res.servsafe_manager_certification_pct == 100.0

def test_farm_to_table_local_sourcing_meter():
    res = FarmToTableLocalSourcingMeterAgent().run()
    assert res.local_farm_partnerships_count >= 20

def test_specialty_dietary_station_auditor():
    res = SpecialtyDietaryStationAuditorAgent().run()
    assert res.dietitian_approved_recipe_pct >= 90.0

def test_culinary_taste_test_csat_auditor():
    res = CulinaryTasteTestCSATAuditorAgent().run()
    assert res.student_culinary_taste_csat_score >= 4.0

def test_culinary_event_theme_night_meter():
    res = CulinaryEventThemeNightMeterAgent().run()
    assert res.theme_night_culinary_events_annual >= 20

def test_dining_culinary_services_scorer():
    res = DiningCulinaryServicesScorerAgent().run(1450)
    assert res.culinary_score >= 90.0
    assert res.confidence_score >= 0.5

def test_dining_culinary_services_orchestrator():
    report = asyncio.run(DiningCulinaryServicesOrchestratorAgent().run_pipeline(1450))
    assert report.department == "Campus Dining Culinary Services"
    assert report.department_id == "dept_092"
    assert report.culinary_tier == "AWARD-WINNING CAMPUS CULINARY EXCELLENCE"
    assert len(report.reasoning_steps) == 4
