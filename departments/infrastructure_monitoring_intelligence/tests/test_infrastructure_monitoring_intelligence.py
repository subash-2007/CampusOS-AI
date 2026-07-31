import pytest, asyncio
from departments.infrastructure_monitoring_intelligence.deterministic import (
    SystemUptimeMeterAgent, CPUMemoryUsageMeterAgent, AlertFiringAuditorAgent,
    ServiceHealthCheckMeterAgent, LogVolumeMeterAgent, InfraScalabilityAuditorAgent, InfraHealthScorerAgent
)
from departments.infrastructure_monitoring_intelligence.orchestrator import InfraMonitoringOrchestratorAgent

def test_system_uptime_meter():
    res = SystemUptimeMeterAgent().run(99.95)
    assert res.uptime_pct_30d >= 99.0
    assert res.mttr_minutes < 60

def test_cpu_memory_usage_meter():
    res = CPUMemoryUsageMeterAgent().run()
    assert res.avg_cpu_utilization_pct < 80.0

def test_alert_firing_auditor():
    res = AlertFiringAuditorAgent().run()
    assert res.false_positive_alert_rate_pct < 20.0

def test_service_health_check_meter():
    res = ServiceHealthCheckMeterAgent().run()
    assert res.unhealthy_services_count == 0
    assert res.healthy_services_count >= 10

def test_log_volume_meter():
    res = LogVolumeMeterAgent().run()
    assert res.error_log_rate_per_min < 10.0

def test_infra_scalability_auditor():
    res = InfraScalabilityAuditorAgent().run()
    assert res.auto_scaling_enabled is True

def test_infra_health_scorer():
    res = InfraHealthScorerAgent().run(99.95)
    assert res.infra_health_score >= 90.0
    assert res.confidence_score >= 0.5

def test_infra_monitoring_orchestrator():
    report = asyncio.run(InfraMonitoringOrchestratorAgent().run_pipeline(99.95))
    assert report.department == "Infrastructure Monitoring Intelligence"
    assert report.department_id == "dept_037"
    assert report.infra_tier == "FIVE NINES INFRASTRUCTURE"
    assert len(report.reasoning_steps) == 4
