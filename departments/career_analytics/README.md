# Department 008: Career Analytics (`career_analytics`)

## Overview
The **Career Analytics Department** delivers an enterprise multi-agent pipeline designed to measure candidate readiness scores, aggregate domain radar distributions, determine market competitiveness tiers, analyze historical progress trends, benchmark against top-tier peers, and compute improvement velocity.

---

## Internal 10-Agent Architecture

### Deterministic Agents (7)
1. **ReadinessMetricCalculatorAgent**: Calculates overall readiness score and percentile rank.
2. **DomainRadarAggregatorAgent**: Aggregates technical, system design, ATS, and behavioral scores.
3. **MarketCompetitivenessTierAgent**: Classifies candidate into market tiers (e.g. Top 10%).
4. **HistoricalTrendAnalyzerAgent**: Analyzes progress data points across recent months.
5. **PeerBenchmarkComparisonAgent**: Benchmarks user score against peer average and top-tier score.
6. **ImprovementVelocityMeterAgent**: Measures weekly improvement velocity rate.
7. **AnalyticsScorerAgent**: Master deterministic aggregator for Career Analytics.

### Reasoning Agents (2)
8. **AnalyticsNarrativeEvaluatorAgent**: Formulates qualitative performance summaries and growth drivers.
9. **ActionableAnalyticsStrategistAgent**: Formulates quick-win recommendations based on radar gaps.

### Orchestrator Agent (1)
10. **AnalyticsOrchestratorAgent**: Master Orchestrator Agent uniting performance metrics and strategic advice.
