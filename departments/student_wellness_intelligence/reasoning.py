from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.student_wellness_intelligence.schemas import (
    StrategicWellnessNarrative, WellnessProgramPlan, ReasoningWellnessPipelineResult, DeterministicWellnessPipelineResult
)

class StrategicWellnessNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates student mental health access, counseling SLAs, and campus wellness culture."""
    def __init__(self):
        super().__init__(agent_id="strategic_wellness_narrative", name="Strategic Wellness Narrative Agent",
                         description="Evaluates counseling wait times, 24/7 telehealth access, screening follow-ups, and stress indexes.", icon="Heart")

    async def evaluate(self, det: DeterministicWellnessPipelineResult) -> StrategicWellnessNarrative:
        fallback = {
            "wellness_summary": f"Holistic student wellness platform ({det.wellness_score:.1f}% score). {det.counseling.avg_wait_time_days}-day avg counseling wait time, {det.mental_health.followup_care_connection_pct}% follow-up connection rate, 24/7 telehealth available.",
            "key_wellness_strengths": [f"{det.counseling.crisis_triage_latency_minutes} min crisis triage response time", f"{det.insurance.student_health_insurance_coverage_pct}% health insurance coverage with {det.insurance.immunization_compliance_pct}% immunization compliance"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Director of Student Health & Counseling", "mental health, crisis triage, telehealth, student wellness"),
                                          PromptBuilder.build_user_context({"score": det.wellness_score}), task_type="wellness_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicWellnessNarrative(wellness_summary=parsed.get("wellness_summary", fallback["wellness_summary"]),
                                             key_wellness_strengths=parsed.get("key_wellness_strengths", fallback["key_wellness_strengths"]))
        except Exception:
            return StrategicWellnessNarrative(**fallback)

class WellnessProgramPlannerAgent(BaseAgent):
    """Agent 9: Generates mental health workshop initiatives and crisis triage protocol frameworks."""
    def __init__(self):
        super().__init__(agent_id="wellness_program_planner", name="Wellness Program Planner Agent",
                         description="Formulates crisis response workflows, peer counseling training, and stress reduction workshops.", icon="Shield")

    async def plan_program(self, det: DeterministicWellnessPipelineResult) -> WellnessProgramPlan:
        fallback = {
            "wellness_initiative_actions": [f"Launch Exam Week Stress Decompression Zone and mindfulness workshops to mitigate {det.stress_burnout.exam_week_stress_spike_pct}% stress spike", "Expand peer mental health advocate certification program across all dormitories"],
            "sample_crisis_triage_protocol": "CRISIS INTERVENTION PROTOCOL\nLevel 1 (Immediate Risk): Direct 24/7 Crisis Hotline connect + Campus Safety dispatch (< 5 min SLA)\nLevel 2 (Urgent Distress): Same-day intake appointment with licensed psychologist\nLevel 3 (Routine Care): Scheduling within 48 hours via Telehealth portal"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Mental Health Coordinator", "crisis protocols, peer counseling, stress prevention"),
                                          PromptBuilder.build_user_context({"screened_pct": det.mental_health.students_screened_pct}), task_type="wellness_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return WellnessProgramPlan(wellness_initiative_actions=parsed.get("wellness_initiative_actions", fallback["wellness_initiative_actions"]),
                                       sample_crisis_triage_protocol=parsed.get("sample_crisis_triage_protocol", fallback["sample_crisis_triage_protocol"]))
        except Exception:
            return WellnessProgramPlan(**fallback)
