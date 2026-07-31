from typing import Dict, Any, List, Optional
from app.agents.base_agent import BaseAgent
from departments.career_analytics.deterministic import AnalyticsScorerAgent
from departments.career_analytics.reasoning import AnalyticsNarrativeEvaluatorAgent, ActionableAnalyticsStrategistAgent
from departments.career_analytics.schemas import (
    AnalyticsOrchestratorReport, ReasoningAnalyticsPipelineResult
)

class AnalyticsOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator Agent for the Career Analytics Department."""
    def __init__(self):
        super().__init__(
            agent_id="analytics_orchestrator",
            name="Career Analytics Master Orchestrator",
            description="Coordinates all 9 sub-agents to deliver a unified Career Analytics Performance Report.",
            icon="PieChart"
        )
        self.scorer = AnalyticsScorerAgent()
        self.narrative_evaluator = AnalyticsNarrativeEvaluatorAgent()
        self.strategist = ActionableAnalyticsStrategistAgent()

    async def run_pipeline(self, domain_scores: Optional[Dict[str, float]] = None) -> AnalyticsOrchestratorReport:
        reasoning_steps = []
        
        # Step 1: Execute Deterministic Pipeline
        reasoning_steps.append("Step 1: Running deterministic Career Analytics pipeline (Readiness metric calculation, Domain radar aggregation, Market competitiveness tiering, Historical trend analysis, Peer benchmarking, Velocity metering).")
        det_result = self.scorer.run(domain_scores)
        
        # Step 2: Execute Analytics Narrative Evaluator Agent
        reasoning_steps.append("Step 2: Executing Analytics Narrative Evaluator Agent to analyze performance drivers and growth trends.")
        narrative = await self.narrative_evaluator.evaluate(det_result)
        
        # Step 3: Execute Actionable Analytics Strategist Agent
        reasoning_steps.append("Step 3: Executing Actionable Analytics Strategist Agent to produce quick-win recommendations.")
        advice = await self.strategist.strategize(det_result)
        
        # Step 4: Synthesize Report
        reasoning_steps.append("Step 4: Compiling Career Analytics Performance Report.")
        reasoning_result = ReasoningAnalyticsPipelineResult(
            narrative=narrative,
            advice=advice,
            reasoning_steps=reasoning_steps
        )
        
        return AnalyticsOrchestratorReport(
            readiness_score=det_result.readiness.overall_readiness_score,
            percentile_rank=det_result.readiness.percentile_rank,
            confidence_score=det_result.confidence_score,
            deterministic_analysis=det_result,
            reasoning_analysis=reasoning_result,
            reasoning_steps=reasoning_steps
        )
