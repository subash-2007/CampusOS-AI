from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.university_campus_relations.schemas import (
    StrategicCampusNarrative, CampusRelationsPlan, ReasoningCampusPipelineResult, DeterministicCampusPipelineResult
)

class StrategicCampusNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates university partnership strength, campus fair engagement, and MOU retention."""
    def __init__(self):
        super().__init__(agent_id="strategic_campus_narrative", name="Strategic Campus Narrative Agent",
                         description="Evaluates university partner counts, placement outcomes, MOU renewal rates, and student adoption.", icon="Landmark")

    async def evaluate(self, det: DeterministicCampusPipelineResult) -> StrategicCampusNarrative:
        fallback = {
            "campus_summary": f"Strategic academic partner network ({det.campus_relations_score:.1f}% score). {det.partners.total_partner_universities} partner universities, {det.placement.overall_campus_placement_rate_pct}% placement rate, {det.mou.mou_renewal_rate_pct}% MOU renewal.",
            "key_campus_strengths": [f"{det.fairs.career_fairs_hosted_annual} annual career fairs reaching {det.fairs.student_attendees_total:,} students across {det.fairs.employer_booths_total} employer booths", f"{det.student_engagement.student_platform_adoption_pct}% student platform adoption with {det.student_engagement.career_center_appointments_booked:,} career center bookings"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Head of University Relations", "campus recruiting, MOUs, career centers, university partnerships"),
                                          PromptBuilder.build_user_context({"score": det.campus_relations_score}), task_type="campus_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicCampusNarrative(campus_summary=parsed.get("campus_summary", fallback["campus_summary"]),
                                           key_campus_strengths=parsed.get("key_campus_strengths", fallback["key_campus_strengths"]))
        except Exception:
            return StrategicCampusNarrative(**fallback)

class CampusRelationsPlannerAgent(BaseAgent):
    """Agent 9: Generates university expansion plans and MOU agreement contract templates."""
    def __init__(self):
        super().__init__(agent_id="campus_relations_planner", name="Campus Relations Planner Agent",
                         description="Formulates university onboarding roadmaps and academic alliance MOU frameworks.", icon="FileText")

    async def plan_relations(self, det: DeterministicCampusPipelineResult) -> CampusRelationsPlan:
        fallback = {
            "university_expansion_actions": [f"Expand Tier-1 university partner network from {det.partners.tier1_universities_count} to 50 top-ranked engineering schools", "Launch Virtual Hybrid Career Fair module for remote student participation"],
            "sample_mou_agreement_summary": "UNIVERSITY ALLIANCE AGREEMENT\nBetween: CampusOS AI Platform & Partner Institution\nKey Terms:\n  1. Campus-wide AI Career Agent Access for all enrolled students\n  2. Dedicated Career Center Admin Dashboard & Analytics\n  3. Joint Annual Career Fair Co-Hosting Rights\n  4. Data Protection: FERPA & GDPR compliant student data privacy guarantee"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Academic Alliances Manager", "MOU, FERPA compliance, career center integration"),
                                          PromptBuilder.build_user_context({"universities": det.partners.total_partner_universities}), task_type="campus_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return CampusRelationsPlan(university_expansion_actions=parsed.get("university_expansion_actions", fallback["university_expansion_actions"]),
                                       sample_mou_agreement_summary=parsed.get("sample_mou_agreement_summary", fallback["sample_mou_agreement_summary"]))
        except Exception:
            return CampusRelationsPlan(**fallback)
