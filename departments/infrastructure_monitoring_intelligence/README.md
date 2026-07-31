# Department 037: Infrastructure Monitoring Intelligence
System uptime, CPU/memory utilization, alert firing audits, service health checks, log volume metrics, and auto-scaling configuration. Generates capacity planning actions and Prometheus alert rules.
## 10-Agent Architecture
Deterministic(7): SystemUptimeMeterAgent, CPUMemoryUsageMeterAgent, AlertFiringAuditorAgent, ServiceHealthCheckMeterAgent, LogVolumeMeterAgent, InfraScalabilityAuditorAgent, InfraHealthScorerAgent
Reasoning(2): StrategicInfraNarrativeAgent, InfraOptimizationPlannerAgent
Orchestrator(1): InfraMonitoringOrchestratorAgent
