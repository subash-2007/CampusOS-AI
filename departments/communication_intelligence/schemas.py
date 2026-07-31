from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class EmailToneAnalysis(BaseModel):
    dominant_tone: str = "PROFESSIONAL & CONFIDENT"
    politeness_score: float = 90.0

class ExecutiveBrevityMetric(BaseModel):
    word_count: int = 120
    brevity_score: float = 85.0

class GrammarSpellingAudit(BaseModel):
    grammar_error_count: int = 0
    flagged_phrases: List[str] = Field(default_factory=list)

class ActionabilityIndex(BaseModel):
    has_clear_call_to_action: bool = True
    actionability_score: float = 92.0

class PersuasivenessScore(BaseModel):
    persuasiveness_score: float = 88.0
    value_proposition_present: bool = True

class VocabularySophistication(BaseModel):
    vocabulary_tier: str = "ADVANCED EXECUTIVE"
    readability_grade: float = 11.5

class DeterministicCommunicationPipelineResult(BaseModel):
    tone: EmailToneAnalysis
    brevity: ExecutiveBrevityMetric
    grammar: GrammarSpellingAudit
    actionability: ActionabilityIndex
    persuasiveness: PersuasivenessScore
    vocabulary: VocabularySophistication
    overall_communication_score: float
    confidence_score: float

class QualitativeCommunicationNarrative(BaseModel):
    communication_critique: str
    tone_alignment_summary: str

class EmailRewriteStrategy(BaseModel):
    optimized_email_draft: str
    key_enhancements_made: List[str]

class ReasoningCommunicationPipelineResult(BaseModel):
    narrative: QualitativeCommunicationNarrative
    rewrite_strategy: EmailRewriteStrategy
    reasoning_steps: List[str]

class CommunicationOrchestratorReport(BaseModel):
    department: str = "Communication Intelligence"
    department_id: str = "dept_013"
    communication_score: float
    confidence_score: float
    deterministic_analysis: DeterministicCommunicationPipelineResult
    reasoning_analysis: ReasoningCommunicationPipelineResult
    reasoning_steps: List[str]
