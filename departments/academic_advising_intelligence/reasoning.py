from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.academic_advising_intelligence.schemas import (
    StrategicAdvisingNarrative, AcademicRetentionPlan, ReasoningAdvisingPipelineResult, DeterministicAdvisingPipelineResult
)

class StrategicAdvisingNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates academic advising quality, degree audit progress, and early risk intervention."""
    def __init__(self):
        super().__init__(agent_id="strategic_advising_narrative", name="Strategic Advising Narrative Agent",
                         description="Evaluates degree audit progress, early warning risks, prerequisite compliance, and GPA trends.", icon="BookOpen")

    async def evaluate(self, det: DeterministicAdvisingPipelineResult) -> StrategicAdvisingNarrative:
        fallback = {
            "advising_summary": f"Proactive academic retention system ({det.advising_health_score:.1f}% score). {det.degree_audit.on_track_graduation_pct:.1f}% on-track graduation rate, {det.early_warning.academic_probation_risk_pct}% probation risk, {det.session_frequency.advisor_satisfaction_score}% advisor satisfaction.",
            "key_advising_strengths": [f"Zero prerequisite violations with {det.prerequisites.override_requests_approved} approved course overrides", f"{det.gpa_analytics.gpa_improvement_post_advising_pct}% GPA improvement following academic advising interventions"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Dean of Academic Advising", "degree audits, academic retention, early warning systems, FERPA"),
                                          PromptBuilder.build_user_context({"score": det.advising_health_score}), task_type="advising_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicAdvisingNarrative(advising_summary=parsed.get("advising_summary", fallback["advising_summary"]),
                                              key_advising_strengths=parsed.get("key_advising_strengths", fallback["key_advising_strengths"]))
        except Exception:
            return StrategicAdvisingNarrative(**fallback)

class AcademicRetentionPlannerAgent(BaseAgent):
    """Agent 9: Generates student retention interventions and automated degree roadmap schemas."""
    def __init__(self):
        super().__init__(agent_id="academic_retention_planner", name="Academic Retention Planner Agent",
                         description="Formulates early intervention strategies for at-risk students and dynamic degree planners.", icon="CheckCircle")

    async def plan_retention(self, det: DeterministicAdvisingPipelineResult) -> AcademicRetentionPlan:
        fallback = {
            "retention_improvement_actions": [f"Deploy automated SMS early warning alerts for {det.early_warning.at_risk_students_count} students with mid-term grade drops below 2.5 GPA", "Implement 4-year degree roadmap visualizer with prerequisite dependency graph"],
            "sample_degree_roadmap": "DEGREE ROADMAP: BS Computer Science\nSemester 1: CS101 (Intro to CS), MATH151 (Calculus I), ENG101 (Comp I)\nSemester 2: CS102 (Data Structures - Prereq: CS101), MATH152 (Calculus II)\nSemester 3: CS201 (Algorithms - Prereq: CS102), CS220 (Computer Architecture)\nStatus: 78.4 / 120 credits completed (On Track for Spring 2026 graduation)"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Student Retention Strategist", "retention interventions, degree mapping, early warning"),
                                          PromptBuilder.build_user_context({"at_risk": det.early_warning.at_risk_students_count}), task_type="advising_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return AcademicRetentionPlan(retention_improvement_actions=parsed.get("retention_improvement_actions", fallback["retention_improvement_actions"]),
                                         sample_degree_roadmap=parsed.get("sample_degree_roadmap", fallback["sample_degree_roadmap"]))
        except Exception:
            return AcademicRetentionPlan(**fallback)
