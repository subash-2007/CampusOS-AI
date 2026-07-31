# Department 009: Memory & Personalization (`memory_personalization`)

## Overview
The **Memory & Personalization Department** delivers an enterprise multi-agent pipeline designed to store user career preferences, track historical session logs, analyze skill mastery trajectories, build domain interest vectors, compute memory retention scores, and dynamically adapt milestone execution plans.

---

## Internal 10-Agent Architecture

### Deterministic Agents (7)
1. **UserPreferencesAuditorAgent**: Audits target roles and geographic preferences.
2. **HistoricalMemoryTrackerAgent**: Tracks historical interaction count and session logs.
3. **SkillTrajectoryAnalyzerAgent**: Tracks mastered vs. in-progress skill acquisition.
4. **PersonalizationVectorBuilderAgent**: Builds domain interest weighting vectors.
5. **ContextRetentionScorerAgent**: Calculates context memory retention score.
6. **UserPersonaClassifierAgent**: Classifies user persona archetype and career stage.
7. **MemoryScorerAgent**: Master deterministic aggregator.

### Reasoning Agents (2)
8. **PersonalizationSynthesizerAgent**: Synthesizes cross-session memory context into tailored guidance.
9. **AdaptiveLearningPathAgent**: Adapts career milestones dynamically based on user velocity.

### Orchestrator Agent (1)
10. **MemoryOrchestratorAgent**: Master Orchestrator Agent uniting session memory and adaptive personalization.
