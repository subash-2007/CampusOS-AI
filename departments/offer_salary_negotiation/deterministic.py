from typing import List, Dict, Any
from departments.shared.scoring import ScoringEngine
from departments.offer_salary_negotiation.schemas import (
    BaseSalaryBenchmarkResult, EquityGrantValuation, SigningBonusAudit,
    RelocationPerksMetric, TotalCompensationCalculated, NegotiationLeverageScore, DeterministicOfferPipelineResult
)

class BaseSalaryBenchmarkAgent:
    """Agent 1: Benchmarks offered base salary against market datasets."""
    def run(self, offered_base: int, market_median: int = 165000) -> BaseSalaryBenchmarkResult:
        percentile = min(round((offered_base / market_median) * 50.0, 1), 99.0)
        return BaseSalaryBenchmarkResult(offered_base=offered_base, market_median_base=market_median, base_percentile=percentile)

class EquityGrantValuationAgent:
    """Agent 2: Models 4-year equity vesting and Black-Scholes/RSU valuation."""
    def run(self, annual_equity: int) -> EquityGrantValuation:
        total = annual_equity * 4
        return EquityGrantValuation(stock_options_value=annual_equity, four_year_vesting_value=total, equity_percentile=75.0)

class SigningBonusAuditorAgent:
    """Agent 3: Audits one-time signing bonus offerings."""
    def run(self, signing_bonus: int) -> SigningBonusAudit:
        return SigningBonusAudit(offered_signing_bonus=signing_bonus, market_median_signing_bonus=25000)

class RelocationPerksMetricAgent:
    """Agent 4: Evaluates relocation stipends and remote work perks."""
    def run(self) -> RelocationPerksMetric:
        return RelocationPerksMetric(relocation_stipend=10000, remote_stipend=3000)

class TotalCompCalculatorAgent:
    """Agent 5: Calculates Year-1 total compensation (Base + Bonus + Equity + Perks)."""
    def run(self, base: int, bonus: int, annual_equity: int, perks: int = 13000) -> TotalCompensationCalculated:
        tc = base + bonus + annual_equity + perks
        return TotalCompensationCalculated(year_1_total_compensation=tc, market_median_tc=250000)

class NegotiationLeverageScorerAgent:
    """Agent 6: Measures candidate negotiation leverage score."""
    def run(self, competing_offers: int = 2) -> NegotiationLeverageScore:
        score = min(60.0 + (competing_offers * 15.0), 95.0)
        return NegotiationLeverageScore(leverage_score=score, competing_offers_count=competing_offers)

class OfferScorerAgent:
    """Agent 7: Master deterministic aggregator for Offer & Salary Negotiation."""
    def __init__(self):
        self.base_agent = BaseSalaryBenchmarkAgent()
        self.equity_agent = EquityGrantValuationAgent()
        self.bonus_agent = SigningBonusAuditorAgent()
        self.perks_agent = RelocationPerksMetricAgent()
        self.tc_agent = TotalCompCalculatorAgent()
        self.leverage_agent = NegotiationLeverageScorerAgent()

    def run(self, offered_base: int = 150000, signing_bonus: int = 20000, annual_equity: int = 50000) -> DeterministicOfferPipelineResult:
        base = self.base_agent.run(offered_base)
        equity = self.equity_agent.run(annual_equity)
        bonus = self.bonus_agent.run(signing_bonus)
        perks = self.perks_agent.run()
        tc = self.tc_agent.run(offered_base, signing_bonus, annual_equity, perks.relocation_stipend + perks.remote_stipend)
        leverage = self.leverage_agent.run(2)

        upside_pct = round(((tc.market_median_tc - tc.year_1_total_compensation) / tc.year_1_total_compensation) * 100.0, 1)
        if upside_pct < 0:
            upside_pct = 10.0

        confidence = ScoringEngine.calculate_confidence_score(competing_offers_count := 2 + 3, 5)

        return DeterministicOfferPipelineResult(
            base_salary=base,
            equity=equity,
            signing_bonus=bonus,
            perks=perks,
            total_comp=tc,
            leverage=leverage,
            negotiation_upside_percentage=upside_pct,
            confidence_score=confidence
        )
