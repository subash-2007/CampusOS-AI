from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.mentorship_intelligence.schemas import (
    QualitativeMentorshipNarrative, SessionAgendaPlan, ReasoningMentorshipPipelineResult, DeterministicMentorshipPipelineResult
)

class QualitativeMentorshipNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates mentorship compatibility narratives and mentor-mentee pairing strategy."""
    def __init__(self):
        super().__init__(
            agent_id="qualitative_mentorship_narrative",
            name="Qualitative Mentorship Narrative Agent",
            description="Evaluates mentorship compatibility narratives and recommended mentor pairings.",
            icon="UserCheck"
        )

    async def evaluate(self, det_result: DeterministicMentorshipPipelineResult) -> QualitativeMentorshipNarrative:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Lead Mentorship Program Director & Executive Coach",
            domain_focus="Mentorship matching, career growth coaching, and executive pairing strategy."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"fit_score": det_result.mentorship_fit_score, "matched_count": det_result.matches.matched_mentors_count}
        )
        
        fallback = {
            "mentorship_strategy_summary": f"High compatibility ({det_result.mentorship_fit_score}% fit score) across {det_result.matches.matched_mentors_count} available senior mentor profiles.",
            "key_mentor_pairings": [
                "Principal Systems Architect at Tier-1 Tech Company (Focus: High-concurrency system design)",
                "Director of Engineering (Focus: Technical leadership & promotion strategy)"
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="mentorship_eval", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return QualitativeMentorshipNarrative(
                mentorship_strategy_summary=parsed.get("mentorship_strategy_summary", fallback["mentorship_strategy_summary"]),
                key_mentor_pairings=parsed.get("key_mentor_pairings", fallback["key_mentor_pairings"])
            )
        except Exception:
            return QualitativeMentorshipNarrative(**fallback)

class SessionAgendaPlannerAgent(BaseAgent):
    """Agent 9: Generates structured 1-on-1 mentorship session agendas and growth milestones."""
    def __init__(self):
        super().__init__(
            agent_id="session_agenda_planner",
            name="Session Agenda Planner Agent",
            description="Formulates structured 1-on-1 mentorship agendas and milestone tracking plans.",
            icon="Calendar"
        )

    async def plan_agendas(self, det_result: DeterministicMentorshipPipelineResult) -> SessionAgendaPlan:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Executive 1-on-1 Facilitator",
            domain_focus="Mentorship meeting agenda design, milestone setting, and accountability tracking."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"cadence": det_result.cadence.recommended_cadence}
        )
        
        fallback = {
            "suggested_session_agendas": [
                "Session 1: Align on 90-day career roadmap & technical skill gaps",
                "Session 2: Architecture review of candidate's microservices portfolio project",
                "Session 3: Mock System Design interview simulation & feedback",
                "Session 4: Executive visibility & promotion readiness audit"
            ],
            "growth_milestones": [
                "Complete 1 System Design architectural mock interview by Month 2",
                "Achieve Senior Engineer benchmark proficiency in cloud architecture"
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="agenda_plan", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return SessionAgendaPlan(
                suggested_session_agendas=parsed.get("suggested_session_agendas", fallback["suggested_session_agendas"]),
                growth_milestones=parsed.get("growth_milestones", fallback["growth_milestones"])
            )
        except Exception:
            return SessionAgendaPlan(**fallback)
