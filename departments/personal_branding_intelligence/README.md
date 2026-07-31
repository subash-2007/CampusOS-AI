# Department 020: Personal Branding Intelligence (`personal_branding_intelligence`)

## Overview
The **Personal Branding Intelligence Department** delivers an enterprise multi-agent pipeline designed to audit LinkedIn profile completeness, measure thought leadership engagement, optimize bio headlines for SEO keywords, track cross-platform developer presence, audit brand narrative voice consistency, catalog media features, and generate monthly content calendars.

---

## Internal 10-Agent Architecture

### Deterministic Agents (7)
1. **LinkedInProfileCompletenessAgent**: Audits LinkedIn section coverage and profile scores.
2. **ThoughtLeadershipEngagementAgent**: Measures post frequency and engagement rates.
3. **BioHeadlineSEOAgent**: Evaluates bio headline SEO keyword density.
4. **CrossPlatformPresenceAgent**: Tracks developer presence across GitHub, LinkedIn, Medium, and X.
5. **BrandConsistencyIndexAgent**: Audits narrative voice consistency across public channels.
6. **MediaFeatureAuditorAgent**: Audits published articles, podcasts, and talks.
7. **BrandingScorerAgent**: Master deterministic aggregator for personal branding metrics.

### Reasoning Agents (2)
8. **StrategicBrandNarrativeAgent**: Formulates thought leadership positioning narratives.
9. **ContentCalendarStrategistAgent**: Generates monthly technical post topics and LinkedIn post drafts.

### Orchestrator Agent (1)
10. **PersonalBrandingOrchestratorAgent**: Master Orchestrator Agent uniting branding metrics and content calendar strategy.
