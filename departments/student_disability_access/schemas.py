from typing import List
from pydantic import BaseModel

class AcademicAccommodationPlanVolumeMetric(BaseModel):
    students_registered_with_disability_office: int = 1850
    active_academic_accommodation_plans: int = 1820
    accommodation_plan_processing_days_avg: float = 3.2

class AccessibleTestingCenterProctoringAudit(BaseModel):
    accommodated_exams_proctored_annual: int = 4200
    distraction_reduced_testing_booths: int = 45
    exam_accommodation_fulfillment_rate_pct: float = 99.6

class DigitalAccessibilityWCAGCourseAudit(BaseModel):
    canvas_lms_courses_scanned_for_wcag: int = 6800
    wcag_21_aa_compliance_score_pct: float = 96.8
    accessible_pdf_conversion_requests: int = 1450

class AssistiveTechnologyScreenReaderMetric(BaseModel):
    assistive_technology_licenses_issued: int = 850
    screen_reader_braille_station_uptime_pct: float = 99.4

class PhysicalCampusADAAcccessibilityAudit(BaseModel):
    wheelchair_ramp_elevator_inspections: int = 180
    ada_physical_accessibility_score_pct: float = 98.2
    automatic_door_opener_uptime_pct: float = 99.0

class SignLanguageInterpretingCARTCaptioningMetric(BaseModel):
    asl_interpreting_hours_provided: int = 2400
    cart_live_captioning_hours_provided: int = 3800
    captioning_fulfillment_rate_pct: float = 100.0

class DeterministicDisabilityPipelineResult(BaseModel):
    accommodations: AcademicAccommodationPlanVolumeMetric
    testing_center: AccessibleTestingCenterProctoringAudit
    digital_accessibility: DigitalAccessibilityWCAGCourseAudit
    assistive_tech: AssistiveTechnologyScreenReaderMetric
    physical_ada: PhysicalCampusADAAcccessibilityAudit
    captioning: SignLanguageInterpretingCARTCaptioningMetric
    disability_access_score: float
    confidence_score: float

class StrategicDisabilityNarrative(BaseModel):
    disability_summary: str
    key_disability_strengths: List[str]

class DisabilityAccessPlan(BaseModel):
    disability_actions: List[str]
    sample_accommodation_letter_schema: str

class ReasoningDisabilityPipelineResult(BaseModel):
    narrative: StrategicDisabilityNarrative
    disability_plan: DisabilityAccessPlan
    reasoning_steps: List[str]

class StudentDisabilityAccessOrchestratorReport(BaseModel):
    department: str = "Student Disability Access"
    department_id: str = "dept_094"
    disability_access_tier: str = "NATIONAL MODEL FOR UNIVERSAL ACCESSIBILITY"
    disability_access_score: float
    confidence_score: float
    deterministic_analysis: DeterministicDisabilityPipelineResult
    reasoning_analysis: ReasoningDisabilityPipelineResult
    reasoning_steps: List[str]
