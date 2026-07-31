from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.residential_housing_operations.schemas import (
    StrategicResidentialHousingNarrative, ResidentialHousingOperationsPlan, ReasoningResidentialHousingPipelineResult, DeterministicResidentialHousingPipelineResult
)

class StrategicResidentialHousingNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates residence hall keycard electronic access control, housekeeping sanitation compliance, and smart package locker operations."""
    def __init__(self):
        super().__init__(agent_id="strategic_residential_housing_narrative", name="Strategic Residential Housing Narrative Agent",
                         description="Evaluates keycard door access uptime, residence hall sanitation inspection scores, IoT laundry machine availability, and mailroom package fulfillment.", icon="Key")

    async def evaluate(self, det: DeterministicResidentialHousingPipelineResult) -> StrategicResidentialHousingNarrative:
        fallback = {
            "residential_housing_summary": f"Premier smart campus residential facility ({det.residential_housing_score:.1f}% score). Managing {det.security.electronic_keycard_doors_managed:,} electronic keycard doors ({det.security.access_control_uptime_pct}% access uptime), {det.housekeeping.daily_sanitation_inspection_score_pct}% sanitation inspection score, {det.laundry.laundry_machine_uptime_pct}% laundry machine uptime.",
            "key_residential_housing_strengths": [f"{det.mailroom.student_packages_processed_annual:,} student packages processed with average {det.mailroom.smart_locker_pickup_time_avg_hours:.1f}-hour smart locker pickup and low {det.mailroom.package_misplacement_rate_pct}% misplacement rate", f"{det.hvac.smart_thermostat_coverage_pct}% smart thermostat coverage across residence halls achieving {det.hvac.building_energy_efficiency_score:.1f}% building energy efficiency score"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Director of Residential Housing Operations & Facilities Management", "keycard access, housekeeping sanitation, HVAC energy, IoT laundry, smart package lockers"),
                                          PromptBuilder.build_user_context({"score": det.residential_housing_score}), task_type="housing_ops_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicResidentialHousingNarrative(residential_housing_summary=parsed.get("residential_housing_summary", fallback["residential_housing_summary"]),
                                                       key_residential_housing_strengths=parsed.get("key_residential_housing_strengths", fallback["key_residential_housing_strengths"]))
        except Exception:
            return StrategicResidentialHousingNarrative(**fallback)

class ResidentialHousingOperationsPlannerAgent(BaseAgent):
    """Agent 9: Formulates mobile NFC room door keyless entry systems and IoT smart laundry notification networks."""
    def __init__(self):
        super().__init__(agent_id="residential_housing_operations_planner", name="Residential Housing Operations Planner Agent",
                         description="Formulates mobile app NFC keyless room entry, smart package barcode scanning, and HVAC predictive maintenance algorithms.", icon="ShieldCheck")

    async def plan_housing_operations(self, det: DeterministicResidentialHousingPipelineResult) -> ResidentialHousingOperationsPlan:
        fallback = {
            "residential_housing_actions": ["Deploy Smart Mobile Wallet NFC Door Locks replacing physical plastic keycards", "Launch Automated Smart Package Locker System notifying residents instantly via push notification"],
            "sample_package_locker_notification_schema": '{\n  "package_id": "PKG_2026_88190",\n  "resident_id": "res_99182",\n  "carrier": "FedEx Express",\n  "locker_unit": "Founders Hall Smart Locker #42",\n  "pickup_pin_code": "849201",\n  "qr_code_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",\n  "delivery_timestamp": "2026-10-14T14:15:00Z",\n  "notification_status": "DELIVERED TO LOCKER & PUSH NOTIFICATION SENT TO MOBILE APP"\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Housing Facilities Operations Specialist", "package locker notification, NFC door lock, IoT laundry app"),
                                          PromptBuilder.build_user_context({"doors": det.security.electronic_keycard_doors_managed}), task_type="housing_ops_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return ResidentialHousingOperationsPlan(residential_housing_actions=parsed.get("residential_housing_actions", fallback["residential_housing_actions"]),
                                                    sample_package_locker_notification_schema=parsed.get("sample_package_locker_notification_schema", fallback["sample_package_locker_notification_schema"]))
        except Exception:
            return ResidentialHousingOperationsPlan(**fallback)
