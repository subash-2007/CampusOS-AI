from typing import Dict, Any, List, Optional
from app.agents.base_agent import BaseAgent
from departments.portfolio_intelligence.deterministic import PortfolioScorerAgent
from departments.portfolio_intelligence.reasoning import PortfolioNarrativeEvaluatorAgent, READMEOptimizationStrategistAgent
from departments.portfolio_intelligence.schemas import (
    PortfolioOrchestratorReport, ReasoningPortfolioPipelineResult
)

class PortfolioOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator Agent for the Portfolio Intelligence Department."""
    def __init__(self):
        super().__init__(
            agent_id="portfolio_orchestrator",
            name="Portfolio Intelligence Master Orchestrator",
            description="Coordinates all 9 sub-agents to deliver a unified Portfolio Review Report.",
            icon="Folder"
        )
        self.scorer = PortfolioScorerAgent()
        self.narrative_evaluator = PortfolioNarrativeEvaluatorAgent()
        self.readme_strategist = READMEOptimizationStrategistAgent()

    async def run_pipeline(self, project_names: Optional[List[str]] = None) -> PortfolioOrchestratorReport:
        reasoning_steps = []
        
        # Step 1: Execute Deterministic Pipeline
        reasoning_steps.append("Step 1: Running deterministic Portfolio Intelligence pipeline (GitHub repo auditing, Tech stack diversity measurement, README quality auditing, Architecture complexity evaluation, Open-source impact metering, Code hygiene auditing).")
        det_result = self.scorer.run(project_names)
        
        # Step 2: Execute Portfolio Narrative Evaluator Agent
        reasoning_steps.append("Step 2: Executing Portfolio Narrative Evaluator Agent to analyze qualitative engineering depth and project impact.")
        narrative = await self.narrative_evaluator.evaluate(det_result)
        
        # Step 3: Execute README Optimization Strategist Agent
        reasoning_steps.append("Step 3: Executing README Optimization Strategist Agent to produce documentation enhancement strategies.")
        strategy = await self.readme_strategist.strategize(det_result)
        
        # Step 4: Synthesize Report
        reasoning_steps.append("Step 4: Compiling Portfolio Review Report.")
        reasoning_result = ReasoningPortfolioPipelineResult(
            narrative_eval=narrative,
            optimization_strategy=strategy,
            reasoning_steps=reasoning_steps
        )
        
        return PortfolioOrchestratorReport(
            portfolio_score=det_result.overall_portfolio_score,
            confidence_score=det_result.confidence_score,
            deterministic_analysis=det_result,
            reasoning_analysis=reasoning_result,
            reasoning_steps=reasoning_steps
        )
