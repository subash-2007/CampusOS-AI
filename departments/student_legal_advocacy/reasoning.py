from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.student_legal_advocacy.schemas import (
    StrategicLegalNarrative, LegalAdvocacyPlan, ReasoningLegalPipelineResult, DeterministicLegalPipelineResult
)

class StrategicLegalNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates student legal representation, landlord/tenant dispute resolution, and due process protection."""
    def __init__(self):
        super().__init__(agent_id="strategic_legal_narrative", name="Strategic Legal Narrative Agent",
                         description="Evaluates student legal consultation volume, tenant lease audits, security deposit recovery, and student conduct defense.", icon="Shield")

    async def evaluate(self, det: DeterministicLegalPipelineResult) -> StrategicLegalNarrative:
        fallback = {
            "legal_summary": f"Comprehensive student legal defense ({det.legal_advocacy_score:.1f}% score). Conducting {det.consultations.legal_consultations_conducted:,} legal consultations, {det.conduct_representation.due_process_compliance_pct}% due process compliance, {det.housing_disputes.tenant_dispute_resolution_pct}% tenant dispute resolution success.",
            "key_advocacy_strengths": [f"${det.housing_disputes.security_deposit_recovery_usd:,.0f} in off-campus tenant security deposits recovered for students across {det.housing_disputes.off_campus_lease_reviews_completed:,} lease reviews", f"{det.literacy_workshops.workshop_attendees_total:,} students educated in 'Know Your Rights' legal literacy workshops"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Managing Attorney & Director of Student Legal Services", "landlord tenant law, off-campus housing, student conduct representation, immigration legal aid"),
                                          PromptBuilder.build_user_context({"score": det.legal_advocacy_score}), task_type="legal_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicLegalNarrative(legal_summary=parsed.get("legal_summary", fallback["legal_summary"]),
                                          key_advocacy_strengths=parsed.get("key_advocacy_strengths", fallback["key_advocacy_strengths"]))
        except Exception:
            return StrategicLegalNarrative(**fallback)

class LegalAdvocacyPlannerAgent(BaseAgent):
    """Agent 9: Formulates tenant lease review checklists and digital legal consultation scheduling systems."""
    def __init__(self):
        super().__init__(agent_id="legal_advocacy_planner", name="Legal Advocacy Planner Agent",
                         description="Formulates legal advice intake workflows, off-campus tenant protection guides, and student conduct hearing advocacy protocols.", icon="FileText")

    async def plan_advocacy(self, det: DeterministicLegalPipelineResult) -> LegalAdvocacyPlan:
        fallback = {
            "advocacy_actions": ["Launch AI Off-Campus Lease Scanner to detect illegal landlord clauses prior to signing", "Deploy Free Campus Legal Hotline for urgent evening/weekend legal guidance"],
            "sample_lease_review_checklist": "STUDENT TENANT LEASE REVIEW CHECKLIST\nKey Clauses Screened:\n  1. Security Deposit Limits & Return Deadline (State Law Max: 1 Month Rent)\n  2. Maintenance & Habitability Obligations (Landlord responsible for heat, water, pest control)\n  3. Automatic Renewal & Notice Requirements (Must require 30-day written notice)\n  4. Unenforceable Penalty Fees (Illegal lock-out or excessive late fee clauses flagged)\nAttorney Review Status: APPROVED FOR STUDENT SIGNATURE"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Student Legal Rights Advocate", "tenant lease review, student advocacy, legal literacy"),
                                          PromptBuilder.build_user_context({"consultations": det.consultations.legal_consultations_conducted}), task_type="legal_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return LegalAdvocacyPlan(advocacy_actions=parsed.get("advocacy_actions", fallback["advocacy_actions"]),
                                     sample_lease_review_checklist=parsed.get("sample_lease_review_checklist", fallback["sample_lease_review_checklist"]))
        except Exception:
            return LegalAdvocacyPlan(**fallback)
