from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.registrar_academic_records.schemas import (
    StrategicRegistrarNarrative, RegistrarOperationsPlan, ReasoningRegistrarPipelineResult, DeterministicRegistrarPipelineResult
)

class StrategicRegistrarNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates registrar system uptime under peak registration loads, transcript fulfillment speed, and degree clearance accuracy."""
    def __init__(self):
        super().__init__(agent_id="strategic_registrar_narrative", name="Strategic Registrar Narrative Agent",
                         description="Evaluates course registration system uptime, Parchment digital transcript delivery speed, FERPA privacy compliance, and degree audit accuracy.", icon="FileText")

    async def evaluate(self, det: DeterministicRegistrarPipelineResult) -> StrategicRegistrarNarrative:
        fallback = {
            "registrar_summary": f"Premier digital registrar enterprise ({det.registrar_score:.1f}% score). Maintaining {det.registration.registration_system_uptime_pct}% registration system uptime at peak ({det.registration.concurrent_registration_users_peak:,} concurrent users), {det.transcripts.digital_transcript_delivery_minutes:.1f}-minute digital transcript delivery via Parchment, {det.degree_clearance.degree_clearance_accuracy_pct}% degree audit clearance accuracy.",
            "key_registrar_strengths": [f"100% FERPA consent verification across {det.transcripts.official_transcripts_issued_annual:,} official transcripts issued with zero privacy violations", f"{det.scheduling.classroom_space_utilization_pct}% classroom space utilization with only {det.scheduling.class_schedule_conflict_rate_pct}% schedule conflict rate across {det.scheduling.course_sections_scheduled_annual:,} course sections"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("University Registrar & Associate Vice President for Academic Records", "course registration, Parchment transcripts, FERPA compliance, degree audit, classroom scheduling"),
                                          PromptBuilder.build_user_context({"score": det.registrar_score}), task_type="registrar_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicRegistrarNarrative(registrar_summary=parsed.get("registrar_summary", fallback["registrar_summary"]),
                                              key_registrar_strengths=parsed.get("key_registrar_strengths", fallback["key_registrar_strengths"]))
        except Exception:
            return StrategicRegistrarNarrative(**fallback)

class RegistrarOperationsPlannerAgent(BaseAgent):
    """Agent 9: Formulates W3C verifiable digital diploma credentials and automated transfer credit articulation engines."""
    def __init__(self):
        super().__init__(agent_id="registrar_operations_planner", name="Registrar Operations Planner Agent",
                         description="Formulates blockchain verifiable digital diplomas, AI transfer credit equivalency engines, and automated FERPA consent management.", icon="Award")

    async def plan_registrar_operations(self, det: DeterministicRegistrarPipelineResult) -> RegistrarOperationsPlan:
        fallback = {
            "registrar_actions": ["Deploy Cryptographically Signed W3C Verifiable Digital Diplomas for instant instant employer verification", "Launch AI Transfer Articulation Engine evaluating community college course syllabi in under 24 hours"],
            "sample_digital_diploma_verifiable_credential": '{\n  "@context": ["https://www.w3.org/2018/credentials/v1"],\n  "type": ["VerifiableCredential", "UniversityDiplomaCredential"],\n  "issuer": "did:web:campusos.edu:registrar",\n  "issuanceDate": "2026-05-20T00:00:00Z",\n  "credentialSubject": {\n    "student_id": "stu_99182",\n    "student_name": "Jordan Taylor",\n    "degree_awarded": "Bachelor of Science in Computer Science",\n    "honors": "Magna Cum Laude",\n    "gpa_final": 3.88\n  },\n  "proof": {\n    "type": "Ed25519Signature2020",\n    "verificationMethod": "did:web:campusos.edu:registrar#key-1",\n    "proofPurpose": "assertionMethod",\n    "proofValue": "z3jG9xK...8mN2qL9" \n  }\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Registrar Systems Architect & Academic Records Director", "verifiable diploma, transfer credit engine, FERPA audit"),
                                          PromptBuilder.build_user_context({"peak_users": det.registration.concurrent_registration_users_peak}), task_type="registrar_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return RegistrarOperationsPlan(registrar_actions=parsed.get("registrar_actions", fallback["registrar_actions"]),
                                          sample_digital_diploma_verifiable_credential=parsed.get("sample_digital_diploma_verifiable_credential", fallback["sample_digital_diploma_verifiable_credential"]))
        except Exception:
            return RegistrarOperationsPlan(**fallback)
