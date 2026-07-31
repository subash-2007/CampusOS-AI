from departments.shared.scoring import ScoringEngine
from departments.student_financial_aid_intelligence.schemas import (
    ScholarshipMatchMetric, FAFSAComplianceAudit, StudentLoanBurdenMetric,
    FinancialAidDisbursementMetric, WorkStudyProgramAudit, EmergencyGrantAudit, DeterministicFinancialAidResult
)

class ScholarshipMatchMeterAgent:
    """Agent 1: Measures scholarship match count, average scholarship value, and application rates."""
    def run(self, matches: int = 480) -> ScholarshipMatchMetric:
        return ScholarshipMatchMetric(scholarships_matched_total=matches, avg_scholarship_value_usd=4500.0, scholarship_application_rate_pct=78.0)

class FAFSAComplianceAuditorAgent:
    """Agent 2: Audits FAFSA completion rates, verification flags, and expected family contribution."""
    def run(self) -> FAFSAComplianceAudit:
        return FAFSAComplianceAudit(fafsa_completion_rate_pct=94.2, fafsa_verification_flagged_pct=4.1, avg_expected_family_contribution_usd=8400.0)

class StudentLoanBurdenMeterAgent:
    """Agent 3: Measures average graduating debt, national comparison, and loan default risk rate."""
    def run(self) -> StudentLoanBurdenMetric:
        return StudentLoanBurdenMetric(avg_graduating_debt_usd=18500.0, national_debt_comparison_pct=-32.0, loan_default_risk_rate_pct=0.8)

class FinancialAidDisbursementMeterAgent:
    """Agent 4: Tracks total aid disbursed (USD) and on-time disbursement percentage."""
    def run(self) -> FinancialAidDisbursementMetric:
        return FinancialAidDisbursementMetric(total_aid_disbursed_usd=14200000.0, on_time_disbursement_pct=99.1)

class WorkStudyProgramAuditorAgent:
    """Agent 5: Audits work-study positions filled and average hourly wage."""
    def run(self) -> WorkStudyProgramAudit:
        return WorkStudyProgramAudit(work_study_positions_filled=420, avg_hourly_work_study_wage_usd=16.50)

class EmergencyGrantAuditorAgent:
    """Agent 6: Measures emergency grants awarded count and average grant size."""
    def run(self) -> EmergencyGrantAudit:
        return EmergencyGrantAudit(emergency_grants_awarded=84, avg_emergency_grant_usd=750.0)

class StudentFinancialAidScorerAgent:
    """Agent 7: Master deterministic aggregator for Student Financial Aid Intelligence."""
    def __init__(self):
        self.match_agent = ScholarshipMatchMeterAgent()
        self.fafsa_agent = FAFSAComplianceAuditorAgent()
        self.loan_agent = StudentLoanBurdenMeterAgent()
        self.disbursement_agent = FinancialAidDisbursementMeterAgent()
        self.work_study_agent = WorkStudyProgramAuditorAgent()
        self.grant_agent = EmergencyGrantAuditorAgent()

    def run(self, matches: int = 480) -> DeterministicFinancialAidResult:
        match = self.match_agent.run(matches)
        fafsa = self.fafsa_agent.run()
        loan = self.loan_agent.run()
        disbursement = self.disbursement_agent.run()
        work_study = self.work_study_agent.run()
        grant = self.grant_agent.run()

        metrics = {
            "fafsa": fafsa.fafsa_completion_rate_pct,
            "disbursement": disbursement.on_time_disbursement_pct,
            "low_default_risk": max(0, 100 - loan.loan_default_risk_rate_pct * 20),
            "match_rate": match.scholarship_application_rate_pct
        }
        weights = {"fafsa": 0.35, "disbursement": 0.30, "low_default_risk": 0.20, "match_rate": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(match.scholarships_matched_total, 50)
        return DeterministicFinancialAidResult(
            scholarship_match=match, fafsa=fafsa, loan_burden=loan,
            disbursement=disbursement, work_study=work_study, emergency_grant=grant,
            financial_aid_score=score, confidence_score=confidence
        )
