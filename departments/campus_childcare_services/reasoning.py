from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.campus_childcare_services.schemas import (
    StrategicChildcareNarrative, FamilySupportPlan, ReasoningChildcarePipelineResult, DeterministicChildcarePipelineResult
)

class StrategicChildcareNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates campus early childhood care quality, student-parent financial subsidies, and academic retention."""
    def __init__(self):
        super().__init__(agent_id="strategic_childcare_narrative", name="Strategic Childcare Narrative Agent",
                         description="Evaluates childcare licensing compliance, student-parent retention rates, financial subsidies, and family housing infrastructure.", icon="Heart")

    async def evaluate(self, det: DeterministicChildcarePipelineResult) -> StrategicChildcareNarrative:
        fallback = {
            "childcare_summary": f"Gold-standard family-friendly campus ({det.childcare_score:.1f}% score). {det.enrollment.enrolled_children_count} children enrolled in campus early learning center ({det.enrollment.childcare_center_capacity_pct}% capacity), {det.licensing.licensing_compliance_score_pct}% licensing compliance, {det.retention.student_parent_retention_rate_pct}% student-parent academic retention rate.",
            "key_childcare_strengths": [f"${det.subsidies.childcare_subsidies_awarded_usd:,.0f} in childcare financial aid subsidies granted to {det.subsidies.student_parent_subsidy_recipients} student parents", f"{det.infrastructure.lactation_nursing_rooms_count} designated campus lactation/nursing rooms and {det.infrastructure.family_study_lounges_count} family study lounges"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Director of Campus Childcare & Family Services", "early childhood education, CCAMPIS grant, student-parent retention, campus lactation policy"),
                                          PromptBuilder.build_user_context({"score": det.childcare_score}), task_type="childcare_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicChildcareNarrative(childcare_summary=parsed.get("childcare_summary", fallback["childcare_summary"]),
                                              key_childcare_strengths=parsed.get("key_childcare_strengths", fallback["key_childcare_strengths"]))
        except Exception:
            return StrategicChildcareNarrative(**fallback)

class FamilySupportPlannerAgent(BaseAgent):
    """Agent 9: Generates CCAMPIS federal grant applications and evening drop-in childcare scheduling workflows."""
    def __init__(self):
        super().__init__(agent_id="family_support_planner", name="Family Support Planner Agent",
                         description="Formulates student-parent stipend programs, lactation room reservation systems, and weekend childcare initiatives.", icon="Smile")

    async def plan_family_support(self, det: DeterministicChildcarePipelineResult) -> FamilySupportPlan:
        fallback = {
            "family_support_actions": ["Expand CCAMPIS Federal Childcare Subsidies to cover 100% of evening class childcare costs for low-income student parents", "Implement Smart Lactation Pod Reservation System accessible via CampusOS mobile app"],
            "sample_childcare_subsidy_grant_application": "STUDENT-PARENT CHILDCARE SUBSIDY GRANT APPLICATION\nStudent ID: par_99182\nProgram: BS Nursing (Junior Year - 16 Credits)\nChildren Enrolled: 2 Children (Age 2 & Age 4)\nFinancial Need Assessment: EFC $0.00 / Pell Grant Eligible\nGrant Approved: $4,800.00 USD / Academic Semester\nProvider: Campus Early Childhood Development Center\nStatus: DISBURSED TO PROVIDER ACCOUNT"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Childcare Financial Aid Specialist", "CCAMPIS grant, student-parent support, drop-in childcare"),
                                          PromptBuilder.build_user_context({"children": det.enrollment.enrolled_children_count}), task_type="childcare_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return FamilySupportPlan(family_support_actions=parsed.get("family_support_actions", fallback["family_support_actions"]),
                                     sample_childcare_subsidy_grant_application=parsed.get("sample_childcare_subsidy_grant_application", fallback["sample_childcare_subsidy_grant_application"]))
        except Exception:
            return FamilySupportPlan(**fallback)
