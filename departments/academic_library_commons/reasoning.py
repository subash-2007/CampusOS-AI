from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.academic_library_commons.schemas import (
    StrategicLibraryNarrative, LibraryStrategicPlan, ReasoningLibraryPipelineResult, DeterministicLibraryPipelineResult
)

class StrategicLibraryNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates academic library collection depth, licensed database cost-per-use efficiency, and learning commons tutoring utilization."""
    def __init__(self):
        super().__init__(agent_id="strategic_library_narrative", name="Strategic Library Narrative Agent",
                         description="Evaluates library research consultation quality, database subscription efficiency, open access repository downloads, and learning commons tutoring outcomes.", icon="BookOpen")

    async def evaluate(self, det: DeterministicLibraryPipelineResult) -> StrategicLibraryNarrative:
        fallback = {
            "library_summary": f"ARL Research Library distinction ({det.library_score:.1f}% score). Holdings of {det.collection.physical_volumes_holdings:,} physical volumes and {det.collection.ebooks_digital_resources_count:,} digital resources across {det.databases.licensed_databases_subscriptions} licensed databases, {det.research_support.research_consultations_annual:,} research consultations ({det.research_support.research_librarian_satisfaction_score:.2f}/5.0 rating).",
            "key_library_strengths": [f"Open Access Digital Repository with {det.repository.open_access_downloads_annual:,} annual downloads of {det.repository.faculty_theses_in_digital_repository:,} faculty theses at {det.repository.repository_uptime_pct}% uptime", f"Learning Commons facilitating {det.learning_commons.tutoring_sessions_facilitated_annual:,} tutoring sessions and {det.learning_commons.writing_center_appointments_annual:,} writing center appointments ({det.learning_commons.tutoring_student_satisfaction_score:.2f}/5.0 CSAT)"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Dean of Libraries & Chief Academic Resource Officer", "library collections, database licensing, research consultations, open access repository, learning commons tutoring"),
                                          PromptBuilder.build_user_context({"score": det.library_score}), task_type="library_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicLibraryNarrative(library_summary=parsed.get("library_summary", fallback["library_summary"]),
                                            key_library_strengths=parsed.get("key_library_strengths", fallback["key_library_strengths"]))
        except Exception:
            return StrategicLibraryNarrative(**fallback)

class LibraryStrategicPlannerAgent(BaseAgent):
    """Agent 9: Formulates AI-powered library research discovery tools and evidence-based database acquisition frameworks."""
    def __init__(self):
        super().__init__(agent_id="library_strategic_planner", name="Library Strategic Planner Agent",
                         description="Formulates AI research discovery, evidence-based collection development, and digital learning commons expansion strategies.", icon="Search")

    async def plan_library_strategy(self, det: DeterministicLibraryPipelineResult) -> LibraryStrategicPlan:
        fallback = {
            "library_actions": ["Deploy AI Semantic Research Discovery Engine integrating cross-database search across all 480 licensed databases with citation graph visualization", "Launch Evidence-Based Database Acquisition Program using COUNTER usage analytics to optimize $2.4M database licensing budget"],
            "sample_research_consultation_schema": '{\n  "consultation_id": "REF_2026_11284",\n  "student_id": "stu_99182",\n  "research_topic": "Machine Learning Applications in Climate Change Prediction",\n  "librarian": "Dr. Priya Sharma, MLIS (Science & Engineering Librarian)",\n  "databases_recommended": ["Web of Science", "Scopus", "arXiv", "IEEE Xplore"],\n  "search_strategies": "Boolean operators: (machine learning OR deep learning) AND (climate change OR global warming) AND (prediction OR modeling)",\n  "sources_identified": 48,\n  "consultation_duration_min": 35,\n  "student_satisfaction": 5.0\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Academic Library Director & Research Information Specialist", "AI research discovery, evidence-based collection development, open access"),
                                          PromptBuilder.build_user_context({"databases": det.databases.licensed_databases_subscriptions}), task_type="library_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return LibraryStrategicPlan(library_actions=parsed.get("library_actions", fallback["library_actions"]),
                                        sample_research_consultation_schema=parsed.get("sample_research_consultation_schema", fallback["sample_research_consultation_schema"]))
        except Exception:
            return LibraryStrategicPlan(**fallback)
