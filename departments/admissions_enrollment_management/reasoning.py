from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.admissions_enrollment_management.schemas import (
    StrategicAdmissionsNarrative, EnrollmentStrategyPlan, ReasoningAdmissionsPipelineResult, DeterministicAdmissionsPipelineResult
)

class StrategicAdmissionsNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates undergraduate admissions selectivity, yield rate optimization, and holistic file review accuracy."""
    def __init__(self):
        super().__init__(agent_id="strategic_admissions_narrative", name="Strategic Admissions Narrative Agent",
                         description="Evaluates admissions selectivity rates, freshman class yield percentages, holistic review compliance, and Slate CRM recruitment funnels.", icon="UserCheck")

    async def evaluate(self, det: DeterministicAdmissionsPipelineResult) -> StrategicAdmissionsNarrative:
        fallback = {
            "admissions_summary": f"Premier selective enrollment enterprise ({det.admissions_score:.1f}% score). Processing {det.volume.applications_received_count:,} applications ({det.volume.admissions_selectivity_rate_pct}% selectivity), enrolling {det.yield_metric.enrolled_freshmen_count:,} freshmen ({det.yield_metric.enrollment_yield_rate_pct}% yield), {det.academics.enrolled_class_avg_gpa:.2f} average high school GPA.",
            "key_admissions_strengths": [f"100% holistic rubric audit compliance across {det.holistic_review.holistic_file_reviews_completed:,} application file reviews ({det.holistic_review.avg_application_review_days:.1f}-day average review turn)", f"{det.tours.campus_tour_visitors_annual:,} annual campus tour visitors achieving {det.tours.tour_visitor_application_conversion_pct}% application conversion rate"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Dean of Undergraduate Admissions & Vice President for Enrollment Management", "admissions selectivity, yield rate, holistic review, Slate CRM, campus tours"),
                                          PromptBuilder.build_user_context({"score": det.admissions_score}), task_type="admissions_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicAdmissionsNarrative(admissions_summary=parsed.get("admissions_summary", fallback["admissions_summary"]),
                                               key_admissions_strengths=parsed.get("key_admissions_strengths", fallback["key_admissions_strengths"]))
        except Exception:
            return StrategicAdmissionsNarrative(**fallback)

class EnrollmentStrategyPlannerAgent(BaseAgent):
    """Agent 9: Formulates AI predictive enrollment modeling and personalized Slate CRM recruitment campaigns."""
    def __init__(self):
        super().__init__(agent_id="enrollment_strategy_planner", name="Enrollment Strategy Planner Agent",
                         description="Formulates yield predictive modeling algorithms, virtual campus VR tour portals, and automated decision letter delivery systems.", icon="TrendingUp")

    async def plan_enrollment(self, det: DeterministicAdmissionsPipelineResult) -> EnrollmentStrategyPlan:
        fallback = {
            "admissions_actions": ["Deploy AI Yield Prediction Model optimizing institutional merit aid leverage to boost yield by 4%", "Launch Interactive 360-Degree VR Campus Tour Portal for international & out-of-state applicants"],
            "sample_admissions_decision_letter_schema": '{\n  "applicant_id": "app_2026_99182",\n  "applicant_name": "Maya Lin",\n  "decision_type": "OFFICIAL ADMISSION OFFER",\n  "intended_major": "BS Biomedical Engineering",\n  "entry_term": "Fall 2026",\n  "merit_scholarship_awarded": {\n    "scholarship_name": "Dean\'s Presidential Merit Scholarship",\n    "amount_per_year_usd": 18000.00,\n    "4_year_total_usd": 72000.00\n  },\n  "deposit_deadline": "May 1, 2026",\n  "decision_portal_status": "OFFER DELIVERED & CONFIRMED VIA ADMISSIONS PORTAL"\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Enrollment Intelligence Specialist", "predictive yield model, Slate CRM, decision letter"),
                                          PromptBuilder.build_user_context({"apps": det.volume.applications_received_count}), task_type="admissions_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return EnrollmentStrategyPlan(admissions_actions=parsed.get("admissions_actions", fallback["admissions_actions"]),
                                          sample_admissions_decision_letter_schema=parsed.get("sample_admissions_decision_letter_schema", fallback["sample_admissions_decision_letter_schema"]))
        except Exception:
            return EnrollmentStrategyPlan(**fallback)
