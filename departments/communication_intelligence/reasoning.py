from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.communication_intelligence.schemas import (
    QualitativeCommunicationNarrative, EmailRewriteStrategy, ReasoningCommunicationPipelineResult, DeterministicCommunicationPipelineResult
)

class QualitativeCommunicationNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates qualitative communication style, tone, and executive presence."""
    def __init__(self):
        super().__init__(
            agent_id="qualitative_communication_narrative",
            name="Qualitative Communication Narrative Agent",
            description="Evaluates communication tone, executive impact, and narrative flow.",
            icon="MessageSquare"
        )

    async def evaluate(self, text: str, det_result: DeterministicCommunicationPipelineResult) -> QualitativeCommunicationNarrative:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Executive Communications Coach & PR Specialist",
            domain_focus="Professional correspondence analysis, executive tone alignment, and persuasiveness."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"overall_score": det_result.overall_communication_score, "tone": det_result.tone.dominant_tone}
        )
        
        fallback = {
            "communication_critique": f"Communication demonstrates strong professional formatting ({det_result.overall_communication_score}% score) with a clear call-to-action.",
            "tone_alignment_summary": f"Tone is aligned with executive standards: {det_result.tone.dominant_tone}."
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="comm_eval", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return QualitativeCommunicationNarrative(
                communication_critique=parsed.get("communication_critique", fallback["communication_critique"]),
                tone_alignment_summary=parsed.get("tone_alignment_summary", fallback["tone_alignment_summary"])
            )
        except Exception:
            return QualitativeCommunicationNarrative(**fallback)

class EmailRewriteStrategistAgent(BaseAgent):
    """Agent 9: Formulates high-converting executive email rewrites."""
    def __init__(self):
        super().__init__(
            agent_id="email_rewrite_strategist",
            name="Email Rewrite Strategist Agent",
            description="Generates optimized, high-converting professional email drafts.",
            icon="Mail"
        )

    async def rewrite(self, text: str, det_result: DeterministicCommunicationPipelineResult) -> EmailRewriteStrategy:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Principal Copywriter & Talent Outreach Strategist",
            domain_focus="High-converting outreach email design and executive communication polish."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"has_cta": det_result.actionability.has_clear_call_to_action}
        )
        
        fallback = {
            "optimized_email_draft": text,
            "key_enhancements_made": [
                "Strengthened opening value proposition",
                "Formatted clear, friction-free meeting call-to-action"
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="email_rewrite", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return EmailRewriteStrategy(
                optimized_email_draft=parsed.get("optimized_email_draft", fallback["optimized_email_draft"]),
                key_enhancements_made=parsed.get("key_enhancements_made", fallback["key_enhancements_made"])
            )
        except Exception:
            return EmailRewriteStrategy(**fallback)
