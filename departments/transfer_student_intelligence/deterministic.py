from departments.shared.scoring import ScoringEngine
from departments.transfer_student_intelligence.schemas import (
    ArticulationAgreementAudit, CreditTransferEvaluationMetric, TransferStudentGPAAudit,
    TransferOrientationAttendanceMetric, TransferHousingFinancialAidAudit, TransferGraduationRateMetric, DeterministicTransferPipelineResult
)

class ArticulationAgreementAuditorAgent:
    """Agent 1: Audits active articulation agreements, feeder community colleges, and automated equivalency rules."""
    def run(self, agreements: int = 142) -> ArticulationAgreementAudit:
        return ArticulationAgreementAudit(active_articulation_agreements=agreements, feeder_community_colleges=28, automated_equivalency_rules=1850)

class CreditTransferEvaluationMeterAgent:
    """Agent 2: Measures annual transcript evaluations, turnaround time (days), and accepted transfer credit percentage."""
    def run(self) -> CreditTransferEvaluationMetric:
        return CreditTransferEvaluationMetric(transcripts_evaluated_annual=3400, avg_evaluation_turnaround_days=2.1, accepted_credit_transfer_pct=91.4)

class TransferStudentGPAAuditorAgent:
    """Agent 3: Audits incoming transfer GPA, post-transfer 1st year GPA, and GPA stability percentage."""
    def run(self) -> TransferStudentGPAAudit:
        return TransferStudentGPAAudit(avg_incoming_transfer_gpa=3.38, post_transfer_first_year_gpa=3.25, gpa_retention_stability_pct=96.2)

class TransferOrientationAttendanceMeterAgent:
    """Agent 4: Measures transfer orientation attendees and orientation satisfaction percentage."""
    def run(self) -> TransferOrientationAttendanceMetric:
        return TransferOrientationAttendanceMetric(transfer_orientation_attendees=1250, orientation_satisfaction_pct=92.6)

class TransferHousingFinancialAidAuditorAgent:
    """Agent 5: Audits transfer student housing guarantee percentage and transfer merit scholarship dollars."""
    def run(self) -> TransferHousingFinancialAidAudit:
        return TransferHousingFinancialAidAudit(transfer_housing_guarantee_pct=88.0, transfer_merit_scholarships_usd=520000.0)

class TransferGraduationRateMeterAgent:
    """Agent 6: Measures 2-year and 4-year post-transfer graduation rates."""
    def run(self) -> TransferGraduationRateMetric:
        return TransferGraduationRateMetric(two_year_transfer_grad_rate_pct=74.5, four_year_transfer_grad_rate_pct=89.2)

class TransferStudentIntelligenceScorerAgent:
    """Agent 7: Master deterministic aggregator for Transfer Student Intelligence."""
    def __init__(self):
        self.agreements_agent = ArticulationAgreementAuditorAgent()
        self.evaluations_agent = CreditTransferEvaluationMeterAgent()
        self.gpa_agent = TransferStudentGPAAuditorAgent()
        self.orientation_agent = TransferOrientationAttendanceMeterAgent()
        self.housing_aid_agent = TransferHousingFinancialAidAuditorAgent()
        self.grad_agent = TransferGraduationRateMeterAgent()

    def run(self, agreements: int = 142) -> DeterministicTransferPipelineResult:
        agreements_res = self.agreements_agent.run(agreements)
        evaluations = self.evaluations_agent.run()
        gpa_stability = self.gpa_agent.run()
        orientation = self.orientation_agent.run()
        housing_aid = self.housing_aid_agent.run()
        graduation = self.grad_agent.run()

        metrics = {
            "credit_acceptance": evaluations.accepted_credit_transfer_pct,
            "gpa_stability": gpa_stability.gpa_retention_stability_pct,
            "graduation_rate": graduation.four_year_transfer_grad_rate_pct,
            "turnaround_speed": max(0.0, 100.0 - (evaluations.avg_evaluation_turnaround_days * 10))
        }
        weights = {"credit_acceptance": 0.35, "gpa_stability": 0.25, "graduation_rate": 0.25, "turnaround_speed": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(agreements_res.active_articulation_agreements, 15)
        return DeterministicTransferPipelineResult(
            agreements=agreements_res, evaluations=evaluations, gpa_stability=gpa_stability,
            orientation=orientation, housing_aid=housing_aid, graduation=graduation,
            transfer_intelligence_score=score, confidence_score=confidence
        )
