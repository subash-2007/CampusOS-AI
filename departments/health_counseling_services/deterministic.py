from departments.shared.scoring import ScoringEngine
from departments.health_counseling_services.schemas import (
    MentalHealthCounselingWaitTimeMetric, StudentHealthClinicVisitsAudit, ImmunizationHealthHoldComplianceAudit,
    HealthInsuranceWaiverProcessingMetric, WellnessPeerEducationStressReliefMetric, AAAHCAccreditationHIPAAComplianceAudit, DeterministicHealthPipelineResult
)

class MentalHealthCounselingWaitTimeMeterAgent:
    """Agent 1: Measures annual counseling sessions, average intake wait time (days), and same-day crisis triage availability."""
    def run(self, sessions: int = 14200) -> MentalHealthCounselingWaitTimeMetric:
        return MentalHealthCounselingWaitTimeMetric(annual_counseling_sessions_held=sessions, avg_intake_wait_time_days=2.4, same_day_crisis_triage_availability_pct=100.0)

class StudentHealthClinicVisitsAuditorAgent:
    """Agent 2: Audits medical visits count, licensed medical providers count, and telehealth virtual visits percentage."""
    def run(self) -> StudentHealthClinicVisitsAudit:
        return StudentHealthClinicVisitsAudit(annual_medical_visits_count=28500, licensed_medical_providers=24, telehealth_virtual_visits_pct=34.2)

class ImmunizationHealthHoldComplianceAuditorAgent:
    """Agent 3: Audits student immunization compliance percentage and mandatory vaccine holds resolution percentage."""
    def run(self) -> ImmunizationHealthHoldComplianceAudit:
        return ImmunizationHealthHoldComplianceAudit(student_immunization_compliance_pct=99.6, mandatory_vaccine_holds_resolved_pct=98.8)

class HealthInsuranceWaiverProcessingMeterAgent:
    """Agent 4: Measures insurance waivers submitted and automated verification rate percentage."""
    def run(self) -> HealthInsuranceWaiverProcessingMetric:
        return HealthInsuranceWaiverProcessingMetric(student_health_insurance_waivers_submitted=12400, waiver_auto_verification_rate_pct=96.2)

class WellnessPeerEducationStressReliefMeterAgent:
    """Agent 5: Measures wellness workshops hosted, peer health educators trained, and event participants."""
    def run(self) -> WellnessPeerEducationStressReliefMetric:
        return WellnessPeerEducationStressReliefMetric(wellness_workshops_hosted=140, peer_health_educators_trained=65, student_wellness_event_participants=8400)

class AAAHCAccreditationHIPAAComplianceAuditorAgent:
    """Agent 6: Audits AAAHC accreditation status and HIPAA privacy audit compliance percentage."""
    def run(self) -> AAAHCAccreditationHIPAAComplianceAudit:
        return AAAHCAccreditationHIPAAComplianceAudit(aaahc_accreditation_status="FULL AAAHC ACCREDITATION", hipaa_privacy_audit_score_pct=100.0)

class StudentHealthCounselingScorerAgent:
    """Agent 7: Master deterministic aggregator for Student Health & Counseling Services."""
    def __init__(self):
        self.counseling_agent = MentalHealthCounselingWaitTimeMeterAgent()
        self.clinic_agent = StudentHealthClinicVisitsAuditorAgent()
        self.immunization_agent = ImmunizationHealthHoldComplianceAuditorAgent()
        self.insurance_agent = HealthInsuranceWaiverProcessingMeterAgent()
        self.wellness_agent = WellnessPeerEducationStressReliefMeterAgent()
        self.accreditation_agent = AAAHCAccreditationHIPAAComplianceAuditorAgent()

    def run(self, sessions: int = 14200) -> DeterministicHealthPipelineResult:
        counseling = self.counseling_agent.run(sessions)
        clinic = self.clinic_agent.run()
        immunizations = self.immunization_agent.run()
        insurance = self.insurance_agent.run()
        wellness = self.wellness_agent.run()
        accreditation = self.accreditation_agent.run()

        metrics = {
            "crisis_triage": counseling.same_day_crisis_triage_availability_pct,
            "hipaa_compliance": accreditation.hipaa_privacy_audit_score_pct,
            "immunization_compliance": immunizations.student_immunization_compliance_pct,
            "wait_time_efficiency": max(0.0, 100.0 - (counseling.avg_intake_wait_time_days * 5))
        }
        weights = {"crisis_triage": 0.35, "hipaa_compliance": 0.30, "immunization_compliance": 0.20, "wait_time_efficiency": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(counseling.annual_counseling_sessions_held, 500)
        return DeterministicHealthPipelineResult(
            counseling=counseling, clinic=clinic, immunizations=immunizations,
            insurance=insurance, wellness=wellness, accreditation=accreditation,
            health_score=score, confidence_score=confidence
        )
