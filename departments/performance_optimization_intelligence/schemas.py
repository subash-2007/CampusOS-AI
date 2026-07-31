from typing import List
from pydantic import BaseModel

class WebVitalsMetric(BaseModel):
    lcp_ms: float = 1200.0
    fid_ms: float = 45.0
    cls_score: float = 0.05
    web_vitals_grade: str = "GOOD"

class APICacheHitMetric(BaseModel):
    cache_hit_rate_pct: float = 88.0
    cache_miss_cost_ms: float = 45.0
    cache_layers: int = 3

class BundleSizeAudit(BaseModel):
    js_bundle_size_kb: float = 285.0
    css_bundle_size_kb: float = 42.0
    code_splitting_enabled: bool = True

class CDNPerformanceMetric(BaseModel):
    cdn_hit_rate_pct: float = 94.0
    cdn_p95_latency_ms: float = 28.0
    edge_locations_count: int = 42

class DatabaseQueryOptimizerMetric(BaseModel):
    n_plus_one_queries_detected: int = 0
    query_plan_cached_pct: float = 96.0
    avg_query_time_ms: float = 6.2

class MemoryLeakAudit(BaseModel):
    memory_leak_detected: bool = False
    heap_growth_rate_mb_per_hour: float = 0.8

class DeterministicPerfPipelineResult(BaseModel):
    web_vitals: WebVitalsMetric
    cache: APICacheHitMetric
    bundle: BundleSizeAudit
    cdn: CDNPerformanceMetric
    db_optimizer: DatabaseQueryOptimizerMetric
    memory: MemoryLeakAudit
    perf_score: float
    confidence_score: float

class StrategicPerfNarrative(BaseModel):
    performance_summary: str
    key_perf_strengths: List[str]

class PerfOptimizationPlan(BaseModel):
    optimization_actions: List[str]
    sample_webpack_config: str

class ReasoningPerfPipelineResult(BaseModel):
    narrative: StrategicPerfNarrative
    optimization_plan: PerfOptimizationPlan
    reasoning_steps: List[str]

class PerformanceOptimizationOrchestratorReport(BaseModel):
    department: str = "Performance Optimization Intelligence"
    department_id: str = "dept_042"
    perf_tier: str = "ELITE PERFORMANCE"
    perf_score: float
    confidence_score: float
    deterministic_analysis: DeterministicPerfPipelineResult
    reasoning_analysis: ReasoningPerfPipelineResult
    reasoning_steps: List[str]
