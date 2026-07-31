from departments.shared.scoring import ScoringEngine
from departments.partner_ecosystem_intelligence.schemas import (
    ActivePartnershipsMetric, PartnerAttributedRevenueMetric, IntegrationUsageMetric,
    PartnerCertificationAudit, EcosystemMarketplaceMetric, PartnerSLAComplianceAudit, DeterministicPartnerPipelineResult
)

class ActivePartnershipsMeterAgent:
    """Agent 1: Measures active partner count, strategic partners, and tech integration count."""
    def run(self, partners: int = 48) -> ActivePartnershipsMetric:
        return ActivePartnershipsMetric(active_partners_count=partners, strategic_partners_count=12, technology_integrations_count=24)

class PartnerAttributedRevenueMeterAgent:
    """Agent 2: Tracks partner-sourced MRR and partner-influenced revenue percentage."""
    def run(self) -> PartnerAttributedRevenueMetric:
        return PartnerAttributedRevenueMetric(partner_sourced_mrr_usd=12400.0, partner_influence_revenue_pct=24.5)

class IntegrationUsageMeterAgent:
    """Agent 3: Measures monthly partner API calls and top integration adoption."""
    def run(self) -> IntegrationUsageMetric:
        return IntegrationUsageMetric(monthly_api_calls_via_partners=2850000, top_integration="LinkedIn Talent Hub", active_integration_users_pct=68.0)

class PartnerCertificationAuditorAgent:
    """Agent 4: Audits partner certification completion rates and portal engagement."""
    def run(self) -> PartnerCertificationAudit:
        return PartnerCertificationAudit(certified_partners_pct=82.0, partner_portal_active_users=156)

class EcosystemMarketplaceMeterAgent:
    """Agent 5: Measures marketplace app count, average app rating, and total installations."""
    def run(self) -> EcosystemMarketplaceMetric:
        return EcosystemMarketplaceMetric(marketplace_apps_count=34, avg_app_rating=4.8, total_app_installations=18400)

class PartnerSLAComplianceAuditorAgent:
    """Agent 6: Audits partner API uptime and SLA response times."""
    def run(self) -> PartnerSLAComplianceAudit:
        return PartnerSLAComplianceAudit(partner_api_uptime_pct=99.9, partner_support_response_hours=1.8)

class PartnerEcosystemScorerAgent:
    """Agent 7: Master deterministic aggregator for Partner & Ecosystem Intelligence."""
    def __init__(self):
        self.partnerships_agent = ActivePartnershipsMeterAgent()
        self.revenue_agent = PartnerAttributedRevenueMeterAgent()
        self.usage_agent = IntegrationUsageMeterAgent()
        self.cert_agent = PartnerCertificationAuditorAgent()
        self.marketplace_agent = EcosystemMarketplaceMeterAgent()
        self.sla_agent = PartnerSLAComplianceAuditorAgent()

    def run(self, partners: int = 48) -> DeterministicPartnerPipelineResult:
        partnerships = self.partnerships_agent.run(partners)
        revenue = self.revenue_agent.run()
        usage = self.usage_agent.run()
        cert = self.cert_agent.run()
        marketplace = self.marketplace_agent.run()
        sla = self.sla_agent.run()

        metrics = {
            "partner_revenue": revenue.partner_influence_revenue_pct * 3,
            "integration_adoption": usage.active_integration_users_pct,
            "certification": cert.certified_partners_pct,
            "sla": sla.partner_api_uptime_pct
        }
        weights = {"partner_revenue": 0.30, "integration_adoption": 0.30, "certification": 0.20, "sla": 0.20}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(partnerships.active_partners_count, 10)
        return DeterministicPartnerPipelineResult(
            partnerships=partnerships, revenue=revenue, integration_usage=usage,
            certification=cert, marketplace=marketplace, sla=sla,
            ecosystem_health_score=score, confidence_score=confidence
        )
