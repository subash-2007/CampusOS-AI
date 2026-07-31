from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.infrastructure_monitoring_intelligence.schemas import (
    StrategicInfraNarrative, InfraOptimizationPlan, ReasoningInfraMonPipelineResult, DeterministicInfraMonPipelineResult
)

class StrategicInfraNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates infrastructure reliability, alerting quality, and scaling posture."""
    def __init__(self):
        super().__init__(agent_id="strategic_infra_narrative", name="Strategic Infrastructure Narrative Agent",
                         description="Evaluates uptime, service health, and alert quality.", icon="Server")

    async def evaluate(self, det: DeterministicInfraMonPipelineResult) -> StrategicInfraNarrative:
        fallback = {
            "infra_health_summary": f"Five-nines infrastructure ({det.infra_health_score:.1f}% health). {det.uptime.uptime_pct_30d}% 30d uptime, {det.service_health.healthy_services_count} healthy services, {det.alerts.active_alerts_count} active alerts.",
            "key_infra_strengths": [f"Auto-scaling enabled with {det.scalability.max_replica_count} max replicas", f"MTTR of {det.uptime.mttr_minutes} minutes with {det.uptime.mtbf_hours}h MTBF"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("SRE Lead", "uptime, SLOs, incident response"),
                                          PromptBuilder.build_user_context({"uptime": det.uptime.uptime_pct_30d}), task_type="infra_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicInfraNarrative(infra_health_summary=parsed.get("infra_health_summary", fallback["infra_health_summary"]),
                                           key_infra_strengths=parsed.get("key_infra_strengths", fallback["key_infra_strengths"]))
        except Exception:
            return StrategicInfraNarrative(**fallback)

class InfraOptimizationPlannerAgent(BaseAgent):
    """Agent 9: Generates capacity planning actions and Prometheus alerting rules."""
    def __init__(self):
        super().__init__(agent_id="infra_optimization_planner", name="Infrastructure Optimization Planner Agent",
                         description="Formulates capacity planning strategies and Prometheus/Grafana alert configs.", icon="Settings")

    async def plan_optimization(self, det: DeterministicInfraMonPipelineResult) -> InfraOptimizationPlan:
        fallback = {
            "capacity_planning_actions": ["Increase database read replicas from 2 to 4 during peak hours (9-11am)", "Implement predictive auto-scaling using historical traffic patterns"],
            "sample_prometheus_alert_rule": "groups:\n  - name: campusos_alerts\n    rules:\n      - alert: HighCPUUsage\n        expr: avg(rate(cpu_seconds_total[5m])) > 0.80\n        for: 5m\n        labels:\n          severity: warning\n        annotations:\n          summary: CPU usage above 80%"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Platform Engineer", "Kubernetes, Prometheus, capacity planning"),
                                          PromptBuilder.build_user_context({"cpu": det.resource_usage.peak_cpu_pct}), task_type="infra_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return InfraOptimizationPlan(capacity_planning_actions=parsed.get("capacity_planning_actions", fallback["capacity_planning_actions"]),
                                         sample_prometheus_alert_rule=parsed.get("sample_prometheus_alert_rule", fallback["sample_prometheus_alert_rule"]))
        except Exception:
            return InfraOptimizationPlan(**fallback)
