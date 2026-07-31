from typing import Dict, Any, List, Optional
from app.agents.base_agent import BaseAgent
from departments.mentorship_intelligence.deterministic import MentorshipScorerAgent
from departments.mentorship_intelligence.reasoning import QualitativeMentorshipNarrativeAgent, SessionAgendaPlannerAgent
from departments.mentorship_intelligence.schemas import (
    MentorshipOrchestratorReport, ReasoningMentorshipPipelineResult
)

class MentorshipOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator Agent for the Mentorship Intelligence Department."""
    def __init__(self):
        super().__init__(
            agent_id="mentorship_orchestrator",
            name="Mentorship Intelligence Master Orchestrator",
            description="Coordinates all 9 sub-agents to deliver a unified Mentorship Matching Report.",
            icon="UserPlus"
        )
        self.scorer = MentorshipScorerAgent()
        self.narrative_agent = QualitativeMentorshipNarrativeAgent()
        self.agenda_planner = SessionAgendaPlannerAgent()

    async def run_pipeline(
        self,
        target_role: str = "Software Engineer",
        skills: Optional[List[str]] = None
    ) -> MentorshipOrchestratorReport:
        reasoning_steps = []
        
        # Step 1: Execute Deterministic Pipeline
        reasoning_steps.append("Step 1: Running deterministic Mentorship Intelligence pipeline (Mentor profile matching, Session cadence planning, Expertise overlap measurement, Goal alignment scoring, Availability evaluation, Feedback loop auditing).")
        det_result = self.scorer.run(target_role, skills)
        
        # Step 2: Execute Qualitative Mentorship Narrative Agent
        reasoning_steps.append("Step 2: Executing Qualitative Mentorship Narrative Agent to evaluate mentor pairing strategy.")
        narrative = await self.narrative_agent.evaluate(det_result)
        
        # Step 3: Execute Session Agenda Planner Agent
        reasoning_steps.append("Step 3: Executing Session Agenda Planner Agent to build structured 1-on-1 session agendas.")
        agendas = await self.agenda_planner.plan_agendas(det_result)
        
        # Step 4: Synthesize Report
        reasoning_steps.append("Step 4: Compiling Mentorship Intelligence Master Report.")
        reasoning_result = ReasoningMentorshipPipelineResult(
            narrative=narrative,
            agenda_plan=agendas,
            reasoning_steps=reasoning_steps
        )
        
        tier = "HIGH COMPATIBILITY" if det_result.mentorship_fit_score >= 80 else "MODERATE COMPATIBILITY"
        
        return MentorshipOrchestratorReport(
            mentorship_fit_tier=tier,
            mentorship_fit_score=det_result.mentorship_fit_score,
            confidence_score=det_result.confidence_score,
            deterministic_analysis=det_result,
            reasoning_analysis=reasoning_result,
            reasoning_steps=reasoning_steps
        )
