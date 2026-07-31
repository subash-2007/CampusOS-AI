# Department 013: Communication Intelligence (`communication_intelligence`)

## Overview
The **Communication Intelligence Department** delivers an enterprise multi-agent pipeline designed to analyze email tone, measure executive brevity word counts, audit grammar patterns, score actionability CTAs, evaluate persuasiveness, grade vocabulary sophistication, and generate high-converting email rewrites.

---

## Internal 10-Agent Architecture

### Deterministic Agents (7)
1. **EmailToneAnalyzerAgent**: Analyzes professional tone and courtesy markers.
2. **ExecutiveBrevityMeterAgent**: Measures concise word counts and executive brevity.
3. **GrammarSpellingAuditorAgent**: Audits basic grammar patterns and flagged weak phrases.
4. **ActionabilityIndexAgent**: Scans for explicit Call-To-Action (CTA) elements.
5. **PersuasivenessScorerAgent**: Evaluates value proposition presence and persuasive strength.
6. **VocabularySophisticationAgent**: Grades vocabulary tier and readability index.
7. **CommunicationScorerAgent**: Master deterministic aggregator for communication metrics.

### Reasoning Agents (2)
8. **QualitativeCommunicationNarrativeAgent**: Evaluates tone alignment and executive impact.
9. **EmailRewriteStrategistAgent**: Formulates high-converting executive email rewrites.

### Orchestrator Agent (1)
10. **CommunicationOrchestratorAgent**: Master Orchestrator Agent uniting communication analysis and rewrite generation.
