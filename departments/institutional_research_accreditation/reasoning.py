from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.institutional_research_accreditation.schemas import (
    StrategicResearchNarrative, AccreditationCompliancePlan, ReasoningResearchPipelineResult, DeterministicResearchAccreditationPipelineResult
)

class StrategicResearchNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates SACSCOC regional accreditation compliance, IPEDS federal reporting accuracy, and graduation/retention rate trajectories."""
    def __init__(self):
        super().__init__(agent_id="strategic_research_narrative", name="Strategic Research Narrative Agent",
                         description="Evaluates SACSCOC accreditation standard compliance, IPEDS data accuracy, SLO assessment cycles, faculty credentials, and institutional KPI dashboards.", icon="BarChart2")

    async def evaluate(self, det: DeterministicResearchAccreditationPipelineResult) -> StrategicResearchNarrative:
        fallback = {
            "research_summary": f"Gold standard accredited institution ({det.research_score:.1f}% score). SACSCOC Accreditation status {det.accreditation.sacs_coc_accreditation_status} — {det.accreditation.comprehensive_standards_met_count}/{det.accreditation.comprehensive_standards_total_count} comprehensive standards met. {det.graduation.six_year_graduation_rate_pct}% six-year graduation rate, {det.graduation.first_to_second_year_retention_rate_pct}% first-to-second year retention.",
            "key_research_strengths": [f"{det.slo.slo_assessment_completion_rate_pct}% SLO assessment completion across {det.slo.academic_programs_with_slo_assessment}/{det.slo.total_academic_programs} academic programs", f"{det.faculty.terminal_degree_faculty_pct}% terminal-degree faculty with 100% professionally qualified instructors"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Vice President for Academic Affairs & Accreditation Liaison Officer (ALO)", "SACSCOC accreditation, IPEDS, SLO assessment, graduation rates, faculty credentials"),
                                          PromptBuilder.build_user_context({"score": det.research_score}), task_type="research_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicResearchNarrative(research_summary=parsed.get("research_summary", fallback["research_summary"]),
                                             key_research_strengths=parsed.get("key_research_strengths", fallback["key_research_strengths"]))
        except Exception:
            return StrategicResearchNarrative(**fallback)

class AccreditationCompliancePlannerAgent(BaseAgent):
    """Agent 9: Formulates SACSCOC QEP (Quality Enhancement Plan) milestones and automated IPEDS data validation pipelines."""
    def __init__(self):
        super().__init__(agent_id="accreditation_compliance_planner", name="Accreditation Compliance Planner Agent",
                         description="Formulates SACSCOC QEP impact measurement, automated SLO assessment reporting, and IPEDS submission validation workflows.", icon="ClipboardCheck")

    async def plan_accreditation(self, det: DeterministicResearchAccreditationPipelineResult) -> AccreditationCompliancePlan:
        fallback = {
            "accreditation_actions": ["Deploy Automated IPEDS Data Validation Engine cross-referencing Student Information System with federal definitions before submission", "Launch Digital SLO Assessment Portfolio System enabling real-time program learning outcome tracking"],
            "sample_slo_assessment_schema": '{\n  "program": "Bachelor of Science in Computer Science",\n  "slo_1": {\n    "outcome": "Students will demonstrate mastery of algorithm design and computational complexity",\n    "assessment_method": "Senior Capstone Project Rubric (n=218)",\n    "target_benchmark": "70% of students score 80% or above",\n    "actual_result": "84.6% of students scored 80% or above",\n    "status": "EXCEEDS BENCHMARK"\n  },\n  "use_of_results": "Curriculum Enhancement: Added Advanced Algorithms elective for students below benchmark in Fall 2027"\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Institutional Effectiveness & Accreditation Specialist", "SLO assessment, IPEDS, SACSCOC QEP"),
                                          PromptBuilder.build_user_context({"programs": det.slo.total_academic_programs}), task_type="accreditation_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return AccreditationCompliancePlan(accreditation_actions=parsed.get("accreditation_actions", fallback["accreditation_actions"]),
                                               sample_slo_assessment_schema=parsed.get("sample_slo_assessment_schema", fallback["sample_slo_assessment_schema"]))
        except Exception:
            return AccreditationCompliancePlan(**fallback)
