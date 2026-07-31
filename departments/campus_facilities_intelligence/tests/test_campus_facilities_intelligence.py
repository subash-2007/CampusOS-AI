import pytest, asyncio
from departments.campus_facilities_intelligence.deterministic import (
    HousingOccupancyMeterAgent, MaintenanceTicketResolutionMeterAgent, CampusEnergySustainabilityAuditorAgent,
    FacilityBookingUtilizationMeterAgent, CampusSafetyAuditorAgent, DiningFacilityQualityAuditorAgent, CampusFacilitiesScorerAgent
)
from departments.campus_facilities_intelligence.orchestrator import CampusFacilitiesOrchestratorAgent

def test_housing_occupancy_meter():
    res = HousingOccupancyMeterAgent().run(4500)
    assert res.occupancy_rate_pct >= 90.0
    assert res.occupied_beds_count > 4000

def test_maintenance_ticket_resolution_meter():
    res = MaintenanceTicketResolutionMeterAgent().run()
    assert res.urgent_maintenance_sla_compliance_pct >= 90.0

def test_campus_energy_sustainability_auditor():
    res = CampusEnergySustainabilityAuditorAgent().run()
    assert res.leed_certified_buildings_count >= 5

def test_facility_booking_utilization_meter():
    res = FacilityBookingUtilizationMeterAgent().run()
    assert res.study_room_booking_utilization_pct >= 70.0

def test_campus_safety_auditor():
    res = CampusSafetyAuditorAgent().run()
    assert res.emergency_call_box_compliance_pct == 100.0

def test_dining_facility_quality_auditor():
    res = DiningFacilityQualityAuditorAgent().run()
    assert res.dining_hall_csat_pct >= 85.0

def test_campus_facilities_scorer():
    res = CampusFacilitiesScorerAgent().run(4500)
    assert res.facilities_health_score >= 85.0
    assert res.confidence_score >= 0.5

def test_campus_facilities_orchestrator():
    report = asyncio.run(CampusFacilitiesOrchestratorAgent().run_pipeline(4500))
    assert report.department == "Campus Housing & Facilities Intelligence"
    assert report.department_id == "dept_057"
    assert report.facilities_tier == "SMART SUSTAINABLE CAMPUS"
    assert len(report.reasoning_steps) == 4
