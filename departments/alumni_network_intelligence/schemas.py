from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class AlumniDirectoryMatch(BaseModel):
    matching_alumni_count: int = 15
    top_alumni_companies: List[str] = Field(default_factory=list)

class ReferralLikelihoodScore(BaseModel):
    referral_likelihood_score: float = 85.0
    warm_introduction_paths_count: int = 4

class SharedBackgroundOverlap(BaseModel):
    shared_universities: List[str] = Field(default_factory=list)
    shared_majors: List[str] = Field(default_factory=list)

class OutreachResponseRateMetric(BaseModel):
    historical_alumni_response_rate: float = 68.0

class AlumniSeniorityDistribution(BaseModel):
    senior_executive_alumni_count: int = 5
    mid_level_alumni_count: int = 10

class GeographicAlumniDensity(BaseModel):
    target_city_alumni_count: int = 45

class DeterministicAlumniPipelineResult(BaseModel):
    matches: AlumniDirectoryMatch
    referral: ReferralLikelihoodScore
    overlap: SharedBackgroundOverlap
    response_rate: OutreachResponseRateMetric
    seniority: AlumniSeniorityDistribution
    density: GeographicAlumniDensity
    alumni_network_power_score: float
    confidence_score: float

class StrategicAlumniOutreachNarrative(BaseModel):
    alumni_networking_strategy: str
    target_alumni_profiles: List[str]

class OutreachIntroScript(BaseModel):
    personalized_alumni_outreach_draft: str
    warm_intro_talking_points: List[str]

class ReasoningAlumniPipelineResult(BaseModel):
    narrative: StrategicAlumniOutreachNarrative
    intro_script: OutreachIntroScript
    reasoning_steps: List[str]

class AlumniNetworkOrchestratorReport(BaseModel):
    department: str = "Alumni Network Intelligence"
    department_id: str = "dept_017"
    network_strength_tier: str = "STRONG NETWORK"
    alumni_network_power_score: float
    confidence_score: float
    deterministic_analysis: DeterministicAlumniPipelineResult
    reasoning_analysis: ReasoningAlumniPipelineResult
    reasoning_steps: List[str]
