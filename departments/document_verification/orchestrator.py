from typing import Dict, Any, List, Optional
from app.agents.base_agent import BaseAgent
from departments.document_verification.deterministic import VerificationScorerAgent
from departments.document_verification.reasoning import VerificationAuditSummaryAgent, DocumentCorrectionGuideAgent
from departments.document_verification.schemas import (
    VerificationOrchestratorReport, ReasoningVerificationPipelineResult
)

class VerificationOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator Agent for the Document Verification Department."""
    def __init__(self):
        super().__init__(
            agent_id="verification_orchestrator",
            name="Document Verification Master Orchestrator",
            description="Coordinates all 9 sub-agents to deliver a unified Document Verification Audit Report.",
            icon="ShieldCheck"
        )
        self.scorer = VerificationScorerAgent()
        self.summary_agent = VerificationAuditSummaryAgent()
        self.guide_agent = DocumentCorrectionGuideAgent()

    async def run_pipeline(self, document_text: str) -> VerificationOrchestratorReport:
        reasoning_steps = []
        
        # Step 1: Execute Deterministic Pipeline
        reasoning_steps.append("Step 1: Running deterministic Document Verification pipeline (Contact verification, Date gap consistency audit, Credential format verification, Structural integrity audit, Duplicate entry detection, Text sanity checks).")
        det_result = self.scorer.run(document_text)
        
        # Step 2: Execute Summary Agent
        reasoning_steps.append("Step 2: Executing Verification Audit Summary Agent to determine document integrity verdict.")
        summary = await self.summary_agent.summarize(document_text, det_result)
        
        # Step 3: Execute Correction Guide Agent
        reasoning_steps.append("Step 3: Executing Document Correction Guide Agent to produce actionable formatting corrections.")
        guide = await self.guide_agent.guide(det_result)
        
        # Step 4: Synthesize Report
        reasoning_steps.append("Step 4: Compiling Document Verification Master Audit Report.")
        reasoning_result = ReasoningVerificationPipelineResult(
            audit_summary=summary,
            correction_guide=guide,
            reasoning_steps=reasoning_steps
        )
        
        status = "VERIFIED" if det_result.verification_score >= 80 else "CORRECTION_NEEDED"
        
        return VerificationOrchestratorReport(
            document_status=status,
            verification_score=det_result.verification_score,
            confidence_score=det_result.confidence_score,
            deterministic_analysis=det_result,
            reasoning_analysis=reasoning_result,
            reasoning_steps=reasoning_steps
        )
