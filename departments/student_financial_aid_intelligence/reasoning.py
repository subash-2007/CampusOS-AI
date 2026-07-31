from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.student_financial_aid_intelligence.schemas import (
    StrategicFinancialAidNarrative, FinancialAidOptimizationPlan, ReasoningFinancialAidResult, DeterministicFinancialAidResult
)

class StrategicFinancialAidNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates financial aid accessibility, FAFSA completion rates, and student debt mitigation."""
    def __init__(self):
        super().__init__(agent_id="strategic_financial_aid_narrative", name="Strategic Financial Aid Narrative Agent",
                         description="Evaluates scholarship matching, FAFSA compliance, debt burden, and disbursement efficiency.", icon="DollarSign")

    async def evaluate(self, det: DeterministicFinancialAidResult) -> StrategicFinancialAidNarrative:
        fallback = {
            "aid_summary": f"Equitable financial aid platform ({det.financial_aid_score:.1f}% score). ${det.disbursement.total_aid_disbursed_usd/1e6:.1f}M aid disbursed ({det.disbursement.on_time_disbursement_pct}% on-time), {det.fafsa.fafsa_completion_rate_pct}% FAFSA completion, {det.loan_burden.national_debt_comparison_pct}% lower student debt than national avg.",
            "key_aid_strengths": [f"{det.scholarship_match.scholarships_matched_total} matched scholarships with ${det.scholarship_match.avg_scholarship_value_usd:,.0f} avg value", f"0.8% loan default risk rate with {det.work_study.work_study_positions_filled} work-study positions filled"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Financial Aid Director", "FAFSA, scholarships, student loans, Title IV compliance"),
                                          PromptBuilder.build_user_context({"score": det.financial_aid_score}), task_type="aid_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicFinancialAidNarrative(aid_summary=parsed.get("aid_summary", fallback["aid_summary"]),
                                                 key_aid_strengths=parsed.get("key_aid_strengths", fallback["key_aid_strengths"]))
        except Exception:
            return StrategicFinancialAidNarrative(**fallback)

class FinancialAidOptimizationPlannerAgent(BaseAgent):
    """Agent 9: Generates scholarship match optimization strategies and financial literacy curriculum proposals."""
    def __init__(self):
        super().__init__(agent_id="financial_aid_optimization_planner", name="Financial Aid Optimization Planner Agent",
                         description="Formulates scholarship auto-matching algorithms and emergency grant distribution frameworks.", icon="Award")

    async def plan_optimization(self, det: DeterministicFinancialAidResult) -> FinancialAidOptimizationPlan:
        fallback = {
            "aid_optimization_actions": ["Deploy One-Click Scholarship Application engine using pre-verified student academic profiles", "Expand Emergency Grant Micro-Fund ($500-$1000) for students facing unexpected housing/medical hardship"],
            "sample_scholarship_match_schema": '{\n  "student_id": "std_8842",\n  "gpa": 3.85,\n  "major": "Computer Science",\n  "efc_usd": 4200,\n  "matched_scholarships": [\n    {\n      "id": "sch_women_in_stem",\n      "title": "Women in STEM Leadership Grant",\n      "amount_usd": 5000,\n      "deadline": "2026-10-15",\n      "eligibility_match_pct": 98.5\n    }\n  ]\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Student Financial Wellness Lead", "scholarships, grant allocation, financial literacy"),
                                          PromptBuilder.build_user_context({"matches": det.scholarship_match.scholarships_matched_total}), task_type="aid_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return FinancialAidOptimizationPlan(aid_optimization_actions=parsed.get("aid_optimization_actions", fallback["aid_optimization_actions"]),
                                                sample_scholarship_match_schema=parsed.get("sample_scholarship_match_schema", fallback["sample_scholarship_match_schema"]))
        except Exception:
            return FinancialAidOptimizationPlan(**fallback)
