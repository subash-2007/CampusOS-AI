# Department 016: Offer & Salary Negotiation (`offer_salary_negotiation`)

## Overview
The **Offer & Salary Negotiation Department** delivers an enterprise multi-agent pipeline designed to benchmark base salary offers, model 4-year equity vesting, audit signing bonuses, evaluate relocation perks, calculate Year-1 Total Compensation (TC), score negotiation leverage, and generate counter-offer email scripts.

---

## Internal 10-Agent Architecture

### Deterministic Agents (7)
1. **BaseSalaryBenchmarkAgent**: Benchmarks offered base salary against market datasets.
2. **EquityGrantValuationAgent**: Models 4-year equity vesting and RSU valuation.
3. **SigningBonusAuditorAgent**: Audits one-time signing bonus offerings.
4. **RelocationPerksMetricAgent**: Evaluates relocation stipends and remote perks.
5. **TotalCompCalculatorAgent**: Calculates Year-1 total compensation.
6. **NegotiationLeverageScorerAgent**: Measures candidate negotiation leverage.
7. **OfferScorerAgent**: Master deterministic aggregator for offer metrics.

### Reasoning Agents (2)
8. **StrategicNegotiationNarrativeAgent**: Formulates negotiation positioning and target counter-offer TC.
9. **CounterOfferScriptGeneratorAgent**: Generates counter-offer email drafts and verbal talking points.

### Orchestrator Agent (1)
10. **OfferSalaryOrchestratorAgent**: Master Orchestrator Agent uniting offer evaluation and counter-offer script generation.
