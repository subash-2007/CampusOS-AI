from typing import List, Optional
from pydantic import BaseModel

class ModelTrainingMetric(BaseModel):
    training_loss: float = 0.042
    validation_loss: float = 0.055
    overfitting_gap: float = 0.013

class ModelAccuracyBenchmark(BaseModel):
    f1_score: float = 0.94
    precision: float = 0.93
    recall: float = 0.95

class FeaturePipelineAudit(BaseModel):
    feature_count: int = 128
    null_feature_pct: float = 0.8
    feature_importance_documented: bool = True

class ModelVersioningMetric(BaseModel):
    mlflow_tracked: bool = True
    model_versions_count: int = 12
    active_version: str = "v8"

class InferenceThroughputMetric(BaseModel):
    inferences_per_second: int = 850
    avg_inference_latency_ms: float = 1.2

class ModelFairnessAudit(BaseModel):
    bias_detected: bool = False
    demographic_parity_diff: float = 0.02

class DeterministicMLPipelineResult(BaseModel):
    training: ModelTrainingMetric
    accuracy: ModelAccuracyBenchmark
    features: FeaturePipelineAudit
    versioning: ModelVersioningMetric
    inference: InferenceThroughputMetric
    fairness: ModelFairnessAudit
    ml_engineering_score: float
    confidence_score: float

class StrategicMLNarrative(BaseModel):
    ml_pipeline_summary: str
    key_ml_strengths: List[str]

class MLRetrainingPlan(BaseModel):
    retraining_triggers: List[str]
    sample_training_config: str

class ReasoningMLPipelineResult(BaseModel):
    narrative: StrategicMLNarrative
    retraining_plan: MLRetrainingPlan
    reasoning_steps: List[str]

class MLEngineeringOrchestratorReport(BaseModel):
    department: str = "Machine Learning Engineering"
    department_id: str = "dept_033"
    ml_tier: str = "PRODUCTION ML PIPELINE"
    ml_engineering_score: float
    confidence_score: float
    deterministic_analysis: DeterministicMLPipelineResult
    reasoning_analysis: ReasoningMLPipelineResult
    reasoning_steps: List[str]
