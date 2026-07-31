from typing import Dict, Any, List, Optional
from app.agents.base_agent import BaseAgent
from departments.communication_intelligence.deterministic import CommunicationScorerAgent
from departments.communication_intelligence.reasoning import QualitativeCommunicationNarrativeAgent, EmailRewriteStrategistAgent
from departments.communication_intelligence.schemas import (
    CommunicationOrchestratorReport, ReasoningCommunicationPipelineResult
)

class CommunicationOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator Agent for the Communication Intelligence Department."""
    def __init__(self):
        super().__init__(
            agent_id="communication_orchestrator",
            name="Communication Intelligence Master Orchestrator",
            description="Coordinates all 9 sub-agents to deliver a unified Communication Audit Report.",
            icon="Send"
        )
        self.scorer = CommunicationScorerAgent()
        self.narrative_agent = QualitativeCommunicationNarrativeAgent()
        self.rewrite_agent = EmailRewriteStrategistAgent()

    async def run_pipeline(self, text: str = "") -> CommunicationOrchestratorReport:
        reasoning_steps = []
        
        # Step 1: Execute Deterministic Pipeline
        reasoning_steps.append("Step 1: Running deterministic Communication Intelligence pipeline (Email tone analysis, Executive brevity metering, Grammar & spelling audit, Actionability indexing, Persuasiveness scoring, Vocabulary sophistication grading).")
        det_result = self.scorer.run(text)
        
        # Step 2: Execute Qualitative Communication Narrative Agent
        reasoning_steps.append("Step 2: Executing Qualitative Communication Narrative Agent to evaluate tone alignment and impact.")
        narrative = await self.narrative_agent.evaluate(text, det_result)
        
        # Step 3: Execute Email Rewrite Strategist Agent
        reasoning_steps.append("Step 3: Executing Email Rewrite Strategist Agent to produce high-converting outreach rewrites.")
        rewrite = await self.rewrite_agent.rewrite(text, det_result)
        
        # Step 4: Synthesize Report
        reasoning_steps.append("Step 4: Compiling Communication Intelligence Master Report.")
        reasoning_result = ReasoningCommunicationPipelineResult(
            narrative=narrative,
            rewrite_strategy=rewrite,
            reasoning_steps=reasoning_steps
        )
        
        return CommunicationOrchestratorReport(
            communication_score=det_result.overall_communication_score,
            confidence_score=det_result.confidence_score,
            deterministic_analysis=det_result,
            reasoning_analysis=reasoning_result,
            reasoning_steps=reasoning_steps
        )
