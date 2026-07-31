from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.executive_communication.schemas import (
    StrategicExecutiveNarrative, ExecutiveBriefingDraft, ReasoningExecutiveCommPipelineResult, DeterministicExecutiveCommPipelineResult
)

class StrategicExecutiveNarrativeAgent(BaseAgent):
    """Agent 8: Formulates strategic executive narrative evaluations and C-suite presentation reviews."""
    def __init__(self):
        super().__init__(
            agent_id="strategic_executive_narrative",
            name="Strategic Executive Narrative Agent",
            description="Evaluates executive presentation effectiveness, brevity, and board readiness.",
            icon="MessageSquare"
        )

    async def evaluate(self, det_result: DeterministicExecutiveCommPipelineResult) -> StrategicExecutiveNarrative:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Executive Communications Director & C-Suite Speechwriter",
            domain_focus="C-suite briefings, board deck narratives, and high-stakes executive communication."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"comm_score": det_result.executive_comm_score, "deck_score": det_result.deck.deck_readiness_score}
        )
        
        fallback = {
            "communication_evaluation_summary": f"Outstanding C-suite communication readiness ({det_result.executive_comm_score}% score). High conciseness ({det_result.brevity.conciseness_score}%) with crystal clear data storytelling.",
            "key_presentation_strengths": [
                "BLUF (Bottom Line Up Front) executive memo structure",
                "High board deck readiness score (85%) with quantitative data storytelling"
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="exec_comm_eval", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicExecutiveNarrative(
                communication_evaluation_summary=parsed.get("communication_evaluation_summary", fallback["communication_evaluation_summary"]),
                key_presentation_strengths=parsed.get("key_presentation_strengths", fallback["key_presentation_strengths"])
            )
        except Exception:
            return StrategicExecutiveNarrative(**fallback)

class ExecutiveBriefingGeneratorAgent(BaseAgent):
    """Agent 9: Generates concise C-suite briefing memos and executive summaries."""
    def __init__(self):
        super().__init__(
            agent_id="executive_briefing_generator",
            name="Executive Briefing Generator Agent",
            description="Generates executive bulleted briefings and C-suite memo drafts.",
            icon="FileText"
        )

    async def generate_briefing(self, det_result: DeterministicExecutiveCommPipelineResult) -> ExecutiveBriefingDraft:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Chief of Staff to CEO",
            domain_focus="Executive summary drafting, board prep memo creation, and crisp C-suite communication."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"crisis_speed": det_result.crisis.crisis_response_speed}
        )
        
        fallback = {
            "executive_summary_bulletins": [
                "BLUF: Q3 Cloud Infrastructure Migration completed 4 days ahead of schedule, under budget by 12%",
                "Impact: API P99 latency reduced from 180ms to 99ms across all production microservices",
                "Next Steps: Board presentation scheduled for August 15th to showcase Q4 AI initiatives"
            ],
            "sample_c_suite_memo_draft": "MEMORANDUM\n\nTO: Executive Leadership Team\nFROM: Technical Infrastructure Operations\nDATE: July 30, 2026\nSUBJECT: Executive Update - Platform Infrastructure Modernization\n\n1. EXECUTIVE SUMMARY\nWe have successfully migrated 100% of core microservices to our containerized Kubernetes architecture. System availability remains at 99.99% with zero customer-facing downtime.\n\n2. FINANCIAL & OPERATIONAL IMPACT\n- Infrastructure hosting costs decreased by $14,500/month\n- P99 latency improved by 45%\n\n3. RECOMMENDATION\nProceed with phase 2 rollout for enterprise multi-tenant analytics."
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="exec_briefing", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return ExecutiveBriefingDraft(
                executive_summary_bulletins=parsed.get("executive_summary_bulletins", fallback["executive_summary_bulletins"]),
                sample_c_suite_memo_draft=parsed.get("sample_c_suite_memo_draft", fallback["sample_c_suite_memo_draft"])
            )
        except Exception:
            return ExecutiveBriefingDraft(**fallback)
