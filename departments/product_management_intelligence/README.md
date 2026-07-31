# Department 024: Product Management Intelligence (`product_management_intelligence`)

## Overview
The **Product Management Intelligence Department** delivers an enterprise multi-agent pipeline designed to audit PRD completeness, compute RICE framework feature priority scores, evaluate strategic roadmap alignment, measure Day-30 user cohort retention, benchmark competitor feature matrices, audit product telemetry (DAU), and generate PRD user story specifications.

---

## Internal 10-Agent Architecture

### Deterministic Agents (7)
1. **PRDCompletenessMeterAgent**: Audits PRD completeness and section coverage.
2. **RICEPrioritizationScorerAgent**: Calculates RICE framework feature priority scores.
3. **FeatureRoadmapAlignerAgent**: Evaluates feature alignment against quarterly roadmaps.
4. **UserCohortRetentionMeterAgent**: Measures Day-30 user cohort retention rates.
5. **CompetitorFeatureMatrixAgent**: Benchmarks feature parity against competitors.
6. **ProductAnalyticsTelemetryAgent**: Audits DAU metrics and funnel telemetry.
7. **ProductScorerAgent**: Master deterministic aggregator for product viability metrics.

### Reasoning Agents (2)
8. **StrategicProductNarrativeAgent**: Formulates product-market fit evaluations.
9. **PRDSpecificationGeneratorAgent**: Generates PRD user stories and acceptance criteria.

### Orchestrator Agent (1)
10. **ProductManagementOrchestratorAgent**: Master Orchestrator Agent uniting product metrics and PRD drafting.
