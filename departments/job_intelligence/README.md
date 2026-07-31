# Department 003: Job Intelligence (`job_intelligence`)

## Overview
The **Job Intelligence Department** delivers an enterprise multi-agent pipeline designed to deconstruct Job Descriptions, extract technical stack requirements, classify seniority levels, benchmark salary expectations, and formulate interview evaluation rubrics.

---

## Internal 10-Agent Architecture

### Deterministic Agents (7)
1. **TechStackExtractorAgent**: Extracts languages, frameworks, databases, and cloud tools.
2. **SeniorityClassifierAgent**: Classifies role seniority and experience year requirements.
3. **ResponsibilityParserAgent**: Extracts core responsibilities and secondary duties.
4. **SalaryBenchmarkAgent**: Estimates salary compensation ranges.
5. **WorkModelExtractorAgent**: Identifies work model (Remote, Hybrid, On-Site).
6. **DomainComplexityAgent**: Measures domain architecture complexity.
7. **JobScorerAgent**: Master deterministic aggregator calculating dataset confidence score.

### Reasoning Agents (2)
8. **IdealCandidateProfilerAgent**: Formulates ideal candidate background and success factors.
9. **InterviewFocusStrategistAgent**: Formulates technical and behavioral evaluation rubrics.

### Orchestrator Agent (1)
10. **JobOrchestratorAgent**: Master Orchestrator uniting deterministic data and LLM reasoning.
