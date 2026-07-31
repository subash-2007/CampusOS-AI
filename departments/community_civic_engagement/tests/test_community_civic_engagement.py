import pytest, asyncio
from departments.community_civic_engagement.deterministic import (ServiceLearningCourseEnrollmentMeterAgent, AmericorpsVolunteerProgramMeterAgent, CivicLeadershipVoterRegistrationMeterAgent, CommunityPartnershipMOUAuditorAgent, SocialEntrepreneurshipImpactMeterAgent, CommunityEngagementResearchScholarshipAuditorAgent, CommunityCivicEngagementScorerAgent)
from departments.community_civic_engagement.orchestrator import CommunityCivicEngagementOrchestratorAgent

def test_service_learning_course_enrollment_meter_agent():
    res = ServiceLearningCourseEnrollmentMeterAgent().run()
    assert res is not None

def test_americorps_volunteer_program_meter_agent():
    res = AmericorpsVolunteerProgramMeterAgent().run()
    assert res is not None

def test_civic_leadership_voter_registration_meter_agent():
    res = CivicLeadershipVoterRegistrationMeterAgent().run()
    assert res is not None

def test_community_partnership_m_o_u_auditor_agent():
    res = CommunityPartnershipMOUAuditorAgent().run()
    assert res is not None

def test_social_entrepreneurship_impact_meter_agent():
    res = SocialEntrepreneurshipImpactMeterAgent().run()
    assert res is not None

def test_community_engagement_research_scholarship_auditor_agent():
    res = CommunityEngagementResearchScholarshipAuditorAgent().run()
    assert res is not None

def test_community_civic_engagement_scorer():
    res = CommunityCivicEngagementScorerAgent().run()
    assert res.engagement_score >= 50.0
    assert res.confidence_score >= 0.5

def test_community_civic_engagement_orchestrator():
    report = asyncio.run(CommunityCivicEngagementOrchestratorAgent().run_pipeline())
    assert report.department == "Community and Civic Engagement"
    assert report.department_id == "dept_105"
    assert report.tier == "CARNEGIE COMMUNITY ENGAGEMENT CLASSIFIED INSTITUTION"
    assert len(report.reasoning_steps) == 4
