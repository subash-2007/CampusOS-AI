from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.offer_salary_negotiation.schemas import (
    StrategicNegotiationNarrative, CounterOfferScript, ReasoningOfferPipelineResult, DeterministicOfferPipelineResult
)

class StrategicNegotiationNarrativeAgent(BaseAgent):
    """Agent 8: Formulates strategic negotiation positioning and target counter-offer TC."""
    def __init__(self):
        super().__init__(
            agent_id="strategic_negotiation_narrative",
            name="Strategic Negotiation Narrative Agent",
            description="Evaluates compensation package competitive gaps and target counter-offer positioning.",
            icon="DollarSign"
        )

    async def evaluate(self, det_result: DeterministicOfferPipelineResult) -> StrategicNegotiationNarrative:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Executive Compensation Advisor & Negotiation Strategist",
            domain_focus="Total compensation modeling, negotiation strategy, and counter-offer targets."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"year_1_tc": det_result.total_comp.year_1_total_compensation, "market_median_tc": det_result.total_comp.market_median_tc}
        )
        
        target_tc = int(det_result.total_comp.year_1_total_compensation * (1.0 + (det_result.negotiation_upside_percentage / 100.0)))
        fallback = {
            "negotiation_positioning_summary": f"Current offer (${det_result.total_comp.year_1_total_compensation:,}) sits below market median (${det_result.total_comp.market_median_tc:,}). Candidate possesses strong leverage with {det_result.leverage.competing_offers_count} competing offers.",
            "target_counter_offer_tc": target_tc
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="negotiation_narrative", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicNegotiationNarrative(
                negotiation_positioning_summary=parsed.get("negotiation_positioning_summary", fallback["negotiation_positioning_summary"]),
                target_counter_offer_tc=parsed.get("target_counter_offer_tc", fallback["target_counter_offer_tc"])
            )
        except Exception:
            return StrategicNegotiationNarrative(**fallback)

class CounterOfferScriptGeneratorAgent(BaseAgent):
    """Agent 9: Generates professional counter-offer email scripts and verbal talking points."""
    def __init__(self):
        super().__init__(
            agent_id="counter_offer_script_generator",
            name="Counter Offer Script Generator Agent",
            description="Generates executive counter-offer email scripts and verbal negotiation talking points.",
            icon="FileText"
        )

    async def generate_script(self, det_result: DeterministicOfferPipelineResult) -> CounterOfferScript:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Executive Negotiation Coach",
            domain_focus="High-leverage counter-offer script generation and verbal negotiation coaching."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"leverage_score": det_result.leverage.leverage_score}
        )
        
        fallback = {
            "counter_offer_email_draft": "Dear Hiring Manager,\n\nThank you for extending the offer to join the team. I am thrilled about the prospect of contributing to your key initiatives. Based on my competing offers and market benchmarks for this role, I would like to explore whether we can adjust the base salary to $165,000 to align with market standards.\n\nBest regards,\nCandidate",
            "negotiation_talking_points": [
                "Anchor counter-offer on market median base salary ($165,000)",
                "Frame counter-offer politely around competing offer timelines"
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="counter_script", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return CounterOfferScript(
                counter_offer_email_draft=parsed.get("counter_offer_email_draft", fallback["counter_offer_email_draft"]),
                negotiation_talking_points=parsed.get("negotiation_talking_points", fallback["negotiation_talking_points"])
            )
        except Exception:
            return CounterOfferScript(**fallback)
