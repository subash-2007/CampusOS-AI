import pytest, asyncio
from departments.performance_optimization_intelligence.deterministic import (
    WebVitalsMeterAgent, APICacheHitMeterAgent, BundleSizeAuditorAgent, CDNPerformanceMeterAgent,
    DatabaseQueryOptimizerAgent, MemoryLeakAuditorAgent, PerformanceScorerAgent
)
from departments.performance_optimization_intelligence.orchestrator import PerformanceOptimizationOrchestratorAgent

def test_web_vitals_meter():
    res = WebVitalsMeterAgent().run(1200.0)
    assert res.web_vitals_grade == "GOOD"
    assert res.cls_score < 0.1

def test_api_cache_hit_meter():
    res = APICacheHitMeterAgent().run()
    assert res.cache_hit_rate_pct >= 80.0

def test_bundle_size_auditor():
    res = BundleSizeAuditorAgent().run()
    assert res.code_splitting_enabled is True
    assert res.js_bundle_size_kb < 500

def test_cdn_performance_meter():
    res = CDNPerformanceMeterAgent().run()
    assert res.cdn_hit_rate_pct >= 90.0
    assert res.cdn_p95_latency_ms < 100

def test_database_query_optimizer():
    res = DatabaseQueryOptimizerAgent().run()
    assert res.n_plus_one_queries_detected == 0

def test_memory_leak_auditor():
    res = MemoryLeakAuditorAgent().run()
    assert res.memory_leak_detected is False

def test_performance_scorer():
    res = PerformanceScorerAgent().run(1200.0)
    assert res.perf_score >= 85.0
    assert res.confidence_score >= 0.5

def test_performance_optimization_orchestrator():
    report = asyncio.run(PerformanceOptimizationOrchestratorAgent().run_pipeline(1200.0))
    assert report.department == "Performance Optimization Intelligence"
    assert report.department_id == "dept_042"
    assert report.perf_tier == "ELITE PERFORMANCE"
    assert len(report.reasoning_steps) == 4
