import pytest, asyncio
from departments.billing_monetization_intelligence.deterministic import (
    SubscriptionARRMeterAgent, ChurnRateMeterAgent, CustomerLifetimeValueMeterAgent,
    PaymentGatewayHealthAuditorAgent, PricingTierOptimizationAuditorAgent, InvoiceTaxComplianceAuditorAgent, BillingHealthScorerAgent
)
from departments.billing_monetization_intelligence.orchestrator import BillingMonetizationOrchestratorAgent

def test_subscription_arr_meter():
    res = SubscriptionARRMeterAgent().run(48500.0)
    assert res.arr_usd == 48500.0 * 12
    assert res.mrr_growth_rate_pct > 0.0

def test_churn_rate_meter():
    res = ChurnRateMeterAgent().run()
    assert res.user_churn_rate_pct < 5.0
    assert res.net_revenue_retention_pct >= 100.0

def test_customer_lifetime_value_meter():
    res = CustomerLifetimeValueMeterAgent().run()
    assert res.ltv_to_cac_ratio >= 3.0

def test_payment_gateway_health_auditor():
    res = PaymentGatewayHealthAuditorAgent().run()
    assert res.stripe_webhook_delivery_pct >= 99.0

def test_pricing_tier_optimization_auditor():
    res = PricingTierOptimizationAuditorAgent().run()
    assert res.active_subscription_plans >= 2

def test_invoice_tax_compliance_auditor():
    res = InvoiceTaxComplianceAuditorAgent().run()
    assert res.automatic_tax_calculation is True
    assert "Level 1" in res.pci_dss_compliance_level

def test_billing_health_scorer():
    res = BillingHealthScorerAgent().run(48500.0)
    assert res.billing_health_score >= 80.0
    assert res.confidence_score >= 0.5

def test_billing_monetization_orchestrator():
    report = asyncio.run(BillingMonetizationOrchestratorAgent().run_pipeline(48500.0))
    assert report.department == "Billing & Monetization Intelligence"
    assert report.department_id == "dept_046"
    assert report.billing_tier == "HIGH GROWTH MONETIZATION"
    assert len(report.reasoning_steps) == 4
