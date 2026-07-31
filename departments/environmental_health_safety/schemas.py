from typing import List
from pydantic import BaseModel

class LaboratoryChemicalInventoryAudit(BaseModel):
    chemical_inventory_items_managed: int = 48000
    properly_labeled_containers_pct: float = 99.2
    expired_chemicals_disposed_annual: int = 1240

class OccupationalSafetyOSHATrainingMetric(BaseModel):
    osha_training_completions_annual: int = 4200
    lab_safety_certifications_annual: int = 1840
    safety_incident_rate_per_100_workers: float = 0.84

class EnvironmentalPermitWastewaterAudit(BaseModel):
    epa_permits_in_compliance: int = 48
    stormwater_inspections_annual: int = 12
    wastewater_discharge_violations: int = 0

class RadiationBiosafetyIBCComplianceAudit(BaseModel):
    ibc_protocol_approvals_annual: int = 184
    radiation_license_reviews_completed: int = 28
    bsl2_lab_audits_completed: int = 48

class FireLifeSafetySystemInspectionMetric(BaseModel):
    fire_suppression_inspections_completed: int = 840
    emergency_exit_lighting_inspections: int = 2840
    fire_drills_per_building_annual: float = 2.0

class ADAFacilitiesAccessibilityAudit(BaseModel):
    ada_compliance_inspections_completed: int = 380
    barrier_removal_projects_annual: int = 48
    transition_plan_completion_pct: float = 94.8

class DeterministicEHSPipelineResult(BaseModel):
    chemicals: LaboratoryChemicalInventoryAudit
    osha: OccupationalSafetyOSHATrainingMetric
    wastewater: EnvironmentalPermitWastewaterAudit
    biosafety: RadiationBiosafetyIBCComplianceAudit
    fire: FireLifeSafetySystemInspectionMetric
    ada: ADAFacilitiesAccessibilityAudit
    ehs_score: float
    confidence_score: float

class StrategicEHSNarrative(BaseModel):
    ehs_summary: str
    key_ehs_strengths: List[str]

class EHSCompliancePlan(BaseModel):
    ehs_actions: List[str]
    sample_hazmat_incident_schema: str

class ReasoningEHSPipelineResult(BaseModel):
    narrative: StrategicEHSNarrative
    ehs_plan: EHSCompliancePlan
    reasoning_steps: List[str]

class EnvironmentalHealthSafetyOrchestratorReport(BaseModel):
    department: str = "Environmental Health and Safety Compliance"
    department_id: str = "dept_103"
    ehs_tier: str = "EPA AND OSHA MODEL COMPLIANCE INSTITUTION"
    ehs_score: float
    confidence_score: float
    deterministic_analysis: DeterministicEHSPipelineResult
    reasoning_analysis: ReasoningEHSPipelineResult
    reasoning_steps: List[str]
