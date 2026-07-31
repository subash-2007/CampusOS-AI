from typing import Dict, Any, List, Optional
from app.agents.base_agent import BaseAgent
from departments.product_management_intelligence.deterministic import ProductScorerAgent
from departments.product_management_intelligence.reasoning import StrategicProductNarrativeAgent, PRDSpecificationGeneratorAgent
from departments.product_management_intelligence.schemas import (
    ProductManagementOrchestratorReport, ReasoningProductPipelineResult
)

class ProductManagementOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator Agent for the Product Management Intelligence Department."""
    def __init__(self):
        super().__init__(
            agent_id="product_management_orchestrator",
            name="Product Management Master Orchestrator",
            description="Coordinates all 9 sub-agents to deliver a unified Product Management Report.",
            icon="Box"
        )
        self.scorer = ProductScorerAgent()
        self.narrative_agent = StrategicProductNarrativeAgent()
        self.prd_generator = PRDSpecificationGeneratorAgent()

    async def run_pipeline(self, has_user_stories: bool = True) -> ProductManagementOrchestratorReport:
        reasoning_steps = []
        
        # Step 1: Execute Deterministic Pipeline
        reasoning_steps.append("Step 1: Running deterministic Product Management Intelligence pipeline (PRD completeness metering, RICE prioritization scoring, Feature roadmap alignment evaluation, User cohort retention metering, Competitor feature matrix benchmarking, Product analytics telemetry auditing).")
        det_result = self.scorer.run(has_user_stories)
        
        # Step 2: Execute Strategic Product Narrative Agent
        reasoning_steps.append("Step 2: Executing Strategic Product Narrative Agent to evaluate product-market fit highlights.")
        narrative = await self.narrative_agent.evaluate(det_result)
        
        # Step 3: Execute PRD Specification Generator Agent
        reasoning_steps.append("Step 3: Executing PRD Specification Generator Agent to produce user stories and acceptance criteria.")
        prd_draft = await self.prd_generator.generate_prd(det_result)
        
        # Step 4: Synthesize Report
        reasoning_steps.append("Step 4: Compiling Product Management Intelligence Master Report.")
        reasoning_result = ReasoningProductPipelineResult(
            narrative=narrative,
            prd_draft=prd_draft,
            reasoning_steps=reasoning_steps
        )
        
        tier = "PRODUCT MARKET FIT" if det_result.product_viability_score >= 80 else "DISCOVERY PHASE"
        
        return ProductManagementOrchestratorReport(
            product_tier=tier,
            product_viability_score=det_result.product_viability_score,
            confidence_score=det_result.confidence_score,
            deterministic_analysis=det_result,
            reasoning_analysis=reasoning_result,
            reasoning_steps=reasoning_steps
        )
