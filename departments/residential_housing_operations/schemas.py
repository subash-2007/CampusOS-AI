from typing import List
from pydantic import BaseModel

class KeycardAccessSecurityAudit(BaseModel):
    electronic_keycard_doors_managed: int = 4800
    access_control_uptime_pct: float = 99.99
    unauthorized_tailgating_incidents: int = 4

class ResidenceHallHousekeepingSanitationAudit(BaseModel):
    residence_hall_common_areas_cleaned: int = 340
    daily_sanitation_inspection_score_pct: float = 98.6
    custodial_staffing_fulfillment_pct: float = 96.5

class HVACUtilityEnergyConsumptionMetric(BaseModel):
    smart_thermostat_coverage_pct: float = 92.4
    hvac_emergency_repairs_annual: int = 24
    building_energy_efficiency_score: float = 91.8

class ResidenceHallLaundryMachineStatusMetric(BaseModel):
    campus_laundry_machines_managed: int = 380
    laundry_machine_uptime_pct: float = 97.8
    mobile_laundry_app_active_users: int = 8400

class MailroomPackageLockerFulfillmentMetric(BaseModel):
    student_packages_processed_annual: int = 145000
    smart_locker_pickup_time_avg_hours: float = 3.2
    package_misplacement_rate_pct: float = 0.05

class SummerConferenceHousingTurnaroundAudit(BaseModel):
    summer_conference_rooms_prepared: int = 3200
    room_turnaround_cleaning_speed_hours: float = 4.0

class DeterministicResidentialHousingPipelineResult(BaseModel):
    security: KeycardAccessSecurityAudit
    housekeeping: ResidenceHallHousekeepingSanitationAudit
    hvac: HVACUtilityEnergyConsumptionMetric
    laundry: ResidenceHallLaundryMachineStatusMetric
    mailroom: MailroomPackageLockerFulfillmentMetric
    summer_housing: SummerConferenceHousingTurnaroundAudit
    residential_housing_score: float
    confidence_score: float

class StrategicResidentialHousingNarrative(BaseModel):
    residential_housing_summary: str
    key_residential_housing_strengths: List[str]

class ResidentialHousingOperationsPlan(BaseModel):
    residential_housing_actions: List[str]
    sample_package_locker_notification_schema: str

class ReasoningResidentialHousingPipelineResult(BaseModel):
    narrative: StrategicResidentialHousingNarrative
    housing_operations_plan: ResidentialHousingOperationsPlan
    reasoning_steps: List[str]

class ResidentialHousingOperationsOrchestratorReport(BaseModel):
    department: str = "Residential Housing Operations"
    department_id: str = "dept_093"
    residential_housing_tier: str = "PREMIER SMART CAMPUS RESIDENTIAL FACILITY"
    residential_housing_score: float
    confidence_score: float
    deterministic_analysis: DeterministicResidentialHousingPipelineResult
    reasoning_analysis: ReasoningResidentialHousingPipelineResult
    reasoning_steps: List[str]
