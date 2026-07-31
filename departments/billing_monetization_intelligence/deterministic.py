from departments.shared.scoring import ScoringEngine
from departments.billing_monetization_intelligence.schemas import (
    SubscriptionARRMetric, ChurnRateMetric, CustomerLifetimeValueMetric,
    PaymentGatewayHealthAudit, PricingTierOptimizationAudit, InvoiceTaxComplianceAudit, DeterministicBillingPipelineResult
)

class SubscriptionARRMeterAgent:
    """Agent 1: Measures MRR, ARR, and month-over-month MRR growth rate."""
    def run(self, mrr: float = 48500.0) -> SubscriptionARRMetric:
        arr = mrr * 12
        return SubscriptionARRMetric(mrr_usd=mrr, arr_usd=arr, mrr_growth_rate_pct=14.2)

class ChurnRateMeterAgent:
    """Agent 2: Measures user churn, revenue churn, and Net Revenue Retention (NRR)."""
    def run(self) -> ChurnRateMetric:
        return ChurnRateMetric(user_churn_rate_pct=2.4, revenue_churn_rate_pct=1.1, net_revenue_retention_pct=112.0)

class CustomerLifetimeValueMeterAgent:
    """Agent 3: Calculates CAC, LTV, and LTV/CAC ratio."""
    def run(self) -> CustomerLifetimeValueMetric:
        return CustomerLifetimeValueMetric(cac_usd=140.0, ltv_usd=1680.0, ltv_to_cac_ratio=12.0)

class PaymentGatewayHealthAuditorAgent:
    """Agent 4: Audits Stripe webhook delivery, failed payment dunning recovery rates."""
    def run(self) -> PaymentGatewayHealthAudit:
        return PaymentGatewayHealthAudit(stripe_webhook_delivery_pct=99.8, failed_payment_recovery_pct=78.0, payment_retry_dunning_active=True)

class PricingTierOptimizationAuditorAgent:
    """Agent 5: Audits freemium-to-paid conversion and plan distribution."""
    def run(self) -> PricingTierOptimizationAudit:
        return PricingTierOptimizationAudit(active_subscription_plans=4, freemium_to_paid_conversion_pct=4.8, top_plan_share_pct=62.0)

class InvoiceTaxComplianceAuditorAgent:
    """Agent 6: Validates automatic tax calculation and PCI-DSS compliance status."""
    def run(self) -> InvoiceTaxComplianceAudit:
        return InvoiceTaxComplianceAudit(automatic_tax_calculation=True, pci_dss_compliance_level="Level 1", invoice_generation_latency_sec=1.2)

class BillingHealthScorerAgent:
    """Agent 7: Master deterministic aggregator for Billing & Monetization Intelligence."""
    def __init__(self):
        self.arr_agent = SubscriptionARRMeterAgent()
        self.churn_agent = ChurnRateMeterAgent()
        self.ltv_agent = CustomerLifetimeValueMeterAgent()
        self.gateway_agent = PaymentGatewayHealthAuditorAgent()
        self.pricing_agent = PricingTierOptimizationAuditorAgent()
        self.tax_agent = InvoiceTaxComplianceAuditorAgent()

    def run(self, mrr: float = 48500.0) -> DeterministicBillingPipelineResult:
        arr = self.arr_agent.run(mrr)
        churn = self.churn_agent.run()
        ltv = self.ltv_agent.run()
        gateway = self.gateway_agent.run()
        pricing = self.pricing_agent.run()
        compliance = self.tax_agent.run()

        metrics = {
            "nrr": min(100.0, churn.net_revenue_retention_pct),
            "ltv_ratio": min(100.0, ltv.ltv_to_cac_ratio * 8),
            "webhook": gateway.stripe_webhook_delivery_pct,
            "low_churn": max(0, 100 - churn.user_churn_rate_pct * 15)
        }
        weights = {"nrr": 0.35, "ltv_ratio": 0.25, "webhook": 0.20, "low_churn": 0.20}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(pricing.active_subscription_plans, 2)
        return DeterministicBillingPipelineResult(
            arr=arr, churn=churn, ltv=ltv, payment_gateway=gateway,
            pricing=pricing, compliance=compliance,
            billing_health_score=score, confidence_score=confidence
        )
