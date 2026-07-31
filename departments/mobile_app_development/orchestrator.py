from typing import Dict, Any, List, Optional
from app.agents.base_agent import BaseAgent
from departments.mobile_app_development.deterministic import MobileScorerAgent
from departments.mobile_app_development.reasoning import StrategicMobileNarrativeAgent, MobileReleasePlannerAgent
from departments.mobile_app_development.schemas import (
    MobileAppDevelopmentOrchestratorReport, ReasoningMobilePipelineResult
)

class MobileAppDevelopmentOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator Agent for the Mobile App Development Department."""
    def __init__(self):
        super().__init__(
            agent_id="mobile_app_development_orchestrator",
            name="Mobile App Development Master Orchestrator",
            description="Coordinates all 9 sub-agents to deliver a unified Mobile App Report.",
            icon="Smartphone"
        )
        self.scorer = MobileScorerAgent()
        self.narrative_agent = StrategicMobileNarrativeAgent()
        self.release_planner = MobileReleasePlannerAgent()

    async def run_pipeline(self, fps: float = 60.0, parity_pct: float = 98.0) -> MobileAppDevelopmentOrchestratorReport:
        reasoning_steps = []
        
        # Step 1: Execute Deterministic Pipeline
        reasoning_steps.append("Step 1: Running deterministic Mobile App Development pipeline (UI FPS performance metering, Memory leak auditing, Offline sync reliability evaluation, App Store ASO keyword scoring, Cross-platform parity metering, Push notification engagement auditing).")
        det_result = self.scorer.run(fps, parity_pct)
        
        # Step 2: Execute Strategic Mobile Narrative Agent
        reasoning_steps.append("Step 2: Executing Strategic Mobile Narrative Agent to evaluate mobile architecture highlights.")
        narrative = await self.narrative_agent.evaluate(det_result)
        
        # Step 3: Execute Mobile Release Planner Agent
        reasoning_steps.append("Step 3: Executing Mobile Release Planner Agent to generate App Store submission checklist.")
        release_plan = await self.release_planner.plan_release(det_result)
        
        # Step 4: Synthesize Report
        reasoning_steps.append("Step 4: Compiling Mobile App Development Master Report.")
        reasoning_result = ReasoningMobilePipelineResult(
            narrative=narrative,
            release_plan=release_plan,
            reasoning_steps=reasoning_steps
        )
        
        tier = "PRODUCTION READY MOBILE" if det_result.mobile_readiness_score >= 85 else "STAGING APP"
        
        return MobileAppDevelopmentOrchestratorReport(
            mobile_tier=tier,
            mobile_readiness_score=det_result.mobile_readiness_score,
            confidence_score=det_result.confidence_score,
            deterministic_analysis=det_result,
            reasoning_analysis=reasoning_result,
            reasoning_steps=reasoning_steps
        )
