# Department 039: User Onboarding Intelligence (`user_onboarding_intelligence`)
Onboarding completion rates, step-level dropoff analysis, time-to-first-value, guided tour engagement, personalization path assignment, and NPS measurement.
## 10-Agent Architecture
Deterministic(7): OnboardingCompletionMeterAgent, OnboardingStepDropoffAuditorAgent, FirstValueEventMeterAgent, GuidedTourEngagementMeterAgent, OnboardingPersonalizationAuditorAgent, OnboardingNPSMeterAgent, OnboardingQualityScorerAgent
Reasoning(2): StrategicOnboardingNarrativeAgent, OnboardingImprovementPlannerAgent
Orchestrator(1): UserOnboardingOrchestratorAgent
