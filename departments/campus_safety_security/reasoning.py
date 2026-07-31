from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.campus_safety_security.schemas import (
    StrategicCampusSafetyNarrative, CampusSafetyOperationsPlan, ReasoningCampusSafetyPipelineResult, DeterministicCampusSafetyPipelineResult
)

class StrategicCampusSafetyNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates campus police emergency response times, CCTV blue light uptime, and mass notification system opt-in rates."""
    def __init__(self):
        super().__init__(agent_id="strategic_campus_safety_narrative", name="Strategic Campus Safety Narrative Agent",
                         description="Evaluates campus police response speed, CCTV uptime, mass notification delivery, escort service satisfaction, and Clery Act compliance.", icon="Shield")

    async def evaluate(self, det: DeterministicCampusSafetyPipelineResult) -> StrategicCampusSafetyNarrative:
        fallback = {
            "safety_summary": f"Nationally accredited campus public safety department ({det.safety_score:.1f}% score). {det.patrol.sworn_campus_officers_count} sworn campus officers with {det.patrol.avg_emergency_response_time_minutes:.1f}-minute average emergency response, {det.cctv.cctv_cameras_operational:,} CCTV cameras at {det.cctv.blue_light_station_uptime_pct}% blue light uptime.",
            "key_safety_strengths": [f"{det.notification.opt_in_enrollment_rate_pct}% mass notification opt-in delivering alerts in {det.notification.avg_notification_delivery_seconds:.0f} seconds with {det.notification.mass_notification_tests_annual} annual system tests", f"{det.escort.safe_walk_escort_requests_fulfilled:,} Safe Walk escorts and {det.escort.night_ride_shuttle_trips_annual:,} NightRide trips ({det.escort.escort_service_satisfaction_score:.2f}/5.0 satisfaction)"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Chief of Campus Public Safety and Emergency Management Director", "campus police, CCTV, blue light, mass notification, Clery Act, Safe Walk"), PromptBuilder.build_user_context({"score": det.safety_score}), task_type="safety_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicCampusSafetyNarrative(safety_summary=parsed.get("safety_summary", fallback["safety_summary"]), key_safety_strengths=parsed.get("key_safety_strengths", fallback["key_safety_strengths"]))
        except Exception:
            return StrategicCampusSafetyNarrative(**fallback)

class CampusSafetyOperationsPlannerAgent(BaseAgent):
    """Agent 9: Formulates AI-powered predictive crime analysis and license plate recognition systems for campus safety."""
    def __init__(self):
        super().__init__(agent_id="campus_safety_operations_planner", name="Campus Safety Operations Planner Agent",
                         description="Formulates predictive crime analytics, AI license plate recognition, and smart blue light emergency station networks.", icon="AlertTriangle")

    async def plan_campus_safety(self, det: DeterministicCampusSafetyPipelineResult) -> CampusSafetyOperationsPlan:
        fallback = {
            "safety_actions": ["Deploy AI Predictive Crime Analysis Dashboard identifying campus hotspots by time of day, weather, and event density", "Launch Smart Blue Light 5G Emergency Station Network with real-time video streaming to Campus Police dispatch"],
            "sample_clery_incident_schema": '{\n  "incident_id": "CLY_2026_00284",\n  "incident_type": "Non-Forcible Sex Offense",\n  "campus_geography": "On-Campus Residence Hall",\n  "incident_date": "2026-09-14",\n  "report_date": "2026-09-14",\n  "reported_to": "Campus Security Authority (CSA) and Title IX Office",\n  "clery_category": "Sex Offenses - Non-Forcible",\n  "notification_issued": "Timely Warning Notice distributed to campus community within 2 hours",\n  "status": "REPORTED TO CLERY ANNUAL SECURITY REPORT 2026"\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Campus Safety Director and Clery Act Compliance Officer", "predictive crime analytics, Clery Act, mass notification, blue light, license plate recognition"), PromptBuilder.build_user_context({"officers": det.patrol.sworn_campus_officers_count}), task_type="safety_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return CampusSafetyOperationsPlan(safety_actions=parsed.get("safety_actions", fallback["safety_actions"]), sample_clery_incident_schema=parsed.get("sample_clery_incident_schema", fallback["sample_clery_incident_schema"]))
        except Exception:
            return CampusSafetyOperationsPlan(**fallback)
