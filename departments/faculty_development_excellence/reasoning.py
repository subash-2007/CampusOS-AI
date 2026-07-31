from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.faculty_development_excellence.schemas import (
    StrategicFacultyNarrative, FacultyDevelopmentPlan, ReasoningFacultyPipelineResult, DeterministicFacultyPipelineResult
)

class StrategicFacultyNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates faculty pedagogy workshop engagement, Quality Matters online certification rates, and research grant output."""
    def __init__(self):
        super().__init__(agent_id="strategic_faculty_narrative", name="Strategic Faculty Narrative Agent",
                         description="Evaluates faculty pedagogy workshop satisfaction, QM online certification, research grant funding, tenure workload equity, and new faculty mentoring retention.", icon="BookOpen")

    async def evaluate(self, det: DeterministicFacultyPipelineResult) -> StrategicFacultyNarrative:
        fallback = {
            "faculty_summary": f"Distinguished teaching & research faculty culture ({det.faculty_score:.1f}% score). {det.workshops.faculty_workshop_participation_count:,} faculty participated in {det.workshops.faculty_pedagogy_workshops_offered} pedagogy workshops ({det.workshops.workshop_avg_satisfaction_score:.2f}/5.0 rating), ${det.research.total_research_grant_funding_millions:.1f}M in external research grants secured.",
            "key_faculty_strengths": [f"{det.online_courses.online_courses_quality_matters_certified}/{det.online_courses.total_online_courses} online courses Quality Matters certified ({det.online_courses.qm_certification_rate_pct}%) with {det.research.faculty_publications_peer_reviewed:,} peer-reviewed publications", f"{det.mentoring.faculty_mentoring_pairs_active} active faculty mentoring pairs achieving {det.mentoring.new_faculty_retention_2yr_pct}% 2-year new faculty retention"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Provost & Vice President for Academic Affairs", "faculty pedagogy, Quality Matters, research grants, tenure, new faculty mentoring"),
                                          PromptBuilder.build_user_context({"score": det.faculty_score}), task_type="faculty_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicFacultyNarrative(faculty_summary=parsed.get("faculty_summary", fallback["faculty_summary"]),
                                            key_faculty_strengths=parsed.get("key_faculty_strengths", fallback["key_faculty_strengths"]))
        except Exception:
            return StrategicFacultyNarrative(**fallback)

class FacultyDevelopmentPlannerAgent(BaseAgent):
    """Agent 9: Formulates digital faculty learning community networks and AI-assisted course design consultation programs."""
    def __init__(self):
        super().__init__(agent_id="faculty_development_planner", name="Faculty Development Planner Agent",
                         description="Formulates faculty AI literacy bootcamps, digital scholarship support, and teaching innovation fellowship programs.", icon="Users")

    async def plan_faculty_development(self, det: DeterministicFacultyPipelineResult) -> FacultyDevelopmentPlan:
        fallback = {
            "faculty_actions": ["Launch AI Faculty Innovation Fellows Program — stipend-supported faculty developing AI-enhanced course modules", "Deploy Digital Faculty Portfolio System enabling tenure-track faculty to showcase teaching innovation evidence"],
            "sample_faculty_grant_schema": '{\n  "grant_id": "GRANT_2026_NSF_0342",\n  "pi_faculty": "Dr. Sarah Chen, Associate Professor of Computational Biology",\n  "funding_agency": "National Science Foundation (NSF)",\n  "program": "Division of Biological Infrastructure - Research Experiences for Undergraduates (REU)",\n  "award_amount": "$378,000",\n  "duration": "3 Years (2026-2029)",\n  "research_area": "AI-Assisted Protein Folding Prediction for Drug Discovery",\n  "undergraduate_researchers_supported": 18\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Faculty Development Center Director & Academic Affairs Strategist", "faculty AI literacy, teaching innovation, research grant, tenure"),
                                          PromptBuilder.build_user_context({"faculty": det.tenure.tenure_track_faculty_count}), task_type="faculty_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return FacultyDevelopmentPlan(faculty_actions=parsed.get("faculty_actions", fallback["faculty_actions"]),
                                          sample_faculty_grant_schema=parsed.get("sample_faculty_grant_schema", fallback["sample_faculty_grant_schema"]))
        except Exception:
            return FacultyDevelopmentPlan(**fallback)
