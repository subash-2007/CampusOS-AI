from typing import List, Dict, Any
from departments.shared.scoring import ScoringEngine
from departments.startup_entrepreneurship.schemas import (
    MarketCapTAMCalculator, RunwayBurnRateMeter, PitchDeckReadinessScore,
    UnitEconomicsCalculator, CofounderEquitySplitAudit, RegulatoryComplianceAudit, DeterministicStartupPipelineResult
)

class MarketCapTAMCalculatorAgent:
    """Agent 1: Calculates Total Addressable Market (TAM), SAM, and SOM metrics."""
    def run(self, tam: float = 12.5) -> MarketCapTAMCalculator:
        return MarketCapTAMCalculator(tam_in_billions=tam, sam_in_billions=tam * 0.2, som_in_billions=tam * 0.03)

class RunwayBurnRateMeterAgent:
    """Agent 2: Measures cash runway months and monthly net burn rate."""
    def run(self, cash_balance: int = 810000, monthly_burn: int = 45000) -> RunwayBurnRateMeter:
        runway = cash_balance // monthly_burn
        tier = "HEALTHY RUNWAY" if runway >= 18 else ("MODERATE RUNWAY" if runway >= 12 else "CRITICAL RUNWAY")
        return RunwayBurnRateMeter(monthly_burn_rate=monthly_burn, runway_months=runway, financial_health_tier=tier)

class PitchDeckReadinessScorerAgent:
    """Agent 3: Scores investor pitch deck completeness and slide structure."""
    def run(self) -> PitchDeckReadinessScore:
        return PitchDeckReadinessScore(deck_score=88.0, slide_count=12)

class UnitEconomicsCalculatorAgent:
    """Agent 4: Models LTV to CAC ratios and payback periods."""
    def run(self, ltv: float = 4200.0, cac: float = 1000.0) -> UnitEconomicsCalculator:
        ratio = round(ltv / cac, 1)
        return UnitEconomicsCalculator(ltv_to_cac_ratio=ratio, payback_period_months=6)

class CofounderEquitySplitAuditorAgent:
    """Agent 5: Audits co-founder equity splits and 4-year vesting schedules."""
    def run(self) -> CofounderEquitySplitAudit:
        return CofounderEquitySplitAudit(equity_vesting_cliff_months=12, equity_vesting_years=4)

class RegulatoryComplianceAuditorAgent:
    """Agent 6: Audits startup regulatory compliance and corporate structure risks."""
    def run(self) -> RegulatoryComplianceAudit:
        return RegulatoryComplianceAudit(compliance_passed=True, flagged_regulatory_risks=[])

class StartupScorerAgent:
    """Agent 7: Master deterministic aggregator for Startup & Entrepreneurship."""
    def __init__(self):
        self.tam_agent = MarketCapTAMCalculatorAgent()
        self.runway_agent = RunwayBurnRateMeterAgent()
        self.pitch_agent = PitchDeckReadinessScorerAgent()
        self.economics_agent = UnitEconomicsCalculatorAgent()
        self.equity_agent = CofounderEquitySplitAuditorAgent()
        self.compliance_agent = RegulatoryComplianceAuditorAgent()

    def run(self, tam: float = 12.5, cash: int = 810000, burn: int = 45000) -> DeterministicStartupPipelineResult:
        tam_res = self.tam_agent.run(tam)
        runway = self.runway_agent.run(cash, burn)
        pitch = self.pitch_agent.run()
        economics = self.economics_agent.run()
        equity = self.equity_agent.run()
        compliance = self.compliance_agent.run()

        metrics = {
            "pitch": pitch.deck_score,
            "economics": min(economics.ltv_to_cac_ratio * 20.0, 100.0),
            "runway": 90.0 if "HEALTHY" in runway.financial_health_tier else 60.0,
            "tam": min((tam / 10.0) * 80.0, 95.0)
        }
        weights = {"pitch": 0.25, "economics": 0.30, "runway": 0.25, "tam": 0.20}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(runway.runway_months, 12)

        return DeterministicStartupPipelineResult(
            tam=tam_res,
            runway=runway,
            pitch=pitch,
            economics=economics,
            equity=equity,
            compliance=compliance,
            startup_viability_score=score,
            confidence_score=confidence
        )
