from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.document_verification.schemas import (
    VerificationAuditSummary, CorrectionGuide, ReasoningVerificationPipelineResult, DeterministicVerificationPipelineResult
)

class VerificationAuditSummaryAgent(BaseAgent):
    """Agent 8: Evaluates document audit summary and integrity verdict."""
    def __init__(self):
        super().__init__(
            agent_id="verification_audit_summary",
            name="Verification Audit Summary Agent",
            description="Evaluates document verification score, credential validity, and timeline integrity.",
            icon="CheckSquare"
        )

    async def summarize(self, text: str, det_result: DeterministicVerificationPipelineResult) -> VerificationAuditSummary:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Lead Document Authenticator & Forensic Resume Auditor",
            domain_focus="Document verification, credential authentication, and timeline audit."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"verification_score": det_result.verification_score, "has_timeline_gaps": det_result.timeline.has_timeline_gaps}
        )
        
        verdict = "VERIFIED PASS" if det_result.verification_score >= 80 else "NEEDS CORRECTION"
        fallback = {
            "audit_verdict": verdict,
            "integrity_summary": f"Document achieved a {det_result.verification_score}% verification score.",
            "flagged_concerns": det_result.timeline.date_gaps if det_result.timeline.has_timeline_gaps else ["No major timeline concerns flagged."]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="verification_summary", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return VerificationAuditSummary(
                audit_verdict=parsed.get("audit_verdict", fallback["audit_verdict"]),
                integrity_summary=parsed.get("integrity_summary", fallback["integrity_summary"]),
                flagged_concerns=parsed.get("flagged_concerns", fallback["flagged_concerns"])
            )
        except Exception:
            return VerificationAuditSummary(**fallback)

class DocumentCorrectionGuideAgent(BaseAgent):
    """Agent 9: Formulates actionable document correction guidelines."""
    def __init__(self):
        super().__init__(
            agent_id="document_correction_guide",
            name="Document Correction Guide Agent",
            description="Formulates step-by-step document formatting and typo correction guides.",
            icon="Edit3"
        )

    async def guide(self, det_result: DeterministicVerificationPipelineResult) -> CorrectionGuide:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Senior Resume Compliance Editor",
            domain_focus="Document formatting correction and structural optimization."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"missing_sections": det_result.structure.missing_core_sections}
        )
        
        fallback = {
            "recommended_corrections": [
                f"Add missing core section: {sec}" for sec in det_result.structure.missing_core_sections
            ] if det_result.structure.missing_core_sections else ["Document layout is clean and verified."]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="correction_guide", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return CorrectionGuide(
                recommended_corrections=parsed.get("recommended_corrections", fallback["recommended_corrections"])
            )
        except Exception:
            return CorrectionGuide(**fallback)
