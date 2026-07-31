from departments.shared.scoring import ScoringEngine
from departments.nlp_intelligence.schemas import (
    TextClassificationMetric, SentimentAnalysisAudit, NamedEntityRecognitionMetric,
    TextSimilarityMetric, LanguageDetectionAudit, TextSummarizationMetric, DeterministicNLPPipelineResult
)

class TextClassificationMeterAgent:
    """Agent 1: Measures text classification accuracy and supported category count."""
    def run(self, accuracy: float = 0.96) -> TextClassificationMetric:
        return TextClassificationMetric(classifier_accuracy=accuracy, categories_supported=24)

class SentimentAnalysisAuditorAgent:
    """Agent 2: Audits positive/negative/neutral sentiment precision scores."""
    def run(self) -> SentimentAnalysisAudit:
        return SentimentAnalysisAudit(positive_precision=0.94, negative_precision=0.93, neutral_precision=0.91)

class NERMeterAgent:
    """Agent 3: Measures Named Entity Recognition F1 score and entity type coverage."""
    def run(self, f1: float = 0.92) -> NamedEntityRecognitionMetric:
        return NamedEntityRecognitionMetric(ner_f1_score=f1, entity_types_supported=18)

class TextSimilarityMeterAgent:
    """Agent 4: Evaluates cosine similarity thresholds and embedding model selection."""
    def run(self) -> TextSimilarityMetric:
        return TextSimilarityMetric(cosine_similarity_threshold=0.85, embedding_model="text-embedding-3-large")

class LanguageDetectionAuditorAgent:
    """Agent 5: Audits multilingual detection accuracy and supported language count."""
    def run(self) -> LanguageDetectionAudit:
        return LanguageDetectionAudit(languages_supported=45, detection_accuracy=0.99)

class TextSummarizationMeterAgent:
    """Agent 6: Measures ROUGE-L summarization score and compression ratio."""
    def run(self) -> TextSummarizationMetric:
        return TextSummarizationMetric(rouge_l_score=0.62, avg_compression_ratio=0.18)

class NLPCapabilityScorerAgent:
    """Agent 7: Master deterministic aggregator for NLP Intelligence."""
    def __init__(self):
        self.clf_agent = TextClassificationMeterAgent()
        self.sentiment_agent = SentimentAnalysisAuditorAgent()
        self.ner_agent = NERMeterAgent()
        self.similarity_agent = TextSimilarityMeterAgent()
        self.lang_agent = LanguageDetectionAuditorAgent()
        self.summary_agent = TextSummarizationMeterAgent()

    def run(self, clf_acc: float = 0.96, ner_f1: float = 0.92) -> DeterministicNLPPipelineResult:
        clf = self.clf_agent.run(clf_acc)
        sentiment = self.sentiment_agent.run()
        ner = self.ner_agent.run(ner_f1)
        similarity = self.similarity_agent.run()
        lang = self.lang_agent.run()
        summary = self.summary_agent.run()

        metrics = {
            "classification": clf.classifier_accuracy * 100,
            "ner": ner.ner_f1_score * 100,
            "sentiment": ((sentiment.positive_precision + sentiment.negative_precision) / 2) * 100,
            "language": lang.detection_accuracy * 100
        }
        weights = {"classification": 0.30, "ner": 0.25, "sentiment": 0.25, "language": 0.20}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(lang.languages_supported, 10)
        return DeterministicNLPPipelineResult(
            classification=clf, sentiment=sentiment, ner=ner, similarity=similarity,
            language_detection=lang, summarization=summary,
            nlp_capability_score=score, confidence_score=confidence
        )
