from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.learning_course_intelligence.schemas import (
    StrategicLearningNarrative, CurriculumOptimizationPlan, ReasoningLearningPipelineResult, DeterministicLearningPipelineResult
)

class StrategicLearningNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates learning platform quality, course completion dynamics, and skill acquisition."""
    def __init__(self):
        super().__init__(agent_id="strategic_learning_narrative", name="Strategic Learning Narrative Agent",
                         description="Evaluates course completion, skill gains, course ratings, and adaptive learning paths.", icon="BookOpen")

    async def evaluate(self, det: DeterministicLearningPipelineResult) -> StrategicLearningNarrative:
        fallback = {
            "learning_summary": f"High impact learning platform ({det.learning_quality_score:.1f}% score). {det.completion.course_completion_rate_pct}% completion rate, {det.feedback.avg_course_rating}/5.0 avg rating across {det.catalog.total_courses_count} courses.",
            "key_learning_strengths": [f"{det.skill_gain.pre_post_assessment_gain_pct}% pre/post skill gain with {det.skill_gain.assessment_pass_rate_pct}% assessment pass rate", f"{det.adaptive.path_personalization_accuracy_pct}% adaptive learning path accuracy with {det.catalog.interactive_labs_count} hands-on labs"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Chief Learning Officer", "curriculum design, skill assessment, edtech, adaptive learning"),
                                          PromptBuilder.build_user_context({"score": det.learning_quality_score}), task_type="learning_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicLearningNarrative(learning_summary=parsed.get("learning_summary", fallback["learning_summary"]),
                                             key_learning_strengths=parsed.get("key_learning_strengths", fallback["key_learning_strengths"]))
        except Exception:
            return StrategicLearningNarrative(**fallback)

class CurriculumOptimizationPlannerAgent(BaseAgent):
    """Agent 9: Formulates course catalog expansion plans and adaptive curriculum JSON schemas."""
    def __init__(self):
        super().__init__(agent_id="curriculum_optimization_planner", name="Curriculum Optimization Planner Agent",
                         description="Formulates curriculum gap closures, interactive lab additions, and adaptive learning paths.", icon="Award")

    async def plan_curriculum(self, det: DeterministicLearningPipelineResult) -> CurriculumOptimizationPlan:
        fallback = {
            "course_improvement_actions": ["Add 10 new hands-on Generative AI & Prompt Engineering interactive labs", "Implement micro-learning video chunking (3-5 min modules) to boost completion rate beyond 72%"],
            "sample_learning_path_schema": '{\n  "path_id": "fullstack_ai_developer",\n  "title": "Full-Stack AI Engineer Path",\n  "total_hours": 45,\n  "courses": [\n    {"course_id": "py_01", "title": "Python for AI", "duration_hrs": 10},\n    {"course_id": "fastapi_01", "title": "FastAPI Masterclass", "duration_hrs": 12},\n    {"course_id": "llm_01", "title": "Building RAG Applications", "duration_hrs": 23}\n  ],\n  "adaptive_rule": "Skip py_01 if user score > 85% on diagnostic quiz"\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Instructional Designer", "learning paths, interactive labs, micro-learning"),
                                          PromptBuilder.build_user_context({"courses": det.catalog.total_courses_count}), task_type="learning_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return CurriculumOptimizationPlan(course_improvement_actions=parsed.get("course_improvement_actions", fallback["course_improvement_actions"]),
                                              sample_learning_path_schema=parsed.get("sample_learning_path_schema", fallback["sample_learning_path_schema"]))
        except Exception:
            return CurriculumOptimizationPlan(**fallback)
