from departments.shared.scoring import ScoringEngine
from departments.human_resources_talent_ops.schemas import (FacultyStaffRecruitmentTimeFillMetric, EmployeeRetentionTurnoverAudit, BenefitsCompensationAdministrationAudit, EmployeePerformanceReviewCycleMetric, StaffProfessionalDevelopmentTrainingMetric, TitleIXEqualOpportunityComplianceAudit, DeterministicHumanResourcesTalentOpsPipelineResult)

class FacultyStaffRecruitmentTimeFillMeterAgent:
    """Agent 1: Evaluates FacultyStaffRecruitmentTimeFillMetric."""
    def run(self) -> FacultyStaffRecruitmentTimeFillMetric:
        return FacultyStaffRecruitmentTimeFillMetric()

class EmployeeRetentionTurnoverAuditorAgent:
    """Agent 2: Evaluates EmployeeRetentionTurnoverAudit."""
    def run(self) -> EmployeeRetentionTurnoverAudit:
        return EmployeeRetentionTurnoverAudit()

class BenefitsCompensationAdministrationAuditorAgent:
    """Agent 3: Evaluates BenefitsCompensationAdministrationAudit."""
    def run(self) -> BenefitsCompensationAdministrationAudit:
        return BenefitsCompensationAdministrationAudit()

class EmployeePerformanceReviewCycleMeterAgent:
    """Agent 4: Evaluates EmployeePerformanceReviewCycleMetric."""
    def run(self) -> EmployeePerformanceReviewCycleMetric:
        return EmployeePerformanceReviewCycleMetric()

class StaffProfessionalDevelopmentTrainingMeterAgent:
    """Agent 5: Evaluates StaffProfessionalDevelopmentTrainingMetric."""
    def run(self) -> StaffProfessionalDevelopmentTrainingMetric:
        return StaffProfessionalDevelopmentTrainingMetric()

class TitleIXEqualOpportunityComplianceAuditorAgent:
    """Agent 6: Evaluates TitleIXEqualOpportunityComplianceAudit."""
    def run(self) -> TitleIXEqualOpportunityComplianceAudit:
        return TitleIXEqualOpportunityComplianceAudit()

class HumanResourcesTalentOpsScorerAgent:
    """Agent 7: Master deterministic aggregator for Campus Human Resources and Talent Operations."""
    def __init__(self):
        self.recruitment_agent = FacultyStaffRecruitmentTimeFillMeterAgent()
        self.retention_agent = EmployeeRetentionTurnoverAuditorAgent()
        self.benefits_agent = BenefitsCompensationAdministrationAuditorAgent()
        self.review_agent = EmployeePerformanceReviewCycleMeterAgent()
        self.training_agent = StaffProfessionalDevelopmentTrainingMeterAgent()
        self.title_ix_agent = TitleIXEqualOpportunityComplianceAuditorAgent()

    def run(self) -> DeterministicHumanResourcesTalentOpsPipelineResult:
        recruitment = self.recruitment_agent.run()
        retention = self.retention_agent.run()
        benefits = self.benefits_agent.run()
        review = self.review_agent.run()
        training = self.training_agent.run()
        title_ix = self.title_ix_agent.run()
        metrics = {
            "staff_retention": retention.annual_staff_retention_rate_pct,
            "eeo_training": title_ix.eeo_compliance_training_completion_pct,
            "performance_reviews": review.annual_performance_reviews_completed_pct,
            "open_enrollment": benefits.open_enrollment_completion_pct
        }
        weights = {"staff_retention": 0.35, "eeo_training": 0.25, "performance_reviews": 0.20, "open_enrollment": 0.20}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(retention.total_campus_employees, 10)
        return DeterministicHumanResourcesTalentOpsPipelineResult(
            recruitment=recruitment,
            retention=retention,
            benefits=benefits,
            review=review,
            training=training,
            title_ix=title_ix,
            hr_score=score, confidence_score=confidence
        )
