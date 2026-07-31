from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.international_student_services.schemas import (
    StrategicISSSNarrative, InternationalStudentPlan, ReasoningISSSPipelineResult, DeterministicISSSPipelineResult
)

class StrategicISSSNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates F-1/J-1 visa compliance, CPT/OPT processing pipelines, and international student integration."""
    def __init__(self):
        super().__init__(agent_id="strategic_isss_narrative", name="Strategic ISSS Narrative Agent",
                         description="Evaluates SEVIS compliance, CPT/OPT work authorizations, international student demographics, and cultural programming.", icon="Globe")

    async def evaluate(self, det: DeterministicISSSPipelineResult) -> StrategicISSSNarrative:
        fallback = {
            "isss_summary": f"Global hub of excellence ({det.isss_score:.1f}% score). Supporting {det.demographics.international_students_count:,} international scholars across {det.demographics.represented_countries_count} countries, {det.sevis.sevis_reporting_compliance_pct}% SEVIS reporting compliance, {det.sevis.i20_ds2019_issuance_speed_days:.1f}-day I-20 issuance speed.",
            "key_isss_strengths": [f"{det.work_auth.cpt_authorizations_approved:,} CPT & {det.work_auth.opt_applications_endorsed:,} OPT work authorizations processed (including {det.work_auth.stem_opt_extensions_processed} STEM OPT extensions)", f"{det.tax_insurance.non_resident_tax_software_utilization_pct}% non-resident Sprintax tax compliance utilization"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Director of International Student & Scholar Services", "SEVIS compliance, F-1 visa, J-1 visa, CPT, OPT, STEM OPT extension"),
                                          PromptBuilder.build_user_context({"score": det.isss_score}), task_type="isss_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicISSSNarrative(isss_summary=parsed.get("isss_summary", fallback["isss_summary"]),
                                        key_isss_strengths=parsed.get("key_isss_strengths", fallback["key_isss_strengths"]))
        except Exception:
            return StrategicISSSNarrative(**fallback)

class InternationalStudentPlannerAgent(BaseAgent):
    """Agent 9: Generates CPT/OPT legal compliance workflows and international student orientation roadmaps."""
    def __init__(self):
        super().__init__(agent_id="international_student_planner", name="International Student Planner Agent",
                         description="Formulates CPT authorization letters, OPT workshop schedules, and cultural integration events.", icon="UserCheck")

    async def plan_student_support(self, det: DeterministicISSSPipelineResult) -> InternationalStudentPlan:
        fallback = {
            "support_actions": ["Deploy Automated CPT Authorization System directly integrated with university registrar", "Launch Global Career Expo connecting F-1/J-1 students with E-Verify employers"],
            "sample_cpt_recommendation_letter": "CURRICULAR PRACTICAL TRAINING (CPT) RECOMMENDATION FORM\nStudent ID: int_77182\nSEVIS ID: N001892104\nVisa Status: F-1 Student\nEmployer: Tech Corp Inc.\nLocation: San Jose, CA\nDuration: June 1, 2027 to August 20, 2027\nCourse Requirement: CS 590 Industrial Internship (3 Credits)\nPDSO Approval: RECOMMENDED & AUTHORIZED IN SEVIS"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Principal Designated School Official (PDSO)", "CPT recommendation, OPT endorsement, SEVIS I-20, F-1 visa regulations"),
                                          PromptBuilder.build_user_context({"students": det.demographics.international_students_count}), task_type="isss_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return InternationalStudentPlan(support_actions=parsed.get("support_actions", fallback["support_actions"]),
                                           sample_cpt_recommendation_letter=parsed.get("sample_cpt_recommendation_letter", fallback["sample_cpt_recommendation_letter"]))
        except Exception:
            return InternationalStudentPlan(**fallback)
