from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.global_engagement_partnerships.schemas import (
    StrategicGlobalEngagementNarrative, GlobalEngagementPlan, ReasoningGlobalEngagementPipelineResult, DeterministicGlobalEngagementPipelineResult
)

class StrategicGlobalEngagementNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates international student enrollment, bilateral MOU partner agreements, and study abroad participation rates."""
    def __init__(self):
        super().__init__(agent_id="strategic_global_engagement_narrative", name="Strategic Global Engagement Narrative Agent",
                         description="Evaluates international student enrollment, study abroad participation, MOU partnership agreements, ELI success rates, and faculty exchange programs.", icon="Globe")

    async def evaluate(self, det: DeterministicGlobalEngagementPipelineResult) -> StrategicGlobalEngagementNarrative:
        fallback = {
            "global_summary": f"World-class global engagement institution ({det.global_score:.1f}% score). Hosting {det.intl_students.students_enrolled_from_international_countries:,} international students with {det.study_abroad.students_studying_abroad_annual:,} students studying abroad annually, {det.mou.active_bilateral_mou_agreements} bilateral MOU agreements with {det.mou.joint_degree_programs_operational} joint degree programs.",
            "key_global_strengths": [f"{det.eli.eli_program_enrollment} ELI English Language students with {det.eli.toefl_ielts_success_rate_pct}% TOEFL/IELTS success rate and {det.eli.eli_graduate_persistence_pct}% academic persistence", f"{det.faculty_exchange.visiting_international_scholars_hosted} visiting international scholars hosted producing {det.faculty_exchange.joint_research_publications} joint research publications"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Vice Provost for Global Engagement & International Affairs", "international students, study abroad, MOU partnerships, ELI, faculty exchange"), PromptBuilder.build_user_context({"score": det.global_score}), task_type="global_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicGlobalEngagementNarrative(global_summary=parsed.get("global_summary", fallback["global_summary"]), key_global_strengths=parsed.get("key_global_strengths", fallback["key_global_strengths"]))
        except Exception:
            return StrategicGlobalEngagementNarrative(**fallback)

class GlobalEngagementPlannerAgent(BaseAgent):
    """Agent 9: Formulates virtual international exchange programs and AI-powered international student success early alert systems."""
    def __init__(self):
        super().__init__(agent_id="global_engagement_planner", name="Global Engagement Planner Agent",
                         description="Formulates COIL virtual exchange programs, international student success dashboards, and strategic global partnership recruitment initiatives.", icon="MapPin")

    async def plan_global_engagement(self, det: DeterministicGlobalEngagementPipelineResult) -> GlobalEngagementPlan:
        fallback = {
            "global_actions": ["Launch COIL (Collaborative Online International Learning) Virtual Exchange connecting 2,400 students with international partner universities digitally", "Deploy International Student AI Success Navigator providing personalized academic, immigration, and cultural adjustment support"],
            "sample_study_abroad_program_schema": '{\n  "program_id": "SA_2026_FLORENCE_0042",\n  "program_name": "Florence Art, Architecture & Italian Renaissance Studies",\n  "partner_institution": "Università degli Studi di Firenze",\n  "duration": "Semester Abroad (16 Weeks)",\n  "participant_count": 48,\n  "tuition_model": "Home Institution Tuition Billing",\n  "courses_offered": ["Italian Language I & II", "Renaissance Art History", "Architectural Drawing", "Mediterranean Culture"],\n  "student_avg_gpa": 3.72,\n  "program_csat": 4.91\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Director of International Education & Study Abroad", "COIL virtual exchange, study abroad, international student success, MOU partnership"), PromptBuilder.build_user_context({"partners": det.mou.active_bilateral_mou_agreements}), task_type="global_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return GlobalEngagementPlan(global_actions=parsed.get("global_actions", fallback["global_actions"]), sample_study_abroad_program_schema=parsed.get("sample_study_abroad_program_schema", fallback["sample_study_abroad_program_schema"]))
        except Exception:
            return GlobalEngagementPlan(**fallback)
