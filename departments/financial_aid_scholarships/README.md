# Department 087: Financial Aid & Scholarships
FAFSA application processing turnaround, institutional scholarship distribution & need-met percentage, Title IV Pell Grant & Direct Loan disbursements, Satisfactory Academic Progress (SAP) evaluations, emergency student aid grants, cohort loan default rates, and financial literacy workshops.
## 10-Agent Architecture
Deterministic(7): FAFSACompletionProcessingSpeedMeterAgent, InstitutionalScholarshipDisbursementAuditorAgent, PellGrantFederalLoanDisbursementMeterAgent, SatisfactoryAcademicProgressSAPAuditorAgent, EmergencyStudentAidGrantMeterAgent, StudentLoanDefaultRateAuditorAgent, FinancialAidScholarshipsScorerAgent
Reasoning(2): StrategicFinancialAidNarrativeAgent, FinancialAidOperationsPlannerAgent
Orchestrator(1): FinancialAidScholarshipsOrchestratorAgent
