# Department 061: Parent & Guardian Relations
Parent portal adoption metrics, FERPA compliance & waiver authorization, family newsletter open rates, parent orientation attendance, family fund giving, and emergency family contact alert dispatch speed.
## 10-Agent Architecture
Deterministic(7): ParentPortalEngagementMeterAgent, FERPAAccessControlAuditorAgent, FamilyNewsletterOpenRateMeterAgent, ParentOrientationAttendanceMeterAgent, ParentAssociationDonationAuditorAgent, EmergencyFamilyNotificationAuditorAgent, ParentGuardianRelationsScorerAgent
Reasoning(2): StrategicParentNarrativeAgent, FamilyEngagementPlannerAgent
Orchestrator(1): ParentGuardianRelationsOrchestratorAgent
