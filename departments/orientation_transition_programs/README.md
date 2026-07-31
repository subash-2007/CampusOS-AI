# Department 090: Student Orientation & Transition Programs
Freshmen & transfer student orientation attendance & completion rates, Orientation Leader staffing & training hours, First-Year Experience (FYE) seminar course enrollment & retention lift, Welcome Week event check-ins, and Parent/Family Association engagement.
## 10-Agent Architecture
Deterministic(7): FreshmenOrientationAttendanceMeterAgent, TransferStudentOrientationMeterAgent, OrientationLeaderStaffingAuditorAgent, FirstYearExperienceFYECourseAuditorAgent, WelcomeWeekCampusEngagementMeterAgent, ParentFamilyOrientationEngagementAuditorAgent, StudentOrientationTransitionScorerAgent
Reasoning(2): StrategicOrientationNarrativeAgent, TransitionProgramPlannerAgent
Orchestrator(1): StudentOrientationTransitionOrchestratorAgent
