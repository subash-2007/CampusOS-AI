import pytest, asyncio
from departments.residential_housing_operations.deterministic import (
    KeycardAccessSecurityAuditorAgent, ResidenceHallHousekeepingSanitationAuditorAgent, HVACUtilityEnergyConsumptionMeterAgent,
    ResidenceHallLaundryMachineStatusMeterAgent, MailroomPackageLockerFulfillmentMeterAgent, SummerConferenceHousingTurnaroundAuditorAgent, ResidentialHousingOperationsScorerAgent
)
from departments.residential_housing_operations.orchestrator import ResidentialHousingOperationsOrchestratorAgent

def test_keycard_access_security_auditor():
    res = KeycardAccessSecurityAuditorAgent().run(4800)
    assert res.electronic_keycard_doors_managed == 4800
    assert res.access_control_uptime_pct >= 99.9

def test_residence_hall_housekeeping_sanitation_auditor():
    res = ResidenceHallHousekeepingSanitationAuditorAgent().run()
    assert res.daily_sanitation_inspection_score_pct >= 95.0

def test_hvac_utility_energy_consumption_meter():
    res = HVACUtilityEnergyConsumptionMeterAgent().run()
    assert res.smart_thermostat_coverage_pct >= 80.0

def test_residence_hall_laundry_machine_status_meter():
    res = ResidenceHallLaundryMachineStatusMeterAgent().run()
    assert res.laundry_machine_uptime_pct >= 95.0

def test_mailroom_package_locker_fulfillment_meter():
    res = MailroomPackageLockerFulfillmentMeterAgent().run()
    assert res.student_packages_processed_annual >= 50000
    assert res.smart_locker_pickup_time_avg_hours <= 12.0

def test_summer_conference_housing_turnaround_auditor():
    res = SummerConferenceHousingTurnaroundAuditorAgent().run()
    assert res.room_turnaround_cleaning_speed_hours <= 8.0

def test_residential_housing_operations_scorer():
    res = ResidentialHousingOperationsScorerAgent().run(4800)
    assert res.residential_housing_score >= 90.0
    assert res.confidence_score >= 0.5

def test_residential_housing_operations_orchestrator():
    report = asyncio.run(ResidentialHousingOperationsOrchestratorAgent().run_pipeline(4800))
    assert report.department == "Residential Housing Operations"
    assert report.department_id == "dept_093"
    assert report.residential_housing_tier == "PREMIER SMART CAMPUS RESIDENTIAL FACILITY"
    assert len(report.reasoning_steps) == 4
