from typing import List
from pydantic import BaseModel

class ChildcareEnrollmentCapacityMetric(BaseModel):
    enrolled_children_count: int = 340
    childcare_center_capacity_pct: float = 94.2
    infant_toddler_preschool_slots: int = 360

class ChildcareSubsidyFinancialAidAudit(BaseModel):
    childcare_subsidies_awarded_usd: float = 480000.0
    student_parent_subsidy_recipients: int = 142
    subsidy_fulfillment_rate_pct: float = 98.5

class StateChildcareLicensingAudit(BaseModel):
    licensing_compliance_score_pct: float = 100.0
    staff_to_child_ratio_avg: float = 4.2
    early_childhood_certified_staff_pct: float = 96.0

class StudentParentAcademicRetentionMetric(BaseModel):
    student_parent_retention_rate_pct: float = 91.8
    student_parent_avg_gpa: float = 3.32

class FamilyFriendlyCampusInfrastructureAudit(BaseModel):
    lactation_nursing_rooms_count: int = 24
    family_study_lounges_count: int = 8
    family_housing_units_occupied: int = 180

class AfterSchoolDropInCareMetric(BaseModel):
    after_school_care_participants: int = 180
    drop_in_emergency_childcare_hours: int = 2400

class DeterministicChildcarePipelineResult(BaseModel):
    enrollment: ChildcareEnrollmentCapacityMetric
    subsidies: ChildcareSubsidyFinancialAidAudit
    licensing: StateChildcareLicensingAudit
    retention: StudentParentAcademicRetentionMetric
    infrastructure: FamilyFriendlyCampusInfrastructureAudit
    after_school: AfterSchoolDropInCareMetric
    childcare_score: float
    confidence_score: float

class StrategicChildcareNarrative(BaseModel):
    childcare_summary: str
    key_childcare_strengths: List[str]

class FamilySupportPlan(BaseModel):
    family_support_actions: List[str]
    sample_childcare_subsidy_grant_application: str

class ReasoningChildcarePipelineResult(BaseModel):
    narrative: StrategicChildcareNarrative
    family_support_plan: FamilySupportPlan
    reasoning_steps: List[str]

class CampusChildcareServicesOrchestratorReport(BaseModel):
    department: str = "Campus Childcare & Family Services"
    department_id: str = "dept_074"
    family_support_tier: str = "GOLD-STANDARD FAMILY-FRIENDLY CAMPUS"
    childcare_score: float
    confidence_score: float
    deterministic_analysis: DeterministicChildcarePipelineResult
    reasoning_analysis: ReasoningChildcarePipelineResult
    reasoning_steps: List[str]
