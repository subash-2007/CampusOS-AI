from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.campus_safety_emergency.schemas import (
    StrategicSafetyNarrative, CampusEmergencyPlan, ReasoningSafetyPipelineResult, DeterministicSafetyPipelineResult
)

class StrategicSafetyNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates campus police readiness, emergency notification speed, and Clery Act compliance."""
    def __init__(self):
        super().__init__(agent_id="strategic_safety_narrative", name="Strategic Safety Narrative Agent",
                         description="Evaluates Clery Act compliance, emergency alert speed, and campus safety app utilization.", icon="Shield")

    async def evaluate(self, det: DeterministicSafetyPipelineResult) -> StrategicSafetyNarrative:
        fallback = {
            "safety_summary": f"Gold-standard safe campus ({det.campus_safety_score:.1f}% score). {det.clery_act.clery_compliance_score_pct}% Clery Act compliance, {det.emergency_alerts.alert_delivery_time_seconds:.1f}-second emergency alert broadcast speed ({det.emergency_alerts.delivery_reach_pct}% reach), {det.callboxes.functional_callboxes_pct}% callbox uptime.",
            "key_safety_strengths": [f"{det.safety_app.app_downloads_count:,} campus safety app downloads with {det.safety_app.safe_walk_escorts_requested:,} SafeWalk escorts completed", f"{det.cameras.security_cameras_active} active CCTV security cameras with {det.cameras.camera_uptime_pct}% uptime"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Chief of Campus Police & Public Safety", "Clery Act, emergency alert dispatch, campus safety, disaster response"),
                                          PromptBuilder.build_user_context({"score": det.campus_safety_score}), task_type="safety_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicSafetyNarrative(safety_summary=parsed.get("safety_summary", fallback["safety_summary"]),
                                          key_safety_strengths=parsed.get("key_safety_strengths", fallback["key_safety_strengths"]))
        except Exception:
            return StrategicSafetyNarrative(**fallback)

class CampusEmergencyPlannerAgent(BaseAgent):
    """Agent 9: Generates active threat response protocols and automated Clery Act emergency broadcast templates."""
    def __init__(self):
        super().__init__(agent_id="campus_emergency_planner", name="Campus Emergency Planner Agent",
                         description="Formulates disaster preparedness plans, emergency siren protocols, and crime prevention alerts.", icon="AlertTriangle")

    async def plan_emergency(self, det: DeterministicSafetyPipelineResult) -> CampusEmergencyPlan:
        fallback = {
            "safety_protocol_actions": ["Deploy Autonomous Security Rovers for nighttime perimeter patrolling", "Integrate Smart Building Lockdown Automation triggered via emergency dispatch button"],
            "sample_clery_alert_broadcast": "CAMPUS EMERGENCY ALERT - SHELTER IN PLACE\nIssued By: CampusOS Public Safety Command\nTime: 2026-09-12 14:15:00 EST\nAlert Details: Hazardous chemical spill reported near Science Building Room 304.\nInstructions: Avoid Science Quad immediately. Close windows and turn off HVAC systems in adjacent buildings. Stand by for further instructions."
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Emergency Management Director", "active shooter protocol, weather emergency, Clery notification"),
                                          PromptBuilder.build_user_context({"callboxes": det.callboxes.callboxes_installed_count}), task_type="safety_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return CampusEmergencyPlan(safety_protocol_actions=parsed.get("safety_protocol_actions", fallback["safety_protocol_actions"]),
                                      sample_clery_alert_broadcast=parsed.get("sample_clery_alert_broadcast", fallback["sample_clery_alert_broadcast"]))
        except Exception:
            return CampusEmergencyPlan(**fallback)
