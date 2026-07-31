from typing import List
from pydantic import BaseModel

class StudentAccommodationRegistrationMetric(BaseModel):
    registered_students_count: int = 1420
    accommodation_letters_issued: int = 3850
    active_accommodations_pct: float = 98.2

class ExamProctoringAccommodationAudit(BaseModel):
    extended_time_exams_proctored: int = 2450
    accessible_testing_rooms: int = 18
    proctoring_sla_fulfillment_pct: float = 99.4

class AssistiveTechnologyUtilizationMetric(BaseModel):
    screen_reader_licenses_issued: int = 340
    speech_to_text_software_users: int = 480
    assistive_tech_satisfaction_score: float = 4.8

class PhysicalCampusAccessibilityAudit(BaseModel):
    wheelchair_accessible_routes_pct: float = 98.5
    automatic_door_opener_uptime_pct: float = 99.1
    accessible_restroom_coverage_pct: float = 100.0

class DigitalCourseMaterialAccessibilityAudit(BaseModel):
    accessible_pdf_conversion_count: int = 5400
    captioned_video_lecture_pct: float = 96.4
    alt_text_image_compliance_pct: float = 94.2

class DisabilityGrantFinancialAidAudit(BaseModel):
    assistive_grant_funding_usd: float = 340000.0
    students_receiving_disability_grants: int = 115

class DeterministicDisabilityServicesPipelineResult(BaseModel):
    registrations: StudentAccommodationRegistrationMetric
    exam_proctoring: ExamProctoringAccommodationAudit
    assistive_tech: AssistiveTechnologyUtilizationMetric
    physical_accessibility: PhysicalCampusAccessibilityAudit
    digital_materials: DigitalCourseMaterialAccessibilityAudit
    grants: DisabilityGrantFinancialAidAudit
    disability_services_score: float
    confidence_score: float

class StrategicDisabilityServicesNarrative(BaseModel):
    services_summary: str
    key_accessibility_strengths: List[str]

class AccommodationPlan(BaseModel):
    accessibility_actions: List[str]
    sample_accommodation_letter_template: str

class ReasoningDisabilityServicesPipelineResult(BaseModel):
    narrative: StrategicDisabilityServicesNarrative
    accommodation_plan: AccommodationPlan
    reasoning_steps: List[str]

class DisabilityServicesAccommodationsOrchestratorReport(BaseModel):
    department: str = "Disability Services & Accommodations"
    department_id: str = "dept_066"
    accessibility_tier: str = "UNIVERSAL ACCESSIBILITY EXCELLENCE"
    disability_services_score: float
    confidence_score: float
    deterministic_analysis: DeterministicDisabilityServicesPipelineResult
    reasoning_analysis: ReasoningDisabilityServicesPipelineResult
    reasoning_steps: List[str]
