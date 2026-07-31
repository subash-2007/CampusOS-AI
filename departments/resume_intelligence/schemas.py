from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class ContactInfo(BaseModel):
    emails: List[str] = Field(default_factory=list)
    phones: List[str] = Field(default_factory=list)
    links: List[str] = Field(default_factory=list)

class ActionVerbAudit(BaseModel):
    action_verbs_found: List[str] = Field(default_factory=list)
    verb_density_score: float = 0.0

class ATSMatchResult(BaseModel):
    match_percentage: float = 0.0
    matched_keywords: List[str] = Field(default_factory=list)
    missing_keywords: List[str] = Field(default_factory=list)

class DateGapResult(BaseModel):
    has_gaps: bool = False
    gaps_detected: List[str] = Field(default_factory=list)

class BulletPointAudit(BaseModel):
    total_bullets: int = 0
    bullets_with_metrics: int = 0
    quantification_rate: float = 0.0

class DeterministicPipelineResult(BaseModel):
    contact: ContactInfo
    sections_found: List[str]
    action_verbs: ActionVerbAudit
    ats_match: ATSMatchResult
    date_gaps: DateGapResult
    bullet_audit: BulletPointAudit
    confidence_score: float

class QualitativeEvaluation(BaseModel):
    impact_narrative: str
    leadership_signal: str
    key_strengths: List[str]

class EnhancementStrategy(BaseModel):
    top_recommendations: List[str]
    suggested_bullet_rewrites: List[Dict[str, str]]

class ReasoningPipelineResult(BaseModel):
    qualitative_eval: QualitativeEvaluation
    enhancements: EnhancementStrategy
    reasoning_steps: List[str]

class ResumeOrchestratorReport(BaseModel):
    department: str = "Resume Intelligence"
    department_id: str = "dept_001"
    overall_score: float
    confidence_score: float
    deterministic_analysis: DeterministicPipelineResult
    reasoning_analysis: ReasoningPipelineResult
    reasoning_steps: List[str]
