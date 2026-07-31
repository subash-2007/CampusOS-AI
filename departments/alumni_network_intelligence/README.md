# Department 017: Alumni Network Intelligence (`alumni_network_intelligence`)

## Overview
The **Alumni Network Intelligence Department** delivers an enterprise multi-agent pipeline designed to match candidate target companies with university alumni directories, score referral likelihood, detect shared academic background overlaps, measure historical alumni outreach response rates, map seniority distributions, and generate high-converting warm introduction drafts.

---

## Internal 10-Agent Architecture

### Deterministic Agents (7)
1. **AlumniDirectoryMatcherAgent**: Matches candidate target companies against alumni directories.
2. **ReferralLikelihoodScorerAgent**: Scores likelihood of obtaining employee referrals.
3. **SharedBackgroundOverlapAgent**: Identifies shared university, major, and student organization overlaps.
4. **OutreachResponseRateMeterAgent**: Measures historical alumni response rates.
5. **AlumniSeniorityDistributionAgent**: Maps alumni seniority distribution.
6. **GeographicAlumniDensityAgent**: Measures alumni density in target metro areas.
7. **AlumniScorerAgent**: Master deterministic aggregator for alumni network metrics.

### Reasoning Agents (2)
8. **StrategicAlumniOutreachNarrativeAgent**: Formulates strategic alumni networking narratives.
9. **OutreachIntroScriptGeneratorAgent**: Generates personalized alumni outreach drafts.

### Orchestrator Agent (1)
10. **AlumniNetworkOrchestratorAgent**: Master Orchestrator Agent uniting alumni network analysis and outreach generation.
