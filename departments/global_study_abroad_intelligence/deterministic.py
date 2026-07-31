from departments.shared.scoring import ScoringEngine
from departments.global_study_abroad_intelligence.schemas import (
    StudyAbroadParticipationMetric, VisaComplianceAudit, InternationalCreditTransferAudit,
    GlobalSafetyTravelRiskAudit, CulturalOrientationEngagementMetric, StudyAbroadScholarshipMetric, DeterministicStudyAbroadPipelineResult
)

class StudyAbroadParticipationMeterAgent:
    """Agent 1: Measures total students abroad, partner countries, and active exchange programs."""
    def run(self, students: int = 420) -> StudyAbroadParticipationMetric:
        return StudyAbroadParticipationMetric(total_students_abroad=students, partner_countries_count=28, active_exchange_programs_count=64)

class VisaComplianceAuditorAgent:
    """Agent 2: Audits visa approval rates, processing delay incidents, and passport warnings."""
    def run(self) -> VisaComplianceAudit:
        return VisaComplianceAudit(visa_approval_rate_pct=98.4, visa_processing_delay_incidents=2, passport_validity_warnings=0)

class InternationalCreditTransferAuditorAgent:
    """Agent 3: Audits pre-approved course equivalency counts and credit transfer approval rates."""
    def run(self) -> InternationalCreditTransferAudit:
        return InternationalCreditTransferAudit(pre_approved_course_equivalencies=340, credit_transfer_approval_pct=96.5)

class GlobalSafetyTravelRiskAuditorAgent:
    """Agent 4: Audits 24/7 travel emergency assistance, high-risk destination flags, and insurance coverage."""
    def run(self) -> GlobalSafetyTravelRiskAudit:
        return GlobalSafetyTravelRiskAudit(emergency_travel_assistance_24_7=True, high_risk_destinations_flagged=0, travel_insurance_coverage_pct=100.0)

class CulturalOrientationEngagementMeterAgent:
    """Agent 5: Measures pre-departure orientation completion rates and language prep participants."""
    def run(self) -> CulturalOrientationEngagementMetric:
        return CulturalOrientationEngagementMetric(pre_departure_orientation_completion_pct=98.0, language_proficiency_prep_count=380)

class StudyAbroadScholarshipMeterAgent:
    """Agent 6: Tracks study abroad grant funding totals (USD) and student funding coverage percentage."""
    def run(self) -> StudyAbroadScholarshipMetric:
        return StudyAbroadScholarshipMetric(total_study_abroad_grants_usd=480000.0, students_receiving_abroad_funding_pct=62.0)

class GlobalStudyAbroadScorerAgent:
    """Agent 7: Master deterministic aggregator for Global Study Abroad Intelligence."""
    def __init__(self):
        self.part_agent = StudyAbroadParticipationMeterAgent()
        self.visa_agent = VisaComplianceAuditorAgent()
        self.credit_agent = InternationalCreditTransferAuditorAgent()
        self.safety_agent = GlobalSafetyTravelRiskAuditorAgent()
        self.orientation_agent = CulturalOrientationEngagementMeterAgent()
        self.scholarship_agent = StudyAbroadScholarshipMeterAgent()

    def run(self, students: int = 420) -> DeterministicStudyAbroadPipelineResult:
        participation = self.part_agent.run(students)
        visa = self.visa_agent.run()
        credit = self.credit_agent.run()
        safety = self.safety_agent.run()
        orientation = self.orientation_agent.run()
        scholarships = self.scholarship_agent.run()

        metrics = {
            "visa_approval": visa.visa_approval_rate_pct,
            "credit_transfer": credit.credit_transfer_approval_pct,
            "safety": safety.travel_insurance_coverage_pct,
            "orientation": orientation.pre_departure_orientation_completion_pct
        }
        weights = {"visa_approval": 0.30, "credit_transfer": 0.30, "safety": 0.20, "orientation": 0.20}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(participation.partner_countries_count, 5)
        return DeterministicStudyAbroadPipelineResult(
            participation=participation, visa=visa, credit_transfer=credit,
            safety_risk=safety, orientation=orientation, scholarships=scholarships,
            study_abroad_score=score, confidence_score=confidence
        )
