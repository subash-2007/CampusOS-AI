# Department 012: Portfolio Intelligence (`portfolio_intelligence`)

## Overview
The **Portfolio Intelligence Department** delivers an enterprise multi-agent pipeline designed to audit GitHub projects, measure technical stack diversity, evaluate README documentation quality, assess system architecture complexity, track open-source contributions, audit code hygiene, and generate GitHub README enhancement guides.

---

## Internal 10-Agent Architecture

### Deterministic Agents (7)
1. **GitHubRepoAuditorAgent**: Audits public repository metadata and live deployment URLs.
2. **TechStackDiversityAgent**: Measures technical stack diversity score.
3. **READMEDocumentationAuditorAgent**: Audits README quality and architecture diagrams.
4. **ArchitectureComplexityEvaluatorAgent**: Assesses system design complexity and patterns.
5. **OpenSourceImpactMeterAgent**: Measures stars, forks, and community contributions.
6. **CodeHygieneAuditorAgent**: Audits test coverage and CI/CD automation.
7. **PortfolioScorerAgent**: Master deterministic aggregator for portfolio metrics.

### Reasoning Agents (2)
8. **PortfolioNarrativeEvaluatorAgent**: Evaluates qualitative engineering depth and project impact.
9. **READMEOptimizationStrategistAgent**: Formulates README markdown rewrites and live demo upgrades.

### Orchestrator Agent (1)
10. **PortfolioOrchestratorAgent**: Master Orchestrator Agent uniting portfolio audits and documentation strategy.
