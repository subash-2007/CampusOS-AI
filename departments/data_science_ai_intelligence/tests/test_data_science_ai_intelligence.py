import pytest
import asyncio
from departments.data_science_ai_intelligence.deterministic import (
    MLModelAccuracyMeterAgent, FeatureEngineeringCoverageAgent, DataPipelineLatencyMeterAgent,
    DataDriftDetectorAgent, HyperparameterOptimizationScorerAgent, AIModelBiasFairnessAuditorAgent, DataScienceScorerAgent
)
from departments.data_science_ai_intelligence.orchestrator import DataScienceAIOrchestratorAgent

F1_SCORE = 0.92
LATENCY_MS = 145

def test_ml_model_accuracy_meter():
    agent = MLModelAccuracyMeterAgent()
    res = agent.run(F1_SCORE)
    assert res.model_f1_score == 0.92
    assert res.accuracy_tier == "PRODUCTION ACCURATE"

def test_feature_engineering_coverage():
    agent = FeatureEngineeringCoverageAgent()
    res = agent.run(48)
    assert res.total_features_engineered == 48

def test_data_pipeline_latency_meter():
    agent = DataPipelineLatencyMeterAgent()
    res = agent.run(LATENCY_MS)
    assert res.pipeline_latency_ms == 145

def test_data_drift_detector():
    agent = DataDriftDetectorAgent()
    res = agent.run(0.04)
    assert res.drift_detected is False

def test_hyperparameter_optimization_scorer():
    agent = HyperparameterOptimizationScorerAgent()
    res = agent.run()
    assert res.best_validation_loss < 0.1

def test_ai_model_bias_fairness_auditor():
    agent = AIModelBiasFairnessAuditorAgent()
    res = agent.run()
    assert res.fairness_audit_passed is True

def test_data_science_scorer():
    agent = DataScienceScorerAgent()
    res = agent.run(F1_SCORE, LATENCY_MS)
    assert res.ai_readiness_score >= 80.0
    assert res.confidence_score > 0.5

def test_data_science_orchestrator_pipeline():
    orchestrator = DataScienceAIOrchestratorAgent()
    report = asyncio.run(orchestrator.run_pipeline(F1_SCORE, LATENCY_MS))
    
    assert report.department == "Data Science & AI Intelligence"
    assert report.department_id == "dept_025"
    assert report.ai_readiness_tier == "ENTERPRISE PRODUCTION AI"
    assert report.confidence_score > 0
    assert len(report.reasoning_steps) == 4
    assert len(report.reasoning_analysis.deployment_strategy.recommended_model_serving_stack) > 0
