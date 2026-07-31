from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class HiringDemandIndex(BaseModel):
    demand_tier: str = "VERY HIGH"
    job_openings_growth_rate: float = 14.5

class TrendingTechStacks(BaseModel):
    top_rising_technologies: List[str] = Field(default_factory=list)
    declining_technologies: List[str] = Field(default_factory=list)

class RegionalCompensationBenchmark(BaseModel):
    median_base_salary: int = 155000
    median_equity_grant: int = 40000

class MacroeconomicHiringSignal(BaseModel):
    remote_hiring_trend: str = "STABLE HIGH"
    layoff_risk_index: float = 12.0

class SkillPremiumScore(BaseModel):
    highest_paid_skill_premiums: Dict[str, float] = Field(default_factory=dict)

class IndustryDomainGrowth(BaseModel):
    fastest_growing_subsectors: List[str] = Field(default_factory=list)

class DeterministicMarketPipelineResult(BaseModel):
    hiring_demand: HiringDemandIndex
    trending_tech: TrendingTechStacks
    compensation: RegionalCompensationBenchmark
    macro_signals: MacroeconomicHiringSignal
    skill_premiums: SkillPremiumScore
    industry_growth: IndustryDomainGrowth
    confidence_score: float

class StrategicMarketNarrative(BaseModel):
    market_outlook_summary: str
    key_opportunities: List[str]

class TechHedgingStrategy(BaseModel):
    recommended_futureproof_skills: List[str]

class ReasoningMarketPipelineResult(BaseModel):
    narrative: StrategicMarketNarrative
    hedging_strategy: TechHedgingStrategy
    reasoning_steps: List[str]

class MarketTrendOrchestratorReport(BaseModel):
    department: str = "Market Trend Intelligence"
    department_id: str = "dept_010"
    target_domain: str
    demand_tier: str
    confidence_score: float
    deterministic_analysis: DeterministicMarketPipelineResult
    reasoning_analysis: ReasoningMarketPipelineResult
    reasoning_steps: List[str]
