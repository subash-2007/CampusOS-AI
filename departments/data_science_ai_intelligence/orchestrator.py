from typing import Dict, Any, List, Optional
from app.agents.base_agent import BaseAgent
from departments.data_science_ai_intelligence.deterministic import DataScienceScorerAgent
from departments.data_science_ai_intelligence.reasoning import StrategicMLOpsNarrativeAgent, MLOpsDeploymentStrategistAgent
from departments.data_science_ai_intelligence.schemas import (
    DataScienceAIOrchestratorReport, ReasoningDataSciencePipelineResult
)

class DataScienceAIOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator Agent for the Data Science & AI Intelligence Department."""
    def __init__(self):
        super().__init__(
            agent_id="data_science_ai_orchestrator",
            name="Data Science & AI Intelligence Master Orchestrator",
            description="Coordinates all 9 sub-agents to deliver a unified Data Science & AI Report.",
            icon="Terminal"
        )
        self.scorer = DataScienceScorerAgent()
        self.narrative_agent = StrategicMLOpsNarrativeAgent()
        self.deployment_strategist = MLOpsDeploymentStrategistAgent()

    async def run_pipeline(self, f1_score: float = 0.92, latency_ms: int = 145) -> DataScienceAIOrchestratorReport:
        reasoning_steps = []
        
        # Step 1: Execute Deterministic Pipeline
        reasoning_steps.append("Step 1: Running deterministic Data Science & AI Intelligence pipeline (ML model accuracy metering, Feature engineering coverage evaluation, Data pipeline latency metering, PSI data drift detection, Hyperparameter optimization scoring, AI model bias fairness auditing).")
        det_result = self.scorer.run(f1_score, latency_ms)
        
        # Step 2: Execute Strategic MLOps Narrative Agent
        reasoning_steps.append("Step 2: Executing Strategic MLOps Narrative Agent to evaluate model governance.")
        narrative = await self.narrative_agent.evaluate(det_result)
        
        # Step 3: Execute MLOps Deployment Strategist Agent
        reasoning_steps.append("Step 3: Executing MLOps Deployment Strategist Agent to formulate model serving stack.")
        deployment = await self.deployment_strategist.recommend_deployment(det_result)
        
        # Step 4: Synthesize Report
        reasoning_steps.append("Step 4: Compiling Data Science & AI Intelligence Master Report.")
        reasoning_result = ReasoningDataSciencePipelineResult(
            narrative=narrative,
            deployment_strategy=deployment,
            reasoning_steps=reasoning_steps
        )
        
        tier = "ENTERPRISE PRODUCTION AI" if det_result.ai_readiness_score >= 85 else "STAGING MODEL"
        
        return DataScienceAIOrchestratorReport(
            ai_readiness_tier=tier,
            ai_readiness_score=det_result.ai_readiness_score,
            confidence_score=det_result.confidence_score,
            deterministic_analysis=det_result,
            reasoning_analysis=reasoning_result,
            reasoning_steps=reasoning_steps
        )
