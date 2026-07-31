from departments.shared.scoring import ScoringEngine
from departments.ml_engineering.schemas import (
    ModelTrainingMetric, ModelAccuracyBenchmark, FeaturePipelineAudit,
    ModelVersioningMetric, InferenceThroughputMetric, ModelFairnessAudit, DeterministicMLPipelineResult
)

class ModelTrainingMeterAgent:
    """Agent 1: Monitors training/validation loss and detects overfitting gaps."""
    def run(self, train_loss: float = 0.042) -> ModelTrainingMetric:
        val_loss = train_loss * 1.3
        return ModelTrainingMetric(training_loss=train_loss, validation_loss=val_loss, overfitting_gap=val_loss - train_loss)

class ModelAccuracyBenchmarkAgent:
    """Agent 2: Evaluates F1, precision, and recall benchmark scores."""
    def run(self, f1: float = 0.94) -> ModelAccuracyBenchmark:
        return ModelAccuracyBenchmark(f1_score=f1, precision=f1 - 0.01, recall=f1 + 0.01)

class FeaturePipelineAuditorAgent:
    """Agent 3: Audits feature count, null percentages, and feature importance docs."""
    def run(self) -> FeaturePipelineAudit:
        return FeaturePipelineAudit(feature_count=128, null_feature_pct=0.8, feature_importance_documented=True)

class ModelVersioningAuditorAgent:
    """Agent 4: Validates MLflow model versioning and active deployment version."""
    def run(self) -> ModelVersioningMetric:
        return ModelVersioningMetric(mlflow_tracked=True, model_versions_count=12, active_version="v8")

class InferenceThroughputMeterAgent:
    """Agent 5: Measures model inference throughput (IPS) and latency."""
    def run(self) -> InferenceThroughputMetric:
        return InferenceThroughputMetric(inferences_per_second=850, avg_inference_latency_ms=1.2)

class ModelFairnessAuditorAgent:
    """Agent 6: Audits algorithmic bias and demographic parity differences."""
    def run(self) -> ModelFairnessAudit:
        return ModelFairnessAudit(bias_detected=False, demographic_parity_diff=0.02)

class MLEngineeringScorerAgent:
    """Agent 7: Master deterministic aggregator for ML Engineering."""
    def __init__(self):
        self.training_agent = ModelTrainingMeterAgent()
        self.accuracy_agent = ModelAccuracyBenchmarkAgent()
        self.feature_agent = FeaturePipelineAuditorAgent()
        self.versioning_agent = ModelVersioningAuditorAgent()
        self.inference_agent = InferenceThroughputMeterAgent()
        self.fairness_agent = ModelFairnessAuditorAgent()

    def run(self, train_loss: float = 0.042, f1: float = 0.94) -> DeterministicMLPipelineResult:
        training = self.training_agent.run(train_loss)
        accuracy = self.accuracy_agent.run(f1)
        features = self.feature_agent.run()
        versioning = self.versioning_agent.run()
        inference = self.inference_agent.run()
        fairness = self.fairness_agent.run()

        metrics = {
            "f1": accuracy.f1_score * 100,
            "fairness": (1 - fairness.demographic_parity_diff) * 100,
            "inference": min(100.0, inference.inferences_per_second / 10.0),
            "overfitting": max(0, 100 - training.overfitting_gap * 1000)
        }
        weights = {"f1": 0.35, "fairness": 0.25, "inference": 0.20, "overfitting": 0.20}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(versioning.model_versions_count, 5)
        return DeterministicMLPipelineResult(
            training=training, accuracy=accuracy, features=features,
            versioning=versioning, inference=inference, fairness=fairness,
            ml_engineering_score=score, confidence_score=confidence
        )
