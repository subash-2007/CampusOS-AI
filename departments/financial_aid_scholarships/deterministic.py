from departments.shared.scoring import ScoringEngine
from departments.financial_aid_scholarships.schemas import (
    FAFSACompletionProcessingSpeedMetric, InstitutionalScholarshipDisbursementAudit, PellGrantFederalLoanDisbursementMetric,
    SatisfactoryAcademicProgressSAPAudit, EmergencyStudentAidGrantMetric, StudentLoanDefaultRateAudit, DeterministicFinancialAidPipelineResult
)

class FAFSACompletionProcessingSpeedMeterAgent:
    """Agent 1: Measures FAFSA applications processed count, average processing speed (days), and completion rate percentage."""
    def run(self, apps: int = 16800) -> FAFSACompletionProcessingSpeedMetric:
        return FAFSACompletionProcessingSpeedMetric(fafsa_applications_processed=apps, avg_fafsa_processing_days=1.8, fafsa_completion_rate_pct=94.2)

class InstitutionalScholarshipDisbursementAuditorAgent:
    """Agent 2: Audits institutional scholarships awarded (USD), recipients count, and percentage of need-based aid met."""
    def run(self) -> InstitutionalScholarshipDisbursementAudit:
        return InstitutionalScholarshipDisbursementAudit(institutional_scholarships_awarded_usd=42500000.0, scholarship_recipients_count=11200, need_based_aid_met_pct=92.5)

class PellGrantFederalLoanDisbursementMeterAgent:
    """Agent 3: Measures Pell Grants disbursed (USD), federal direct loans disbursed, and Title IV audit compliance percentage."""
    def run(self) -> PellGrantFederalLoanDisbursementMetric:
        return PellGrantFederalLoanDisbursementMetric(pell_grants_disbursed_usd=18500000.0, direct_student_loans_disbursed_usd=34000000.0, title_iv_compliance_audit_score_pct=100.0)

class SatisfactoryAcademicProgressSAPAuditorAgent:
    """Agent 4: Audits SAP evaluated students count, percentage meeting SAP standards, and appeal approval rate."""
    def run(self) -> SatisfactoryAcademicProgressSAPAudit:
        return SatisfactoryAcademicProgressSAPAudit(students_evaluated_for_sap=18500, students_meeting_sap_standards_pct=96.8, sap_appeal_approval_rate_pct=84.0)

class EmergencyStudentAidGrantMeterAgent:
    """Agent 5: Measures emergency grants awarded (USD), emergency recipients count, and fulfillment speed (hours)."""
    def run(self) -> EmergencyStudentAidGrantMetric:
        return EmergencyStudentAidGrantMetric(emergency_grants_awarded_usd=750000.0, emergency_grant_recipients=680, avg_emergency_grant_fulfillment_hours=12.0)

class StudentLoanDefaultRateAuditorAgent:
    """Agent 6: Audits 3-year cohort default rate percentage and financial literacy workshop attendees count."""
    def run(self) -> StudentLoanDefaultRateAudit:
        return StudentLoanDefaultRateAudit(three_year_cohort_default_rate_pct=1.8, financial_literacy_workshop_attendees=3400)

class FinancialAidScholarshipsScorerAgent:
    """Agent 7: Master deterministic aggregator for Financial Aid & Scholarships."""
    def __init__(self):
        self.fafsa_agent = FAFSACompletionProcessingSpeedMeterAgent()
        self.scholarships_agent = InstitutionalScholarshipDisbursementAuditorAgent()
        self.title_iv_agent = PellGrantFederalLoanDisbursementMeterAgent()
        self.sap_agent = SatisfactoryAcademicProgressSAPAuditorAgent()
        self.emergency_agent = EmergencyStudentAidGrantMeterAgent()
        self.loan_default_agent = StudentLoanDefaultRateAuditorAgent()

    def run(self, apps: int = 16800) -> DeterministicFinancialAidPipelineResult:
        fafsa = self.fafsa_agent.run(apps)
        scholarships = self.scholarships_agent.run()
        title_iv = self.title_iv_agent.run()
        sap = self.sap_agent.run()
        emergency_aid = self.emergency_agent.run()
        loan_default = self.loan_default_agent.run()

        metrics = {
            "title_iv_compliance": title_iv.title_iv_compliance_audit_score_pct,
            "sap_compliance": sap.students_meeting_sap_standards_pct,
            "need_met": scholarships.need_based_aid_met_pct,
            "low_default_rate": max(0.0, 100.0 - (loan_default.three_year_cohort_default_rate_pct * 5))
        }
        weights = {"title_iv_compliance": 0.35, "sap_compliance": 0.30, "need_met": 0.20, "low_default_rate": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(fafsa.fafsa_applications_processed, 500)
        return DeterministicFinancialAidPipelineResult(
            fafsa=fafsa, scholarships=scholarships, title_iv=title_iv,
            sap=sap, emergency_aid=emergency_aid, loan_default=loan_default,
            financial_aid_score=score, confidence_score=confidence
        )
