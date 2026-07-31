import pytest
import asyncio
from departments.cloud_devops_engineering.deterministic import (
    InfrastructureAsCodeCoverageAgent, CICDPipelineSuccessMeterAgent, KubernetesClusterHealthAgent,
    CloudCostFinOpsMeterAgent, ObservabilitySLOAchievementAgent, DisasterRecoveryRPO_RTOAgent, CloudDevOpsScorerAgent
)
from departments.cloud_devops_engineering.orchestrator import CloudDevOpsEngineeringOrchestratorAgent

IAC_PCT = 95.0
PASS_RATE = 98.5

def test_infrastructure_as_code_coverage():
    agent = InfrastructureAsCodeCoverageAgent()
    res = agent.run(IAC_PCT)
    assert res.terraform_coverage_pct == 95.0

def test_cicd_pipeline_success_meter():
    agent = CICDPipelineSuccessMeterAgent()
    res = agent.run(PASS_RATE)
    assert res.pipeline_pass_rate_pct == 98.5

def test_kubernetes_cluster_health():
    agent = KubernetesClusterHealthAgent()
    res = agent.run(0)
    assert res.pod_restart_count == 0
    assert res.health_tier == "OPTIMAL CLUSTER"

def test_cloud_cost_finops_meter():
    agent = CloudCostFinOpsMeterAgent()
    res = agent.run(42000)
    assert res.monthly_cloud_spend_usd == 42000

def test_observability_slo_achievement():
    agent = ObservabilitySLOAchievementAgent()
    res = agent.run(99.99)
    assert res.slo_uptime_pct == 99.99

def test_disaster_recovery_rpo_rto():
    agent = DisasterRecoveryRPO_RTOAgent()
    res = agent.run()
    assert res.recovery_point_objective_minutes == 5

def test_cloud_devops_scorer():
    agent = CloudDevOpsScorerAgent()
    res = agent.run(IAC_PCT, PASS_RATE)
    assert res.devops_maturity_score >= 85.0
    assert res.confidence_score >= 0.5

def test_cloud_devops_orchestrator_pipeline():
    orchestrator = CloudDevOpsEngineeringOrchestratorAgent()
    report = asyncio.run(orchestrator.run_pipeline(IAC_PCT, PASS_RATE))
    
    assert report.department == "Cloud & DevOps Engineering"
    assert report.department_id == "dept_027"
    assert report.devops_tier == "HIGH MATURITY DEVOPS"
    assert report.confidence_score > 0
    assert len(report.reasoning_steps) == 4
    assert len(report.reasoning_analysis.optimization_plan.terraform_automation_roadmap) > 0
