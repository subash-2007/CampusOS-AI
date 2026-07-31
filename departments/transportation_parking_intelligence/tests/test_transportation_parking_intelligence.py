import pytest, asyncio
from departments.transportation_parking_intelligence.deterministic import (
    ParkingPermitIssuanceMeterAgent, CampusShuttleBusRidershipMeterAgent, MicroMobilityBikeScooterAuditorAgent,
    ParkingEnforcementCitationAuditorAgent, CommuterSubsidiesCarpoolMeterAgent, TrafficCongestionSafetyAuditorAgent, TransportationParkingIntelligenceScorerAgent
)
from departments.transportation_parking_intelligence.orchestrator import TransportationParkingOrchestratorAgent

def test_parking_permit_issuance_meter():
    res = ParkingPermitIssuanceMeterAgent().run(14200)
    assert res.permits_issued_active == 14200
    assert res.ev_charging_stations_active >= 20

def test_campus_shuttle_bus_ridership_meter():
    res = CampusShuttleBusRidershipMeterAgent().run()
    assert res.annual_shuttle_passengers > 500000
    assert res.shuttle_on_time_performance_pct >= 90.0

def test_micro_mobility_bike_scooter_auditor():
    res = MicroMobilityBikeScooterAuditorAgent().run()
    assert res.designated_parking_hubs >= 20

def test_parking_enforcement_citation_auditor():
    res = ParkingEnforcementCitationAuditorAgent().run()
    assert res.license_plate_recognition_accuracy_pct >= 95.0

def test_commuter_subsidies_carpool_meter():
    res = CommuterSubsidiesCarpoolMeterAgent().run()
    assert res.public_transit_pass_subsidies_usd > 100000.0

def test_traffic_congestion_safety_auditor():
    res = TrafficCongestionSafetyAuditorAgent().run()
    assert res.pedestrian_crosswalk_safety_score >= 4.0

def test_transportation_parking_intelligence_scorer():
    res = TransportationParkingIntelligenceScorerAgent().run(14200)
    assert res.transportation_score >= 88.0
    assert res.confidence_score >= 0.5

def test_transportation_parking_orchestrator():
    report = asyncio.run(TransportationParkingOrchestratorAgent().run_pipeline(14200))
    assert report.department == "Transportation & Parking Intelligence"
    assert report.department_id == "dept_072"
    assert report.mobility_tier == "SMART MULTI-MODAL CAMPUS MOBILITY"
    assert len(report.reasoning_steps) == 4
