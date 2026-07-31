from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.internship_coop_intelligence.schemas import (
    StrategicInternshipNarrative, InternshipProgramPlan, ReasoningInternshipPipelineResult, DeterministicInternshipPipelineResult
)

class StrategicInternshipNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates internship placement outcomes, full-time conversion rates, and employer satisfaction."""
    def __init__(self):
        super().__init__(agent_id="strategic_internship_narrative", name="Strategic Internship Narrative Agent",
                         description="Evaluates placement rates, conversion to full-time, hourly stipends, and academic credit compliance.", icon="Briefcase")

    async def evaluate(self, det: DeterministicInternshipPipelineResult) -> StrategicInternshipNarrative:
        fallback = {
            "internship_summary": f"Top tier co-op program ({det.internship_program_score:.1f}% score). {det.placement.placement_rate_pct:.1f}% placement rate, {det.conversion.intern_to_fulltime_offer_pct}% full-time conversion, ${det.stipend.avg_hourly_stipend_usd}/hr avg stipend.",
            "key_internship_strengths": [f"{det.stipend.paid_internships_pct}% paid internships with highest stipends in {det.stipend.highest_stipend_domain}", f"{det.employer_satisfaction.employer_csat_pct}% employer CSAT with {det.employer_satisfaction.employer_rehire_intent_pct}% rehire intent"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Director of Experiential Learning", "internships, co-ops, employer relations, academic credit"),
                                          PromptBuilder.build_user_context({"score": det.internship_program_score}), task_type="internship_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicInternshipNarrative(internship_summary=parsed.get("internship_summary", fallback["internship_summary"]),
                                                key_internship_strengths=parsed.get("key_internship_strengths", fallback["key_internship_strengths"]))
        except Exception:
            return StrategicInternshipNarrative(**fallback)

class InternshipProgramPlannerAgent(BaseAgent):
    """Agent 9: Generates co-op expansion strategies and internship agreement contract templates."""
    def __init__(self):
        super().__init__(agent_id="internship_program_planner", name="Internship Program Planner Agent",
                         description="Formulates corporate partner co-op agreements and student learning outcome rubrics.", icon="FileCheck")

    async def plan_program(self, det: DeterministicInternshipPipelineResult) -> InternshipProgramPlan:
        fallback = {
            "program_expansion_actions": [f"Partner with 20 new high-growth tech startups to increase placement rate beyond {det.placement.placement_rate_pct:.0f}%", "Launch Mid-Term Internship Performance Review system for early intervention"],
            "sample_internship_agreement_template": "MEMORANDUM OF UNDERSTANDING\nBetween: CampusOS University & Partner Employer\nTerms:\n  1. Work Term: 12-16 weeks\n  2. Minimum Compensation: $25.00/hour\n  3. Learning Objectives: Approved by Academic Advisor\n  4. Mid-Term & Final Evaluation: Required for academic credit grant\n  5. IP Rights: Retained by Employer per standard agreement"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Corporate Partnerships Director", "co-op agreements, student placements, MOU"),
                                          PromptBuilder.build_user_context({"placed": det.placement.placed_students_count}), task_type="internship_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return InternshipProgramPlan(program_expansion_actions=parsed.get("program_expansion_actions", fallback["program_expansion_actions"]),
                                         sample_internship_agreement_template=parsed.get("sample_internship_agreement_template", fallback["sample_internship_agreement_template"]))
        except Exception:
            return InternshipProgramPlan(**fallback)
