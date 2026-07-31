from typing import Dict, Any, List, Optional
from app.agents.base_agent import BaseAgent
from departments.memory_personalization.deterministic import MemoryScorerAgent
from departments.memory_personalization.reasoning import PersonalizationSynthesizerAgent, AdaptiveLearningPathAgent
from departments.memory_personalization.schemas import (
    MemoryOrchestratorReport, ReasoningMemoryPipelineResult
)

class MemoryOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator Agent for the Memory & Personalization Department."""
    def __init__(self):
        super().__init__(
            agent_id="memory_orchestrator",
            name="Memory & Personalization Master Orchestrator",
            description="Coordinates all 9 sub-agents to deliver a personalized, cross-session user memory state.",
            icon="Database"
        )
        self.scorer = MemoryScorerAgent()
        self.synthesizer = PersonalizationSynthesizerAgent()
        self.adaptive_path = AdaptiveLearningPathAgent()

    async def run_pipeline(
        self,
        user_id: str = "usr_99812",
        target_roles: Optional[List[str]] = None
    ) -> MemoryOrchestratorReport:
        reasoning_steps = []
        
        # Step 1: Execute Deterministic Pipeline
        reasoning_steps.append("Step 1: Running deterministic Memory & Personalization pipeline (User preferences audit, Historical memory tracking, Skill trajectory analysis, Personalization vector building, Context retention scoring, Persona classification).")
        det_result = self.scorer.run(user_id, target_roles)
        
        # Step 2: Execute Personalization Synthesizer Agent
        reasoning_steps.append("Step 2: Executing Personalization Synthesizer Agent to synthesize cross-session context.")
        synthesis = await self.synthesizer.synthesize(det_result)
        
        # Step 3: Execute Adaptive Learning Path Agent
        reasoning_steps.append("Step 3: Executing Adaptive Learning Path Agent to dynamically adapt milestones.")
        adapted = await self.adaptive_path.adapt(det_result)
        
        # Step 4: Synthesize Report
        reasoning_steps.append("Step 4: Compiling Memory & Personalization Report.")
        reasoning_result = ReasoningMemoryPipelineResult(
            synthesis=synthesis,
            adaptive_path=adapted,
            reasoning_steps=reasoning_steps
        )
        
        return MemoryOrchestratorReport(
            user_id=user_id,
            retention_score=det_result.retention.retention_score,
            confidence_score=det_result.confidence_score,
            deterministic_analysis=det_result,
            reasoning_analysis=reasoning_result,
            reasoning_steps=reasoning_steps
        )
