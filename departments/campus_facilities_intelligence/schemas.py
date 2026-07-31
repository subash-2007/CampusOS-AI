from typing import List
from pydantic import BaseModel

class HousingOccupancyMetric(BaseModel):
    total_bed_capacity: int = 4500
    occupied_beds_count: int = 4320
    occupancy_rate_pct: float = 96.0

class MaintenanceTicketResolutionMetric(BaseModel):
    avg_maintenance_resolution_hours: float = 14.5
    urgent_maintenance_sla_compliance_pct: float = 98.2
    open_tickets_count: int = 24

class CampusEnergySustainabilityAudit(BaseModel):
    renewable_energy_share_pct: float = 42.0
    leed_certified_buildings_count: int = 14
    carbon_footprint_reduction_pct: float = 18.5

class FacilityBookingUtilizationMetric(BaseModel):
    study_room_booking_utilization_pct: float = 84.0
    lab_space_utilization_pct: float = 76.5

class CampusSafetyAudit(BaseModel):
    keycard_access_points_active: int = 420
    emergency_call_box_compliance_pct: float = 100.0
    safety_incident_rate_per_1k: float = 0.4

class DiningFacilityQualityAudit(BaseModel):
    dining_hall_csat_pct: float = 91.0
    dietary_restriction_options_count: int = 18

class DeterministicFacilitiesPipelineResult(BaseModel):
    occupancy: HousingOccupancyMetric
    maintenance: MaintenanceTicketResolutionMetric
    sustainability: CampusEnergySustainabilityAudit
    utilization: FacilityBookingUtilizationMetric
    safety: CampusSafetyAudit
    dining: DiningFacilityQualityAudit
    facilities_health_score: float
    confidence_score: float

class StrategicFacilitiesNarrative(BaseModel):
    facilities_summary: str
    key_facilities_strengths: List[str]

class FacilitiesModernizationPlan(BaseModel):
    modernization_actions: List[str]
    sample_smart_campus_iot_spec: str

class ReasoningFacilitiesPipelineResult(BaseModel):
    narrative: StrategicFacilitiesNarrative
    modernization_plan: FacilitiesModernizationPlan
    reasoning_steps: List[str]

class CampusFacilitiesOrchestratorReport(BaseModel):
    department: str = "Campus Housing & Facilities Intelligence"
    department_id: str = "dept_057"
    facilities_tier: str = "SMART SUSTAINABLE CAMPUS"
    facilities_health_score: float
    confidence_score: float
    deterministic_analysis: DeterministicFacilitiesPipelineResult
    reasoning_analysis: ReasoningFacilitiesPipelineResult
    reasoning_steps: List[str]
