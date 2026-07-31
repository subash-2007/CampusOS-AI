from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class MarketCapTAMCalculator(BaseModel):
    tam_in_billions: float = 12.5
    sam_in_billions: float = 2.4
    som_in_billions: float = 0.35

class RunwayBurnRateMeter(BaseModel):
    monthly_burn_rate: int = 45000
    runway_months: int = 18
    financial_health_tier: str = "HEALTHY RUNWAY"

class PitchDeckReadinessScore(BaseModel):
    deck_score: float = 88.0
    slide_count: int = 12

class UnitEconomicsCalculator(BaseModel):
    ltv_to_cac_ratio: float = 4.2
    payback_period_months: int = 6

class CofounderEquitySplitAudit(BaseModel):
    equity_vesting_cliff_months: int = 12
    equity_vesting_years: int = 4

class RegulatoryComplianceAudit(BaseModel):
    compliance_passed: bool = True
    flagged_regulatory_risks: List[str] = Field(default_factory=list)

class DeterministicStartupPipelineResult(BaseModel):
    tam: MarketCapTAMCalculator
    runway: RunwayBurnRateMeter
    pitch: PitchDeckReadinessScore
    economics: UnitEconomicsCalculator
    equity: CofounderEquitySplitAudit
    compliance: RegulatoryComplianceAudit
    startup_viability_score: float
    confidence_score: float

class StrategicVentureNarrative(BaseModel):
    venture_summary: str
    key_investor_highlights: List[str]

class InvestorPitchNarrative(BaseModel):
    investor_elevator_pitch: str
    fundraising_strategy: List[str]

class ReasoningStartupPipelineResult(BaseModel):
    narrative: StrategicVentureNarrative
    pitch_narrative: InvestorPitchNarrative
    reasoning_steps: List[str]

class StartupEntrepreneurshipOrchestratorReport(BaseModel):
    department: str = "Startup & Entrepreneurship"
    department_id: str = "dept_023"
    venture_tier: str = "VENTURE READY"
    startup_viability_score: float
    confidence_score: float
    deterministic_analysis: DeterministicStartupPipelineResult
    reasoning_analysis: ReasoningStartupPipelineResult
    reasoning_steps: List[str]
