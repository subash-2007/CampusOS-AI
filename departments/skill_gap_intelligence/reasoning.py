from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.skill_gap_intelligence.schemas import (
    QualitativeSkillReport, LearningRoadmapStrategy, ReasoningSkillGapPipelineResult, DeterministicSkillGapPipelineResult
)

class SkillGapQualitativeAuditorAgent(BaseAgent):
    """Agent 8: Evaluates qualitative candidate readiness and competitive edge."""
    def __init__(self):
        super().__init__(
            agent_id="skill_gap_qualitative_auditor",
            name="Skill Gap Qualitative Auditor Agent",
            description="Evaluates technical readiness index, market competitiveness, and skill gaps.",
            icon="Brain"
        )

    async def evaluate(self, target_role: str, det_result: DeterministicSkillGapPipelineResult) -> QualitativeSkillReport:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Principal Technical Career Coach",
            domain_focus="Skill gap analysis and market readiness assessment."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"target_role": target_role, "readiness_index": det_result.mastery_score.readiness_index},
            extra_context=f"Critical missing skills: {', '.join(det_result.gap_matrix.critical_missing_skills)}"
        )
        
        fallback = {
            "readiness_summary": f"Candidate holds a {det_result.mastery_score.readiness_index}% readiness index for {target_role}.",
            "competitive_edge_analysis": f"Strong baseline in {', '.join(det_result.candidate_skills.mastered_hard_skills[:3])}."
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="skill_gap_eval", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return QualitativeSkillReport(
                readiness_summary=parsed.get("readiness_summary", fallback["readiness_summary"]),
                competitive_edge_analysis=parsed.get("competitive_edge_analysis", fallback["competitive_edge_analysis"])
            )
        except Exception:
            return QualitativeSkillReport(**fallback)

class LearningRoadmapStrategistAgent(BaseAgent):
    """Agent 9: Formulates structured learning roadmap and portfolio project ideas."""
    def __init__(self):
        super().__init__(
            agent_id="learning_roadmap_strategist",
            name="Learning Roadmap Strategist Agent",
            description="Formulates milestone learning paths and hands-on project ideas.",
            icon="Map"
        )

    async def strategize(self, target_role: str, det_result: DeterministicSkillGapPipelineResult) -> LearningRoadmapStrategy:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Senior Curriculum Architect",
            domain_focus="Personalized learning paths and portfolio project design."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"critical_missing_skills": det_result.gap_matrix.critical_missing_skills}
        )
        
        fallback = {
            "learning_path": [
                f"Week 1-2: Master core concepts in {s}" for s in det_result.gap_matrix.critical_missing_skills[:2]
            ],
            "project_ideas": [
                f"Build an end-to-end full-stack application leveraging {', '.join(det_result.gap_matrix.critical_missing_skills[:2])}"
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="learning_roadmap", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return LearningRoadmapStrategy(
                learning_path=parsed.get("learning_path", fallback["learning_path"]),
                project_ideas=parsed.get("project_ideas", fallback["project_ideas"])
            )
        except Exception:
            return LearningRoadmapStrategy(**fallback)
