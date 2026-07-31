from typing import Dict, Any, List, Optional
from app.agents.base_agent import BaseAgent
from departments.skill_gap_intelligence.deterministic import SkillGapScorerAgent
from departments.skill_gap_intelligence.reasoning import SkillGapQualitativeAuditorAgent, LearningRoadmapStrategistAgent
from departments.skill_gap_intelligence.schemas import (
    SkillGapOrchestratorReport, ReasoningSkillGapPipelineResult
)

class SkillGapOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator Agent for the Skill Gap Intelligence Department."""
    def __init__(self):
        super().__init__(
            agent_id="skill_gap_orchestrator",
            name="Skill Gap Intelligence Master Orchestrator",
            description="Coordinates all 9 sub-agents to deliver a unified Skill Gap Report.",
            icon="Layers"
        )
        self.gap_scorer = SkillGapScorerAgent()
        self.qual_auditor = SkillGapQualitativeAuditorAgent()
        self.roadmap_strategist = LearningRoadmapStrategistAgent()

    async def run_pipeline(
        self,
        candidate_skills: List[str],
        required_skills: Optional[List[str]] = None,
        target_role: str = "Software Engineer"
    ) -> SkillGapOrchestratorReport:
        reasoning_steps = []
        
        # Step 1: Execute Deterministic Pipeline
        reasoning_steps.append("Step 1: Running deterministic Skill Gap pipeline (Skill inventory audit, Missing matrix calculation, Skill priority ranking, Course recommendation mapping, Timeline estimation, Mastery scoring).")
        det_result = self.gap_scorer.run(candidate_skills, required_skills)
        
        # Step 2: Execute Qualitative Auditor Agent
        reasoning_steps.append("Step 2: Executing Skill Gap Qualitative Auditor Agent to analyze readiness index and competitive edge.")
        qual_report = await self.qual_auditor.evaluate(target_role, det_result)
        
        # Step 3: Execute Learning Roadmap Strategist Agent
        reasoning_steps.append("Step 3: Executing Learning Roadmap Strategist Agent to formulate weekly learning paths and portfolio project ideas.")
        roadmap_strategy = await self.roadmap_strategist.strategize(target_role, det_result)
        
        # Step 4: Synthesize Report
        reasoning_steps.append("Step 4: Compiling Skill Gap Intelligence Report.")
        reasoning_result = ReasoningSkillGapPipelineResult(
            qualitative_report=qual_report,
            roadmap_strategy=roadmap_strategy,
            reasoning_steps=reasoning_steps
        )
        
        return SkillGapOrchestratorReport(
            target_role=target_role,
            readiness_index=det_result.mastery_score.readiness_index,
            confidence_score=det_result.confidence_score,
            deterministic_analysis=det_result,
            reasoning_analysis=reasoning_result,
            reasoning_steps=reasoning_steps
        )
