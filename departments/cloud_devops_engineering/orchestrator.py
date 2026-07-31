from typing import Dict, Any, List, Optional
from app.agents.base_agent import BaseAgent
from departments.cloud_devops_engineering.deterministic import CloudDevOpsScorerAgent
from departments.cloud_devops_engineering.reasoning import StrategicDevOpsNarrativeAgent, InfrastructureOptimizationPlannerAgent
from departments.cloud_devops_engineering.schemas import (
    CloudDevOpsEngineeringOrchestratorReport, ReasoningCloudPipelineResult
)

class CloudDevOpsEngineeringOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator Agent for the Cloud & DevOps Engineering Department."""
    def __init__(self):
        super().__init__(
            agent_id="cloud_devops_engineering_orchestrator",
            name="Cloud & DevOps Engineering Master Orchestrator",
            description="Coordinates all 9 sub-agents to deliver a unified Cloud & DevOps Report.",
            icon="Cpu"
        )
        self.scorer = CloudDevOpsScorerAgent()
        self.narrative_agent = StrategicDevOpsNarrativeAgent()
        self.optimization_planner = InfrastructureOptimizationPlannerAgent()

    async def run_pipeline(self, iac_pct: float = 95.0, pass_rate: float = 98.5) -> CloudDevOpsEngineeringOrchestratorReport:
        reasoning_steps = []
        
        # Step 1: Execute Deterministic Pipeline
        reasoning_steps.append("Step 1: Running deterministic Cloud & DevOps Engineering pipeline (Terraform IaC coverage auditing, CI/CD pipeline pass rate metering, Kubernetes cluster health evaluation, Cloud FinOps spend auditing, Observability SLO uptime metering, Disaster Recovery RPO/RTO verification).")
        det_result = self.scorer.run(iac_pct, pass_rate)
        
        # Step 2: Execute Strategic DevOps Narrative Agent
        reasoning_steps.append("Step 2: Executing Strategic DevOps Narrative Agent to evaluate SRE infrastructure maturity.")
        narrative = await self.narrative_agent.evaluate(det_result)
        
        # Step 3: Execute Infrastructure Optimization Planner Agent
        reasoning_steps.append("Step 3: Executing Infrastructure Optimization Planner Agent to formulate Terraform automation and GitHub Actions workflows.")
        optimization = await self.optimization_planner.plan_optimization(det_result)
        
        # Step 4: Synthesize Report
        reasoning_steps.append("Step 4: Compiling Cloud & DevOps Engineering Master Report.")
        reasoning_result = ReasoningCloudPipelineResult(
            narrative=narrative,
            optimization_plan=optimization,
            reasoning_steps=reasoning_steps
        )
        
        tier = "HIGH MATURITY DEVOPS" if det_result.devops_maturity_score >= 85 else "OPERATIONAL DEVOPS"
        
        return CloudDevOpsEngineeringOrchestratorReport(
            devops_tier=tier,
            devops_maturity_score=det_result.devops_maturity_score,
            confidence_score=det_result.confidence_score,
            deterministic_analysis=det_result,
            reasoning_analysis=reasoning_result,
            reasoning_steps=reasoning_steps
        )
