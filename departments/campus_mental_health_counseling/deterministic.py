from departments.shared.scoring import ScoringEngine
from departments.campus_mental_health_counseling.schemas import (
    CounselingIntakeWaitTimeMetric, CounselorToStudentRatioAudit, GroupTherapyPsychoeducationMetric,
    CrisisInterventionHotlineMetric, MentalHealthOutreachPeerSupportMetric, ClinicalSupervisionDocumentationAudit, DeterministicMentalHealthPipelineResult
)

class CounselingIntakeWaitTimeMeterAgent:
    """Agent 1: Measures students served annually, average intake wait days, and same-day crisis walk-ins served."""
    def run(self) -> CounselingIntakeWaitTimeMetric:
        return CounselingIntakeWaitTimeMetric()

class CounselorToStudentRatioAuditorAgent:
    """Agent 2: Audits licensed counselors count, total enrolled students, and counselor-to-student ratio."""
    def run(self) -> CounselorToStudentRatioAudit:
        return CounselorToStudentRatioAudit()

class GroupTherapyPsychoeducationMeterAgent:
    """Agent 3: Measures group therapy sessions offered, psychoeducation workshop participants, and group therapy CSAT."""
    def run(self) -> GroupTherapyPsychoeducationMetric:
        return GroupTherapyPsychoeducationMetric()

class CrisisInterventionHotlineMeterAgent:
    """Agent 4: Measures crisis calls answered, average crisis response time (minutes), and after-hours coverage days."""
    def run(self) -> CrisisInterventionHotlineMetric:
        return CrisisInterventionHotlineMetric()

class MentalHealthOutreachPeerSupportMeterAgent:
    """Agent 5: Measures mental health peer educators trained, campus outreach events, and student reach from events."""
    def run(self) -> MentalHealthOutreachPeerSupportMetric:
        return MentalHealthOutreachPeerSupportMetric()

class ClinicalSupervisionDocumentationAuditorAgent:
    """Agent 6: Audits HIPAA-compliant EHR records percentage, clinical supervision hours, and practicum interns supervised."""
    def run(self) -> ClinicalSupervisionDocumentationAudit:
        return ClinicalSupervisionDocumentationAudit()

class CampusMentalHealthCounselingScorerAgent:
    """Agent 7: Master deterministic aggregator for Campus Mental Health Counseling."""
    def __init__(self):
        self.intake_agent = CounselingIntakeWaitTimeMeterAgent()
        self.ratio_agent = CounselorToStudentRatioAuditorAgent()
        self.group_agent = GroupTherapyPsychoeducationMeterAgent()
        self.crisis_agent = CrisisInterventionHotlineMeterAgent()
        self.outreach_agent = MentalHealthOutreachPeerSupportMeterAgent()
        self.clinical_agent = ClinicalSupervisionDocumentationAuditorAgent()

    def run(self) -> DeterministicMentalHealthPipelineResult:
        intake = self.intake_agent.run()
        ratio = self.ratio_agent.run()
        group_therapy = self.group_agent.run()
        crisis = self.crisis_agent.run()
        outreach = self.outreach_agent.run()
        clinical = self.clinical_agent.run()
        metrics = {
            "hipaa_compliance": clinical.hipaa_compliant_ehr_records_pct,
            "group_csat": (group_therapy.group_therapy_avg_csat / 5.0) * 100,
            "crisis_response": max(0.0, 100.0 - (crisis.avg_crisis_response_time_minutes * 3)),
            "intake_speed": max(0.0, 100.0 - (intake.avg_intake_appointment_wait_days * 8))
        }
        weights = {"hipaa_compliance": 0.35, "group_csat": 0.25, "crisis_response": 0.25, "intake_speed": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(intake.students_served_annually, 100)
        return DeterministicMentalHealthPipelineResult(
            intake=intake, ratio=ratio, group_therapy=group_therapy,
            crisis=crisis, outreach=outreach, clinical=clinical,
            mental_health_score=score, confidence_score=confidence
        )
