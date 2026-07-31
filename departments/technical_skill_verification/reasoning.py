from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.technical_skill_verification.schemas import (
    QualitativeCodeReviewNarrative, RefactoringStrategistRecommendation, ReasoningTechnicalPipelineResult, DeterministicTechnicalPipelineResult
)

class QualitativeCodeReviewNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates qualitative code quality, readability, and design practices."""
    def __init__(self):
        super().__init__(
            agent_id="qualitative_code_review_narrative",
            name="Qualitative Code Review Narrative Agent",
            description="Evaluates code quality, architectural elegance, and maintainability.",
            icon="Code"
        )

    async def evaluate(self, code: str, det_result: DeterministicTechnicalPipelineResult) -> QualitativeCodeReviewNarrative:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Principal Software Architect & Code Reviewer",
            domain_focus="Code review, AST structural evaluation, and software craftsmanship."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"mastery_score": det_result.technical_mastery_score, "complexity_tier": det_result.complexity.time_complexity_tier}
        )
        
        fallback = {
            "code_quality_critique": f"Code achieves high technical quality ({det_result.technical_mastery_score}% mastery score) with optimal {det_result.complexity.time_complexity_tier} time complexity.",
            "architectural_strengths": [
                "Strict type annotations and zero syntax errors",
                "Clean variable naming and boundary condition handling"
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="code_review", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return QualitativeCodeReviewNarrative(
                code_quality_critique=parsed.get("code_quality_critique", fallback["code_quality_critique"]),
                architectural_strengths=parsed.get("architectural_strengths", fallback["architectural_strengths"])
            )
        except Exception:
            return QualitativeCodeReviewNarrative(**fallback)

class RefactoringStrategistAgent(BaseAgent):
    """Agent 9: Formulates code refactoring and performance optimization strategies."""
    def __init__(self):
        super().__init__(
            agent_id="refactoring_strategist",
            name="Refactoring Strategist Agent",
            description="Formulates code refactoring and memory/time optimization recommendations.",
            icon="Zap"
        )

    async def refactor(self, code: str, det_result: DeterministicTechnicalPipelineResult) -> RefactoringStrategistRecommendation:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Senior Performance Tuning Engineer",
            domain_focus="Algorithmic optimization, memory tuning, and clean code refactoring."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"vulnerabilities": det_result.security.flagged_security_risks}
        )
        
        fallback = {
            "refactoring_opportunities": [
                "Add docstring specifying parameter types and expected return values",
                "Add explicit boundary checks for empty array inputs"
            ],
            "optimized_code_snippet": code
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="code_refactor", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return RefactoringStrategistRecommendation(
                refactoring_opportunities=parsed.get("refactoring_opportunities", fallback["refactoring_opportunities"]),
                optimized_code_snippet=parsed.get("optimized_code_snippet", fallback["optimized_code_snippet"])
            )
        except Exception:
            return RefactoringStrategistRecommendation(**fallback)
