# Department 046: Billing & Monetization Intelligence
MRR/ARR metrics, user & revenue churn analysis, LTV/CAC ratio calculations, Stripe gateway webhook health, freemium conversion rates, and PCI-DSS invoice compliance.
## 10-Agent Architecture
Deterministic(7): SubscriptionARRMeterAgent, ChurnRateMeterAgent, CustomerLifetimeValueMeterAgent, PaymentGatewayHealthAuditorAgent, PricingTierOptimizationAuditorAgent, InvoiceTaxComplianceAuditorAgent, BillingHealthScorerAgent
Reasoning(2): StrategicBillingNarrativeAgent, MonetizationOptimizationPlannerAgent
Orchestrator(1): BillingMonetizationOrchestratorAgent
