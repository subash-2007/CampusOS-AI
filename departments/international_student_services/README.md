# Department 068: International Student & Scholar Services
International student headcount, country diversity, SEVIS reporting compliance, I-20 issuance turnaround, CPT/OPT work authorizations, Sprintax tax compliance, and English language support.
## 10-Agent Architecture
Deterministic(7): InternationalStudentDemographicsMeterAgent, SEVISComplianceAuditorAgent, CPTOPTWorkAuthorizationAuditorAgent, InternationalHostFamilyCultureMeterAgent, EnglishProficiencySupportMeterAgent, InternationalTaxHealthInsuranceAuditorAgent, InternationalStudentServicesScorerAgent
Reasoning(2): StrategicISSSNarrativeAgent, InternationalStudentPlannerAgent
Orchestrator(1): InternationalStudentServicesOrchestratorAgent
