from typing import Dict, Any, List, Optional
from app.agents.base_agent import BaseAgent
from departments.interview_intelligence.deterministic import InterviewScorerAgent
from departments.interview_intelligence.reasoning import STARResponseCoachAgent, MockSimulationStrategistAgent
from departments.interview_intelligence.schemas import (
    InterviewOrchestratorReport, ReasoningInterviewPipelineResult
)

class InterviewOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator Agent for the Interview Intelligence Department."""
    def __init__(self):
        super().__init__(
            agent_id="interview_orchestrator",
            name="Interview Intelligence Master Orchestrator",
            description="Coordinates all 9 sub-agents to deliver a unified Interview Preparation Kit.",
            icon="HelpCircle"
        )
        self.scorer = InterviewScorerAgent()
        self.star_coach = STARResponseCoachAgent()
        self.simulation_strategist = MockSimulationStrategistAgent()

    async def run_pipeline(
        self,
        tech_stack: List[str],
        target_role: str = "Software Engineer",
        target_company: str = "TechCorp",
        seniority: str = "Senior"
    ) -> InterviewOrchestratorReport:
        reasoning_steps = []
        
        # Step 1: Execute Deterministic Pipeline
        reasoning_steps.append("Step 1: Running deterministic Interview Intelligence pipeline (Tech question generation, Behavioral STAR generation, System design prompts, Difficulty mapping, Rubric criteria building, Duration calculation).")
        det_result = self.scorer.run(tech_stack, target_role, seniority)
        
        # Step 2: Execute STAR Response Coach Agent
        reasoning_steps.append("Step 2: Executing STAR Response Coach Agent to formulate high-impact behavioral answer frameworks.")
        star_guide = await self.star_coach.coach(target_role, det_result)
        
        # Step 3: Execute Mock Simulation Strategist Agent
        reasoning_steps.append("Step 3: Executing Mock Simulation Strategist Agent to design timed mock interview sessions and pitfall avoidance plans.")
        simulation_strategy = await self.simulation_strategist.plan(target_role, det_result)
        
        # Step 4: Synthesize Report
        reasoning_steps.append("Step 4: Compiling Interview Intelligence Master Report.")
        reasoning_result = ReasoningInterviewPipelineResult(
            star_guide=star_guide,
            simulation_strategy=simulation_strategy,
            reasoning_steps=reasoning_steps
        )
        
        return InterviewOrchestratorReport(
            target_role=target_role,
            target_company=target_company,
            confidence_score=det_result.confidence_score,
            deterministic_analysis=det_result,
            reasoning_analysis=reasoning_result,
            reasoning_steps=reasoning_steps
        )
