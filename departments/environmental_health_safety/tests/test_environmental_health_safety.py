import pytest, asyncio
from departments.environmental_health_safety.deterministic import (
    LaboratoryChemicalInventoryAuditorAgent, OccupationalSafetyOSHATrainingMeterAgent, EnvironmentalPermitWastewaterAuditorAgent,
    RadiationBiosafetyIBCComplianceAuditorAgent, FireLifeSafetySystemInspectionMeterAgent, ADAFacilitiesAccessibilityAuditorAgent, EnvironmentalHealthSafetyComplianceScorerAgent
)
from departments.environmental_health_safety.orchestrator import EnvironmentalHealthSafetyOrchestratorAgent

def test_laboratory_chemical_inventory_auditor():
    res = LaboratoryChemicalInventoryAuditorAgent().run()
    assert res.properly_labeled_containers_pct >= 95.0

def test_occupational_safety_osha_training_meter():
    res = OccupationalSafetyOSHATrainingMeterAgent().run()
    assert res.osha_training_completions_annual >= 100

def test_environmental_permit_wastewater_auditor():
    res = EnvironmentalPermitWastewaterAuditorAgent().run()
    assert res.wastewater_discharge_violations == 0

def test_radiation_biosafety_ibc_compliance_auditor():
    res = RadiationBiosafetyIBCComplianceAuditorAgent().run()
    assert res.ibc_protocol_approvals_annual >= 10

def test_fire_life_safety_system_inspection_meter():
    res = FireLifeSafetySystemInspectionMeterAgent().run()
    assert res.fire_suppression_inspections_completed >= 100

def test_ada_facilities_accessibility_auditor():
    res = ADAFacilitiesAccessibilityAuditorAgent().run()
    assert res.transition_plan_completion_pct >= 80.0

def test_environmental_health_safety_compliance_scorer():
    res = EnvironmentalHealthSafetyComplianceScorerAgent().run()
    assert res.ehs_score >= 90.0
    assert res.confidence_score >= 0.5

def test_environmental_health_safety_orchestrator():
    report = asyncio.run(EnvironmentalHealthSafetyOrchestratorAgent().run_pipeline())
    assert report.department == "Environmental Health and Safety Compliance"
    assert report.department_id == "dept_103"
    assert report.ehs_tier == "EPA AND OSHA MODEL COMPLIANCE INSTITUTION"
    assert len(report.reasoning_steps) == 4
