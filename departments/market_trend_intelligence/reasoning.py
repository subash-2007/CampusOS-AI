from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.market_trend_intelligence.schemas import (
    StrategicMarketNarrative, TechHedgingStrategy, ReasoningMarketPipelineResult, DeterministicMarketPipelineResult
)

class MarketNarrativeEvaluatorAgent(BaseAgent):
    """Agent 8: Evaluates qualitative hiring trends and market outlook narratives."""
    def __init__(self):
        super().__init__(
            agent_id="market_narrative_evaluator",
            name="Market Narrative Evaluator Agent",
            description="Evaluates industry hiring outlook narratives and macro economic market trends.",
            icon="TrendingUp"
        )

    async def evaluate(self, target_domain: str, det_result: DeterministicMarketPipelineResult) -> StrategicMarketNarrative:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Principal Tech Industry Analyst & Economist",
            domain_focus="Macro tech hiring trends and compensation benchmarking."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"target_domain": target_domain, "demand_tier": det_result.hiring_demand.demand_tier}
        )
        
        fallback = {
            "market_outlook_summary": f"The hiring outlook for {target_domain} remains {det_result.hiring_demand.demand_tier} with strong growth in distributed systems and AI infrastructure.",
            "key_opportunities": [
                "High demand for cloud-native microservices architecture",
                "Significant compensation premium for Rust & Kubernetes skills"
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="market_eval", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicMarketNarrative(
                market_outlook_summary=parsed.get("market_outlook_summary", fallback["market_outlook_summary"]),
                key_opportunities=parsed.get("key_opportunities", fallback["key_opportunities"])
            )
        except Exception:
            return StrategicMarketNarrative(**fallback)

class TechHedgingStrategistAgent(BaseAgent):
    """Agent 9: Formulates technology skill hedging and future-proofing strategies."""
    def __init__(self):
        super().__init__(
            agent_id="tech_hedging_strategist",
            name="Tech Hedging Strategist Agent",
            description="Formulates skill future-proofing strategies against technological obsolescence.",
            icon="ShieldCheck"
        )

    async def strategize(self, det_result: DeterministicMarketPipelineResult) -> TechHedgingStrategy:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Chief Technology Advisor",
            domain_focus="Skill future-proofing and technology hedging strategies."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"declining_tech": det_result.trending_tech.declining_technologies}
        )
        
        fallback = {
            "recommended_futureproof_skills": det_result.trending_tech.top_rising_technologies
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="tech_hedging", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return TechHedgingStrategy(
                recommended_futureproof_skills=parsed.get("recommended_futureproof_skills", fallback["recommended_futureproof_skills"])
            )
        except Exception:
            return TechHedgingStrategy(**fallback)
