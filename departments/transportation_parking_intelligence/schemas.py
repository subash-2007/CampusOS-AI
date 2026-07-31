from typing import List
from pydantic import BaseModel

class ParkingPermitIssuanceMetric(BaseModel):
    permits_issued_active: int = 14200
    garage_occupancy_rate_pct: float = 86.4
    ev_charging_stations_active: int = 48

class CampusShuttleBusRidershipMetric(BaseModel):
    annual_shuttle_passengers: int = 1250000
    shuttle_on_time_performance_pct: float = 94.8
    shuttle_fleet_electric_pct: float = 65.0

class MicroMobilityBikeScooterAudit(BaseModel):
    e_bike_scooter_rides_annual: int = 185000
    designated_parking_hubs: int = 34
    sidewalk_parking_violations_logged: int = 142

class ParkingEnforcementCitationAudit(BaseModel):
    parking_citations_issued: int = 3400
    citation_appeal_approval_pct: float = 24.5
    license_plate_recognition_accuracy_pct: float = 99.2

class CommuterSubsidiesCarpoolMetric(BaseModel):
    carpool_permit_holders: int = 680
    public_transit_pass_subsidies_usd: float = 380000.0

class TrafficCongestionSafetyAudit(BaseModel):
    peak_traffic_clearance_minutes: float = 12.4
    pedestrian_crosswalk_safety_score: float = 4.85

class DeterministicTransportationPipelineResult(BaseModel):
    permits: ParkingPermitIssuanceMetric
    shuttles: CampusShuttleBusRidershipMetric
    micro_mobility: MicroMobilityBikeScooterAudit
    enforcement: ParkingEnforcementCitationAudit
    subsidies: CommuterSubsidiesCarpoolMetric
    traffic_safety: TrafficCongestionSafetyAudit
    transportation_score: float
    confidence_score: float

class StrategicTransportationNarrative(BaseModel):
    transportation_summary: str
    key_transportation_strengths: List[str]

class CampusMobilityPlan(BaseModel):
    mobility_actions: List[str]
    sample_shuttle_route_schedule: str

class ReasoningTransportationPipelineResult(BaseModel):
    narrative: StrategicTransportationNarrative
    mobility_plan: CampusMobilityPlan
    reasoning_steps: List[str]

class TransportationParkingOrchestratorReport(BaseModel):
    department: str = "Transportation & Parking Intelligence"
    department_id: str = "dept_072"
    mobility_tier: str = "SMART MULTI-MODAL CAMPUS MOBILITY"
    transportation_score: float
    confidence_score: float
    deterministic_analysis: DeterministicTransportationPipelineResult
    reasoning_analysis: ReasoningTransportationPipelineResult
    reasoning_steps: List[str]
