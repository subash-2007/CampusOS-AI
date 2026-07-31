from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.peer_benchmarking.schemas import (
    StrategicPeerNarrative, PeerOutperformanceStrategy, ReasoningPeerPipelineResult, DeterministicPeerPipelineResult
)

class StrategicPeerNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates qualitative peer competitiveness and competitive differentiation."""
    def __init__(self):
        super().__init__(
            agent_id="strategic_peer_narrative",
            name="Strategic Peer Narrative Agent",
            description="Evaluates competitive positioning against peer cohorts and candidate differentiators.",
            icon="Users"
        )

    async def evaluate(self, det_result: DeterministicPeerPipelineResult) -> StrategicPeerNarrative:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Executive Talent Strategist & Peer Benchmark Analyst",
            domain_focus="Competitive cohort benchmarking, peer differentiation, and talent positioning."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"percentile": det_result.percentile.overall_percentile, "cohort_tier": det_result.percentile.cohort_tier}
        )
        
        fallback = {
            "competitive_positioning_summary": f"Candidate ranks in the {det_result.percentile.cohort_tier} ({det_result.percentile.overall_percentile}th percentile) relative to engineering peers.",
            "key_differentiators": [
                f"Top 10% GitHub contribution activity ({det_result.open_source.github_contributions_percentile}th percentile)",
                f"Higher skill density ({det_result.skills.skill_count_vs_peer_median}x peer median)"
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="peer_eval", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicPeerNarrative(
                competitive_positioning_summary=parsed.get("competitive_positioning_summary", fallback["competitive_positioning_summary"]),
                key_differentiators=parsed.get("key_differentiators", fallback["key_differentiators"])
            )
        except Exception:
            return StrategicPeerNarrative(**fallback)

class PeerOutperformanceStrategistAgent(BaseAgent):
    """Agent 9: Formulates strategies to outperform peer cohorts and secure top 5% positioning."""
    def __init__(self):
        super().__init__(
            agent_id="peer_outperformance_strategist",
            name="Peer Outperformance Strategist Agent",
            description="Formulates actionable strategies to outperform peer cohorts and maximize offer rates.",
            icon="Award"
        )

    async def strategize(self, det_result: DeterministicPeerPipelineResult) -> PeerOutperformanceStrategy:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Chief Career Strategist",
            domain_focus="Peer outperformance, competitive advantage leverage, and career growth velocity."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"composite_score": det_result.composite_benchmark_score}
        )
        
        fallback = {
            "recommended_leverage_points": [
                "Leverage top 10% open-source contributions in technical interview narratives",
                "Highlight high skill acquisition velocity to demonstrate senior readiness"
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="peer_strategy", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return PeerOutperformanceStrategy(
                recommended_leverage_points=parsed.get("recommended_leverage_points", fallback["recommended_leverage_points"])
            )
        except Exception:
            return PeerOutperformanceStrategy(**fallback)
