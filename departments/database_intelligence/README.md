# Department 032: Database Intelligence (`database_intelligence`)
Audits query performance, index coverage, normalization form, connection pool utilization, data integrity constraints, and backup/recovery metrics.
## 10-Agent Architecture
Deterministic(7): QueryPerformanceMeterAgent, IndexCoverageAuditorAgent, DatabaseNormalizationScorerAgent, ConnectionPoolMeterAgent, DataIntegrityAuditorAgent, BackupRecoveryAuditorAgent, DatabaseScorerAgent
Reasoning(2): StrategicDBNarrativeAgent, DBOptimizationPlannerAgent
Orchestrator(1): DatabaseIntelligenceOrchestratorAgent
