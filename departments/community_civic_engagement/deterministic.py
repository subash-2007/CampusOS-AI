from departments.shared.scoring import ScoringEngine
from departments.community_civic_engagement.schemas import (ServiceLearningCourseEnrollmentMetric, AmericorpsVolunteerProgramMetric, CivicLeadershipVoterRegistrationMetric, CommunityPartnershipMOUAudit, SocialEntrepreneurshipImpactMetric, CommunityEngagementResearchScholarshipAudit, DeterministicCommunityCivicEngagementPipelineResult)

class ServiceLearningCourseEnrollmentMeterAgent:
    """Agent 1: Evaluates ServiceLearningCourseEnrollmentMetric."""
    def run(self) -> ServiceLearningCourseEnrollmentMetric:
        return ServiceLearningCourseEnrollmentMetric()

class AmericorpsVolunteerProgramMeterAgent:
    """Agent 2: Evaluates AmericorpsVolunteerProgramMetric."""
    def run(self) -> AmericorpsVolunteerProgramMetric:
        return AmericorpsVolunteerProgramMetric()

class CivicLeadershipVoterRegistrationMeterAgent:
    """Agent 3: Evaluates CivicLeadershipVoterRegistrationMetric."""
    def run(self) -> CivicLeadershipVoterRegistrationMetric:
        return CivicLeadershipVoterRegistrationMetric()

class CommunityPartnershipMOUAuditorAgent:
    """Agent 4: Evaluates CommunityPartnershipMOUAudit."""
    def run(self) -> CommunityPartnershipMOUAudit:
        return CommunityPartnershipMOUAudit()

class SocialEntrepreneurshipImpactMeterAgent:
    """Agent 5: Evaluates SocialEntrepreneurshipImpactMetric."""
    def run(self) -> SocialEntrepreneurshipImpactMetric:
        return SocialEntrepreneurshipImpactMetric()

class CommunityEngagementResearchScholarshipAuditorAgent:
    """Agent 6: Evaluates CommunityEngagementResearchScholarshipAudit."""
    def run(self) -> CommunityEngagementResearchScholarshipAudit:
        return CommunityEngagementResearchScholarshipAudit()

class CommunityCivicEngagementScorerAgent:
    """Agent 7: Master deterministic aggregator for Community and Civic Engagement."""
    def __init__(self):
        self.service_learning_agent = ServiceLearningCourseEnrollmentMeterAgent()
        self.americorps_agent = AmericorpsVolunteerProgramMeterAgent()
        self.civic_agent = CivicLeadershipVoterRegistrationMeterAgent()
        self.partnerships_agent = CommunityPartnershipMOUAuditorAgent()
        self.social_venture_agent = SocialEntrepreneurshipImpactMeterAgent()
        self.research_agent = CommunityEngagementResearchScholarshipAuditorAgent()

    def run(self) -> DeterministicCommunityCivicEngagementPipelineResult:
        service_learning = self.service_learning_agent.run()
        americorps = self.americorps_agent.run()
        civic = self.civic_agent.run()
        partnerships = self.partnerships_agent.run()
        social_venture = self.social_venture_agent.run()
        research = self.research_agent.run()
        metrics = {
            "partner_satisfaction": (partnerships.community_partner_satisfaction_score / 5.0) * 100,
            "service_hours": min(100.0, (service_learning.community_service_hours_logged / 2000) * 100),
            "voter_rate": civic.campus_vote_rate_pct,
            "community_mous": min(100.0, partnerships.active_community_partnership_mous * 0.75)
        }
        weights = {"partner_satisfaction": 0.30, "service_hours": 0.30, "voter_rate": 0.20, "community_mous": 0.20}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(service_learning.student_enrollment_service_learning, 10)
        return DeterministicCommunityCivicEngagementPipelineResult(
            service_learning=service_learning,
            americorps=americorps,
            civic=civic,
            partnerships=partnerships,
            social_venture=social_venture,
            research=research,
            engagement_score=score, confidence_score=confidence
        )
