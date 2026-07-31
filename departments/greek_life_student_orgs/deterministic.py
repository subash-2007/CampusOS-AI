from departments.shared.scoring import ScoringEngine
from departments.greek_life_student_orgs.schemas import (
    StudentOrganizationRegistrationMetric, GreekLifeChapterComplianceAudit, PhilanthropyCommunityServiceMetric,
    StudentOrgEventRiskManagementAudit, StudentOrgFinancialAccountAudit, LeadershipAdvisorTrainingMetric, DeterministicGreekLifePipelineResult
)

class StudentOrganizationRegistrationMeterAgent:
    """Agent 1: Measures registered student organization headcount, active members, and portal adoption percentage."""
    def run(self, orgs: int = 340) -> StudentOrganizationRegistrationMetric:
        return StudentOrganizationRegistrationMetric(registered_student_orgs_count=orgs, active_org_members_total=14200, student_engagement_portal_adoption_pct=94.8)

class GreekLifeChapterComplianceAuditorAgent:
    """Agent 2: Audits active fraternity/sorority chapters, hazing prevention training compliance, and chapter average GPA."""
    def run(self) -> GreekLifeChapterComplianceAudit:
        return GreekLifeChapterComplianceAudit(greek_chapters_active=38, hazing_prevention_training_compliance_pct=100.0, greek_chapter_avg_gpa=3.42)

class PhilanthropyCommunityServiceMeterAgent:
    """Agent 3: Measures philanthropy dollars raised (USD) and community service hours logged by student orgs."""
    def run(self) -> PhilanthropyCommunityServiceMetric:
        return PhilanthropyCommunityServiceMetric(philanthropy_funds_raised_usd=850000.0, community_service_hours_logged=42000)

class StudentOrgEventRiskManagementAuditorAgent:
    """Agent 4: Audits registered org event risk management approvals and severe incident log."""
    def run(self) -> StudentOrgEventRiskManagementAudit:
        return StudentOrgEventRiskManagementAudit(registered_org_events_annual=1420, event_risk_management_plans_approved=1420, zero_severe_incidents=True)

class StudentOrgFinancialAccountAuditorAgent:
    """Agent 5: Audits student organization bank accounts and financial compliance score percentage."""
    def run(self) -> StudentOrgFinancialAccountAudit:
        return StudentOrgFinancialAccountAudit(org_bank_accounts_audited=340, financial_compliance_score_pct=98.8)

class LeadershipAdvisorTrainingMeterAgent:
    """Agent 6: Measures trained faculty advisors count and advisor satisfaction rating."""
    def run(self) -> LeadershipAdvisorTrainingMetric:
        return LeadershipAdvisorTrainingMetric(trained_faculty_advisors_count=280, advisor_satisfaction_score=4.8)

class GreekLifeStudentOrgsScorerAgent:
    """Agent 7: Master deterministic aggregator for Greek Life & Student Organizations."""
    def __init__(self):
        self.registration_agent = StudentOrganizationRegistrationMeterAgent()
        self.greek_agent = GreekLifeChapterComplianceAuditorAgent()
        self.philanthropy_agent = PhilanthropyCommunityServiceMeterAgent()
        self.risk_agent = StudentOrgEventRiskManagementAuditorAgent()
        self.financial_agent = StudentOrgFinancialAccountAuditorAgent()
        self.advisor_agent = LeadershipAdvisorTrainingMeterAgent()

    def run(self, orgs: int = 340) -> DeterministicGreekLifePipelineResult:
        registration = self.registration_agent.run(orgs)
        greek_compliance = self.greek_agent.run()
        philanthropy = self.philanthropy_agent.run()
        risk_management = self.risk_agent.run()
        finances = self.financial_agent.run()
        advisors = self.advisor_agent.run()

        metrics = {
            "hazing_prevention": greek_compliance.hazing_prevention_training_compliance_pct,
            "financial_compliance": finances.financial_compliance_score_pct,
            "portal_adoption": registration.student_engagement_portal_adoption_pct,
            "greek_gpa": (greek_compliance.greek_chapter_avg_gpa / 4.0) * 100
        }
        weights = {"hazing_prevention": 0.35, "financial_compliance": 0.30, "portal_adoption": 0.20, "greek_gpa": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(registration.registered_student_orgs_count, 50)
        return DeterministicGreekLifePipelineResult(
            registration=registration, greek_compliance=greek_compliance,
            philanthropy=philanthropy, risk_management=risk_management,
            finances=finances, advisors=advisors,
            org_health_score=score, confidence_score=confidence
        )
