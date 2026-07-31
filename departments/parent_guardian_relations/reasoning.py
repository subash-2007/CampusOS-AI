from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.parent_guardian_relations.schemas import (
    StrategicParentNarrative, FamilyEngagementPlan, ReasoningParentPipelineResult, DeterministicParentPipelineResult
)

class StrategicParentNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates family engagement metrics, FERPA compliance safety, and parent fundraising."""
    def __init__(self):
        super().__init__(agent_id="strategic_parent_narrative", name="Strategic Parent Narrative Agent",
                         description="Evaluates parent portal adoption, FERPA privacy compliance, newsletter readership, and family support.", icon="Users")

    async def evaluate(self, det: DeterministicParentPipelineResult) -> StrategicParentNarrative:
        fallback = {
            "parent_summary": f"Highly engaged family network ({det.parent_relations_score:.1f}% score). {det.portal.registered_parents_count:,} registered parents, {det.ferpa.ferpa_compliance_pct}% FERPA compliance, {det.emergency.emergency_contact_verification_pct}% emergency contact verification.",
            "key_parent_strengths": [f"{det.newsletter.avg_open_rate_pct}% family newsletter open rate across {det.newsletter.newsletter_subscribers_count:,} subscribers", f"${det.donations.family_fund_donations_usd:,.0f} in Family Fund contributions from {det.donations.parent_donor_count} parent donors"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Director of Parent & Family Programs", "FERPA, parent orientation, family weekend, emergency communication"),
                                          PromptBuilder.build_user_context({"score": det.parent_relations_score}), task_type="parent_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicParentNarrative(parent_summary=parsed.get("parent_summary", fallback["parent_summary"]),
                                            key_parent_strengths=parsed.get("key_parent_strengths", fallback["key_parent_strengths"]))
        except Exception:
            return StrategicParentNarrative(**fallback)

class FamilyEngagementPlannerAgent(BaseAgent):
    """Agent 9: Generates family weekend event plans and FERPA digital waiver consent workflows."""
    def __init__(self):
        super().__init__(agent_id="family_engagement_planner", name="Family Engagement Planner Agent",
                         description="Formulates family weekend programming, parent advisory board structures, and FERPA consent forms.", icon="Heart")

    async def plan_engagement(self, det: DeterministicParentPipelineResult) -> FamilyEngagementPlan:
        fallback = {
            "engagement_actions": ["Launch Annual Family Weekend with 20+ campus workshops and faculty receptions", "Implement One-Click Digital FERPA Portal for granular student data sharing permissions"],
            "sample_ferpa_waiver_schema": '{\n  "student_id": "std_10924",\n  "granted_to": "parent_guardian",\n  "parent_email": "parent@example.com",\n  "scopes": [\n    "academic_grades",\n    "financial_aid_billing",\n    "housing_status"\n  ],\n  "expiration_date": "2027-05-31",\n  "signature_timestamp": "2026-08-15T10:30:00Z"\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Family Relations Strategist", "FERPA permissions, parent webinars, campus events"),
                                          PromptBuilder.build_user_context({"parents": det.portal.registered_parents_count}), task_type="parent_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return FamilyEngagementPlan(engagement_actions=parsed.get("engagement_actions", fallback["engagement_actions"]),
                                        sample_ferpa_waiver_schema=parsed.get("sample_ferpa_waiver_schema", fallback["sample_ferpa_waiver_schema"]))
        except Exception:
            return FamilyEngagementPlan(**fallback)
