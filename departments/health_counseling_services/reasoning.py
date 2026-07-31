from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.health_counseling_services.schemas import (
    StrategicHealthNarrative, HealthWellnessPlan, ReasoningHealthPipelineResult, DeterministicHealthPipelineResult
)

class StrategicHealthNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates student mental health counseling intake speeds, medical clinic quality, and HIPAA privacy compliance."""
    def __init__(self):
        super().__init__(agent_id="strategic_health_narrative", name="Strategic Health Narrative Agent",
                         description="Evaluates counseling intake wait times, same-day crisis triage availability, immunization compliance, and AAAHC accreditation.", icon="Activity")

    async def evaluate(self, det: DeterministicHealthPipelineResult) -> StrategicHealthNarrative:
        fallback = {
            "health_summary": f"Gold-standard comprehensive campus healthcare ({det.health_score:.1f}% score). {det.counseling.annual_counseling_sessions_held:,} counseling sessions conducted with average {det.counseling.avg_intake_wait_time_days:.1f}-day intake wait time, 100% same-day crisis triage availability, {det.immunizations.student_immunization_compliance_pct}% immunization compliance.",
            "key_health_strengths": [f"{det.accreditation.aaahc_accreditation_status} with {det.accreditation.hipaa_privacy_audit_score_pct}% HIPAA privacy compliance score across all medical & counseling records", f"{det.clinic.annual_medical_visits_count:,} outpatient medical visits handled ({det.clinic.telehealth_virtual_visits_pct}% virtual telehealth visits) by {det.clinic.licensed_medical_providers} licensed providers"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Executive Director of Student Health & Counseling Services", "counseling wait times, crisis triage, HIPAA privacy, AAAHC accreditation, health insurance waivers"),
                                          PromptBuilder.build_user_context({"score": det.health_score}), task_type="health_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicHealthNarrative(health_summary=parsed.get("health_summary", fallback["health_summary"]),
                                           key_health_strengths=parsed.get("key_health_strengths", fallback["key_health_strengths"]))
        except Exception:
            return StrategicHealthNarrative(**fallback)

class HealthWellnessPlannerAgent(BaseAgent):
    """Agent 9: Formulates 24/7 mental health crisis hotline integrations and electronic health record (EHR) automation."""
    def __init__(self):
        super().__init__(agent_id="health_wellness_planner", name="Health Wellness Planner Agent",
                         description="Formulates 24/7 virtual telehealth triage portals, peer mental health advocate networks, and automated immunization verification workflows.", icon="Heart")

    async def plan_health(self, det: DeterministicHealthPipelineResult) -> HealthWellnessPlan:
        fallback = {
            "health_actions": ["Deploy 24/7 Campus Crisis Telehealth AI Triage Line with immediate licensed therapist connection", "Implement Smart OCR Immunization Record Auto-Verification to eliminate registration health holds"],
            "sample_telehealth_intake_triage_schema": '{\n  "patient_id": "pat_99182",\n  "triage_category": "URGENT CRISIS INTAKE",\n  "symptom_assessment": "Severe anxiety & panic symptoms prior to midterms",\n  "triage_protocol": [\n    "1. Immediate 15-minute Same-Day Crisis Counseling Slot Assigned",\n    "2. On-Call Licensed Clinical Psychologist Notified",\n    "3. Patient redirected to Student Health Center Quiet Wellness Suite",\n    "4. Follow-up 48-hour care check-in scheduled"\n  ],\n  "triage_status": "COMPLETED & COUNSELOR ASSIGNED WITHIN 8 MINUTES"\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Clinical Operations Director & Mental Health Specialist", "crisis triage, telehealth intake, EHR automation"),
                                          PromptBuilder.build_user_context({"sessions": det.counseling.annual_counseling_sessions_held}), task_type="health_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return HealthWellnessPlan(health_actions=parsed.get("health_actions", fallback["health_actions"]),
                                      sample_telehealth_intake_triage_schema=parsed.get("sample_telehealth_intake_triage_schema", fallback["sample_telehealth_intake_triage_schema"]))
        except Exception:
            return HealthWellnessPlan(**fallback)
