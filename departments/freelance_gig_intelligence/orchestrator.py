from typing import Dict, Any, List, Optional
from app.agents.base_agent import BaseAgent
from departments.freelance_gig_intelligence.deterministic import FreelanceScorerAgent
from departments.freelance_gig_intelligence.reasoning import StrategicProposalNarrativeAgent, ProposalDraftGeneratorAgent
from departments.freelance_gig_intelligence.schemas import (
    FreelanceGigOrchestratorReport, ReasoningFreelancePipelineResult
)

class FreelanceGigOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator Agent for the Freelance & Gig Intelligence Department."""
    def __init__(self):
        super().__init__(
            agent_id="freelance_gig_orchestrator",
            name="Freelance & Gig Intelligence Master Orchestrator",
            description="Coordinates all 9 sub-agents to deliver a unified Freelance & Gig Intelligence Report.",
            icon="DollarSign"
        )
        self.scorer = FreelanceScorerAgent()
        self.narrative_agent = StrategicProposalNarrativeAgent()
        self.draft_generator = ProposalDraftGeneratorAgent()

    async def run_pipeline(
        self,
        proposed_rate: int = 95,
        estimated_hours: int = 80
    ) -> FreelanceGigOrchestratorReport:
        reasoning_steps = []
        
        # Step 1: Execute Deterministic Pipeline
        reasoning_steps.append("Step 1: Running deterministic Freelance & Gig Intelligence pipeline (Hourly rate benchmarking, Contract scope complexity evaluation, Client reputation auditing, Proposal win probability calculation, Platform fee modeling, Self-employment tax auditing).")
        det_result = self.scorer.run(proposed_rate, estimated_hours)
        
        # Step 2: Execute Strategic Proposal Narrative Agent
        reasoning_steps.append("Step 2: Executing Strategic Proposal Narrative Agent to evaluate competitive positioning.")
        narrative = await self.narrative_agent.evaluate(det_result)
        
        # Step 3: Execute Proposal Draft Generator Agent
        reasoning_steps.append("Step 3: Executing Proposal Draft Generator Agent to generate proposal cover letter and milestone breakdown.")
        proposal_draft = await self.draft_generator.generate_draft(det_result)
        
        # Step 4: Synthesize Report
        reasoning_steps.append("Step 4: Compiling Freelance & Gig Intelligence Master Report.")
        reasoning_result = ReasoningFreelancePipelineResult(
            narrative=narrative,
            proposal_draft=proposal_draft,
            reasoning_steps=reasoning_steps
        )
        
        tier = "HIGHLY PROFITABLE" if det_result.freelance_viability_score >= 80 else "MODERATE PROFITABILITY"
        
        return FreelanceGigOrchestratorReport(
            project_viability_tier=tier,
            freelance_viability_score=det_result.freelance_viability_score,
            confidence_score=det_result.confidence_score,
            deterministic_analysis=det_result,
            reasoning_analysis=reasoning_result,
            reasoning_steps=reasoning_steps
        )
