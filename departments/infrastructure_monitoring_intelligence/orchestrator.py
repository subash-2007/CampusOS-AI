from app.agents.base_agent import BaseAgent
from departments.infrastructure_monitoring_intelligence.deterministic import InfraHealthScorerAgent
from departments.infrastructure_monitoring_intelligence.reasoning import StrategicInfraNarrativeAgent, InfraOptimizationPlannerAgent
from departments.infrastructure_monitoring_intelligence.schemas import InfraMonitoringOrchestratorReport, ReasoningInfraMonPipelineResult

class InfraMonitoringOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Infrastructure Monitoring Intelligence Department."""
    def __init__(self):
        super().__init__(agent_id="infra_monitoring_orchestrator", name="Infrastructure Monitoring Intelligence Master Orchestrator",
                         description="Coordinates all 9 infrastructure monitoring sub-agents.", icon="Activity")
        self.scorer = InfraHealthScorerAgent()
        self.narrative_agent = StrategicInfraNarrativeAgent()
        self.optimization_planner = InfraOptimizationPlannerAgent()

    async def run_pipeline(self, uptime: float = 99.95) -> InfraMonitoringOrchestratorReport:
        steps = ["Step 1: Running deterministic Infrastructure Monitoring pipeline (uptime, CPU/memory, alerts, service health, logs, scalability)."]
        det = self.scorer.run(uptime)
        steps.append("Step 2: Executing Strategic Infrastructure Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Infrastructure Optimization Planner Agent.")
        optimization = await self.optimization_planner.plan_optimization(det)
        steps.append("Step 4: Compiling Infrastructure Monitoring Master Report.")
        tier = "FIVE NINES INFRASTRUCTURE" if det.infra_health_score >= 90 else "STANDARD INFRASTRUCTURE"
        return InfraMonitoringOrchestratorReport(
            infra_tier=tier, infra_health_score=det.infra_health_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningInfraMonPipelineResult(narrative=narrative, optimization_plan=optimization, reasoning_steps=steps),
            reasoning_steps=steps
        )
