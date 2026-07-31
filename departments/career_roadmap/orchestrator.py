from typing import Dict, Any, List, Optional
from app.agents.base_agent import BaseAgent
from departments.career_roadmap.deterministic import RoadmapScorerAgent
from departments.career_roadmap.reasoning import StrategicCareerAdvisorAgent, LongTermVisionStrategistAgent
from departments.career_roadmap.schemas import (
    RoadmapOrchestratorReport, ReasoningRoadmapPipelineResult
)

class RoadmapOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator Agent for the Career Roadmap Department."""
    def __init__(self):
        super().__init__(
            agent_id="roadmap_orchestrator",
            name="Career Roadmap Master Orchestrator",
            description="Coordinates all 9 sub-agents to deliver a unified 30-60-90 Day Career Execution Plan.",
            icon="MapPin"
        )
        self.scorer = RoadmapScorerAgent()
        self.advisor = StrategicCareerAdvisorAgent()
        self.vision_strategist = LongTermVisionStrategistAgent()

    async def run_pipeline(
        self,
        target_role: str = "Senior Software Engineer",
        current_salary: int = 100000,
        target_salary: int = 150000,
        timeframe_months: int = 3
    ) -> RoadmapOrchestratorReport:
        reasoning_steps = []
        
        # Step 1: Execute Deterministic Pipeline
        reasoning_steps.append("Step 1: Running deterministic Career Roadmap pipeline (30-60-90 milestone generation, Salary trajectory calculation, Role progression mapping, Weekly task planning, Risk mitigation analysis, Feasibility scoring).")
        det_result = self.scorer.run(target_role, current_salary, target_salary)
        
        # Step 2: Execute Strategic Advisor Agent
        reasoning_steps.append("Step 2: Executing Strategic Career Advisor Agent to formulate executive narratives and networking tactics.")
        advice = await self.advisor.advise(target_role, det_result)
        
        # Step 3: Execute Long-Term Vision Strategist Agent
        reasoning_steps.append("Step 3: Executing Long-Term Vision Strategist Agent to project 5-year career progression and strategic pivots.")
        vision = await self.vision_strategist.project_vision(target_role, det_result)
        
        # Step 4: Synthesize Report
        reasoning_steps.append("Step 4: Compiling Career Roadmap Master Execution Report.")
        reasoning_result = ReasoningRoadmapPipelineResult(
            career_advice=advice,
            long_term_vision=vision,
            reasoning_steps=reasoning_steps
        )
        
        return RoadmapOrchestratorReport(
            target_role=target_role,
            timeframe_months=timeframe_months,
            confidence_score=det_result.confidence_score,
            deterministic_analysis=det_result,
            reasoning_analysis=reasoning_result,
            reasoning_steps=reasoning_steps
        )
