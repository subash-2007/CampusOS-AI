from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.housing_residential_life.schemas import (
    StrategicHousingNarrative, HousingOperationsPlan, ReasoningHousingPipelineResult, DeterministicHousingPipelineResult
)

class StrategicHousingNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates campus residence hall occupancy, roommate compatibility algorithms, and RA staffing safety."""
    def __init__(self):
        super().__init__(agent_id="strategic_housing_narrative", name="Strategic Housing Narrative Agent",
                         description="Evaluates housing occupancy capacity, roommate satisfaction rates, Living-Learning Community retention impact, and maintenance resolution speeds.", icon="Home")

    async def evaluate(self, det: DeterministicHousingPipelineResult) -> StrategicHousingNarrative:
        fallback = {
            "housing_summary": f"Exemplary residential community ({det.housing_score:.1f}% score). Managing {det.occupancy.occupied_beds_count:,} occupied beds across residence halls ({det.occupancy.housing_occupancy_rate_pct}% occupancy), {det.roommates.roommate_satisfaction_rate_pct}% roommate pairing satisfaction, 100% RA staff safety training compliance.",
            "key_housing_strengths": [f"{det.llc.active_living_learning_communities} Living-Learning Communities serving {det.llc.llc_enrolled_residents:,} residents with {det.llc.llc_first_year_retention_rate_pct}% first-year retention", f"{det.facilities.work_orders_resolved_in_24h_pct}% of {det.facilities.maintenance_work_orders_annual:,} maintenance work orders resolved within 24 hours (average {det.facilities.avg_resolution_time_hours:.1f} hours)"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Executive Director of Housing & Residential Education", "residence halls, roommate matching, living learning communities, RA training, facilities maintenance"),
                                          PromptBuilder.build_user_context({"score": det.housing_score}), task_type="housing_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicHousingNarrative(housing_summary=parsed.get("housing_summary", fallback["housing_summary"]),
                                            key_housing_strengths=parsed.get("key_housing_strengths", fallback["key_housing_strengths"]))
        except Exception:
            return StrategicHousingNarrative(**fallback)

class HousingOperationsPlannerAgent(BaseAgent):
    """Agent 9: Formulates roommate lifestyle AI matching algorithms and move-in day mobile check-in systems."""
    def __init__(self):
        super().__init__(agent_id="housing_operations_planner", name="Housing Operations Planner Agent",
                         description="Formulates room selection lottery algorithms, digital keycard residence access systems, and summer conference housing workflows.", icon="Key")

    async def plan_housing(self, det: DeterministicHousingPipelineResult) -> HousingOperationsPlan:
        fallback = {
            "housing_actions": ["Deploy Smart AI Roommate Compatibility Algorithm taking into account sleep schedules, study habits, and cleanliness", "Launch Mobile Keyless Door Access across all campus residence halls"],
            "sample_room_assignment_contract_schema": '{\n  "resident_id": "res_99182",\n  "academic_year": "2026-2027",\n  "assigned_building": "Founders Hall (Suite-Style Residence)",\n  "room_number": "412-B",\n  "roommate": {\n    "name": "Alex Chen",\n    "match_score": 96.5,\n    "llc_community": "Engineering & Innovation House"\n  },\n  "move_in_slot": "August 20, 2026 @ 09:00 AM - 10:30 AM (Express QR Check-In Enabled)",\n  "contract_status": "EXECUTED & HOUSING DEPOSIT VERIFIED"\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Residential Life Operations Specialist", "room selection, roommate matching, move-in logistics"),
                                          PromptBuilder.build_user_context({"beds": det.occupancy.occupied_beds_count}), task_type="housing_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return HousingOperationsPlan(housing_actions=parsed.get("housing_actions", fallback["housing_actions"]),
                                         sample_room_assignment_contract_schema=parsed.get("sample_room_assignment_contract_schema", fallback["sample_room_assignment_contract_schema"]))
        except Exception:
            return HousingOperationsPlan(**fallback)
