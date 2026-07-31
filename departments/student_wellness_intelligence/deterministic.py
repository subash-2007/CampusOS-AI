from departments.shared.scoring import ScoringEngine
from departments.student_wellness_intelligence.schemas import (
    CounselingAppointmentMetric, MentalHealthScreeningAudit, CampusRecreationUtilizationMetric,
    StressBurnoutIndexMetric, TelehealthAccessibilityAudit, HealthInsuranceCoverageAudit, DeterministicWellnessPipelineResult
)

class CounselingAppointmentMeterAgent:
    """Agent 1: Measures counseling appointments count, wait time in days, and crisis triage latency."""
    def run(self, wait_days: float = 2.4) -> CounselingAppointmentMetric:
        return CounselingAppointmentMetric(total_counseling_appointments=1840, avg_wait_time_days=wait_days, crisis_triage_latency_minutes=4.5)

class MentalHealthScreeningAuditorAgent:
    """Agent 2: Audits student screening percentage, anxiety/depression flags, and follow-up connection rate."""
    def run(self) -> MentalHealthScreeningAudit:
        return MentalHealthScreeningAudit(students_screened_pct=78.0, anxiety_depression_flagged_pct=14.2, followup_care_connection_pct=94.0)

class CampusRecreationUtilizationMeterAgent:
    """Agent 3: Measures rec center active members percentage and intramural sports participation."""
    def run(self) -> CampusRecreationUtilizationMetric:
        return CampusRecreationUtilizationMetric(rec_center_active_members_pct=68.0, intramural_sports_participants=1250)

class StressBurnoutIndexMeterAgent:
    """Agent 4: Measures campus stress index score and exam week stress spike percentage."""
    def run(self) -> StressBurnoutIndexMetric:
        return StressBurnoutIndexMetric(campus_stress_index_score=42.0, exam_week_stress_spike_pct=22.0)

class TelehealthAccessibilityAuditorAgent:
    """Agent 5: Audits 24/7 telehealth availability status and virtual consultation count."""
    def run(self) -> TelehealthAccessibilityAudit:
        return TelehealthAccessibilityAudit(telehealth_available_24_7=True, virtual_consultations_count=3400)

class HealthInsuranceCoverageAuditorAgent:
    """Agent 6: Audits student health insurance coverage percentage and immunization compliance."""
    def run(self) -> HealthInsuranceCoverageAudit:
        return HealthInsuranceCoverageAudit(student_health_insurance_coverage_pct=98.4, immunization_compliance_pct=99.2)

class StudentWellnessScorerAgent:
    """Agent 7: Master deterministic aggregator for Student Health & Wellness Intelligence."""
    def __init__(self):
        self.counseling_agent = CounselingAppointmentMeterAgent()
        self.mental_health_agent = MentalHealthScreeningAuditorAgent()
        self.rec_agent = CampusRecreationUtilizationMeterAgent()
        self.stress_agent = StressBurnoutIndexMeterAgent()
        self.telehealth_agent = TelehealthAccessibilityAuditorAgent()
        self.insurance_agent = HealthInsuranceCoverageAuditorAgent()

    def run(self, wait_days: float = 2.4) -> DeterministicWellnessPipelineResult:
        counseling = self.counseling_agent.run(wait_days)
        mental_health = self.mental_health_agent.run()
        rec = self.rec_agent.run()
        stress = self.stress_agent.run()
        telehealth = self.telehealth_agent.run()
        insurance = self.insurance_agent.run()

        metrics = {
            "followup_care": mental_health.followup_care_connection_pct,
            "short_wait_time": max(0, 100 - counseling.avg_wait_time_days * 10),
            "telehealth": 100.0 if telehealth.telehealth_available_24_7 else 50.0,
            "insurance": insurance.student_health_insurance_coverage_pct
        }
        weights = {"followup_care": 0.35, "short_wait_time": 0.25, "telehealth": 0.20, "insurance": 0.20}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(telehealth.virtual_consultations_count, 100)
        return DeterministicWellnessPipelineResult(
            counseling=counseling, mental_health=mental_health, recreation=rec,
            stress_burnout=stress, telehealth=telehealth, insurance=insurance,
            wellness_score=score, confidence_score=confidence
        )
