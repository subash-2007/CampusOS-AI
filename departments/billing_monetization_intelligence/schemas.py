from typing import List
from pydantic import BaseModel

class SubscriptionARRMetric(BaseModel):
    mrr_usd: float = 48500.0
    arr_usd: float = 582000.0
    mrr_growth_rate_pct: float = 14.2

class ChurnRateMetric(BaseModel):
    user_churn_rate_pct: float = 2.4
    revenue_churn_rate_pct: float = 1.1
    net_revenue_retention_pct: float = 112.0

class CustomerLifetimeValueMetric(BaseModel):
    cac_usd: float = 140.0
    ltv_usd: float = 1680.0
    ltv_to_cac_ratio: float = 12.0

class PaymentGatewayHealthAudit(BaseModel):
    stripe_webhook_delivery_pct: float = 99.8
    failed_payment_recovery_pct: float = 78.0
    payment_retry_dunning_active: bool = True

class PricingTierOptimizationAudit(BaseModel):
    active_subscription_plans: int = 4
    freemium_to_paid_conversion_pct: float = 4.8
    top_plan_share_pct: float = 62.0

class InvoiceTaxComplianceAudit(BaseModel):
    automatic_tax_calculation: bool = True
    pci_dss_compliance_level: str = "Level 1"
    invoice_generation_latency_sec: float = 1.2

class DeterministicBillingPipelineResult(BaseModel):
    arr: SubscriptionARRMetric
    churn: ChurnRateMetric
    ltv: CustomerLifetimeValueMetric
    payment_gateway: PaymentGatewayHealthAudit
    pricing: PricingTierOptimizationAudit
    compliance: InvoiceTaxComplianceAudit
    billing_health_score: float
    confidence_score: float

class StrategicBillingNarrative(BaseModel):
    billing_summary: str
    key_billing_strengths: List[str]

class MonetizationOptimizationPlan(BaseModel):
    pricing_improvement_actions: List[str]
    sample_stripe_webhook_handler: str

class ReasoningBillingPipelineResult(BaseModel):
    narrative: StrategicBillingNarrative
    monetization_plan: MonetizationOptimizationPlan
    reasoning_steps: List[str]

class BillingMonetizationOrchestratorReport(BaseModel):
    department: str = "Billing & Monetization Intelligence"
    department_id: str = "dept_046"
    billing_tier: str = "HIGH GROWTH MONETIZATION"
    billing_health_score: float
    confidence_score: float
    deterministic_analysis: DeterministicBillingPipelineResult
    reasoning_analysis: ReasoningBillingPipelineResult
    reasoning_steps: List[str]
