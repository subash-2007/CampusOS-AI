from typing import Dict, Any, List, Optional
from app.agents.base_agent import BaseAgent
from departments.executive_communication.deterministic import ExecutiveCommScorerAgent
from departments.executive_communication.reasoning import StrategicExecutiveNarrativeAgent, ExecutiveBriefingGeneratorAgent
from departments.executive_communication.schemas import (
    ExecutiveCommunicationOrchestratorReport, ReasoningExecutiveCommPipelineResult
)

class ExecutiveCommunicationOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator Agent for the Executive Communication Department."""
    def __init__(self):
        super().__init__(
            agent_id="executive_communication_orchestrator",
            name="Executive Communication Master Orchestrator",
            description="Coordinates all 9 sub-agents to deliver a unified Executive Communication Report.",
            icon="Volume2"
        )
        self.scorer = ExecutiveCommScorerAgent()
        self.narrative_agent = StrategicExecutiveNarrativeAgent()
        self.briefing_generator = ExecutiveBriefingGeneratorAgent()

    async def run_pipeline(self, raw_word_count: int = 300) -> ExecutiveCommunicationOrchestratorReport:
        reasoning_steps = []
        
        # Step 1: Execute Deterministic Pipeline
        reasoning_steps.append("Step 1: Running deterministic Executive Communication pipeline (Brevity conciseness metering, Executive tone auditing, Board deck readiness scoring, Active listening metering, Data storytelling evaluation, Crisis communication auditing).")
        det_result = self.scorer.run(raw_word_count)
        
        # Step 2: Execute Strategic Executive Narrative Agent
        reasoning_steps.append("Step 2: Executing Strategic Executive Narrative Agent to evaluate C-suite presentation readiness.")
        narrative = await self.narrative_agent.evaluate(det_result)
        
        # Step 3: Execute Executive Briefing Generator Agent
        reasoning_steps.append("Step 3: Executing Executive Briefing Generator Agent to draft executive memos.")
        briefing = await self.briefing_generator.generate_briefing(det_result)
        
        # Step 4: Synthesize Report
        reasoning_steps.append("Step 4: Compiling Executive Communication Master Report.")
        reasoning_result = ReasoningExecutiveCommPipelineResult(
            narrative=narrative,
            briefing_draft=briefing,
            reasoning_steps=reasoning_steps
        )
        
        tier = "C-SUITE PERSUASIVE" if det_result.executive_comm_score >= 85 else "OPERATIONAL BRIEFING"
        
        return ExecutiveCommunicationOrchestratorReport(
            communication_tier=tier,
            executive_comm_score=det_result.executive_comm_score,
            confidence_score=det_result.confidence_score,
            deterministic_analysis=det_result,
            reasoning_analysis=reasoning_result,
            reasoning_steps=reasoning_steps
        )
