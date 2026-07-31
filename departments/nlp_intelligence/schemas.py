from typing import List
from pydantic import BaseModel

class TextClassificationMetric(BaseModel):
    classifier_accuracy: float = 0.96
    categories_supported: int = 24

class SentimentAnalysisAudit(BaseModel):
    positive_precision: float = 0.94
    negative_precision: float = 0.93
    neutral_precision: float = 0.91

class NamedEntityRecognitionMetric(BaseModel):
    ner_f1_score: float = 0.92
    entity_types_supported: int = 18

class TextSimilarityMetric(BaseModel):
    cosine_similarity_threshold: float = 0.85
    embedding_model: str = "text-embedding-3-large"

class LanguageDetectionAudit(BaseModel):
    languages_supported: int = 45
    detection_accuracy: float = 0.99

class TextSummarizationMetric(BaseModel):
    rouge_l_score: float = 0.62
    avg_compression_ratio: float = 0.18

class DeterministicNLPPipelineResult(BaseModel):
    classification: TextClassificationMetric
    sentiment: SentimentAnalysisAudit
    ner: NamedEntityRecognitionMetric
    similarity: TextSimilarityMetric
    language_detection: LanguageDetectionAudit
    summarization: TextSummarizationMetric
    nlp_capability_score: float
    confidence_score: float

class StrategicNLPNarrative(BaseModel):
    nlp_pipeline_summary: str
    key_nlp_strengths: List[str]

class NLPEnhancementPlan(BaseModel):
    model_upgrade_recommendations: List[str]
    sample_nlp_pipeline_config: str

class ReasoningNLPPipelineResult(BaseModel):
    narrative: StrategicNLPNarrative
    enhancement_plan: NLPEnhancementPlan
    reasoning_steps: List[str]

class NLPIntelligenceOrchestratorReport(BaseModel):
    department: str = "NLP Intelligence"
    department_id: str = "dept_034"
    nlp_tier: str = "ADVANCED NLP CAPABILITY"
    nlp_capability_score: float
    confidence_score: float
    deterministic_analysis: DeterministicNLPPipelineResult
    reasoning_analysis: ReasoningNLPPipelineResult
    reasoning_steps: List[str]
