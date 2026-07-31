import pytest, asyncio
from departments.database_intelligence.deterministic import (
    QueryPerformanceMeterAgent, IndexCoverageAuditorAgent, DatabaseNormalizationScorerAgent,
    ConnectionPoolMeterAgent, DataIntegrityAuditorAgent, BackupRecoveryAuditorAgent, DatabaseScorerAgent
)
from departments.database_intelligence.orchestrator import DatabaseIntelligenceOrchestratorAgent

def test_query_performance_meter():
    res = QueryPerformanceMeterAgent().run(8.5)
    assert res.query_performance_tier == "OPTIMAL"
    assert res.slow_queries_count == 0

def test_index_coverage_auditor():
    res = IndexCoverageAuditorAgent().run(95.0)
    assert res.index_coverage_pct >= 90.0

def test_database_normalization_scorer():
    res = DatabaseNormalizationScorerAgent().run()
    assert res.normalization_form == "3NF"

def test_connection_pool_meter():
    res = ConnectionPoolMeterAgent().run(20)
    assert res.pool_utilization_pct <= 80.0

def test_data_integrity_auditor():
    res = DataIntegrityAuditorAgent().run()
    assert res.foreign_key_constraints_enforced is True

def test_backup_recovery_auditor():
    res = BackupRecoveryAuditorAgent().run()
    assert res.backup_frequency_hours <= 12

def test_database_scorer():
    res = DatabaseScorerAgent().run(8.5, 95.0)
    assert res.db_health_score >= 80.0
    assert res.confidence_score >= 0.5

def test_database_intelligence_orchestrator():
    report = asyncio.run(DatabaseIntelligenceOrchestratorAgent().run_pipeline(8.5, 95.0))
    assert report.department == "Database Intelligence"
    assert report.department_id == "dept_032"
    assert len(report.reasoning_steps) == 4
