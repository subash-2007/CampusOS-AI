# Department 010: Market Trend Intelligence (`market_trend_intelligence`)

## Overview
The **Market Trend Intelligence Department** delivers an enterprise multi-agent pipeline designed to measure hiring demand indices, track rising vs. declining technology stacks, benchmark regional compensation packages, evaluate macro hiring signals, calculate skill salary premiums, and formulate skill future-proofing strategies.

---

## Internal 10-Agent Architecture

### Deterministic Agents (7)
1. **HiringDemandIndexAgent**: Measures live hiring demand tier and YoY job growth rate.
2. **TrendingTechTrackerAgent**: Tracks rising vs. declining tech stacks.
3. **CompensationBenchmarkAgent**: Measures base salary and equity benchmarks.
4. **MacroHiringSignalAgent**: Evaluates remote hiring trends and layoff risk indices.
5. **SkillPremiumCalculatorAgent**: Calculates percentage salary premiums for skills.
6. **IndustrySubsectorGrowthAgent**: Maps fastest growing industry subsectors.
7. **MarketScorerAgent**: Master deterministic aggregator.

### Reasoning Agents (2)
8. **MarketNarrativeEvaluatorAgent**: Evaluates hiring outlook narratives and market opportunities.
9. **TechHedgingStrategistAgent**: Formulates skill future-proofing recommendations.

### Orchestrator Agent (1)
10. **MarketTrendOrchestratorAgent**: Master Orchestrator Agent uniting market trends and strategic guidance.
