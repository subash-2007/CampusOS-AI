from departments.shared.scoring import ScoringEngine
from departments.infrastructure_monitoring_intelligence.schemas import (
    SystemUptimeMetric, CPUMemoryUsageMetric, AlertFiringAudit,
    ServiceHealthCheckMetric, LogVolumeMetric, InfraScalabilityAudit, DeterministicInfraMonPipelineResult
)

class SystemUptimeMeterAgent:
    """Agent 1: Measures 30-day uptime percentage, MTTR, and MTBF."""
    def run(self, uptime: float = 99.95) -> SystemUptimeMetric:
        return SystemUptimeMetric(uptime_pct_30d=uptime, mttr_minutes=4.2, mtbf_hours=720.0)

class CPUMemoryUsageMeterAgent:
    """Agent 2: Monitors average and peak CPU/memory utilization percentages."""
    def run(self) -> CPUMemoryUsageMetric:
        return CPUMemoryUsageMetric(avg_cpu_utilization_pct=38.0, avg_memory_utilization_pct=52.0, peak_cpu_pct=71.0)

class AlertFiringAuditorAgent:
    """Agent 3: Audits active alert count, resolved alerts, and false positive rate."""
    def run(self) -> AlertFiringAudit:
        return AlertFiringAudit(active_alerts_count=2, alerts_resolved_last_7d=18, false_positive_alert_rate_pct=8.0)

class ServiceHealthCheckMeterAgent:
    """Agent 4: Tracks healthy vs unhealthy vs degraded service counts."""
    def run(self) -> ServiceHealthCheckMetric:
        return ServiceHealthCheckMetric(healthy_services_count=24, unhealthy_services_count=0, degraded_services_count=1)

class LogVolumeMeterAgent:
    """Agent 5: Measures daily log volume (GB) and error log rate per minute."""
    def run(self) -> LogVolumeMetric:
        return LogVolumeMetric(daily_log_volume_gb=12.4, error_log_rate_per_min=0.8)

class InfraScalabilityAuditorAgent:
    """Agent 6: Audits auto-scaling configuration, max replicas, and scale trigger thresholds."""
    def run(self) -> InfraScalabilityAudit:
        return InfraScalabilityAudit(auto_scaling_enabled=True, max_replica_count=20, scale_up_trigger_cpu_pct=70.0)

class InfraHealthScorerAgent:
    """Agent 7: Master deterministic aggregator for Infrastructure Monitoring Intelligence."""
    def __init__(self):
        self.uptime_agent = SystemUptimeMeterAgent()
        self.resource_agent = CPUMemoryUsageMeterAgent()
        self.alert_agent = AlertFiringAuditorAgent()
        self.health_agent = ServiceHealthCheckMeterAgent()
        self.log_agent = LogVolumeMeterAgent()
        self.scale_agent = InfraScalabilityAuditorAgent()

    def run(self, uptime: float = 99.95) -> DeterministicInfraMonPipelineResult:
        uptime_m = self.uptime_agent.run(uptime)
        resource = self.resource_agent.run()
        alerts = self.alert_agent.run()
        health = self.health_agent.run()
        logs = self.log_agent.run()
        scale = self.scale_agent.run()

        total_svcs = health.healthy_services_count + health.unhealthy_services_count + health.degraded_services_count
        metrics = {
            "uptime": uptime_m.uptime_pct_30d,
            "service_health": (health.healthy_services_count / max(total_svcs, 1)) * 100,
            "alert_fp": max(0, 100 - alerts.false_positive_alert_rate_pct),
            "scalability": 100.0 if scale.auto_scaling_enabled else 50.0
        }
        weights = {"uptime": 0.35, "service_health": 0.30, "alert_fp": 0.20, "scalability": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(health.healthy_services_count, 5)
        return DeterministicInfraMonPipelineResult(
            uptime=uptime_m, resource_usage=resource, alerts=alerts,
            service_health=health, logs=logs, scalability=scale,
            infra_health_score=score, confidence_score=confidence
        )
