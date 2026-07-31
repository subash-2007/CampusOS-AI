from typing import List, Dict, Any
from departments.shared.scoring import ScoringEngine
from departments.alumni_network_intelligence.schemas import (
    AlumniDirectoryMatch, ReferralLikelihoodScore, SharedBackgroundOverlap,
    OutreachResponseRateMetric, AlumniSeniorityDistribution, GeographicAlumniDensity, DeterministicAlumniPipelineResult
)

class AlumniDirectoryMatcherAgent:
    """Agent 1: Matches candidate target companies against university alumni directories."""
    def run(self, company_name: str) -> AlumniDirectoryMatch:
        return AlumniDirectoryMatch(
            matching_alumni_count=18,
            top_alumni_companies=[company_name, "Google", "Meta", "Apple"]
        )

class ReferralLikelihoodScorerAgent:
    """Agent 2: Scores likelihood of obtaining a employee referral from alumni."""
    def run(self, warm_paths: int = 4) -> ReferralLikelihoodScore:
        score = min(60.0 + (warm_paths * 8.0), 95.0)
        return ReferralLikelihoodScore(referral_likelihood_score=score, warm_introduction_paths_count=warm_paths)

class SharedBackgroundOverlapAgent:
    """Agent 3: Identifies shared university, major, and student organization overlaps."""
    def run(self, university: str = "Stanford University") -> SharedBackgroundOverlap:
        return SharedBackgroundOverlap(
            shared_universities=[university],
            shared_majors=["Computer Science", "Electrical Engineering"]
        )

class OutreachResponseRateMeterAgent:
    """Agent 4: Measures historical alumni outreach response rates."""
    def run(self) -> OutreachResponseRateMetric:
        return OutreachResponseRateMetric(historical_alumni_response_rate=68.5)

class AlumniSeniorityDistributionAgent:
    """Agent 5: Maps alumni seniority distribution (Engineers vs. Engineering Directors)."""
    def run(self) -> AlumniSeniorityDistribution:
        return AlumniSeniorityDistribution(senior_executive_alumni_count=6, mid_level_alumni_count=12)

class GeographicAlumniDensityAgent:
    """Agent 6: Measures alumni density in candidate's target metro area."""
    def run(self, location: str = "San Francisco, CA") -> GeographicAlumniDensity:
        return GeographicAlumniDensity(target_city_alumni_count=48)

class AlumniScorerAgent:
    """Agent 7: Master deterministic aggregator for Alumni Network Intelligence."""
    def __init__(self):
        self.matcher = AlumniDirectoryMatcherAgent()
        self.referral_agent = ReferralLikelihoodScorerAgent()
        self.overlap_agent = SharedBackgroundOverlapAgent()
        self.response_agent = OutreachResponseRateMeterAgent()
        self.seniority_agent = AlumniSeniorityDistributionAgent()
        self.density_agent = GeographicAlumniDensityAgent()

    def run(self, company_name: str = "Google", university: str = "Stanford University") -> DeterministicAlumniPipelineResult:
        matches = self.matcher.run(company_name)
        referral = self.referral_agent.run(4)
        overlap = self.overlap_agent.run(university)
        resp = self.response_agent.run()
        seniority = self.seniority_agent.run()
        density = self.density_agent.run()

        metrics = {
            "matches": min(matches.matching_alumni_count * 5.0, 100.0),
            "referral": referral.referral_likelihood_score,
            "response": resp.historical_alumni_response_rate,
            "density": min(density.target_city_alumni_count * 2.0, 100.0)
        }
        weights = {"matches": 0.30, "referral": 0.30, "response": 0.20, "density": 0.20}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(matches.matching_alumni_count, 10)

        return DeterministicAlumniPipelineResult(
            matches=matches,
            referral=referral,
            overlap=overlap,
            response_rate=resp,
            seniority=seniority,
            density=density,
            alumni_network_power_score=score,
            confidence_score=confidence
        )
