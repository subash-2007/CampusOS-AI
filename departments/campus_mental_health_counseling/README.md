# Department 098: Campus Mental Health Counseling
Counseling intake appointment wait times, counselor-to-student ratios, group therapy & psychoeducation workshop participation, crisis intervention hotline response speed, mental health peer educator outreach, and HIPAA-compliant EHR clinical documentation.
## 10-Agent Architecture
Deterministic(7): CounselingIntakeWaitTimeMeterAgent, CounselorToStudentRatioAuditorAgent, GroupTherapyPsychoeducationMeterAgent, CrisisInterventionHotlineMeterAgent, MentalHealthOutreachPeerSupportMeterAgent, ClinicalSupervisionDocumentationAuditorAgent, CampusMentalHealthCounselingScorerAgent
Reasoning(2): StrategicMentalHealthNarrativeAgent, MentalHealthClinicalPlannerAgent
Orchestrator(1): CampusMentalHealthCounselingOrchestratorAgent
