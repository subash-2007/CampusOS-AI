# Department 089: Admissions & Enrollment Management
Undergraduate application volume & selectivity rates, freshman enrollment yield rates & tuition deposit fulfillment, holistic application review turnaround speed, campus tour visitor conversion, Slate CRM recruitment funnels, and high school academic profiles.
## 10-Agent Architecture
Deterministic(7): UndergraduateAdmissionsApplicationVolumeMeterAgent, EnrollmentYieldDepositMeterAgent, ApplicationHolisticReviewTurnaroundAuditorAgent, CampusTourOpenHouseVisitorMeterAgent, CRMRecruitmentCampaignAuditorAgent, HighSchoolGPAStandardizedTestAuditorAgent, AdmissionsEnrollmentManagementScorerAgent
Reasoning(2): StrategicAdmissionsNarrativeAgent, EnrollmentStrategyPlannerAgent
Orchestrator(1): AdmissionsEnrollmentManagementOrchestratorAgent
