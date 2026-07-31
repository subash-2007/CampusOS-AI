from typing import List
from pydantic import BaseModel

class HousingOccupancyCapacityMetric(BaseModel):
    total_residence_hall_beds: int = 9500
    occupied_beds_count: int = 9320
    housing_occupancy_rate_pct: float = 98.1

class RoommateMatchingSatisfactionAudit(BaseModel):
    roommate_pairings_created: int = 4200
    roommate_conflict_transfer_requests: int = 84
    roommate_satisfaction_rate_pct: float = 98.0

class ResidentAdvisorStaffingRatioAudit(BaseModel):
    resident_advisors_active: int = 180
    ra_to_resident_ratio: float = 51.7
    ra_training_completion_pct: float = 100.0

class LivingLearningCommunityEngagementMetric(BaseModel):
    active_living_learning_communities: int = 14
    llc_enrolled_residents: int = 1850
    llc_first_year_retention_rate_pct: float = 94.2

class FacilitiesWorkOrderResolutionAudit(BaseModel):
    maintenance_work_orders_annual: int = 8400
    work_orders_resolved_in_24h_pct: float = 96.5
    avg_resolution_time_hours: float = 14.2

class MoveInOutCheckinCheckoutMetric(BaseModel):
    move_in_digital_checkins_completed: int = 4200
    avg_move_in_checkin_minutes: float = 3.8

class DeterministicHousingPipelineResult(BaseModel):
    occupancy: HousingOccupancyCapacityMetric
    roommates: RoommateMatchingSatisfactionAudit
    staffing: ResidentAdvisorStaffingRatioAudit
    llc: LivingLearningCommunityEngagementMetric
    facilities: FacilitiesWorkOrderResolutionAudit
    move_in: MoveInOutCheckinCheckoutMetric
    housing_score: float
    confidence_score: float

class StrategicHousingNarrative(BaseModel):
    housing_summary: str
    key_housing_strengths: List[str]

class HousingOperationsPlan(BaseModel):
    housing_actions: List[str]
    sample_room_assignment_contract_schema: str

class ReasoningHousingPipelineResult(BaseModel):
    narrative: StrategicHousingNarrative
    housing_plan: HousingOperationsPlan
    reasoning_steps: List[str]

class StudentHousingResidentialLifeOrchestratorReport(BaseModel):
    department: str = "Student Housing & Residential Life"
    department_id: str = "dept_083"
    housing_tier: str = "EXEMPLARY RESIDENTIAL COMMUNITY"
    housing_score: float
    confidence_score: float
    deterministic_analysis: DeterministicHousingPipelineResult
    reasoning_analysis: ReasoningHousingPipelineResult
    reasoning_steps: List[str]
