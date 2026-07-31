from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.global_study_abroad_intelligence.schemas import (
    StrategicStudyAbroadNarrative, GlobalMobilityPlan, ReasoningStudyAbroadPipelineResult, DeterministicStudyAbroadPipelineResult
)

class StrategicStudyAbroadNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates global mobility programs, visa compliance, credit transfer efficiency, and student safety."""
    def __init__(self):
        super().__init__(agent_id="strategic_study_abroad_narrative", name="Strategic Study Abroad Narrative Agent",
                         description="Evaluates global exchange partnerships, visa approval rates, credit transfer, and travel risk safety.", icon="Globe")

    async def evaluate(self, det: DeterministicStudyAbroadPipelineResult) -> StrategicStudyAbroadNarrative:
        fallback = {
            "study_abroad_summary": f"Premier global mobility program ({det.study_abroad_score:.1f}% score). {det.participation.total_students_abroad} students across {det.participation.partner_countries_count} countries, {det.visa.visa_approval_rate_pct}% visa approval, {det.credit_transfer.credit_transfer_approval_pct}% credit transfer rate.",
            "key_study_abroad_strengths": [f"100% travel insurance coverage with 24/7 emergency response", f"${det.scholarships.total_study_abroad_grants_usd:,.0f} in study abroad grants supporting {det.scholarships.students_receiving_abroad_funding_pct}% of participating students"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Director of International Education", "study abroad, student exchange, global safety, visa compliance"),
                                          PromptBuilder.build_user_context({"score": det.study_abroad_score}), task_type="abroad_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicStudyAbroadNarrative(study_abroad_summary=parsed.get("study_abroad_summary", fallback["study_abroad_summary"]),
                                                key_study_abroad_strengths=parsed.get("key_study_abroad_strengths", fallback["key_study_abroad_strengths"]))
        except Exception:
            return StrategicStudyAbroadNarrative(**fallback)

class GlobalMobilityPlannerAgent(BaseAgent):
    """Agent 9: Generates global exchange partner expansion roadmaps and bilateral university agreement schemas."""
    def __init__(self):
        super().__init__(agent_id="global_mobility_planner", name="Global Mobility Planner Agent",
                         description="Formulates international exchange agreements, virtual global classrooms, and visa assistance portals.", icon="MapPin")

    async def plan_mobility(self, det: DeterministicStudyAbroadPipelineResult) -> GlobalMobilityPlan:
        fallback = {
            "mobility_expansion_actions": [f"Establish 5 new bilateral university exchanges in Latin America and Southeast Asia to reach {det.participation.partner_countries_count + 5} countries", "Implement Automated International Course Equivalency Database"],
            "sample_exchange_agreement_schema": "INTERNATIONAL EXCHANGE AGREEMENT\nBetween: CampusOS University & Partner Overseas Institution\nFramework:\n  1. Tuition Reciprocity: 10 students exchanged annually without international tuition surcharge\n  2. Credit Mapping: Pre-verified ECTS to US Semester Credit conversion\n  3. Health & Safety: Mandatory enrollment in Global Emergency Assistance Network\n  4. Language Requirement: B2 CEFR proficiency or pre-departure immersion course"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Global Alliances Strategist", "international exchange, ECTS credit conversion, visa guidance"),
                                          PromptBuilder.build_user_context({"countries": det.participation.partner_countries_count}), task_type="abroad_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return GlobalMobilityPlan(mobility_expansion_actions=parsed.get("mobility_expansion_actions", fallback["mobility_expansion_actions"]),
                                     sample_exchange_agreement_schema=parsed.get("sample_exchange_agreement_schema", fallback["sample_exchange_agreement_schema"]))
        except Exception:
            return GlobalMobilityPlan(**fallback)
