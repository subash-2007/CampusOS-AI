from typing import List
from pydantic import BaseModel

class OnboardingCompletionMetric(BaseModel):
    avg_completion_pct: float = 76.0
    avg_completion_time_minutes: float = 8.4
    completion_rate_tier: str = "HIGH"

class OnboardingStepDropoffAudit(BaseModel):
    total_steps_count: int = 7
    highest_dropoff_step: int = 3
    highest_dropoff_step_name: str = "Resume Upload"
    dropoff_rate_at_step_pct: float = 18.0

class FirstValueEventMetric(BaseModel):
    avg_time_to_first_value_hours: float = 0.25
    first_value_event: str = "first_job_match_viewed"

class GuidedTourEngagementMetric(BaseModel):
    tour_started_pct: float = 68.0
    tour_completed_pct: float = 54.0
    tour_skip_rate_pct: float = 24.0

class OnboardingPersonalizationAudit(BaseModel):
    personalized_onboarding_paths: int = 6
    path_assignment_accuracy_pct: float = 88.0

class OnboardingNPSMetric(BaseModel):
    nps_score: float = 62.0
    promoters_pct: float = 74.0
    detractors_pct: float = 12.0

class DeterministicOnboardingPipelineResult(BaseModel):
    completion: OnboardingCompletionMetric
    dropoff: OnboardingStepDropoffAudit
    first_value: FirstValueEventMetric
    guided_tour: GuidedTourEngagementMetric
    personalization: OnboardingPersonalizationAudit
    nps: OnboardingNPSMetric
    onboarding_quality_score: float
    confidence_score: float

class StrategicOnboardingNarrative(BaseModel):
    onboarding_summary: str
    key_onboarding_strengths: List[str]

class OnboardingImprovementPlan(BaseModel):
    dropoff_reduction_actions: List[str]
    sample_onboarding_flow: str

class ReasoningOnboardingPipelineResult(BaseModel):
    narrative: StrategicOnboardingNarrative
    improvement_plan: OnboardingImprovementPlan
    reasoning_steps: List[str]

class UserOnboardingOrchestratorReport(BaseModel):
    department: str = "User Onboarding Intelligence"
    department_id: str = "dept_039"
    onboarding_tier: str = "WORLD-CLASS ONBOARDING"
    onboarding_quality_score: float
    confidence_score: float
    deterministic_analysis: DeterministicOnboardingPipelineResult
    reasoning_analysis: ReasoningOnboardingPipelineResult
    reasoning_steps: List[str]
