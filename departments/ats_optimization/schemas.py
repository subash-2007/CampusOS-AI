from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class KeywordMatchBreakdown(BaseModel):
    hard_skills_match: float = 0.0
    soft_skills_match: float = 0.0
    missing_critical_keywords: List[str] = Field(default_factory=list)
    present_critical_keywords: List[str] = Field(default_factory=list)

class FormatCompatibilityResult(BaseModel):
    is_ats_parseable: bool = True
    formatting_issues: List[str] = Field(default_factory=list)
    font_safety_score: float = 100.0

class SectionHeaderAudit(BaseModel):
    standard_headers_count: int = 0
    non_standard_headers: List[str] = Field(default_factory=list)

class ActionVerbDensityResult(BaseModel):
    strong_action_verb_count: int = 0
    weak_phrase_count: int = 0

class QuantificationScore(BaseModel):
    quantified_bullets_percentage: float = 0.0

class FrequencyAnalysis(BaseModel):
    keyword_frequencies: Dict[str, int] = Field(default_factory=dict)

class DeterministicATSPipelineResult(BaseModel):
    keyword_match: KeywordMatchBreakdown
    format_compat: FormatCompatibilityResult
    section_audit: SectionHeaderAudit
    verb_density: ActionVerbDensityResult
    quantification: QuantificationScore
    frequency: FrequencyAnalysis
    overall_ats_score: float
    confidence_score: float

class ATSOptimizationStrategy(BaseModel):
    top_priority_rewrites: List[Dict[str, str]]
    keyword_insertion_guide: List[str]

class QualitativeATSReport(BaseModel):
    executive_summary: str
    ats_pass_probability: str
    strategic_recommendations: List[str]

class ReasoningATSPipelineResult(BaseModel):
    qualitative_report: QualitativeATSReport
    strategy: ATSOptimizationStrategy
    reasoning_steps: List[str]

class ATSOrchestratorReport(BaseModel):
    department: str = "ATS Optimization"
    department_id: str = "dept_002"
    overall_ats_score: float
    confidence_score: float
    deterministic_analysis: DeterministicATSPipelineResult
    reasoning_analysis: ReasoningATSPipelineResult
    reasoning_steps: List[str]
