from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.orientation_transition_programs.schemas import (
    StrategicOrientationNarrative, TransitionProgramPlan, ReasoningOrientationPipelineResult, DeterministicOrientationPipelineResult
)

class StrategicOrientationNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates new student orientation completion rates, First-Year Experience (FYE) retention lift, and Welcome Week engagement."""
    def __init__(self):
        super().__init__(agent_id="strategic_orientation_narrative", name="Strategic Orientation Narrative Agent",
                         description="Evaluates freshmen & transfer student orientation completion, FYE seminar course retention impact, Orientation Leader training, and parent engagement.", icon="Compass")

    async def evaluate(self, det: DeterministicOrientationPipelineResult) -> StrategicOrientationNarrative:
        fallback = {
            "orientation_summary": f"National model for student transition & retention ({det.orientation_score:.1f}% score). Welcoming {det.freshmen.new_freshmen_attending_orientation:,} new freshmen ({det.freshmen.freshmen_orientation_completion_pct}% completion) and {det.transfers.new_transfer_students_attending:,} transfer students ({det.transfers.transfer_orientation_completion_pct}% completion), {det.fye_course.fye_retention_lift_pct}% FYE course retention lift.",
            "key_orientation_strengths": [f"{det.fye_course.fye_course_enrollment_pct}% of first-year students enrolled in {det.fye_course.fye_seminar_sections_offered} FYE seminar sections led by {det.staffing.orientation_leaders_active} trained Orientation Leaders", f"{det.welcome_week.welcome_week_event_checkins_total:,} Welcome Week event check-ins across {det.welcome_week.welcome_week_events_hosted} events with {det.welcome_week.welcome_week_satisfaction_score:.2f}/5.0 student satisfaction rating"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Director of New Student & Family Orientation Programs", "freshmen orientation, transfer transition, FYE seminar, Welcome Week, Orientation Leaders"),
                                          PromptBuilder.build_user_context({"score": det.orientation_score}), task_type="orientation_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicOrientationNarrative(orientation_summary=parsed.get("orientation_summary", fallback["orientation_summary"]),
                                                key_orientation_strengths=parsed.get("key_orientation_strengths", fallback["key_orientation_strengths"]))
        except Exception:
            return StrategicOrientationNarrative(**fallback)

class TransitionProgramPlannerAgent(BaseAgent):
    """Agent 9: Formulates mobile orientation scheduling apps and First-Year Experience (FYE) digital onboarding toolkits."""
    def __init__(self):
        super().__init__(agent_id="transition_program_planner", name="Transition Program Planner Agent",
                         description="Formulates mobile orientation agenda builders, peer mentor pairing systems for incoming freshmen, and parent transition webinars.", icon="Layers")

    async def plan_transition(self, det: DeterministicOrientationPipelineResult) -> TransitionProgramPlan:
        fallback = {
            "orientation_actions": ["Deploy Smart Mobile Orientation App with personalized schedule, campus map, and peer group chat", "Launch Extended First-Year Transition Mentorship Program pairing every freshman with an upperclassman Orientation Leader"],
            "sample_orientation_schedule_schema": '{\n  "student_id": "stu_2026_ fresh_99182",\n  "orientation_group": "Group 14 - Engineering Trailblazers",\n  "assigned_orientation_leader": "Jordan Rivera (Junior, Computer Engineering)",\n  "day_1_schedule": [\n    {"time": "08:30 AM", "session": "Check-In & Convocation Welcome (Student Union Ballroom)"},\n    {"time": "10:30 AM", "session": "Academic Advising & Course Registration (Engineering Center)"},\n    {"time": "01:30 PM", "session": "Small Group Peer Icebreakers & Campus Scavenger Hunt"},\n    {"time": "04:00 PM", "session": "Campus Safety & Wellness Resource Fair"}\n  ],\n  "attendance_status": "DIGITAL CHECK-IN VERIFIED VIA CAMPUSOS MOBILE APP"\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Orientation Operations Specialist & First-Year Advisor", "orientation schedule, FYE onboarding, peer mentor app"),
                                          PromptBuilder.build_user_context({"freshmen": det.freshmen.new_freshmen_attending_orientation}), task_type="orientation_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return TransitionProgramPlan(orientation_actions=parsed.get("orientation_actions", fallback["orientation_actions"]),
                                         sample_orientation_schedule_schema=parsed.get("sample_orientation_schedule_schema", fallback["sample_orientation_schedule_schema"]))
        except Exception:
            return TransitionProgramPlan(**fallback)
