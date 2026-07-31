# Department 083: Student Housing & Residential Life
Residence hall bed capacity & occupancy, roommate pairing satisfaction, Resident Advisor staffing ratios & safety training compliance, Living-Learning Community first-year retention, 24-hour maintenance work order resolution, and digital move-in check-in speed.
## 10-Agent Architecture
Deterministic(7): HousingOccupancyCapacityMeterAgent, RoommateMatchingSatisfactionAuditorAgent, ResidentAdvisorStaffingRatioAuditorAgent, LivingLearningCommunityEngagementMeterAgent, FacilitiesWorkOrderResolutionAuditorAgent, MoveInOutCheckinCheckoutMeterAgent, StudentHousingResidentialLifeScorerAgent
Reasoning(2): StrategicHousingNarrativeAgent, HousingOperationsPlannerAgent
Orchestrator(1): StudentHousingResidentialLifeOrchestratorAgent
