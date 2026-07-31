from typing import List
from pydantic import BaseModel

class CertificationValidityMetric(BaseModel):
    total_certifications_tracked: int = 1250
    active_certifications_count: int = 1180
    expired_certifications_count: int = 70
    validity_pct: float = 94.4

class AssessmentProctoringAudit(BaseModel):
    proctored_assessments_count: int = 840
    ai_proctoring_integrity_score: float = 98.2
    flagged_anomalies_count: int = 12

class CertificationVerificationMetric(BaseModel):
    blockchain_verified_certs_pct: float = 88.0
    avg_verification_time_seconds: float = 1.4

class AssessmentDifficultyAudit(BaseModel):
    item_response_theory_calibrated: bool = True
    cronbach_alpha_reliability: float = 0.91
    average_assessment_score_pct: float = 76.5

class CertificateIssuanceMetric(BaseModel):
    digital_badges_issued: int = 4200
    linkedin_share_rate_pct: float = 64.0

class SkillTaxonomyAlignmentAudit(BaseModel):
    mapped_to_esco_framework: bool = True
    skills_certified_count: int = 156

class DeterministicAssessmentPipelineResult(BaseModel):
    validity: CertificationValidityMetric
    proctoring: AssessmentProctoringAudit
    verification: CertificationVerificationMetric
    difficulty: AssessmentDifficultyAudit
    issuance: CertificateIssuanceMetric
    taxonomy: SkillTaxonomyAlignmentAudit
    assessment_health_score: float
    confidence_score: float

class StrategicAssessmentNarrative(BaseModel):
    assessment_summary: str
    key_assessment_strengths: List[str]

class CertificationExpansionPlan(BaseModel):
    certification_roadmap_actions: List[str]
    sample_certificate_schema: str

class ReasoningAssessmentPipelineResult(BaseModel):
    narrative: StrategicAssessmentNarrative
    expansion_plan: CertificationExpansionPlan
    reasoning_steps: List[str]

class AssessmentCertificationOrchestratorReport(BaseModel):
    department: str = "Assessment & Certification Intelligence"
    department_id: str = "dept_051"
    assessment_tier: str = "ENTERPRISE CERTIFICATION ENGINE"
    assessment_health_score: float
    confidence_score: float
    deterministic_analysis: DeterministicAssessmentPipelineResult
    reasoning_analysis: ReasoningAssessmentPipelineResult
    reasoning_steps: List[str]
