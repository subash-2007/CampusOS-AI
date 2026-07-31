from departments.shared.scoring import ScoringEngine
from departments.student_disability_access.schemas import (
    AcademicAccommodationPlanVolumeMetric, AccessibleTestingCenterProctoringAudit, DigitalAccessibilityWCAGCourseAudit,
    AssistiveTechnologyScreenReaderMetric, PhysicalCampusADAAcccessibilityAudit, SignLanguageInterpretingCARTCaptioningMetric, DeterministicDisabilityPipelineResult
)

class AcademicAccommodationPlanVolumeMeterAgent:
    """Agent 1: Measures students registered, active accommodation plans count, and processing speed (days)."""
    def run(self, students: int = 1850) -> AcademicAccommodationPlanVolumeMetric:
        return AcademicAccommodationPlanVolumeMetric(students_registered_with_disability_office=students, active_academic_accommodation_plans=1820, accommodation_plan_processing_days_avg=3.2)

class AccessibleTestingCenterProctoringAuditorAgent:
    """Agent 2: Audits accommodated exams proctored, distraction-reduced testing booths, and fulfillment rate percentage."""
    def run(self) -> AccessibleTestingCenterProctoringAudit:
        return AccessibleTestingCenterProctoringAudit(accommodated_exams_proctored_annual=4200, distraction_reduced_testing_booths=45, exam_accommodation_fulfillment_rate_pct=99.6)

class DigitalAccessibilityWCAGCourseAuditorAgent:
    """Agent 3: Audits Canvas LMS courses scanned for WCAG, WCAG 2.1 AA compliance score percentage, and PDF conversions."""
    def run(self) -> DigitalAccessibilityWCAGCourseAudit:
        return DigitalAccessibilityWCAGCourseAudit(canvas_lms_courses_scanned_for_wcag=6800, wcag_21_aa_compliance_score_pct=96.8, accessible_pdf_conversion_requests=1450)

class AssistiveTechnologyScreenReaderMeterAgent:
    """Agent 4: Measures assistive technology licenses issued and screen reader/Braille station uptime percentage."""
    def run(self) -> AssistiveTechnologyScreenReaderMetric:
        return AssistiveTechnologyScreenReaderMetric(assistive_technology_licenses_issued=850, screen_reader_braille_station_uptime_pct=99.4)

class PhysicalCampusADAAcccessibilityAuditorAgent:
    """Agent 5: Audits wheelchair ramp/elevator inspections, physical ADA accessibility score, and automatic door opener uptime."""
    def run(self) -> PhysicalCampusADAAcccessibilityAudit:
        return PhysicalCampusADAAcccessibilityAudit(wheelchair_ramp_elevator_inspections=180, ada_physical_accessibility_score_pct=98.2, automatic_door_opener_uptime_pct=99.0)

class SignLanguageInterpretingCARTCaptioningMeterAgent:
    """Agent 6: Measures ASL interpreting hours, CART live captioning hours, and captioning fulfillment rate percentage."""
    def run(self) -> SignLanguageInterpretingCARTCaptioningMetric:
        return SignLanguageInterpretingCARTCaptioningMetric(asl_interpreting_hours_provided=2400, cart_live_captioning_hours_provided=3800, captioning_fulfillment_rate_pct=100.0)

class StudentDisabilityAccessScorerAgent:
    """Agent 7: Master deterministic aggregator for Student Disability Access."""
    def __init__(self):
        self.accommodations_agent = AcademicAccommodationPlanVolumeMeterAgent()
        self.testing_agent = AccessibleTestingCenterProctoringAuditorAgent()
        self.digital_agent = DigitalAccessibilityWCAGCourseAuditorAgent()
        self.tech_agent = AssistiveTechnologyScreenReaderMeterAgent()
        self.ada_agent = PhysicalCampusADAAcccessibilityAuditorAgent()
        self.captioning_agent = SignLanguageInterpretingCARTCaptioningMeterAgent()

    def run(self, students: int = 1850) -> DeterministicDisabilityPipelineResult:
        accommodations = self.accommodations_agent.run(students)
        testing_center = self.testing_agent.run()
        digital_accessibility = self.digital_agent.run()
        assistive_tech = self.tech_agent.run()
        physical_ada = self.ada_agent.run()
        captioning = self.captioning_agent.run()

        metrics = {
            "exam_fulfillment": testing_center.exam_accommodation_fulfillment_rate_pct,
            "captioning_fulfillment": captioning.captioning_fulfillment_rate_pct,
            "wcag_compliance": digital_accessibility.wcag_21_aa_compliance_score_pct,
            "ada_score": physical_ada.ada_physical_accessibility_score_pct
        }
        weights = {"exam_fulfillment": 0.35, "captioning_fulfillment": 0.30, "wcag_compliance": 0.20, "ada_score": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(accommodations.students_registered_with_disability_office, 100)
        return DeterministicDisabilityPipelineResult(
            accommodations=accommodations, testing_center=testing_center,
            digital_accessibility=digital_accessibility, assistive_tech=assistive_tech,
            physical_ada=physical_ada, captioning=captioning,
            disability_access_score=score, confidence_score=confidence
        )
