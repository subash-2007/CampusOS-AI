# Department 077: Greek Life & Student Organizations
Registered student organization counts, active member involvement, fraternity/sorority chapter anti-hazing compliance, Greek average GPA, annual philanthropy fundraising, community service hours, and event risk management.
## 10-Agent Architecture
Deterministic(7): StudentOrganizationRegistrationMeterAgent, GreekLifeChapterComplianceAuditorAgent, PhilanthropyCommunityServiceMeterAgent, StudentOrgEventRiskManagementAuditorAgent, StudentOrgFinancialAccountAuditorAgent, LeadershipAdvisorTrainingMeterAgent, GreekLifeStudentOrgsScorerAgent
Reasoning(2): StrategicGreekLifeNarrativeAgent, StudentOrgManagementPlannerAgent
Orchestrator(1): GreekLifeStudentOrgsOrchestratorAgent
