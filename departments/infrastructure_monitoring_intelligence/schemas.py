from typing import List
from pydantic import BaseModel

class SystemUptimeMetric(BaseModel):
    uptime_pct_30d: float = 99.95
    mttr_minutes: float = 4.2
    mtbf_hours: float = 720.0

class CPUMemoryUsageMetric(BaseModel):
    avg_cpu_utilization_pct: float = 38.0
    avg_memory_utilization_pct: float = 52.0
    peak_cpu_pct: float = 71.0

class AlertFiringAudit(BaseModel):
    active_alerts_count: int = 2
    alerts_resolved_last_7d: int = 18
    false_positive_alert_rate_pct: float = 8.0

class ServiceHealthCheckMetric(BaseModel):
    healthy_services_count: int = 24
    unhealthy_services_count: int = 0
    degraded_services_count: int = 1

class LogVolumeMetric(BaseModel):
    daily_log_volume_gb: float = 12.4
    error_log_rate_per_min: float = 0.8

class InfraScalabilityAudit(BaseModel):
    auto_scaling_enabled: bool = True
    max_replica_count: int = 20
    scale_up_trigger_cpu_pct: float = 70.0

class DeterministicInfraMonPipelineResult(BaseModel):
    uptime: SystemUptimeMetric
    resource_usage: CPUMemoryUsageMetric
    alerts: AlertFiringAudit
    service_health: ServiceHealthCheckMetric
    logs: LogVolumeMetric
    scalability: InfraScalabilityAudit
    infra_health_score: float
    confidence_score: float

class StrategicInfraNarrative(BaseModel):
    infra_health_summary: str
    key_infra_strengths: List[str]

class InfraOptimizationPlan(BaseModel):
    capacity_planning_actions: List[str]
    sample_prometheus_alert_rule: str

class ReasoningInfraMonPipelineResult(BaseModel):
    narrative: StrategicInfraNarrative
    optimization_plan: InfraOptimizationPlan
    reasoning_steps: List[str]

class InfraMonitoringOrchestratorReport(BaseModel):
    department: str = "Infrastructure Monitoring Intelligence"
    department_id: str = "dept_037"
    infra_tier: str = "FIVE NINES INFRASTRUCTURE"
    infra_health_score: float
    confidence_score: float
    deterministic_analysis: DeterministicInfraMonPipelineResult
    reasoning_analysis: ReasoningInfraMonPipelineResult
    reasoning_steps: List[str]
