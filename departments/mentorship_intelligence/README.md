# Department 018: Mentorship Intelligence (`mentorship_intelligence`)

## Overview
The **Mentorship Intelligence Department** delivers an enterprise multi-agent pipeline designed to match candidate career goals with senior mentors, plan 1-on-1 session cadences, measure technical expertise overlaps, align mentorship goals, score mentor availability, audit feedback ratings, and generate structured meeting agendas.

---

## Internal 10-Agent Architecture

### Deterministic Agents (7)
1. **MentorProfileMatcherAgent**: Matches candidate career goals against mentor profiles.
2. **MentorshipCadencePlannerAgent**: Recommends session cadence and frequency.
3. **MentorExpertiseOverlapAgent**: Measures domain expertise overlap score.
4. **MentorshipGoalAlignerAgent**: Aligns mentee career goals with mentor strengths.
5. **MentorAvailabilityScorerAgent**: Scores mentor scheduling availability.
6. **FeedbackLoopAuditorAgent**: Audits session feedback completion and rating history.
7. **MentorshipScorerAgent**: Master deterministic aggregator for mentorship metrics.

### Reasoning Agents (2)
8. **QualitativeMentorshipNarrativeAgent**: Evaluates mentorship compatibility narratives.
9. **SessionAgendaPlannerAgent**: Formulates 1-on-1 meeting agendas and milestones.

### Orchestrator Agent (1)
10. **MentorshipOrchestratorAgent**: Master Orchestrator Agent uniting mentorship matching and agenda planning.
