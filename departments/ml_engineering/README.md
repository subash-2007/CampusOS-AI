# Department 033: Machine Learning Engineering (`ml_engineering`)
Monitors training/validation loss, F1/precision/recall benchmarks, feature pipeline null rates, MLflow model versioning, inference throughput, and algorithmic fairness audits. Generates retraining triggers and MLflow configs.
## 10-Agent Architecture
Deterministic(7): ModelTrainingMeterAgent, ModelAccuracyBenchmarkAgent, FeaturePipelineAuditorAgent, ModelVersioningAuditorAgent, InferenceThroughputMeterAgent, ModelFairnessAuditorAgent, MLEngineeringScorerAgent
Reasoning(2): StrategicMLNarrativeAgent, MLRetrainingPlannerAgent
Orchestrator(1): MLEngineeringOrchestratorAgent
