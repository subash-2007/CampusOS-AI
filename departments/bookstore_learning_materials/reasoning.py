from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.bookstore_learning_materials.schemas import (
    StrategicBookstoreNarrative, AffordableLearningPlan, ReasoningBookstorePipelineResult, DeterministicBookstorePipelineResult
)

class StrategicBookstoreNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates textbook affordability programs, OER adoption rates, and day-one digital access fulfillment."""
    def __init__(self):
        super().__init__(agent_id="strategic_bookstore_narrative", name="Strategic Bookstore Narrative Agent",
                         description="Evaluates faculty textbook adoption compliance, student OER savings, digital course materials, and retail merchandise revenue.", icon="BookOpen")

    async def evaluate(self, det: DeterministicBookstorePipelineResult) -> StrategicBookstoreNarrative:
        fallback = {
            "bookstore_summary": f"Affordable learning excellence center ({det.bookstore_score:.1f}% score). {det.adoptions.faculty_adoption_deadline_compliance_pct}% adoption deadline compliance across {det.adoptions.courses_with_textbook_adoptions_logged:,} courses, ${det.oer.student_cost_savings_oer_usd/1e6:.2f}M OER student cost savings, {det.digital_access.instant_day_one_access_pct}% day-one access fulfillment.",
            "key_bookstore_strengths": [f"{det.oer.oer_courses_adopted} courses converted to Open Educational Resources (OER) with {det.oer.zero_textbook_cost_sections} zero-cost sections", f"${det.buyback.textbook_rental_savings_usd:,.0f} in textbook rental savings and ${det.buyback.buyback_payout_to_students_usd:,.0f} in buyback cash returned to students"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Director of Campus Retail & Learning Materials", "textbook affordability, Open Educational Resources (OER), Day-One Inclusive Access, textbook rental"),
                                          PromptBuilder.build_user_context({"score": det.bookstore_score}), task_type="bookstore_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicBookstoreNarrative(bookstore_summary=parsed.get("bookstore_summary", fallback["bookstore_summary"]),
                                              key_bookstore_strengths=parsed.get("key_bookstore_strengths", fallback["key_bookstore_strengths"]))
        except Exception:
            return StrategicBookstoreNarrative(**fallback)

class AffordableLearningPlannerAgent(BaseAgent):
    """Agent 9: Generates OER faculty grant incentives and Day-One Inclusive Access digital courseware contracts."""
    def __init__(self):
        super().__init__(agent_id="affordable_learning_planner", name="Affordable Learning Planner Agent",
                         description="Formulates faculty OER grant programs, digital access code automation, and zero-textbook cost degree pathways.", icon="DollarSign")

    async def plan_affordability(self, det: DeterministicBookstorePipelineResult) -> AffordableLearningPlan:
        fallback = {
            "affordability_actions": ["Launch ZTC (Zero Textbook Cost) Associate Degree Pathway in Business & General Studies", "Deploy LMS-Integrated Instant Digital Courseware Access to reduce textbook prices by 60%"],
            "sample_inclusive_access_contract": "DAY-ONE INCLUSIVE ACCESS AGREEMENT\nPublisher: Major Academic Publishing Group\nInstitution: CampusOS University\nAgreement:\n  1. Automated LMS Delivery: Digital ebooks and adaptive courseware available on 1st day of class\n  2. Wholesale Pricing: Guaranteed 60-70% discount off print list price (Billed to student bursar account)\n  3. Opt-Out Window: 14-day add/drop period opt-out capability with instant refund\n  4. Faculty Choice: 100% voluntary faculty course selection"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Open Education Officer & Learning Material Strategist", "OER adoption, ZTC degrees, Day-One Access"),
                                          PromptBuilder.build_user_context({"adoptions": det.adoptions.courses_with_textbook_adoptions_logged}), task_type="bookstore_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return AffordableLearningPlan(affordability_actions=parsed.get("affordability_actions", fallback["affordability_actions"]),
                                         sample_inclusive_access_contract=parsed.get("sample_inclusive_access_contract", fallback["sample_inclusive_access_contract"]))
        except Exception:
            return AffordableLearningPlan(**fallback)
