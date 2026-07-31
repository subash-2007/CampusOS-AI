# Department 067: Veteran & Military Student Services
Veteran & military student headcount, GI Bill certification turnaround & compliance, Yellow Ribbon institutional match funding, Joint Services Transcript (JST) evaluations, Veteran Resource Center visits, and veteran career placement rates.
## 10-Agent Architecture
Deterministic(7): VeteranStudentEnrollmentMeterAgent, GIBillDisbursementAuditorAgent, YellowRibbonProgramAuditorAgent, MilitaryJointServicesTranscriptAuditorAgent, VeteranResourceCenterMeterAgent, VeteranGraduationEmploymentMeterAgent, VeteranMilitaryServicesScorerAgent
Reasoning(2): StrategicVeteranNarrativeAgent, VeteranTransitionPlannerAgent
Orchestrator(1): VeteranMilitaryServicesOrchestratorAgent
