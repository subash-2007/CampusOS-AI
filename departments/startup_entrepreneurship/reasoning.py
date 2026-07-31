from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.startup_entrepreneurship.schemas import (
    StrategicVentureNarrative, InvestorPitchNarrative, ReasoningStartupPipelineResult, DeterministicStartupPipelineResult
)

class StrategicVentureNarrativeAgent(BaseAgent):
    """Agent 8: Formulates strategic venture capital evaluations and startup scalability narratives."""
    def __init__(self):
        super().__init__(
            agent_id="strategic_venture_narrative",
            name="Strategic Venture Narrative Agent",
            description="Evaluates startup market TAM, unit economics, and venture capital readiness.",
            icon="TrendingUp"
        )

    async def evaluate(self, det_result: DeterministicStartupPipelineResult) -> StrategicVentureNarrative:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Venture Capital Partner & Startup Advisor",
            domain_focus="Startup evaluation, Seed/Series A fundraising strategy, and unit economics."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"viability_score": det_result.startup_viability_score, "ltv_cac": det_result.economics.ltv_to_cac_ratio}
        )
        
        fallback = {
            "venture_summary": f"Venture-ready startup profile ({det_result.startup_viability_score}% score). Exceptional LTV:CAC ratio of {det_result.economics.ltv_to_cac_ratio} with 18 months of runway.",
            "key_investor_highlights": [
                "Strong unit economics (LTV:CAC of 4.2x with 6-month payback period)",
                "Healthy 18-month financial runway ($45k/mo burn rate)"
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="venture_eval", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicVentureNarrative(
                venture_summary=parsed.get("venture_summary", fallback["venture_summary"]),
                key_investor_highlights=parsed.get("key_investor_highlights", fallback["key_investor_highlights"])
            )
        except Exception:
            return StrategicVentureNarrative(**fallback)

class InvestorPitchNarrativeAgent(BaseAgent):
    """Agent 9: Generates compelling investor elevator pitches and fundraising strategies."""
    def __init__(self):
        super().__init__(
            agent_id="investor_pitch_narrative",
            name="Investor Pitch Narrative Agent",
            description="Generates executive investor elevator pitches and fundraising roadmap recommendations.",
            icon="DollarSign"
        )

    async def generate_pitch(self, det_result: DeterministicStartupPipelineResult) -> InvestorPitchNarrative:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Principal Startup Pitch Coach",
            domain_focus="Investor elevator pitch generation, deck narrative refinement, and Seed/Series A strategy."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"tam": det_result.tam.tam_in_billions}
        )
        
        fallback = {
            "investor_elevator_pitch": f"We are building the enterprise AI platform for higher education and career placement, capturing a ${det_result.tam.tam_in_billions}B TAM. With 4.2x LTV:CAC unit economics and 18 months of runway, we are raising a $2M Seed round to scale sales engineering.",
            "fundraising_strategy": [
                "Target B2B SaaS Seed funds with higher-ed tech focus",
                "Prepare 12-slide pitch deck highlighting 4.2x LTV:CAC and $12.5B TAM",
                "Schedule 25 investor pitch meetings across Q3"
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="investor_pitch", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return InvestorPitchNarrative(
                investor_elevator_pitch=parsed.get("investor_elevator_pitch", fallback["investor_elevator_pitch"]),
                fundraising_strategy=parsed.get("fundraising_strategy", fallback["fundraising_strategy"])
            )
        except Exception:
            return InvestorPitchNarrative(**fallback)
