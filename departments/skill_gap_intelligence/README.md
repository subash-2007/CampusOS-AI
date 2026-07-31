# Department 005: Skill Gap Intelligence (`skill_gap_intelligence`)

## Overview
The **Skill Gap Intelligence Department** delivers an enterprise multi-agent pipeline designed to audit candidate skills, identify missing technical and soft skill gaps, rank learning priorities, estimate bridging timelines, and generate tailored course recommendations.

---

## Internal 10-Agent Architecture

### Deterministic Agents (7)
1. **SkillInventoryAuditorAgent**: Audits candidate mastered skills.
2. **GapMatrixCalculatorAgent**: Calculates missing skill gap matrices.
3. **SkillPriorityRankerAgent**: Ranks missing skills by learning urgency.
4. **CourseRecommendationEngineAgent**: Maps missing skills to enterprise courses.
5. **LearningTimelineEstimatorAgent**: Estimates learning timeline duration.
6. **SkillReadinessScorerAgent**: Calculates readiness index score.
7. **SkillGapScorerAgent**: Master deterministic aggregator.

### Reasoning Agents (2)
8. **SkillGapQualitativeAuditorAgent**: Evaluates readiness index and competitive edge.
9. **LearningRoadmapStrategistAgent**: Formulates weekly learning paths and portfolio projects.

### Orchestrator Agent (1)
10. **SkillGapOrchestratorAgent**: Master Orchestrator Agent uniting deterministic metrics and LLM roadmap guidance.
