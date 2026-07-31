import pytest, asyncio
from departments.alumni_career_networking.deterministic import (
    AlumniNetworkMentorshipEngagementMeterAgent, AlumniMidCareerTransitionCoachingAuditorAgent, RegionalAlumniChapterEventMeterAgent,
    AlumniJobBoardHiringReferralAuditorAgent, LifelongLearningAlumniUpskillingMeterAgent, AlumniDirectoryDataFreshnessAuditorAgent, AlumniCareerNetworkingScorerAgent
)
from departments.alumni_career_networking.orchestrator import AlumniCareerNetworkingOrchestratorAgent

def test_alumni_network_mentorship_engagement_meter():
    res = AlumniNetworkMentorshipEngagementMeterAgent().run(8450)
    assert res.registered_alumni_mentors_count == 8450
    assert res.mentorship_satisfaction_rate_pct >= 90.0

def test_alumni_mid_career_transition_coaching_auditor():
    res = AlumniMidCareerTransitionCoachingAuditorAgent().run()
    assert res.career_pivot_success_rate_pct >= 80.0

def test_regional_alumni_chapter_event_meter():
    res = RegionalAlumniChapterEventMeterAgent().run()
    assert res.active_regional_chapters_count >= 20

def test_alumni_job_board_hiring_referral_auditor():
    res = AlumniJobBoardHiringReferralAuditorAgent().run()
    assert res.alumni_posted_job_openings >= 1000

def test_lifelong_learning_alumni_upskilling_meter():
    res = LifelongLearningAlumniUpskillingMeterAgent().run()
    assert res.alumni_enrolled_in_micro_credentials >= 1000

def test_alumni_directory_data_freshness_auditor():
    res = AlumniDirectoryDataFreshnessAuditorAgent().run()
    assert res.linkedin_sync_accuracy_pct >= 90.0

def test_alumni_career_networking_scorer():
    res = AlumniCareerNetworkingScorerAgent().run(8450)
    assert res.alumni_career_score >= 90.0
    assert res.confidence_score >= 0.5

def test_alumni_career_networking_orchestrator():
    report = asyncio.run(AlumniCareerNetworkingOrchestratorAgent().run_pipeline(8450))
    assert report.department == "Alumni Career Services & Networking"
    assert report.department_id == "dept_081"
    assert report.alumni_career_tier == "GLOBAL ALUMNI CAREER POWERHOUSE"
    assert len(report.reasoning_steps) == 4
