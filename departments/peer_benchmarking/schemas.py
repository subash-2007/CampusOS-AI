from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class CohortPercentileScore(BaseModel):
    overall_percentile: float = 88.5
    cohort_tier: str = "TOP 15%"

class AcademicPeerComparison(BaseModel):
    gpa_percentile: float = 90.0
    coursework_rigor_score: float = 85.0

class SkillDensityBenchmark(BaseModel):
    skill_count_vs_peer_median: float = 1.35
    unique_skills_count: int = 14

class ExperienceVelocityIndex(BaseModel):
    promotions_per_year: float = 0.8
    experience_velocity_tier: str = "FAST TRACK"

class OpenSourcePeerRank(BaseModel):
    github_contributions_percentile: float = 92.0

class CertificationRigorBenchmark(BaseModel):
    industry_certification_count: int = 3
    certification_prestige_score: float = 88.0

class DeterministicPeerPipelineResult(BaseModel):
    percentile: CohortPercentileScore
    academic: AcademicPeerComparison
    skills: SkillDensityBenchmark
    velocity: ExperienceVelocityIndex
    open_source: OpenSourcePeerRank
    certifications: CertificationRigorBenchmark
    composite_benchmark_score: float
    confidence_score: float

class StrategicPeerNarrative(BaseModel):
    competitive_positioning_summary: str
    key_differentiators: List[str]

class PeerOutperformanceStrategy(BaseModel):
    recommended_leverage_points: List[str]

class ReasoningPeerPipelineResult(BaseModel):
    narrative: StrategicPeerNarrative
    strategy: PeerOutperformanceStrategy
    reasoning_steps: List[str]

class PeerBenchmarkingOrchestratorReport(BaseModel):
    department: str = "Peer Benchmarking"
    department_id: str = "dept_015"
    cohort_tier: str
    composite_benchmark_score: float
    confidence_score: float
    deterministic_analysis: DeterministicPeerPipelineResult
    reasoning_analysis: ReasoningPeerPipelineResult
    reasoning_steps: List[str]
