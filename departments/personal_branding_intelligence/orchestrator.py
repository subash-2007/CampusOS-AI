from typing import Dict, Any, List, Optional
from app.agents.base_agent import BaseAgent
from departments.personal_branding_intelligence.deterministic import BrandingScorerAgent
from departments.personal_branding_intelligence.reasoning import StrategicBrandNarrativeAgent, ContentCalendarStrategistAgent
from departments.personal_branding_intelligence.schemas import (
    PersonalBrandingOrchestratorReport, ReasoningBrandingPipelineResult
)

class PersonalBrandingOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator Agent for the Personal Branding Intelligence Department."""
    def __init__(self):
        super().__init__(
            agent_id="personal_branding_orchestrator",
            name="Personal Branding Intelligence Master Orchestrator",
            description="Coordinates all 9 sub-agents to deliver a unified Personal Branding Report.",
            icon="Share2"
        )
        self.scorer = BrandingScorerAgent()
        self.narrative_agent = StrategicBrandNarrativeAgent()
        self.content_strategist = ContentCalendarStrategistAgent()

    async def run_pipeline(
        self,
        headline: str = "Senior Software Engineer | Distributed Systems & Cloud Architecture"
    ) -> PersonalBrandingOrchestratorReport:
        reasoning_steps = []
        
        # Step 1: Execute Deterministic Pipeline
        reasoning_steps.append("Step 1: Running deterministic Personal Branding Intelligence pipeline (LinkedIn profile completeness audit, Thought leadership engagement metering, Bio headline SEO evaluation, Cross-platform presence tracking, Brand consistency index calculation, Media feature auditing).")
        det_result = self.scorer.run(headline)
        
        # Step 2: Execute Strategic Brand Narrative Agent
        reasoning_steps.append("Step 2: Executing Strategic Brand Narrative Agent to establish thought leadership positioning.")
        narrative = await self.narrative_agent.evaluate(det_result)
        
        # Step 3: Execute Content Calendar Strategist Agent
        reasoning_steps.append("Step 3: Executing Content Calendar Strategist Agent to produce monthly technical post ideas and drafts.")
        calendar = await self.content_strategist.generate_calendar(det_result)
        
        # Step 4: Synthesize Report
        reasoning_steps.append("Step 4: Compiling Personal Branding Intelligence Master Report.")
        reasoning_result = ReasoningBrandingPipelineResult(
            narrative=narrative,
            content_calendar=calendar,
            reasoning_steps=reasoning_steps
        )
        
        tier = "TOP TIER BRAND" if det_result.personal_brand_score >= 85 else "DEVELOPING BRAND"
        
        return PersonalBrandingOrchestratorReport(
            brand_strength_tier=tier,
            personal_brand_score=det_result.personal_brand_score,
            confidence_score=det_result.confidence_score,
            deterministic_analysis=det_result,
            reasoning_analysis=reasoning_result,
            reasoning_steps=reasoning_steps
        )
