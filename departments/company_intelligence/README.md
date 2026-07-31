# Department 004: Company Intelligence (`company_intelligence`)

## Overview
The **Company Intelligence Department** delivers an enterprise multi-agent pipeline designed to research company firmographics, engineering tech stacks, interview focus signals, corporate news sentiment, compensation ratings, and competitive landscape.

---

## Internal 10-Agent Architecture

### Deterministic Agents (7)
1. **CompanyOverviewAgent**: Generates firmographic company metadata.
2. **TechCultureAuditorAgent**: Audits primary tech stack and engineering values.
3. **InterviewPatternSignalAgent**: Maps system design, coding, and behavioral interview weights.
4. **NewsSentimentAgent**: Evaluates corporate events and news sentiment.
5. **CompensationCultureAgent**: Audits compensation transparency and work-life balance ratings.
6. **CompetitiveLandscapeAgent**: Identifies primary industry competitors and market positioning.
7. **CompanyScorerAgent**: Master deterministic aggregator for company metrics.

### Reasoning Agents (2)
8. **CompanyCultureAnalyzerAgent**: Evaluates engineering principles and qualitative workplace culture.
9. **CompanyPrepStrategistAgent**: Formulates company-specific interview preparation guides and question banks.

### Orchestrator Agent (1)
10. **CompanyOrchestratorAgent**: Master Orchestrator Agent uniting deterministic metrics and LLM strategic guidance.
