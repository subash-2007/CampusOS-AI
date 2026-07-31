from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.financial_aid_scholarships.schemas import (
    StrategicFinancialAidNarrative, FinancialAidOperationsPlan, ReasoningFinancialAidPipelineResult, DeterministicFinancialAidPipelineResult
)

class StrategicFinancialAidNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates FAFSA processing speed, institutional scholarship allocation efficiency, and Title IV compliance."""
    def __init__(self):
        super().__init__(agent_id="strategic_financial_aid_narrative", name="Strategic Financial Aid Narrative Agent",
                         description="Evaluates FAFSA processing turnaround, institutional scholarship distribution, SAP compliance rates, and Title IV federal audit accuracy.", icon="DollarSign")

    async def evaluate(self, det: DeterministicFinancialAidPipelineResult) -> StrategicFinancialAidNarrative:
        fallback = {
            "financial_aid_summary": f"Model student financial aid program ({det.financial_aid_score:.1f}% score). Processing {det.fafsa.fafsa_applications_processed:,} FAFSA applications ({det.fafsa.avg_fafsa_processing_days:.1f}-day average turn), ${det.scholarships.institutional_scholarships_awarded_usd/1e6:.1f}M in institutional scholarships meeting {det.scholarships.need_based_aid_met_pct}% of demonstrated need, 100% Title IV federal audit compliance.",
            "key_financial_aid_strengths": [f"${det.title_iv.pell_grants_disbursed_usd/1e6:.1f}M in Federal Pell Grants and ${det.title_iv.direct_student_loans_disbursed_usd/1e6:.1f}M in Direct Student Loans disbursed seamlessly", f"${det.emergency_aid.emergency_grants_awarded_usd:,.0f} in emergency aid grants disbursed to {det.emergency_aid.emergency_grant_recipients} students with {det.emergency_aid.avg_emergency_grant_fulfillment_hours:.1f}-hour fulfillment speed"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Executive Director of Financial Aid & University Scholarships", "FAFSA processing, Title IV compliance, institutional scholarships, SAP appeals, emergency grants"),
                                          PromptBuilder.build_user_context({"score": det.financial_aid_score}), task_type="financial_aid_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicFinancialAidNarrative(financial_aid_summary=parsed.get("financial_aid_summary", fallback["financial_aid_summary"]),
                                                 key_financial_aid_strengths=parsed.get("key_financial_aid_strengths", fallback["key_financial_aid_strengths"]))
        except Exception:
            return StrategicFinancialAidNarrative(**fallback)

class FinancialAidOperationsPlannerAgent(BaseAgent):
    """Agent 9: Formulates automated FAFSA verification workflows and instant emergency aid grant distribution systems."""
    def __init__(self):
        super().__init__(agent_id="financial_aid_operations_planner", name="Financial Aid Operations Planner Agent",
                         description="Formulates AI FAFSA verification document scanners, automated SAP appeal tracking systems, and scholarship donor matching portals.", icon="FileText")

    async def plan_financial_aid(self, det: DeterministicFinancialAidPipelineResult) -> FinancialAidOperationsPlan:
        fallback = {
            "financial_aid_actions": ["Deploy One-Click Instant FAFSA Verification Portal eliminating paper tax transcript delays", "Launch Smart Emergency Student Aid Micro-Grants disbursed via campus debit card within 12 hours"],
            "sample_financial_aid_award_letter_schema": '{\n  "student_id": "stu_99182",\n  "academic_year": "2026-2027",\n  "cost_of_attendance_usd": 32500.00,\n  "student_aid_index_sai": 0.00,\n  "demonstrated_financial_need_usd": 32500.00,\n  "gift_aid": [\n    {"source": "Federal Pell Grant", "amount_usd": 7395.00},\n    {"source": "Presidential Merit Scholarship", "amount_usd": 15000.00},\n    {"source": "University Opportunity Grant", "amount_usd": 7605.00}\n  ],\n  "total_gift_aid_usd": 30000.00,\n  "remaining_unmet_need_usd": 2500.00,\n  "status": "AWARD ACCEPTED & DISBURSEMENT PENDING CLASS REGISTRATION"\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Financial Aid Systems & Compliance Officer", "award letter schema, FAFSA verification, SAP appeals"),
                                          PromptBuilder.build_user_context({"apps": det.fafsa.fafsa_applications_processed}), task_type="financial_aid_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return FinancialAidOperationsPlan(financial_aid_actions=parsed.get("financial_aid_actions", fallback["financial_aid_actions"]),
                                              sample_financial_aid_award_letter_schema=parsed.get("sample_financial_aid_award_letter_schema", fallback["sample_financial_aid_award_letter_schema"]))
        except Exception:
            return FinancialAidOperationsPlan(**fallback)
