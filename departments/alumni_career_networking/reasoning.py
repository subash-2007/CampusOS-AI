from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.alumni_career_networking.schemas import (
    StrategicAlumniCareerNarrative, AlumniCareerPlan, ReasoningAlumniCareerPipelineResult, DeterministicAlumniCareerPipelineResult
)

class StrategicAlumniCareerNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates global alumni network career impact, mentorship program engagement, and mid-career coaching success."""
    def __init__(self):
        super().__init__(agent_id="strategic_alumni_career_narrative", name="Strategic Alumni Career Narrative Agent",
                         description="Evaluates alumni mentor-mentee matching satisfaction, mid-career coaching transitions, regional chapter events, and alumni job referrals.", icon="Briefcase")

    async def evaluate(self, det: DeterministicAlumniCareerPipelineResult) -> StrategicAlumniCareerNarrative:
        fallback = {
            "alumni_career_summary": f"Global alumni career powerhouse ({det.alumni_career_score:.1f}% score). {det.mentorship.registered_alumni_mentors_count:,} registered alumni mentors ({det.mentorship.active_alumni_student_matches:,} active matches), {det.mentorship.mentorship_satisfaction_rate_pct}% mentorship satisfaction rate, {det.coaching.career_pivot_success_rate_pct}% mid-career pivot success rate.",
            "key_alumni_career_strengths": [f"{det.chapters.active_regional_chapters_count} regional alumni chapters hosting {det.chapters.annual_alumni_networking_events} events for {det.chapters.chapter_event_attendees_annual:,} attendees", f"{det.job_board.alumni_posted_job_openings:,} alumni-posted job openings resulting in {det.job_board.alumni_referrals_submitted:,} referrals and {det.job_board.alumni_hire_conversion_rate_pct}% hire conversion"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Director of Alumni Career Engagement & Professional Networks", "alumni mentorship, mid-career coaching, regional chapters, alumni job board"),
                                          PromptBuilder.build_user_context({"score": det.alumni_career_score}), task_type="alumni_career_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicAlumniCareerNarrative(alumni_career_summary=parsed.get("alumni_career_summary", fallback["alumni_career_summary"]),
                                                 key_alumni_career_strengths=parsed.get("key_alumni_career_strengths", fallback["key_alumni_career_strengths"]))
        except Exception:
            return StrategicAlumniCareerNarrative(**fallback)

class AlumniCareerPlannerAgent(BaseAgent):
    """Agent 9: Formulates AI-powered alumni mentor matching systems and executive upskilling roadmaps."""
    def __init__(self):
        super().__init__(agent_id="alumni_career_planner", name="Alumni Career Planner Agent",
                         description="Formulates alumni-student career mentorship matching algorithms, regional alumni career fairs, and lifelong learning subscription benefits.", icon="UserPlus")

    async def plan_alumni_career(self, det: DeterministicAlumniCareerPipelineResult) -> AlumniCareerPlan:
        fallback = {
            "alumni_career_actions": ["Deploy Smart AI Mentorship Matchmaker pairing alumni with students based on career trajectory, industry, and identity", "Launch Global Alumni Mid-Career Transition Accelerator & Micro-Credential Portal"],
            "sample_alumni_mentor_matching_schema": '{\n  "student_id": "stu_99182",\n  "student_major": "Computer Science & Business Administration",\n  "target_career": "Product Manager at Tier-1 Tech Firm",\n  "recommended_alumni_mentor": {\n    "alumni_id": "alm_44012",\n    "name": "Sarah Jenkins (Class of 2018)",\n    "title": "Senior Staff PM at Google Cloud",\n    "match_score": 98.4,\n    "common_interests": ["Product Strategy", "CS-Business Dual Degree", "Women in Tech Leader"]\n  },\n  "status": "MENTORSHIP MATCH PROPOSED & NOTIFICATION SENT"\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Alumni Career Strategy Specialist", "alumni mentor match, career pivot, upskilling"),
                                          PromptBuilder.build_user_context({"mentors": det.mentorship.registered_alumni_mentors_count}), task_type="alumni_career_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return AlumniCareerPlan(alumni_career_actions=parsed.get("alumni_career_actions", fallback["alumni_career_actions"]),
                                    sample_alumni_mentor_matching_schema=parsed.get("sample_alumni_mentor_matching_schema", fallback["sample_alumni_mentor_matching_schema"]))
        except Exception:
            return AlumniCareerPlan(**fallback)
