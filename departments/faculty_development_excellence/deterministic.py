from departments.shared.scoring import ScoringEngine
from departments.faculty_development_excellence.schemas import (
    FacultyPedagogyWorkshopParticipationMetric, OnlineCourseDesignQualityMattersCertAudit, FacultyResearchGrantOutputAudit,
    TenurePromotionWorkloadReviewAudit, FacultyMentoringNewFacultyMetric, FacultySatisfactionWorkplaceEngagementAudit, DeterministicFacultyPipelineResult
)

class FacultyPedagogyWorkshopParticipationMeterAgent:
    """Agent 1: Measures pedagogy workshops offered, faculty participation count, and workshop satisfaction score."""
    def run(self) -> FacultyPedagogyWorkshopParticipationMetric:
        return FacultyPedagogyWorkshopParticipationMetric()

class OnlineCourseDesignQualityMattersCertAuditorAgent:
    """Agent 2: Audits Quality Matters certified online courses, total online courses, and QM certification rate."""
    def run(self) -> OnlineCourseDesignQualityMattersCertAudit:
        return OnlineCourseDesignQualityMattersCertAudit()

class FacultyResearchGrantOutputAuditorAgent:
    """Agent 3: Audits external research grants secured, total research funding (millions), and peer-reviewed publications."""
    def run(self) -> FacultyResearchGrantOutputAudit:
        return FacultyResearchGrantOutputAudit()

class TenurePromotionWorkloadReviewAuditorAgent:
    """Agent 4: Audits tenure-track faculty count, promotion cases reviewed annually, and workload equity audit score."""
    def run(self) -> TenurePromotionWorkloadReviewAudit:
        return TenurePromotionWorkloadReviewAudit()

class FacultyMentoringNewFacultyMeterAgent:
    """Agent 5: Measures new faculty orientation participants, active mentoring pairs, and 2-year new faculty retention rate."""
    def run(self) -> FacultyMentoringNewFacultyMetric:
        return FacultyMentoringNewFacultyMetric()

class FacultySatisfactionWorkplaceEngagementAuditorAgent:
    """Agent 6: Audits faculty engagement survey response rate, overall satisfaction score, and voluntary turnover rate."""
    def run(self) -> FacultySatisfactionWorkplaceEngagementAudit:
        return FacultySatisfactionWorkplaceEngagementAudit()

class FacultyDevelopmentExcellenceScorerAgent:
    """Agent 7: Master deterministic aggregator for Faculty Development & Academic Excellence."""
    def __init__(self):
        self.workshops_agent = FacultyPedagogyWorkshopParticipationMeterAgent()
        self.online_agent = OnlineCourseDesignQualityMattersCertAuditorAgent()
        self.research_agent = FacultyResearchGrantOutputAuditorAgent()
        self.tenure_agent = TenurePromotionWorkloadReviewAuditorAgent()
        self.mentoring_agent = FacultyMentoringNewFacultyMeterAgent()
        self.satisfaction_agent = FacultySatisfactionWorkplaceEngagementAuditorAgent()

    def run(self) -> DeterministicFacultyPipelineResult:
        workshops = self.workshops_agent.run()
        online_courses = self.online_agent.run()
        research = self.research_agent.run()
        tenure = self.tenure_agent.run()
        mentoring = self.mentoring_agent.run()
        satisfaction = self.satisfaction_agent.run()
        metrics = {
            "workshop_satisfaction": (workshops.workshop_avg_satisfaction_score / 5.0) * 100,
            "qm_certification": online_courses.qm_certification_rate_pct,
            "workload_equity": tenure.workload_equity_audit_score_pct,
            "new_faculty_retention": mentoring.new_faculty_retention_2yr_pct
        }
        weights = {"workshop_satisfaction": 0.25, "qm_certification": 0.30, "workload_equity": 0.25, "new_faculty_retention": 0.20}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(tenure.tenure_track_faculty_count, 50)
        return DeterministicFacultyPipelineResult(
            workshops=workshops, online_courses=online_courses, research=research,
            tenure=tenure, mentoring=mentoring, satisfaction=satisfaction,
            faculty_score=score, confidence_score=confidence
        )
