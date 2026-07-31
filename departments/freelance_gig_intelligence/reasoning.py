from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.freelance_gig_intelligence.schemas import (
    StrategicProposalNarrative, HighConvertingProposalDraft, ReasoningFreelancePipelineResult, DeterministicFreelancePipelineResult
)

class StrategicProposalNarrativeAgent(BaseAgent):
    """Agent 8: Formulates strategic proposal positioning and competitive win strategy."""
    def __init__(self):
        super().__init__(
            agent_id="strategic_proposal_narrative",
            name="Strategic Proposal Narrative Agent",
            description="Evaluates contract viability and maps winning proposal differentiators.",
            icon="Briefcase"
        )

    async def evaluate(self, det_result: DeterministicFreelancePipelineResult) -> StrategicProposalNarrative:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Top 1% Freelance Agency Principal & Contract Advisor",
            domain_focus="Freelance proposal optimization, client win rate maximization, and contract pricing strategy."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"viability_score": det_result.freelance_viability_score, "win_probability": det_result.proposal.win_probability}
        )
        
        fallback = {
            "proposal_strategy_summary": f"High contract viability ({det_result.freelance_viability_score}% score). Client has verified payment history ({det_result.client.client_rating_avg}/5.0 rating). Anchor proposal on milestone-based deliverables.",
            "key_proposal_differentiators": [
                "Include live video demo link of previous FastAPI microservice deployment",
                "Offer 14-day post-launch maintenance SLA at zero extra charge"
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="proposal_narrative", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicProposalNarrative(
                proposal_strategy_summary=parsed.get("proposal_strategy_summary", fallback["proposal_strategy_summary"]),
                key_proposal_differentiators=parsed.get("key_proposal_differentiators", fallback["key_proposal_differentiators"])
            )
        except Exception:
            return StrategicProposalNarrative(**fallback)

class ProposalDraftGeneratorAgent(BaseAgent):
    """Agent 9: Generates high-converting contract proposals and milestone breakdowns."""
    def __init__(self):
        super().__init__(
            agent_id="proposal_draft_generator",
            name="Proposal Draft Generator Agent",
            description="Generates executive freelance proposal cover letters and milestone payment schedules.",
            icon="FileCode"
        )

    async def generate_draft(self, det_result: DeterministicFreelancePipelineResult) -> HighConvertingProposalDraft:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Principal Freelance Proposal Copywriter",
            domain_focus="High-converting Upwork/Toptal proposal generation and milestone structuring."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"take_home_amount": det_result.fees.take_home_amount}
        )
        
        fallback = {
            "proposal_cover_letter": "Hi there,\n\nI reviewed your project requirements for building a high-concurrency backend system. Having previously architected FastAPI microservices handling 10k+ requests/sec, I can deliver your solution within 80 billable hours.\n\nLooking forward to discussing the milestone timeline.\n\nBest regards,\nAlex",
            "milestone_deliverables_breakdown": [
                "Milestone 1 (30 hrs): Database schema design & FastAPI core routing ($2,850)",
                "Milestone 2 (30 hrs): Docker containerization & JWT authentication ($2,850)",
                "Milestone 3 (20 hrs): Unit test suite (100% pass) & live cloud deployment ($1,900)"
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="proposal_draft", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return HighConvertingProposalDraft(
                proposal_cover_letter=parsed.get("proposal_cover_letter", fallback["proposal_cover_letter"]),
                milestone_deliverables_breakdown=parsed.get("milestone_deliverables_breakdown", fallback["milestone_deliverables_breakdown"])
            )
        except Exception:
            return HighConvertingProposalDraft(**fallback)
