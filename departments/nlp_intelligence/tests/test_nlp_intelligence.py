import pytest, asyncio
from departments.nlp_intelligence.deterministic import (
    TextClassificationMeterAgent, SentimentAnalysisAuditorAgent, NERMeterAgent,
    TextSimilarityMeterAgent, LanguageDetectionAuditorAgent, TextSummarizationMeterAgent, NLPCapabilityScorerAgent
)
from departments.nlp_intelligence.orchestrator import NLPIntelligenceOrchestratorAgent

def test_text_classification_meter():
    res = TextClassificationMeterAgent().run(0.96)
    assert res.classifier_accuracy >= 0.90

def test_sentiment_analysis_auditor():
    res = SentimentAnalysisAuditorAgent().run()
    assert res.positive_precision >= 0.85

def test_ner_meter():
    res = NERMeterAgent().run(0.92)
    assert res.ner_f1_score >= 0.85
    assert res.entity_types_supported >= 10

def test_text_similarity_meter():
    res = TextSimilarityMeterAgent().run()
    assert res.cosine_similarity_threshold > 0.5

def test_language_detection_auditor():
    res = LanguageDetectionAuditorAgent().run()
    assert res.languages_supported >= 20
    assert res.detection_accuracy >= 0.95

def test_text_summarization_meter():
    res = TextSummarizationMeterAgent().run()
    assert res.rouge_l_score >= 0.50

def test_nlp_scorer():
    res = NLPCapabilityScorerAgent().run(0.96, 0.92)
    assert res.nlp_capability_score >= 85.0
    assert res.confidence_score >= 0.5

def test_nlp_orchestrator():
    report = asyncio.run(NLPIntelligenceOrchestratorAgent().run_pipeline(0.96, 0.92))
    assert report.department == "NLP Intelligence"
    assert report.department_id == "dept_034"
    assert report.nlp_tier == "ADVANCED NLP CAPABILITY"
    assert len(report.reasoning_steps) == 4
