from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class BaseSalaryBenchmarkResult(BaseModel):
    offered_base: int = 150000
    market_median_base: int = 165000
    base_percentile: float = 40.0

class EquityGrantValuation(BaseModel):
    stock_options_value: int = 50000
    four_year_vesting_value: int = 200000
    equity_percentile: float = 75.0

class SigningBonusAudit(BaseModel):
    offered_signing_bonus: int = 20000
    market_median_signing_bonus: int = 25000

class RelocationPerksMetric(BaseModel):
    relocation_stipend: int = 10000
    remote_stipend: int = 3000

class TotalCompensationCalculated(BaseModel):
    year_1_total_compensation: int = 230000
    market_median_tc: int = 250000

class NegotiationLeverageScore(BaseModel):
    leverage_score: float = 85.0
    competing_offers_count: int = 2

class DeterministicOfferPipelineResult(BaseModel):
    base_salary: BaseSalaryBenchmarkResult
    equity: EquityGrantValuation
    signing_bonus: SigningBonusAudit
    perks: RelocationPerksMetric
    total_comp: TotalCompensationCalculated
    leverage: NegotiationLeverageScore
    negotiation_upside_percentage: float
    confidence_score: float

class StrategicNegotiationNarrative(BaseModel):
    negotiation_positioning_summary: str
    target_counter_offer_tc: int

class CounterOfferScript(BaseModel):
    counter_offer_email_draft: str
    negotiation_talking_points: List[str]

class ReasoningOfferPipelineResult(BaseModel):
    narrative: StrategicNegotiationNarrative
    counter_script: CounterOfferScript
    reasoning_steps: List[str]

class OfferSalaryOrchestratorReport(BaseModel):
    department: str = "Offer & Salary Negotiation"
    department_id: str = "dept_016"
    negotiation_readiness_tier: str = "HIGH LEVERAGE"
    negotiation_upside_percentage: float
    confidence_score: float
    deterministic_analysis: DeterministicOfferPipelineResult
    reasoning_analysis: ReasoningOfferPipelineResult
    reasoning_steps: List[str]
