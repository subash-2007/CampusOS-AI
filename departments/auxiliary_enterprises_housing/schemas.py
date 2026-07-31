from typing import List
from pydantic import BaseModel

class CampusHousingOccupancyRateMetric(BaseModel):
    residence_hall_beds_capacity: int = 8400
    housing_occupancy_rate_pct: float = 98.4
    housing_revenue_annual_millions: float = 68.4

class CampusDiningMealPlanRevenueAudit(BaseModel):
    active_student_meal_plans: int = 11200
    dining_halls_retail_venues_count: int = 24
    dining_satisfaction_score: float = 4.64

class CampusBookstoreRetailOperationsAudit(BaseModel):
    course_materials_digital_inclusive_access_pct: float = 88.2
    bookstore_net_revenue_millions: float = 12.8
    student_textbook_cost_savings_millions: float = 3.4

class ConferenceEventServicesRevenueMetric(BaseModel):
    conferences_events_hosted_annual: int = 420
    summer_conference_housing_guests: int = 8400
    conference_services_revenue_millions: float = 8.6

class CampusVendingLaundryConcessionAudit(BaseModel):
    smart_laundry_machines_managed: int = 480
    vending_machines_cashless_pct: float = 100.0
    auxiliary_vending_commissions_usd: float = 840000.0

class FacilityMaintenanceWorkOrderTurnaroundMetric(BaseModel):
    residence_hall_work_orders_annual: int = 18400
    avg_work_order_resolution_hours: float = 4.2
    emergency_maintenance_response_minutes: float = 18.0

class DeterministicAuxiliaryEnterprisesHousingPipelineResult(BaseModel):
    housing: CampusHousingOccupancyRateMetric
    dining: CampusDiningMealPlanRevenueAudit
    bookstore: CampusBookstoreRetailOperationsAudit
    conference: ConferenceEventServicesRevenueMetric
    vending: CampusVendingLaundryConcessionAudit
    work_orders: FacilityMaintenanceWorkOrderTurnaroundMetric
    auxiliary_score: float
    confidence_score: float

class StrategicAuxiliaryNarrative(BaseModel):
    auxiliary_summary: str
    key_auxiliary_strengths: List[str]

class AuxiliaryOperationsPlan(BaseModel):
    auxiliary_actions: List[str]
    sample_schema_data: str

class ReasoningAuxiliaryPipelineResult(BaseModel):
    narrative: StrategicAuxiliaryNarrative
    plan: AuxiliaryOperationsPlan
    reasoning_steps: List[str]

class AuxiliaryEnterprisesHousingOrchestratorReport(BaseModel):
    department: str = "Auxiliary Enterprises and Housing Operations"
    department_id: str = "dept_108"
    tier: str = "PREMIER CAMPUS AUXILIARY SERVICES AND HOUSING OPERATIONS"
    auxiliary_score: float
    confidence_score: float
    deterministic_analysis: DeterministicAuxiliaryEnterprisesHousingPipelineResult
    reasoning_analysis: ReasoningAuxiliaryPipelineResult
    reasoning_steps: List[str]
