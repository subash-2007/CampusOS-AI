# Department 002: ATS Optimization (`ats_optimization`)

## Overview
The **ATS Optimization Department** delivers an enterprise multi-agent pipeline designed to parse, benchmark, audit formatting safety, and optimize resumes against Applicant Tracking System (ATS) filters.

---

## Internal 10-Agent Architecture

### Deterministic Agents (7)
1. **HardSkillMatcherAgent**: Calculates hard technical skill keyword overlap.
2. **SoftSkillMatcherAgent**: Audits soft skill presence and frequency.
3. **FormatCompatibilityAgent**: Checks for tab characters, non-ASCII unicode, and font safety.
4. **SectionHeaderAuditorAgent**: Verifies standardness of section titles.
5. **WeakPhraseDetectorAgent**: Flags passive phrases like "responsible for".
6. **QuantificationMeterAgent**: Measures percentage of metric-quantified bullet points.
7. **ATSScorerAgent**: Aggregates metrics into composite ATS score and confidence rating.

### Reasoning Agents (2)
8. **ATSQualitativeAuditorAgent**: Evaluates ATS pass probability and recruiter readability.
9. **ATSKeywordOptimizerAgent**: Formulates keyword placement guides and ATS bullet rewrites.

### Orchestrator Agent (1)
10. **ATSOrchestratorAgent**: Master Orchestrator Agent uniting deterministic scores and LLM recommendations.
