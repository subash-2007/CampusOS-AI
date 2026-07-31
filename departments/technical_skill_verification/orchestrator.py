from typing import Dict, Any, List, Optional
from app.agents.base_agent import BaseAgent
from departments.technical_skill_verification.deterministic import TechnicalMasteryScorerAgent
from departments.technical_skill_verification.reasoning import QualitativeCodeReviewNarrativeAgent, RefactoringStrategistAgent
from departments.technical_skill_verification.schemas import (
    TechnicalSkillOrchestratorReport, ReasoningTechnicalPipelineResult
)

class TechnicalSkillOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator Agent for the Technical Skill Verification Department."""
    def __init__(self):
        super().__init__(
            agent_id="technical_skill_orchestrator",
            name="Technical Skill Verification Master Orchestrator",
            description="Coordinates all 9 sub-agents to deliver a unified Technical Skill Verification Report.",
            icon="Terminal"
        )
        self.scorer = TechnicalMasteryScorerAgent()
        self.review_narrative = QualitativeCodeReviewNarrativeAgent()
        self.refactoring = RefactoringStrategistAgent()

    async def run_pipeline(self, code: str = "") -> TechnicalSkillOrchestratorReport:
        reasoning_steps = []
        
        # Step 1: Execute Deterministic Pipeline
        reasoning_steps.append("Step 1: Running deterministic Technical Skill Verification pipeline (AST syntax validation, Algorithmic complexity evaluation, Unit test coverage auditing, Security vulnerability scanning, Design pattern detection, Memory/execution performance benchmarking).")
        det_result = self.scorer.run(code)
        
        # Step 2: Execute Qualitative Code Review Narrative Agent
        reasoning_steps.append("Step 2: Executing Qualitative Code Review Narrative Agent to analyze code quality and maintainability.")
        narrative = await self.review_narrative.evaluate(code, det_result)
        
        # Step 3: Execute Refactoring Strategist Agent
        reasoning_steps.append("Step 3: Executing Refactoring Strategist Agent to formulate code optimization recommendations.")
        refactoring_rec = await self.refactoring.refactor(code, det_result)
        
        # Step 4: Synthesize Report
        reasoning_steps.append("Step 4: Compiling Technical Skill Verification Master Report.")
        reasoning_result = ReasoningTechnicalPipelineResult(
            narrative=narrative,
            refactoring=refactoring_rec,
            reasoning_steps=reasoning_steps
        )
        
        verdict = "PASSED" if det_result.technical_mastery_score >= 80 else "NEEDS_REFACTORING"
        
        return TechnicalSkillOrchestratorReport(
            verification_verdict=verdict,
            technical_mastery_score=det_result.technical_mastery_score,
            confidence_score=det_result.confidence_score,
            deterministic_analysis=det_result,
            reasoning_analysis=reasoning_result,
            reasoning_steps=reasoning_steps
        )
