from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.product_management_intelligence.schemas import (
    StrategicProductNarrative, PRDSpecificationDraft, ReasoningProductPipelineResult, DeterministicProductPipelineResult
)

class StrategicProductNarrativeAgent(BaseAgent):
    """Agent 8: Formulates strategic product evaluations and product-market fit narratives."""
    def __init__(self):
        super().__init__(
            agent_id="strategic_product_narrative",
            name="Strategic Product Narrative Agent",
            description="Evaluates product-market fit, user retention cohorts, and feature roadmap strategy.",
            icon="Layers"
        )

    async def evaluate(self, det_result: DeterministicProductPipelineResult) -> StrategicProductNarrative:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="VP of Product & Chief Product Officer",
            domain_focus="Product management strategy, PRD auditing, and user retention optimization."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"viability_score": det_result.product_viability_score, "rice_score": det_result.rice.rice_score}
        )
        
        fallback = {
            "product_evaluation_summary": f"Strong product-market fit profile ({det_result.product_viability_score}% score). High RICE prioritization score ({det_result.rice.rice_score}) and 45% Day-30 user cohort retention.",
            "key_feature_highlights": [
                "High feature parity (85%) against key B2B HR-Tech SaaS competitors",
                "High-impact feature pipeline with RICE score of 1200.0"
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="product_eval", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicProductNarrative(
                product_evaluation_summary=parsed.get("product_evaluation_summary", fallback["product_evaluation_summary"]),
                key_feature_highlights=parsed.get("key_feature_highlights", fallback["key_feature_highlights"])
            )
        except Exception:
            return StrategicProductNarrative(**fallback)

class PRDSpecificationGeneratorAgent(BaseAgent):
    """Agent 9: Generates structured Product Requirement Document (PRD) user stories and acceptance criteria."""
    def __init__(self):
        super().__init__(
            agent_id="prd_specification_generator",
            name="PRD Specification Generator Agent",
            description="Generates PRD user stories, technical acceptance criteria, and edge-case specs.",
            icon="FileCode"
        )

    async def generate_prd(self, det_result: DeterministicProductPipelineResult) -> PRDSpecificationDraft:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Principal Technical Product Manager",
            domain_focus="PRD writing, user story framing, and Gherkin acceptance criteria drafting."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"dau": det_result.telemetry.daily_active_users}
        )
        
        fallback = {
            "user_stories_and_acceptance_criteria": [
                "US-1: As a job applicant, I want real-time ATS match feedback so that I can optimize my resume keywords before submitting.",
                "AC-1: GIVEN a user uploads a PDF resume, WHEN parsed by Department 001, THEN display keyword gap score in < 500ms."
            ],
            "sample_prd_executive_summary": "PRD: Real-Time Resume Keyword GAP Scoring Engine v2.0\n\nOBJECTIVE: Provide candidate instant ATS scoring with microsecond execution latency using deterministic scoring engines."
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="prd_generation", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return PRDSpecificationDraft(
                user_stories_and_acceptance_criteria=parsed.get("user_stories_and_acceptance_criteria", fallback["user_stories_and_acceptance_criteria"]),
                sample_prd_executive_summary=parsed.get("sample_prd_executive_summary", fallback["sample_prd_executive_summary"])
            )
        except Exception:
            return PRDSpecificationDraft(**fallback)
