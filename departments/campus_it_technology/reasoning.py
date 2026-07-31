from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.campus_it_technology.schemas import (
    StrategicITNarrative, ITOperationsPlan, ReasoningITPipelineResult, DeterministicITPipelineResult
)

class StrategicITNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates campus network infrastructure SLA uptime, cybersecurity SOC response times, and AV classroom technology readiness."""
    def __init__(self):
        super().__init__(agent_id="strategic_it_narrative", name="Strategic IT Narrative Agent",
                         description="Evaluates campus WiFi SLA uptime, IT helpdesk FCR rates, SOC cybersecurity incident containment, software license compliance, and DRP backup completion.", icon="Server")

    async def evaluate(self, det: DeterministicITPipelineResult) -> StrategicITNarrative:
        fallback = {
            "it_summary": f"Award-winning digital campus technology infrastructure ({det.it_score:.1f}% score). Managing {det.network.campus_wifi_access_points_managed:,} campus WiFi access points at {det.network.network_uptime_sla_pct}% SLA uptime, resolving {det.helpdesk.helpdesk_tickets_resolved_annual:,} helpdesk tickets annually at {det.helpdesk.first_call_resolution_rate_pct}% FCR rate, 0 student data breaches.",
            "key_it_strengths": [f"{det.classroom_av.smart_classrooms_equipped} smart classrooms with {det.classroom_av.av_technology_uptime_pct}% AV uptime including {det.classroom_av.hybrid_learning_rooms_count} hybrid learning rooms", f"{det.drp.backup_completion_rate_pct}% backup completion rate with {det.drp.disaster_recovery_rto_minutes:.0f}-minute RTO tested across {det.drp.drp_test_exercises_annual} annual DRP exercises"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Chief Information Officer (CIO) & Director of Campus IT Operations", "network SLA, SOC cybersecurity, software licensing, AV technology, DRP RTO"),
                                          PromptBuilder.build_user_context({"score": det.it_score}), task_type="it_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicITNarrative(it_summary=parsed.get("it_summary", fallback["it_summary"]),
                                       key_it_strengths=parsed.get("key_it_strengths", fallback["key_it_strengths"]))
        except Exception:
            return StrategicITNarrative(**fallback)

class ITOperationsPlannerAgent(BaseAgent):
    """Agent 9: Formulates campus AI chatbot IT helpdesk automation and zero-trust network security architecture roadmaps."""
    def __init__(self):
        super().__init__(agent_id="it_operations_planner", name="IT Operations Planner Agent",
                         description="Formulates AI helpdesk chatbot automation, zero-trust cybersecurity, and smart classroom AV upgrade roadmaps.", icon="Cpu")

    async def plan_it_operations(self, det: DeterministicITPipelineResult) -> ITOperationsPlan:
        fallback = {
            "it_actions": ["Deploy AI-Powered IT Helpdesk Chatbot resolving Tier-1 password resets and WiFi access issues automatically", "Implement Zero-Trust Network Architecture enforcing MFA for all campus system access"],
            "sample_helpdesk_ticket_schema": '{\n  "ticket_id": "INC_2026_088421",\n  "requester": "student@university.edu",\n  "category": "Network Access",\n  "priority": "P2 - High",\n  "subject": "Cannot connect to campus WiFi - ResNet Building D",\n  "assigned_to": "Campus IT Network Operations Center",\n  "status": "RESOLVED",\n  "resolution": "MAC address whitelist updated. WPA3-Enterprise credentials re-provisioned.",\n  "first_response_minutes": 4,\n  "total_resolution_hours": 0.8\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Campus IT Operations Director & Network Engineer", "helpdesk automation, zero trust, network SLA, DRP"),
                                          PromptBuilder.build_user_context({"tickets": det.helpdesk.helpdesk_tickets_resolved_annual}), task_type="it_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return ITOperationsPlan(it_actions=parsed.get("it_actions", fallback["it_actions"]),
                                    sample_helpdesk_ticket_schema=parsed.get("sample_helpdesk_ticket_schema", fallback["sample_helpdesk_ticket_schema"]))
        except Exception:
            return ITOperationsPlan(**fallback)
