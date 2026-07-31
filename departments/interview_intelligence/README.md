# Department 006: Interview Intelligence (`interview_intelligence`)

## Overview
The **Interview Intelligence Department** delivers an enterprise multi-agent pipeline designed to generate tailored technical coding questions, STAR-method behavioral scenarios, system design prompts, difficulty distributions, evaluation rubrics, and mock interview simulation plans.

---

## Internal 10-Agent Architecture

### Deterministic Agents (7)
1. **TechQuestionGeneratorAgent**: Generates stack-specific technical coding questions.
2. **BehavioralSTARGeneratorAgent**: Generates STAR-method behavioral scenarios.
3. **SystemDesignPromptGeneratorAgent**: Generates system design scenarios.
4. **DifficultyDistributionAgent**: Maps easy/medium/hard question ratios.
5. **RubricCriteriaBuilderAgent**: Builds 4-dimension interview evaluation rubrics.
6. **InterviewDurationCalculatorAgent**: Calculates interview rounds and total time.
7. **InterviewScorerAgent**: Master deterministic aggregator.

### Reasoning Agents (2)
8. **STARResponseCoachAgent**: Formulates high-impact STAR answer frameworks.
9. **MockSimulationStrategistAgent**: Formulates timed mock simulation plans and pitfall mitigation.

### Orchestrator Agent (1)
10. **InterviewOrchestratorAgent**: Master Orchestrator Agent uniting questions, rubrics, and simulation plans.
