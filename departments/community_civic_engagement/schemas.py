from typing import List
from pydantic import BaseModel

class ServiceLearningCourseEnrollmentMetric(BaseModel):
    service_learning_courses_offered: int = 184
    student_enrollment_service_learning: int = 8400
    community_service_hours_logged: int = 248000

class AmericorpsVolunteerProgramMetric(BaseModel):
    americorps_vista_members_hosted: int = 28
    americorps_service_hours_annual: int = 84000
    partner_nonprofit_organizations: int = 180

class CivicLeadershipVoterRegistrationMetric(BaseModel):
    voter_registration_drives_annual: int = 12
    students_registered_to_vote: int = 4200
    campus_vote_rate_pct: float = 68.4

class CommunityPartnershipMOUAudit(BaseModel):
    active_community_partnership_mous: int = 124
    k12_school_partnerships: int = 48
    community_partner_satisfaction_score: float = 4.72

class SocialEntrepreneurshipImpactMetric(BaseModel):
    social_enterprise_student_ventures: int = 28
    community_impact_beneficiaries: int = 48000
    social_venture_sustainability_pct: float = 72.4

class CommunityEngagementResearchScholarshipAudit(BaseModel):
    community_based_research_projects: int = 84
    cbr_publications_peer_reviewed: int = 124
    community_co_investigator_projects: int = 48

class DeterministicCommunityCivicEngagementPipelineResult(BaseModel):
    service_learning: ServiceLearningCourseEnrollmentMetric
    americorps: AmericorpsVolunteerProgramMetric
    civic: CivicLeadershipVoterRegistrationMetric
    partnerships: CommunityPartnershipMOUAudit
    social_venture: SocialEntrepreneurshipImpactMetric
    research: CommunityEngagementResearchScholarshipAudit
    engagement_score: float
    confidence_score: float

class StrategicCivicNarrative(BaseModel):
    civic_summary: str
    key_civic_strengths: List[str]

class CivicOperationsPlan(BaseModel):
    civic_actions: List[str]
    sample_schema_data: str

class ReasoningCivicPipelineResult(BaseModel):
    narrative: StrategicCivicNarrative
    plan: CivicOperationsPlan
    reasoning_steps: List[str]

class CommunityCivicEngagementOrchestratorReport(BaseModel):
    department: str = "Community and Civic Engagement"
    department_id: str = "dept_105"
    tier: str = "CARNEGIE COMMUNITY ENGAGEMENT CLASSIFIED INSTITUTION"
    engagement_score: float
    confidence_score: float
    deterministic_analysis: DeterministicCommunityCivicEngagementPipelineResult
    reasoning_analysis: ReasoningCivicPipelineResult
    reasoning_steps: List[str]
