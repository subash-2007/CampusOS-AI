from departments.shared.scoring import ScoringEngine
from departments.transportation_parking_intelligence.schemas import (
    ParkingPermitIssuanceMetric, CampusShuttleBusRidershipMetric, MicroMobilityBikeScooterAudit,
    ParkingEnforcementCitationAudit, CommuterSubsidiesCarpoolMetric, TrafficCongestionSafetyAudit, DeterministicTransportationPipelineResult
)

class ParkingPermitIssuanceMeterAgent:
    """Agent 1: Measures active parking permits issued, garage occupancy rate, and EV charging stations."""
    def run(self, permits: int = 14200) -> ParkingPermitIssuanceMetric:
        return ParkingPermitIssuanceMetric(permits_issued_active=permits, garage_occupancy_rate_pct=86.4, ev_charging_stations_active=48)

class CampusShuttleBusRidershipMeterAgent:
    """Agent 2: Measures annual campus shuttle passengers, on-time performance percentage, and electric fleet percentage."""
    def run(self) -> CampusShuttleBusRidershipMetric:
        return CampusShuttleBusRidershipMetric(annual_shuttle_passengers=1250000, shuttle_on_time_performance_pct=94.8, shuttle_fleet_electric_pct=65.0)

class MicroMobilityBikeScooterAuditorAgent:
    """Agent 3: Audits annual e-bike and e-scooter rides, designated hub counts, and parking violations."""
    def run(self) -> MicroMobilityBikeScooterAudit:
        return MicroMobilityBikeScooterAudit(e_bike_scooter_rides_annual=185000, designated_parking_hubs=34, sidewalk_parking_violations_logged=142)

class ParkingEnforcementCitationAuditorAgent:
    """Agent 4: Audits parking citations issued, appeal approvals, and License Plate Recognition (LPR) camera accuracy."""
    def run(self) -> ParkingEnforcementCitationAudit:
        return ParkingEnforcementCitationAudit(parking_citations_issued=3400, citation_appeal_approval_pct=24.5, license_plate_recognition_accuracy_pct=99.2)

class CommuterSubsidiesCarpoolMeterAgent:
    """Agent 5: Measures carpool permit holders and transit pass subsidies distributed (USD)."""
    def run(self) -> CommuterSubsidiesCarpoolMetric:
        return CommuterSubsidiesCarpoolMetric(carpool_permit_holders=680, public_transit_pass_subsidies_usd=380000.0)

class TrafficCongestionSafetyAuditorAgent:
    """Agent 6: Audits peak traffic clearance speed (minutes) and pedestrian crosswalk safety score."""
    def run(self) -> TrafficCongestionSafetyAudit:
        return TrafficCongestionSafetyAudit(peak_traffic_clearance_minutes=12.4, pedestrian_crosswalk_safety_score=4.85)

class TransportationParkingIntelligenceScorerAgent:
    """Agent 7: Master deterministic aggregator for Transportation & Parking Intelligence."""
    def __init__(self):
        self.permit_agent = ParkingPermitIssuanceMeterAgent()
        self.shuttle_agent = CampusShuttleBusRidershipMeterAgent()
        self.micro_agent = MicroMobilityBikeScooterAuditorAgent()
        self.enforcement_agent = ParkingEnforcementCitationAuditorAgent()
        self.subsidy_agent = CommuterSubsidiesCarpoolMeterAgent()
        self.traffic_agent = TrafficCongestionSafetyAuditorAgent()

    def run(self, permits: int = 14200) -> DeterministicTransportationPipelineResult:
        permit_res = self.permit_agent.run(permits)
        shuttles = self.shuttle_agent.run()
        micro_mobility = self.micro_agent.run()
        enforcement = self.enforcement_agent.run()
        subsidies = self.subsidy_agent.run()
        traffic_safety = self.traffic_agent.run()

        metrics = {
            "shuttle_on_time": shuttles.shuttle_on_time_performance_pct,
            "lpr_accuracy": enforcement.license_plate_recognition_accuracy_pct,
            "shuttle_electric": shuttles.shuttle_fleet_electric_pct,
            "occupancy_rate": permit_res.garage_occupancy_rate_pct
        }
        weights = {"shuttle_on_time": 0.35, "lpr_accuracy": 0.30, "shuttle_electric": 0.20, "occupancy_rate": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(permit_res.permits_issued_active, 500)
        return DeterministicTransportationPipelineResult(
            permits=permit_res, shuttles=shuttles, micro_mobility=micro_mobility,
            enforcement=enforcement, subsidies=subsidies, traffic_safety=traffic_safety,
            transportation_score=score, confidence_score=confidence
        )
