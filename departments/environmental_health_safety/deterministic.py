from departments.shared.scoring import ScoringEngine
from departments.environmental_health_safety.schemas import (
    LaboratoryChemicalInventoryAudit, OccupationalSafetyOSHATrainingMetric, EnvironmentalPermitWastewaterAudit,
    RadiationBiosafetyIBCComplianceAudit, FireLifeSafetySystemInspectionMetric, ADAFacilitiesAccessibilityAudit, DeterministicEHSPipelineResult
)

class LaboratoryChemicalInventoryAuditorAgent:
    """Agent 1: Audits chemical inventory items managed, properly labeled containers percentage, and expired chemicals disposed."""
    def run(self) -> LaboratoryChemicalInventoryAudit:
        return LaboratoryChemicalInventoryAudit()

class OccupationalSafetyOSHATrainingMeterAgent:
    """Agent 2: Measures OSHA training completions, lab safety certifications, and safety incident rate per 100 workers."""
    def run(self) -> OccupationalSafetyOSHATrainingMetric:
        return OccupationalSafetyOSHATrainingMetric()

class EnvironmentalPermitWastewaterAuditorAgent:
    """Agent 3: Audits EPA permits in compliance, stormwater inspections, and wastewater discharge violations."""
    def run(self) -> EnvironmentalPermitWastewaterAudit:
        return EnvironmentalPermitWastewaterAudit()

class RadiationBiosafetyIBCComplianceAuditorAgent:
    """Agent 4: Audits IBC protocol approvals, radiation license reviews, and BSL-2 lab audits completed."""
    def run(self) -> RadiationBiosafetyIBCComplianceAudit:
        return RadiationBiosafetyIBCComplianceAudit()

class FireLifeSafetySystemInspectionMeterAgent:
    """Agent 5: Measures fire suppression inspections, emergency exit lighting inspections, and fire drills per building."""
    def run(self) -> FireLifeSafetySystemInspectionMetric:
        return FireLifeSafetySystemInspectionMetric()

class ADAFacilitiesAccessibilityAuditorAgent:
    """Agent 6: Audits ADA compliance inspections, barrier removal projects, and transition plan completion percentage."""
    def run(self) -> ADAFacilitiesAccessibilityAudit:
        return ADAFacilitiesAccessibilityAudit()

class EnvironmentalHealthSafetyComplianceScorerAgent:
    """Agent 7: Master deterministic aggregator for Environmental Health and Safety Compliance."""
    def __init__(self):
        self.chemicals_agent = LaboratoryChemicalInventoryAuditorAgent()
        self.osha_agent = OccupationalSafetyOSHATrainingMeterAgent()
        self.wastewater_agent = EnvironmentalPermitWastewaterAuditorAgent()
        self.biosafety_agent = RadiationBiosafetyIBCComplianceAuditorAgent()
        self.fire_agent = FireLifeSafetySystemInspectionMeterAgent()
        self.ada_agent = ADAFacilitiesAccessibilityAuditorAgent()

    def run(self) -> DeterministicEHSPipelineResult:
        chemicals = self.chemicals_agent.run()
        osha = self.osha_agent.run()
        wastewater = self.wastewater_agent.run()
        biosafety = self.biosafety_agent.run()
        fire = self.fire_agent.run()
        ada = self.ada_agent.run()
        metrics = {
            "chemical_labeling": chemicals.properly_labeled_containers_pct,
            "wastewater_compliance": max(0.0, 100.0 - (wastewater.wastewater_discharge_violations * 20)),
            "ada_completion": ada.transition_plan_completion_pct,
            "fire_inspection": min(100.0, (fire.fire_suppression_inspections_completed / 8) * 100)
        }
        weights = {"chemical_labeling": 0.30, "wastewater_compliance": 0.35, "ada_completion": 0.20, "fire_inspection": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(osha.osha_training_completions_annual, 100)
        return DeterministicEHSPipelineResult(
            chemicals=chemicals, osha=osha, wastewater=wastewater,
            biosafety=biosafety, fire=fire, ada=ada,
            ehs_score=score, confidence_score=confidence
        )
