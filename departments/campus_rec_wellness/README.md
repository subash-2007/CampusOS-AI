# Department 085: Campus Recreation & Wellness
Recreation center turnstile check-ins & student body utilization rates, weekly group fitness class fill rates, intramural sports leagues, outdoor gear rentals & expeditions, aquatic pool chemical safety & lifeguard certifications, and personal wellness coaching.
## 10-Agent Architecture
Deterministic(7): RecreationCenterCheckinTurnstileMeterAgent, GroupFitnessClassAttendanceAuditorAgent, IntramuralSportsLeagueParticipationMeterAgent, OutdoorAdventuresEquipmentRentalAuditorAgent, AquaticCenterPoolSafetyAuditorAgent, WellnessCoachingPersonalTrainingMeterAgent, CampusRecreationWellnessScorerAgent
Reasoning(2): StrategicCampusRecNarrativeAgent, CampusRecOperationsPlannerAgent
Orchestrator(1): CampusRecreationWellnessOrchestratorAgent
