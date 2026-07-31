from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.campus_mental_health_counseling.schemas import (
    StrategicMentalHealthNarrative, MentalHealthClinicalPlan, ReasoningMentalHealthPipelineResult, DeterministicMentalHealthPipelineResult
)

class StrategicMentalHealthNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates campus counseling intake wait times, crisis intervention response speed, and peer mental health educator outreach coverage."""
    def __init__(self):
        super().__init__(agent_id="strategic_mental_health_narrative", name="Strategic Mental Health Narrative Agent",
                         description="Evaluates counseling intake wait times, counselor-to-student ratios, crisis hotline response speed, group therapy CSAT, and HIPAA EHR compliance.", icon="Heart")

    async def evaluate(self, det: DeterministicMentalHealthPipelineResult) -> StrategicMentalHealthNarrative:
        fallback = {
            "mental_health_summary": f"JCAHO-level campus mental health excellence ({det.mental_health_score:.1f}% score). Serving {det.intake.students_served_annually:,} students annually with {det.intake.avg_intake_appointment_wait_days:.1f}-day average intake wait, {det.intake.same_day_crisis_walk_in_served} same-day crisis walk-ins served, 100% HIPAA EHR compliance.",
            "key_mental_health_strengths": [f"{det.outreach.mental_health_peer_educators_trained} trained peer mental health educators reaching {det.outreach.student_reach_outreach_events:,} students across {det.outreach.outreach_events_campus_annual} campus outreach events", f"Crisis hotline answering {det.crisis.crisis_calls_answered_annual:,} calls with {det.crisis.avg_crisis_response_time_minutes:.1f}-minute average response time and {det.crisis.after_hours_coverage_days_annual}-day annual after-hours coverage"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Director of Counseling Services & Licensed Clinical Psychologist", "counseling intake, crisis intervention, group therapy, peer mental health, HIPAA EHR"),
                                          PromptBuilder.build_user_context({"score": det.mental_health_score}), task_type="mental_health_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicMentalHealthNarrative(mental_health_summary=parsed.get("mental_health_summary", fallback["mental_health_summary"]),
                                                 key_mental_health_strengths=parsed.get("key_mental_health_strengths", fallback["key_mental_health_strengths"]))
        except Exception:
            return StrategicMentalHealthNarrative(**fallback)

class MentalHealthClinicalPlannerAgent(BaseAgent):
    """Agent 9: Formulates AI-assisted mental health screening triage tools and embedded counselor models for academic departments."""
    def __init__(self):
        super().__init__(agent_id="mental_health_clinical_planner", name="Mental Health Clinical Planner Agent",
                         description="Formulates AI triage mental health screening, embedded counselor academic department models, and telemental health digital access expansion.", icon="Shield")

    async def plan_mental_health(self, det: DeterministicMentalHealthPipelineResult) -> MentalHealthClinicalPlan:
        fallback = {
            "mental_health_actions": ["Deploy AI-Powered Mental Health Triage Chatbot (PHQ-9/GAD-7) for initial screening and automatic appointment priority routing", "Launch Embedded Counselor in High-Stress Departments (Engineering, Business, Pre-Med) providing drop-in hours in academic buildings"],
            "sample_counseling_session_schema": '{\n  "session_id": "CSL_2026_09384",\n  "clinician": "Dr. Amara Okonkwo, LPC, NCC",\n  "session_type": "Individual Counseling - CBT (60 min)",\n  "presenting_concern": "Academic Anxiety & Perfectionism",\n  "risk_assessment": "Columbia Protocol (C-SSRS) - No Active Risk",\n  "interventions": [\n    "Cognitive Restructuring of Catastrophic Thoughts",\n    "Progressive Muscle Relaxation Technique",\n    "Academic Calendar Pacing & Priority Matrix"\n  ],\n  "next_appointment": "2026-10-21",\n  "ehr_status": "SOAP Note Completed - HIPAA Secure"\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Licensed Clinical Mental Health Director", "AI triage, embedded counselor, telemental health, crisis intervention"),
                                          PromptBuilder.build_user_context({"students": det.intake.students_served_annually}), task_type="mental_health_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return MentalHealthClinicalPlan(mental_health_actions=parsed.get("mental_health_actions", fallback["mental_health_actions"]),
                                            sample_counseling_session_schema=parsed.get("sample_counseling_session_schema", fallback["sample_counseling_session_schema"]))
        except Exception:
            return MentalHealthClinicalPlan(**fallback)
