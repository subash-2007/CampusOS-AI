from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class ContactVerificationResult(BaseModel):
    is_valid_email: bool = True
    is_valid_phone: bool = True
    verified_emails: List[str] = Field(default_factory=list)
    verified_phones: List[str] = Field(default_factory=list)

class DateConsistencyResult(BaseModel):
    has_timeline_gaps: bool = False
    date_gaps: List[str] = Field(default_factory=list)
    chronological_order_valid: bool = True

class CredentialFormatAudit(BaseModel):
    is_standard_degree_format: bool = True
    unrecognized_degrees: List[str] = Field(default_factory=list)

class StructuralIntegrityResult(BaseModel):
    missing_core_sections: List[str] = Field(default_factory=list)
    formatting_risk_score: float = 0.0

class DuplicateEntryResult(BaseModel):
    duplicate_skills_found: List[str] = Field(default_factory=list)
    redundancies_count: int = 0

class TextSanityResult(BaseModel):
    typo_count: int = 0
    flagged_typos: List[str] = Field(default_factory=list)

class DeterministicVerificationPipelineResult(BaseModel):
    contact: ContactVerificationResult
    timeline: DateConsistencyResult
    credentials: CredentialFormatAudit
    structure: StructuralIntegrityResult
    duplicates: DuplicateEntryResult
    sanity: TextSanityResult
    verification_score: float
    confidence_score: float

class VerificationAuditSummary(BaseModel):
    audit_verdict: str = "VERIFIED PASS"
    integrity_summary: str
    flagged_concerns: List[str]

class CorrectionGuide(BaseModel):
    recommended_corrections: List[str]

class ReasoningVerificationPipelineResult(BaseModel):
    audit_summary: VerificationAuditSummary
    correction_guide: CorrectionGuide
    reasoning_steps: List[str]

class VerificationOrchestratorReport(BaseModel):
    department: str = "Document Verification"
    department_id: str = "dept_011"
    document_status: str = "VERIFIED"
    verification_score: float
    confidence_score: float
    deterministic_analysis: DeterministicVerificationPipelineResult
    reasoning_analysis: ReasoningVerificationPipelineResult
    reasoning_steps: List[str]
