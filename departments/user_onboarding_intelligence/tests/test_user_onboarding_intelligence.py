import pytest, asyncio
from departments.user_onboarding_intelligence.deterministic import (
    OnboardingCompletionMeterAgent, OnboardingStepDropoffAuditorAgent, FirstValueEventMeterAgent,
    GuidedTourEngagementMeterAgent, OnboardingPersonalizationAuditorAgent, OnboardingNPSMeterAgent, OnboardingQualityScorerAgent
)
from departments.user_onboarding_intelligence.orchestrator import UserOnboardingOrchestratorAgent

def test_onboarding_completion_meter():
    res = OnboardingCompletionMeterAgent().run(76.0)
    assert res.completion_rate_tier == "HIGH"

def test_onboarding_step_dropoff_auditor():
    res = OnboardingStepDropoffAuditorAgent().run()
    assert res.total_steps_count >= 5
    assert res.dropoff_rate_at_step_pct < 50.0

def test_first_value_event_meter():
    res = FirstValueEventMeterAgent().run()
    assert res.avg_time_to_first_value_hours < 1.0

def test_guided_tour_engagement_meter():
    res = GuidedTourEngagementMeterAgent().run()
    assert res.tour_completed_pct < res.tour_started_pct

def test_onboarding_personalization_auditor():
    res = OnboardingPersonalizationAuditorAgent().run()
    assert res.personalized_onboarding_paths >= 3

def test_onboarding_nps_meter():
    res = OnboardingNPSMeterAgent().run()
    assert res.nps_score >= 0.0
    assert res.promoters_pct > res.detractors_pct

def test_onboarding_quality_scorer():
    res = OnboardingQualityScorerAgent().run(76.0)
    assert res.onboarding_quality_score >= 65.0
    assert res.confidence_score >= 0.5

def test_user_onboarding_orchestrator():
    report = asyncio.run(UserOnboardingOrchestratorAgent().run_pipeline(76.0))
    assert report.department == "User Onboarding Intelligence"
    assert report.department_id == "dept_039"
    assert report.onboarding_tier == "WORLD-CLASS ONBOARDING"
    assert len(report.reasoning_steps) == 4
