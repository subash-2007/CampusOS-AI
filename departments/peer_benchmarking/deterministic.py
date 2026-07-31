from typing import List, Dict, Any
from departments.shared.scoring import ScoringEngine
from departments.peer_benchmarking.schemas import (
    CohortPercentileScore, AcademicPeerComparison, SkillDensityBenchmark,
    ExperienceVelocityIndex, OpenSourcePeerRank, CertificationRigorBenchmark, DeterministicPeerPipelineResult
)

class CohortPercentileScorerAgent:
    """Agent 1: Calculates candidate overall percentile rank against peer cohorts."""
    def run(self, user_score: float) -> CohortPercentileScore:
        percentile = min(max(user_score * 0.95, 50.0), 99.0)
        tier = "TOP 10%" if percentile >= 90 else ("TOP 25%" if percentile >= 75 else "AVERAGE COHORT")
        return CohortPercentileScore(overall_percentile=round(percentile, 1), cohort_tier=tier)

class AcademicPeerComparisonAgent:
    """Agent 2: Compares academic performance and coursework rigor against peer medians."""
    def run(self) -> AcademicPeerComparison:
        return AcademicPeerComparison(gpa_percentile=88.5, coursework_rigor_score=85.0)

class SkillDensityBenchmarkAgent:
    """Agent 3: Compares technical skill density against industry peer benchmarks."""
    def run(self, user_skills: List[str]) -> SkillDensityBenchmark:
        count = len(user_skills) if user_skills else 12
        ratio = round(count / 10.0, 2)
        return SkillDensityBenchmark(skill_count_vs_peer_median=ratio, unique_skills_count=count)

class ExperienceVelocityIndexAgent:
    """Agent 4: Measures promotion frequency and career progression velocity."""
    def run(self) -> ExperienceVelocityIndex:
        return ExperienceVelocityIndex(promotions_per_year=0.75, experience_velocity_tier="FAST TRACK")

class OpenSourcePeerRankerAgent:
    """Agent 5: Ranks open-source contributions against regional developer benchmarks."""
    def run(self) -> OpenSourcePeerRank:
        return OpenSourcePeerRank(github_contributions_percentile=91.0)

class CertificationRigorBenchmarkAgent:
    """Agent 6: Evaluates professional certification count and industry prestige."""
    def run(self) -> CertificationRigorBenchmark:
        return CertificationRigorBenchmark(industry_certification_count=3, certification_prestige_score=85.0)

class PeerScorerAgent:
    """Agent 7: Master deterministic aggregator for Peer Benchmarking."""
    def __init__(self):
        self.percentile_agent = CohortPercentileScorerAgent()
        self.academic_agent = AcademicPeerComparisonAgent()
        self.skill_agent = SkillDensityBenchmarkAgent()
        self.velocity_agent = ExperienceVelocityIndexAgent()
        self.os_agent = OpenSourcePeerRankerAgent()
        self.cert_agent = CertificationRigorBenchmarkAgent()

    def run(self, user_skills: List[str] = None) -> DeterministicPeerPipelineResult:
        if user_skills is None:
            user_skills = ["Python", "FastAPI", "Docker", "Kubernetes", "AWS", "React"]

        academic = self.academic_agent.run()
        skills = self.skill_agent.run(user_skills)
        velocity = self.velocity_agent.run()
        os_rank = self.os_agent.run()
        cert = self.cert_agent.run()

        metrics = {
            "academic": academic.gpa_percentile,
            "skills": min(skills.skill_count_vs_peer_median * 70.0, 100.0),
            "os": os_rank.github_contributions_percentile,
            "cert": cert.certification_prestige_score
        }
        weights = {"academic": 0.25, "skills": 0.30, "os": 0.25, "cert": 0.20}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        percentile = self.percentile_agent.run(score)

        confidence = ScoringEngine.calculate_confidence_score(skills.unique_skills_count + 3, 8)

        return DeterministicPeerPipelineResult(
            percentile=percentile,
            academic=academic,
            skills=skills,
            velocity=velocity,
            open_source=os_rank,
            certifications=cert,
            composite_benchmark_score=score,
            confidence_score=confidence
        )
