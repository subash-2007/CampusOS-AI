from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.transportation_parking_intelligence.schemas import (
    StrategicTransportationNarrative, CampusMobilityPlan, ReasoningTransportationPipelineResult, DeterministicTransportationPipelineResult
)

class StrategicTransportationNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates multi-modal campus transit options, LPR enforcement accuracy, and electric fleet sustainability."""
    def __init__(self):
        super().__init__(agent_id="strategic_transportation_narrative", name="Strategic Transportation Narrative Agent",
                         description="Evaluates shuttle bus punctuality, electric vehicle infrastructure, micro-mobility rides, and parking garage occupancy.", icon="Truck")

    async def evaluate(self, det: DeterministicTransportationPipelineResult) -> StrategicTransportationNarrative:
        fallback = {
            "transportation_summary": f"Smart multi-modal campus mobility ({det.transportation_score:.1f}% score). Serving {det.shuttles.annual_shuttle_passengers:,} annual shuttle riders ({det.shuttles.shuttle_on_time_performance_pct}% on-time performance), {det.permits.permits_issued_active:,} active parking permits, {det.shuttles.shuttle_fleet_electric_pct}% electric shuttle fleet.",
            "key_transportation_strengths": [f"{det.enforcement.license_plate_recognition_accuracy_pct}% LPR (License Plate Recognition) enforcement camera accuracy", f"{det.micro_mobility.e_bike_scooter_rides_annual:,} e-bike & e-scooter rides across {det.micro_mobility.designated_parking_hubs} designated mobility hubs"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Director of Campus Transportation & Parking Services", "campus shuttles, parking permits, LPR cameras, EV charging, micro-mobility"),
                                          PromptBuilder.build_user_context({"score": det.transportation_score}), task_type="transportation_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicTransportationNarrative(transportation_summary=parsed.get("transportation_summary", fallback["transportation_summary"]),
                                                  key_transportation_strengths=parsed.get("key_transportation_strengths", fallback["key_transportation_strengths"]))
        except Exception:
            return StrategicTransportationNarrative(**fallback)

class CampusMobilityPlannerAgent(BaseAgent):
    """Agent 9: Generates real-time shuttle tracking integrations and EV fleet expansion roadmaps."""
    def __init__(self):
        super().__init__(agent_id="campus_mobility_planner", name="Campus Mobility Planner Agent",
                         description="Formulates autonomous electric shuttle routes, dynamic parking guidance systems, and carpool reward incentives.", icon="MapPin")

    async def plan_mobility(self, det: DeterministicTransportationPipelineResult) -> CampusMobilityPlan:
        fallback = {
            "mobility_actions": ["Transition 100% of campus shuttle fleet to zero-emission electric buses", "Deploy Real-Time Garage Occupancy Sensors linked to mobile navigation app"],
            "sample_shuttle_route_schedule": "CAMPUS EXPRESS SHUTTLE SCHEDULE (BLUE ROUTE)\nFrequency: Every 8 Minutes (Peak Hours 07:00 - 19:00)\nStops:\n  1. North Campus Parking Garage (Stop 01)\n  2. Science & Engineering Complex (Stop 02)\n  3. Student Union Central Plaza (Stop 03)\n  4. South Campus Residence Quad (Stop 04)\nLive GPS Tracking API: Enabled via CampusOS Mobile App"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Urban Transit Planner & Campus Mobility Specialist", "shuttle route optimization, EV chargers, parking guidance"),
                                          PromptBuilder.build_user_context({"permits": det.permits.permits_issued_active}), task_type="transportation_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return CampusMobilityPlan(mobility_actions=parsed.get("mobility_actions", fallback["mobility_actions"]),
                                     sample_shuttle_route_schedule=parsed.get("sample_shuttle_route_schedule", fallback["sample_shuttle_route_schedule"]))
        except Exception:
            return CampusMobilityPlan(**fallback)
