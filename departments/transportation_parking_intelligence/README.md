# Department 072: Transportation & Parking Intelligence
Active parking permit counts, garage occupancy, electric shuttle bus ridership & punctuality, e-scooter micro-mobility hubs, LPR citation enforcement accuracy, and transit pass subsidies.
## 10-Agent Architecture
Deterministic(7): ParkingPermitIssuanceMeterAgent, CampusShuttleBusRidershipMeterAgent, MicroMobilityBikeScooterAuditorAgent, ParkingEnforcementCitationAuditorAgent, CommuterSubsidiesCarpoolMeterAgent, TrafficCongestionSafetyAuditorAgent, TransportationParkingIntelligenceScorerAgent
Reasoning(2): StrategicTransportationNarrativeAgent, CampusMobilityPlannerAgent
Orchestrator(1): TransportationParkingOrchestratorAgent
