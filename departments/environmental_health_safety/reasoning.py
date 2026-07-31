from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.environmental_health_safety.schemas import (
    StrategicEHSNarrative, EHSCompliancePlan, ReasoningEHSPipelineResult, DeterministicEHSPipelineResult
)

class StrategicEHSNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates EPA/OSHA regulatory compliance scores, laboratory chemical inventory safety ratings, and biosafety protocol adherence."""
    def __init__(self):
        super().__init__(agent_id="strategic_ehs_narrative", name="Strategic EHS Narrative Agent",
                         description="Evaluates EPA permit compliance, OSHA training completion rates, chemical inventory labeling, biosafety IBC protocols, fire safety inspections, and ADA transition plan progress.", icon="AlertCircle")

    async def evaluate(self, det: DeterministicEHSPipelineResult) -> StrategicEHSNarrative:
        fallback = {
            "ehs_summary": f"EPA and OSHA model compliance institution ({det.ehs_score:.1f}% score). Managing {det.chemicals.chemical_inventory_items_managed:,} chemical inventory items at {det.chemicals.properly_labeled_containers_pct}% labeling compliance, {det.wastewater.wastewater_discharge_violations} wastewater violations, {det.osha.osha_training_completions_annual:,} annual OSHA training completions.",
            "key_ehs_strengths": [f"Zero EPA wastewater discharge violations with {det.wastewater.epa_permits_in_compliance} active EPA permits maintained in full compliance", f"{det.ada.ada_compliance_inspections_completed} ADA compliance inspections with {det.ada.transition_plan_completion_pct}% transition plan completion and {det.ada.barrier_removal_projects_annual} barrier removal projects annually"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Director of Environmental Health and Safety", "EPA, OSHA, chemical inventory, biosafety, fire safety, ADA compliance"), PromptBuilder.build_user_context({"score": det.ehs_score}), task_type="ehs_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicEHSNarrative(ehs_summary=parsed.get("ehs_summary", fallback["ehs_summary"]), key_ehs_strengths=parsed.get("key_ehs_strengths", fallback["key_ehs_strengths"]))
        except Exception:
            return StrategicEHSNarrative(**fallback)

class EHSCompliancePlannerAgent(BaseAgent):
    """Agent 9: Formulates AI-powered chemical inventory digital management systems and automated EPA permit monitoring dashboards."""
    def __init__(self):
        super().__init__(agent_id="ehs_compliance_planner", name="EHS Compliance Planner Agent",
                         description="Formulates AI chemical inventory ERP systems, IoT biosafety lab monitoring, and automated EPA compliance reporting workflows.", icon="Activity")

    async def plan_ehs_compliance(self, det: DeterministicEHSPipelineResult) -> EHSCompliancePlan:
        fallback = {
            "ehs_actions": ["Deploy AI Chemical Inventory Management System (CIMS) with real-time barcode scanning, automatic GHS labeling validation, and expiration date alerts", "Launch IoT Biosafety Lab Monitoring Network installing real-time CO2, temperature, and pressure sensors in all BSL-2 laboratories"],
            "sample_hazmat_incident_schema": '{\n  "incident_id": "EHS_2026_00142",\n  "incident_type": "Hazardous Material Spill - Laboratory",\n  "chemical_spilled": "Sodium Hydroxide (NaOH) - 2 Liters",\n  "location": "Organic Chemistry Lab, Building C, Room 218",\n  "incident_date": "2026-10-08",\n  "response_team": "EHS Emergency Response Team + Campus Police",\n  "personal_protective_equipment": "PPE Level B - Chemical Splash Goggles, Gloves, Lab Coat",\n  "epa_reportable": false,\n  "corrective_action": "Improved secondary containment requirements for all corrosive chemicals >1L",\n  "root_cause": "Missing drip tray under chemical storage cabinet"\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("EHS Director and Environmental Compliance Officer", "AI chemical inventory, IoT biosafety monitoring, EPA automation, OSHA training"), PromptBuilder.build_user_context({"chemicals": det.chemicals.chemical_inventory_items_managed}), task_type="ehs_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return EHSCompliancePlan(ehs_actions=parsed.get("ehs_actions", fallback["ehs_actions"]), sample_hazmat_incident_schema=parsed.get("sample_hazmat_incident_schema", fallback["sample_hazmat_incident_schema"]))
        except Exception:
            return EHSCompliancePlan(**fallback)
