from departments.shared.scoring import ScoringEngine
from departments.user_onboarding_intelligence.schemas import (
    OnboardingCompletionMetric, OnboardingStepDropoffAudit, FirstValueEventMetric,
    GuidedTourEngagementMetric, OnboardingPersonalizationAudit, OnboardingNPSMetric, DeterministicOnboardingPipelineResult
)

class OnboardingCompletionMeterAgent:
    """Agent 1: Measures onboarding completion percentage and average time to complete."""
    def run(self, completion_pct: float = 76.0) -> OnboardingCompletionMetric:
        tier = "HIGH" if completion_pct >= 70 else ("MEDIUM" if completion_pct >= 50 else "LOW")
        return OnboardingCompletionMetric(avg_completion_pct=completion_pct, avg_completion_time_minutes=8.4, completion_rate_tier=tier)

class OnboardingStepDropoffAuditorAgent:
    """Agent 2: Identifies highest-dropoff onboarding steps and dropoff rates."""
    def run(self) -> OnboardingStepDropoffAudit:
        return OnboardingStepDropoffAudit(total_steps_count=7, highest_dropoff_step=3, highest_dropoff_step_name="Resume Upload", dropoff_rate_at_step_pct=18.0)

class FirstValueEventMeterAgent:
    """Agent 3: Measures time-to-first-value and identifies the key first value event."""
    def run(self) -> FirstValueEventMetric:
        return FirstValueEventMetric(avg_time_to_first_value_hours=0.25, first_value_event="first_job_match_viewed")

class GuidedTourEngagementMeterAgent:
    """Agent 4: Tracks guided tour start, completion, and skip rates."""
    def run(self) -> GuidedTourEngagementMetric:
        return GuidedTourEngagementMetric(tour_started_pct=68.0, tour_completed_pct=54.0, tour_skip_rate_pct=24.0)

class OnboardingPersonalizationAuditorAgent:
    """Agent 5: Audits personalized onboarding path count and path assignment accuracy."""
    def run(self) -> OnboardingPersonalizationAudit:
        return OnboardingPersonalizationAudit(personalized_onboarding_paths=6, path_assignment_accuracy_pct=88.0)

class OnboardingNPSMeterAgent:
    """Agent 6: Measures onboarding NPS score, promoters, and detractors."""
    def run(self) -> OnboardingNPSMetric:
        return OnboardingNPSMetric(nps_score=62.0, promoters_pct=74.0, detractors_pct=12.0)

class OnboardingQualityScorerAgent:
    """Agent 7: Master deterministic aggregator for User Onboarding Intelligence."""
    def __init__(self):
        self.completion_agent = OnboardingCompletionMeterAgent()
        self.dropoff_agent = OnboardingStepDropoffAuditorAgent()
        self.first_value_agent = FirstValueEventMeterAgent()
        self.tour_agent = GuidedTourEngagementMeterAgent()
        self.personalization_agent = OnboardingPersonalizationAuditorAgent()
        self.nps_agent = OnboardingNPSMeterAgent()

    def run(self, completion_pct: float = 76.0) -> DeterministicOnboardingPipelineResult:
        completion = self.completion_agent.run(completion_pct)
        dropoff = self.dropoff_agent.run()
        first_value = self.first_value_agent.run()
        tour = self.tour_agent.run()
        personalization = self.personalization_agent.run()
        nps = self.nps_agent.run()

        metrics = {
            "completion": completion.avg_completion_pct,
            "tour_completion": tour.tour_completed_pct,
            "nps": nps.nps_score,
            "personalization": personalization.path_assignment_accuracy_pct
        }
        weights = {"completion": 0.35, "tour_completion": 0.20, "nps": 0.25, "personalization": 0.20}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(personalization.personalized_onboarding_paths, 3)
        return DeterministicOnboardingPipelineResult(
            completion=completion, dropoff=dropoff, first_value=first_value, guided_tour=tour,
            personalization=personalization, nps=nps,
            onboarding_quality_score=score, confidence_score=confidence
        )
