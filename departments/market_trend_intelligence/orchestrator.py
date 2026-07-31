from typing import Dict, Any, List, Optional
from app.agents.base_agent import BaseAgent
from departments.market_trend_intelligence.deterministic import MarketScorerAgent
from departments.market_trend_intelligence.reasoning import MarketNarrativeEvaluatorAgent, TechHedgingStrategistAgent
from departments.market_trend_intelligence.schemas import (
    MarketTrendOrchestratorReport, ReasoningMarketPipelineResult
)

class MarketTrendOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator Agent for the Market Trend Intelligence Department."""
    def __init__(self):
        super().__init__(
            agent_id="market_trend_orchestrator",
            name="Market Trend Intelligence Master Orchestrator",
            description="Coordinates all 9 sub-agents to deliver a unified Market Trend Report.",
            icon="Globe"
        )
        self.scorer = MarketScorerAgent()
        self.narrative_evaluator = MarketNarrativeEvaluatorAgent()
        self.hedging_strategist = TechHedgingStrategistAgent()

    async def run_pipeline(self, target_domain: str = "Cloud Software Engineering") -> MarketTrendOrchestratorReport:
        reasoning_steps = []
        
        # Step 1: Execute Deterministic Pipeline
        reasoning_steps.append("Step 1: Running deterministic Market Trend Intelligence pipeline (Hiring demand indexing, Trending tech tracking, Compensation benchmarking, Macro signal evaluation, Skill premium scoring, Industry subsector growth mapping).")
        det_result = self.scorer.run(target_domain)
        
        # Step 2: Execute Market Narrative Evaluator Agent
        reasoning_steps.append("Step 2: Executing Market Narrative Evaluator Agent to analyze macro hiring outlook and opportunities.")
        narrative = await self.narrative_evaluator.evaluate(target_domain, det_result)
        
        # Step 3: Execute Tech Hedging Strategist Agent
        reasoning_steps.append("Step 3: Executing Tech Hedging Strategist Agent to formulate future-proofing skill recommendations.")
        hedging = await self.hedging_strategist.strategize(det_result)
        
        # Step 4: Synthesize Report
        reasoning_steps.append("Step 4: Compiling Market Trend Intelligence Master Report.")
        reasoning_result = ReasoningMarketPipelineResult(
            narrative=narrative,
            hedging_strategy=hedging,
            reasoning_steps=reasoning_steps
        )
        
        return MarketTrendOrchestratorReport(
            target_domain=target_domain,
            demand_tier=det_result.hiring_demand.demand_tier,
            confidence_score=det_result.confidence_score,
            deterministic_analysis=det_result,
            reasoning_analysis=reasoning_result,
            reasoning_steps=reasoning_steps
        )
