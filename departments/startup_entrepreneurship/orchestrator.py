from typing import Dict, Any, List, Optional
from app.agents.base_agent import BaseAgent
from departments.startup_entrepreneurship.deterministic import StartupScorerAgent
from departments.startup_entrepreneurship.reasoning import StrategicVentureNarrativeAgent, InvestorPitchNarrativeAgent
from departments.startup_entrepreneurship.schemas import (
    StartupEntrepreneurshipOrchestratorReport, ReasoningStartupPipelineResult
)

class StartupEntrepreneurshipOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator Agent for the Startup & Entrepreneurship Department."""
    def __init__(self):
        super().__init__(
            agent_id="startup_entrepreneurship_orchestrator",
            name="Startup & Entrepreneurship Master Orchestrator",
            description="Coordinates all 9 sub-agents to deliver a unified Startup & Entrepreneurship Report.",
            icon="Zap"
        )
        self.scorer = StartupScorerAgent()
        self.narrative_agent = StrategicVentureNarrativeAgent()
        self.pitch_agent = InvestorPitchNarrativeAgent()

    async def run_pipeline(self, tam: float = 12.5, cash: int = 810000, burn: int = 45000) -> StartupEntrepreneurshipOrchestratorReport:
        reasoning_steps = []
        
        # Step 1: Execute Deterministic Pipeline
        reasoning_steps.append("Step 1: Running deterministic Startup & Entrepreneurship pipeline (TAM/SAM/SOM market sizing, Runway burn rate metering, Pitch deck readiness scoring, Unit economics calculation, Co-founder equity audit, Regulatory compliance auditing).")
        det_result = self.scorer.run(tam, cash, burn)
        
        # Step 2: Execute Strategic Venture Narrative Agent
        reasoning_steps.append("Step 2: Executing Strategic Venture Narrative Agent to evaluate investor highlights.")
        narrative = await self.narrative_agent.evaluate(det_result)
        
        # Step 3: Execute Investor Pitch Narrative Agent
        reasoning_steps.append("Step 3: Executing Investor Pitch Narrative Agent to refine elevator pitch and fundraising strategy.")
        pitch_narrative = await self.pitch_agent.generate_pitch(det_result)
        
        # Step 4: Synthesize Report
        reasoning_steps.append("Step 4: Compiling Startup & Entrepreneurship Master Report.")
        reasoning_result = ReasoningStartupPipelineResult(
            narrative=narrative,
            pitch_narrative=pitch_narrative,
            reasoning_steps=reasoning_steps
        )
        
        tier = "VENTURE READY" if det_result.startup_viability_score >= 80 else "EARLY SEED"
        
        return StartupEntrepreneurshipOrchestratorReport(
            venture_tier=tier,
            startup_viability_score=det_result.startup_viability_score,
            confidence_score=det_result.confidence_score,
            deterministic_analysis=det_result,
            reasoning_analysis=reasoning_result,
            reasoning_steps=reasoning_steps
        )
