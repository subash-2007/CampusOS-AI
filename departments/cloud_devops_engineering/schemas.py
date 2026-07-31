from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class InfrastructureAsCodeCoverage(BaseModel):
    terraform_coverage_pct: float = 95.0
    drift_detected: bool = False

class CICDPipelineSuccessRate(BaseModel):
    pipeline_pass_rate_pct: float = 98.5
    average_build_duration_minutes: float = 4.2

class KubernetesClusterHealth(BaseModel):
    node_utilization_pct: float = 68.0
    pod_restart_count: int = 0
    health_tier: str = "OPTIMAL CLUSTER"

class CloudCostFinOpsMetric(BaseModel):
    monthly_cloud_spend_usd: int = 42000
    wasted_spend_pct: float = 4.5

class ObservabilitySLOAchievement(BaseModel):
    slo_uptime_pct: float = 99.99
    p99_latency_ms: int = 99

class DisasterRecoveryRPO_RTO(BaseModel):
    recovery_point_objective_minutes: int = 5
    recovery_time_objective_minutes: int = 15

class DeterministicCloudPipelineResult(BaseModel):
    iac: InfrastructureAsCodeCoverage
    cicd: CICDPipelineSuccessRate
    k8s: KubernetesClusterHealth
    finops: CloudCostFinOpsMetric
    slo: ObservabilitySLOAchievement
    dr: DisasterRecoveryRPO_RTO
    devops_maturity_score: float
    confidence_score: float

class StrategicDevOpsNarrative(BaseModel):
    devops_architecture_summary: str
    key_infrastructure_highlights: List[str]

class InfrastructureOptimizationPlan(BaseModel):
    terraform_automation_roadmap: List[str]
    sample_github_actions_workflow: str

class ReasoningCloudPipelineResult(BaseModel):
    narrative: StrategicDevOpsNarrative
    optimization_plan: InfrastructureOptimizationPlan
    reasoning_steps: List[str]

class CloudDevOpsEngineeringOrchestratorReport(BaseModel):
    department: str = "Cloud & DevOps Engineering"
    department_id: str = "dept_027"
    devops_tier: str = "HIGH MATURITY DEVOPS"
    devops_maturity_score: float
    confidence_score: float
    deterministic_analysis: DeterministicCloudPipelineResult
    reasoning_analysis: ReasoningCloudPipelineResult
    reasoning_steps: List[str]
