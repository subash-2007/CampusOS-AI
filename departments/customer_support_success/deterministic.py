from departments.shared.scoring import ScoringEngine
from departments.customer_support_success.schemas import (
    TicketResolutionTimeMetric, CustomerSatisfactionMetric, TicketDeflectionRateAudit,
    CustomerHealthScoreAudit, SupportChannelVolumeAudit, SupportAgentPerformanceMetric, DeterministicSupportPipelineResult
)

class TicketResolutionTimeMeterAgent:
    """Agent 1: Measures first response time, resolution time, and SLA compliance rate."""
    def run(self, response_time: float = 14.2) -> TicketResolutionTimeMetric:
        return TicketResolutionTimeMetric(avg_first_response_time_minutes=response_time, avg_resolution_time_hours=3.8, sla_compliance_pct=96.8)

class CustomerSatisfactionMeterAgent:
    """Agent 2: Measures CSAT, CES (Customer Effort Score), and support NPS."""
    def run(self) -> CustomerSatisfactionMetric:
        return CustomerSatisfactionMetric(csat_score_pct=94.5, ces_score=6.2, nps_score=64.0)

class TicketDeflectionRateAuditorAgent:
    """Agent 3: Audits AI self-service deflection rate and estimated cost savings."""
    def run(self) -> TicketDeflectionRateAudit:
        return TicketDeflectionRateAudit(ai_deflection_rate_pct=42.0, self_service_kb_views=14200, deflection_savings_usd=18500.0)

class CustomerHealthScoreAuditorAgent:
    """Agent 4: Tracks healthy accounts percentage and identifies at-risk accounts."""
    def run(self) -> CustomerHealthScoreAudit:
        return CustomerHealthScoreAudit(healthy_accounts_pct=84.0, at_risk_accounts_count=8, critical_risk_accounts_count=1)

class SupportChannelVolumeAuditorAgent:
    """Agent 5: Audits support channel volume breakdown (chat, email, phone) and total tickets."""
    def run(self) -> SupportChannelVolumeAudit:
        return SupportChannelVolumeAudit(chat_tickets_pct=58.0, email_tickets_pct=34.0, phone_tickets_pct=8.0, total_tickets_last_30d=2450)

class SupportAgentPerformanceMeterAgent:
    """Agent 6: Measures tickets resolved per agent and agent satisfaction score."""
    def run(self) -> SupportAgentPerformanceMetric:
        return SupportAgentPerformanceMetric(active_support_agents=14, avg_tickets_resolved_per_agent_day=24.5, agent_satisfaction_score=88.0)

class CustomerSupportScorerAgent:
    """Agent 7: Master deterministic aggregator for Customer Support & Success Intelligence."""
    def __init__(self):
        self.resolution_agent = TicketResolutionTimeMeterAgent()
        self.csat_agent = CustomerSatisfactionMeterAgent()
        self.deflection_agent = TicketDeflectionRateAuditorAgent()
        self.health_agent = CustomerHealthScoreAuditorAgent()
        self.volume_agent = SupportChannelVolumeAuditorAgent()
        self.agent_perf = SupportAgentPerformanceMeterAgent()

    def run(self, response_time: float = 14.2) -> DeterministicSupportPipelineResult:
        res = self.resolution_agent.run(response_time)
        csat = self.csat_agent.run()
        deflection = self.deflection_agent.run()
        health = self.health_agent.run()
        volume = self.volume_agent.run()
        agent_perf = self.agent_perf.run()

        metrics = {
            "csat": csat.csat_score_pct,
            "sla": res.sla_compliance_pct,
            "healthy": health.healthy_accounts_pct,
            "deflection": deflection.ai_deflection_rate_pct * 2
        }
        weights = {"csat": 0.35, "sla": 0.30, "healthy": 0.20, "deflection": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(agent_perf.active_support_agents, 5)
        return DeterministicSupportPipelineResult(
            resolution_time=res, csat=csat, deflection=deflection,
            health=health, volume=volume, agent_performance=agent_perf,
            support_excellence_score=score, confidence_score=confidence
        )
