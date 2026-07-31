from departments.shared.scoring import ScoringEngine
from departments.continuing_executive_ed.schemas import (
    ExecutiveEnrollmentMetric, NonDegreeCertificateCompletionMetric, CorporatePartnershipRevenueAudit,
    ProfessionalCEUAccreditationAudit, ExecutiveNPSNetPromoterMetric, ExecutiveCareerPromotionAudit, DeterministicExecEdPipelineResult
)

class ExecutiveEnrollmentMeterAgent:
    """Agent 1: Measures executive learner headcount, custom corporate cohorts, and average professional experience."""
    def run(self, learners: int = 1850) -> ExecutiveEnrollmentMetric:
        return ExecutiveEnrollmentMetric(executive_learners_count=learners, corporate_custom_cohorts=34, avg_executive_experience_years=12.4)

class NonDegreeCertificateCompletionMeterAgent:
    """Agent 2: Measures annual non-degree certificates awarded and certificate completion rate."""
    def run(self) -> NonDegreeCertificateCompletionMetric:
        return NonDegreeCertificateCompletionMetric(certificates_awarded_annual=2400, certificate_completion_rate_pct=88.5)

class CorporatePartnershipRevenueAuditorAgent:
    """Agent 3: Audits B2B corporate revenue (USD), enterprise clients, and repeat contract rates."""
    def run(self) -> CorporatePartnershipRevenueAudit:
        return CorporatePartnershipRevenueAudit(b2b_corporate_revenue_usd=3800000.0, enterprise_client_count=42, repeat_contract_rate_pct=82.0)

class ProfessionalCEUAccreditationAuditorAgent:
    """Agent 4: Audits continuing education units (CEUs) issued and accreditation compliance percentage."""
    def run(self) -> ProfessionalCEUAccreditationAudit:
        return ProfessionalCEUAccreditationAudit(ceu_credits_issued=14200, accreditation_compliance_pct=100.0)

class ExecutiveNPSNetPromoterMeterAgent:
    """Agent 5: Measures executive NPS score and instructor rating score (out of 5)."""
    def run(self) -> ExecutiveNPSNetPromoterMetric:
        return ExecutiveNPSNetPromoterMetric(executive_nps_score=72.0, instructor_rating_score=4.85)

class ExecutiveCareerPromotionAuditorAgent:
    """Agent 6: Audits learner 1-year promotion percentage and average post-program salary increase."""
    def run(self) -> ExecutiveCareerPromotionAudit:
        return ExecutiveCareerPromotionAudit(learners_promoted_within_1_year_pct=34.2, avg_salary_increase_pct=18.5)

class ContinuingExecutiveEdScorerAgent:
    """Agent 7: Master deterministic aggregator for Continuing Education & Executive Ed."""
    def __init__(self):
        self.enrollment_agent = ExecutiveEnrollmentMeterAgent()
        self.certificate_agent = NonDegreeCertificateCompletionMeterAgent()
        self.revenue_agent = CorporatePartnershipRevenueAuditorAgent()
        self.ceu_agent = ProfessionalCEUAccreditationAuditorAgent()
        self.nps_agent = ExecutiveNPSNetPromoterMeterAgent()
        self.promotion_agent = ExecutiveCareerPromotionAuditorAgent()

    def run(self, learners: int = 1850) -> DeterministicExecEdPipelineResult:
        enrollment = self.enrollment_agent.run(learners)
        certificates = self.certificate_agent.run()
        revenue = self.revenue_agent.run()
        ceu = self.ceu_agent.run()
        nps = self.nps_agent.run()
        promotions = self.promotion_agent.run()

        metrics = {
            "nps_satisfaction": max(0.0, min(100.0, (nps.executive_nps_score + 100) / 2.0)),
            "completion_rate": certificates.certificate_completion_rate_pct,
            "repeat_contract": revenue.repeat_contract_rate_pct,
            "accreditation": ceu.accreditation_compliance_pct
        }
        weights = {"nps_satisfaction": 0.30, "completion_rate": 0.30, "repeat_contract": 0.20, "accreditation": 0.20}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(enrollment.executive_learners_count, 100)
        return DeterministicExecEdPipelineResult(
            enrollment=enrollment, certificates=certificates, revenue=revenue,
            ceu=ceu, nps=nps, promotions=promotions,
            exec_ed_score=score, confidence_score=confidence
        )
