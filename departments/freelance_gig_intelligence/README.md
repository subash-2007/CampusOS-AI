# Department 019: Freelance & Gig Intelligence (`freelance_gig_intelligence`)

## Overview
The **Freelance & Gig Intelligence Department** delivers an enterprise multi-agent pipeline designed to benchmark freelance hourly billing rates, evaluate contract scope complexity, audit client payment reputation, calculate proposal win probabilities, model platform fees, estimate self-employment tax liabilities, and generate high-converting proposal drafts.

---

## Internal 10-Agent Architecture

### Deterministic Agents (7)
1. **HourlyRateBenchmarkAgent**: Benchmarks hourly rates against market datasets.
2. **ContractScopeComplexityAgent**: Evaluates scope creep risks and billable hours.
3. **ClientReputationAuditorAgent**: Audits client payment verification and reviews.
4. **ProposalWinProbabilityAgent**: Calculates win probability based on competition.
5. **PlatformFeeCalculatorAgent**: Models platform service fees and net take-home pay.
6. **TaxComplianceAuditorAgent**: Estimates self-employment taxes and deductibles.
7. **FreelanceScorerAgent**: Master deterministic aggregator for contract metrics.

### Reasoning Agents (2)
8. **StrategicProposalNarrativeAgent**: Formulates proposal strategy and differentiators.
9. **ProposalDraftGeneratorAgent**: Generates proposal cover letters and milestone schedules.

### Orchestrator Agent (1)
10. **FreelanceGigOrchestratorAgent**: Master Orchestrator Agent uniting contract evaluation and proposal generation.
