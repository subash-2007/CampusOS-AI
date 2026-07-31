from typing import List, Optional
from pydantic import BaseModel, Field

class QueryPerformanceMetric(BaseModel):
    avg_query_time_ms: float = 8.5
    slow_queries_count: int = 0
    query_performance_tier: str = "OPTIMAL"

class IndexCoverageAudit(BaseModel):
    index_coverage_pct: float = 95.0
    missing_indexes_count: int = 1

class DatabaseNormalizationScore(BaseModel):
    normalization_form: str = "3NF"
    denormalization_tables: int = 0

class ConnectionPoolMetric(BaseModel):
    pool_size: int = 20
    active_connections: int = 8
    pool_utilization_pct: float = 40.0

class DataIntegrityAudit(BaseModel):
    foreign_key_constraints_enforced: bool = True
    nullable_critical_fields: int = 0

class BackupRecoveryMetric(BaseModel):
    backup_frequency_hours: int = 6
    last_restore_test_days_ago: int = 7

class DeterministicDBPipelineResult(BaseModel):
    query_perf: QueryPerformanceMetric
    index_coverage: IndexCoverageAudit
    normalization: DatabaseNormalizationScore
    connection_pool: ConnectionPoolMetric
    data_integrity: DataIntegrityAudit
    backup_recovery: BackupRecoveryMetric
    db_health_score: float
    confidence_score: float

class StrategicDBNarrative(BaseModel):
    db_architecture_summary: str
    key_db_strengths: List[str]

class DBOptimizationPlan(BaseModel):
    indexing_recommendations: List[str]
    sample_query_optimization: str

class ReasoningDBPipelineResult(BaseModel):
    narrative: StrategicDBNarrative
    optimization_plan: DBOptimizationPlan
    reasoning_steps: List[str]

class DatabaseIntelligenceOrchestratorReport(BaseModel):
    department: str = "Database Intelligence"
    department_id: str = "dept_032"
    db_tier: str = "HIGH PERFORMANCE DATABASE"
    db_health_score: float
    confidence_score: float
    deterministic_analysis: DeterministicDBPipelineResult
    reasoning_analysis: ReasoningDBPipelineResult
    reasoning_steps: List[str]
