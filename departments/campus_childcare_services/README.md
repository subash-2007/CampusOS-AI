# Department 074: Campus Childcare & Family Services
Childcare center capacity & enrollment, CCAMPIS financial aid subsidies, state licensing compliance, student-parent retention & GPA, lactation room infrastructure, and after-school drop-in care.
## 10-Agent Architecture
Deterministic(7): ChildcareEnrollmentCapacityMeterAgent, ChildcareSubsidyFinancialAidAuditorAgent, StateChildcareLicensingAuditorAgent, StudentParentAcademicRetentionMeterAgent, FamilyFriendlyCampusInfrastructureAuditorAgent, AfterSchoolDropInCareMeterAgent, CampusChildcareServicesScorerAgent
Reasoning(2): StrategicChildcareNarrativeAgent, FamilySupportPlannerAgent
Orchestrator(1): CampusChildcareServicesOrchestratorAgent
