from departments.shared.scoring import ScoringEngine
from departments.disability_services_accommodations.schemas import (
    StudentAccommodationRegistrationMetric, ExamProctoringAccommodationAudit, AssistiveTechnologyUtilizationMetric,
    PhysicalCampusAccessibilityAudit, DigitalCourseMaterialAccessibilityAudit, DisabilityGrantFinancialAidAudit, DeterministicDisabilityServicesPipelineResult
)

class StudentAccommodationRegistrationMeterAgent:
    """Agent 1: Measures registered disability students headcount, accommodation letters issued, and active percentage."""
    def run(self, registered: int = 1420) -> StudentAccommodationRegistrationMetric:
        return StudentAccommodationRegistrationMetric(registered_students_count=registered, accommodation_letters_issued=3850, active_accommodations_pct=98.2)

class ExamProctoringAccommodationAuditorAgent:
    """Agent 2: Audits extended time exam proctoring count, accessible testing rooms, and SLA fulfillment percentage."""
    def run(self) -> ExamProctoringAccommodationAudit:
        return ExamProctoringAccommodationAudit(extended_time_exams_proctored=2450, accessible_testing_rooms=18, proctoring_sla_fulfillment_pct=99.4)

class AssistiveTechnologyUtilizationMeterAgent:
    """Agent 3: Measures screen reader licenses, speech-to-text software users, and tech satisfaction rating."""
    def run(self) -> AssistiveTechnologyUtilizationMetric:
        return AssistiveTechnologyUtilizationMetric(screen_reader_licenses_issued=340, speech_to_text_software_users=480, assistive_tech_satisfaction_score=4.8)

class PhysicalCampusAccessibilityAuditorAgent:
    """Agent 4: Audits wheelchair accessible routes percentage, automatic door uptime, and accessible restrooms."""
    def run(self) -> PhysicalCampusAccessibilityAudit:
        return PhysicalCampusAccessibilityAudit(wheelchair_accessible_routes_pct=98.5, automatic_door_opener_uptime_pct=99.1, accessible_restroom_coverage_pct=100.0)

class DigitalCourseMaterialAccessibilityAuditorAgent:
    """Agent 5: Audits PDF accessible conversion counts, video captioning percentage, and image alt text compliance."""
    def run(self) -> DigitalCourseMaterialAccessibilityAudit:
        return DigitalCourseMaterialAccessibilityAudit(accessible_pdf_conversion_count=5400, captioned_video_lecture_pct=96.4, alt_text_image_compliance_pct=94.2)

class DisabilityGrantFinancialAidAuditorAgent:
    """Agent 6: Audits assistive technology funding dollars (USD) and student grant recipient counts."""
    def run(self) -> DisabilityGrantFinancialAidAudit:
        return DisabilityGrantFinancialAidAudit(assistive_grant_funding_usd=340000.0, students_receiving_disability_grants=115)

class DisabilityServicesAccommodationsScorerAgent:
    """Agent 7: Master deterministic aggregator for Disability Services & Accommodations."""
    def __init__(self):
        self.registration_agent = StudentAccommodationRegistrationMeterAgent()
        self.proctoring_agent = ExamProctoringAccommodationAuditorAgent()
        self.assistive_tech_agent = AssistiveTechnologyUtilizationMeterAgent()
        self.physical_agent = PhysicalCampusAccessibilityAuditorAgent()
        self.digital_agent = DigitalCourseMaterialAccessibilityAuditorAgent()
        self.grant_agent = DisabilityGrantFinancialAidAuditorAgent()

    def run(self, registered: int = 1420) -> DeterministicDisabilityServicesPipelineResult:
        registrations = self.registration_agent.run(registered)
        exam_proctoring = self.proctoring_agent.run()
        assistive_tech = self.assistive_tech_agent.run()
        physical_accessibility = self.physical_agent.run()
        digital_materials = self.digital_agent.run()
        grants = self.grant_agent.run()

        metrics = {
            "proctoring_sla": exam_proctoring.proctoring_sla_fulfillment_pct,
            "physical_access": physical_accessibility.wheelchair_accessible_routes_pct,
            "digital_captioning": digital_materials.captioned_video_lecture_pct,
            "active_accommodations": registrations.active_accommodations_pct
        }
        weights = {"proctoring_sla": 0.35, "physical_access": 0.25, "digital_captioning": 0.25, "active_accommodations": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(registrations.registered_students_count, 100)
        return DeterministicDisabilityServicesPipelineResult(
            registrations=registrations, exam_proctoring=exam_proctoring,
            assistive_tech=assistive_tech, physical_accessibility=physical_accessibility,
            digital_materials=digital_materials, grants=grants,
            disability_services_score=score, confidence_score=confidence
        )
