from typing import Dict, Any, List, Optional
from app.agents.base_agent import BaseAgent
from departments.leadership_management_intelligence.deterministic import LeadershipScorerAgent
from departments.leadership_management_intelligence.reasoning import StrategicLeadershipNarrativeAgent, ExecutiveCoachingPlannerAgent
from departments.leadership_management_intelligence.schemas import (
    LeadershipManagementOrchestratorReport, ReasoningLeadershipPipelineResult
)

class LeadershipManagementOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator Agent for the Leadership & Management Intelligence Department."""
    def __init__(self):
        super().__init__(
            agent_id="leadership_management_orchestrator",
            name="Leadership & Management Intelligence Master Orchestrator",
            description="Coordinates all 9 sub-agents to deliver a unified Leadership & Management Report.",
            icon="Shield"
        )
        self.scorer = LeadershipScorerAgent()
        self.narrative_agent = StrategicLeadershipNarrativeAgent()
        self.coaching_planner = ExecutiveCoachingPlannerAgent()

    async def run_pipeline(self, team_size: int = 12) -> LeadershipManagementOrchestratorReport:
        reasoning_steps = []
        
        # Step 1: Execute Deterministic Pipeline
        reasoning_steps.append("Step 1: Running deterministic Leadership & Management Intelligence pipeline (Team size capacity metering, Leadership style analysis, Conflict resolution scoring, Strategic vision evaluation, Cross-functional influence auditing, Retention performance metrics).")
        det_result = self.scorer.run(team_size)
        
        # Step 2: Execute Strategic Leadership Narrative Agent
        reasoning_steps.append("Step 2: Executing Strategic Leadership Narrative Agent to analyze executive strengths.")
        narrative = await self.narrative_agent.evaluate(det_result)
        
        # Step 3: Execute Executive Coaching Planner Agent
        reasoning_steps.append("Step 3: Executing Executive Coaching Planner Agent to produce leadership action items.")
        coaching = await self.coaching_planner.plan_coaching(det_result)
        
        # Step 4: Synthesize Report
        reasoning_steps.append("Step 4: Compiling Leadership & Management Intelligence Master Report.")
        reasoning_result = ReasoningLeadershipPipelineResult(
            narrative=narrative,
            coaching_plan=coaching,
            reasoning_steps=reasoning_steps
        )
        
        tier = "EXECUTIVE READY" if det_result.leadership_readiness_score >= 85 else "EMERGING LEADER"
        
        return LeadershipManagementOrchestratorReport(
            leadership_tier=tier,
            leadership_readiness_score=det_result.leadership_readiness_score,
            confidence_score=det_result.confidence_score,
            deterministic_analysis=det_result,
            reasoning_analysis=reasoning_result,
            reasoning_steps=reasoning_steps
        )
