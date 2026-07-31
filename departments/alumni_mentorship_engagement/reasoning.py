from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.alumni_mentorship_engagement.schemas import (
    StrategicAlumniNarrative, AlumniEngagementPlan, ReasoningAlumniPipelineResult, DeterministicAlumniPipelineResult
)

class StrategicAlumniNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates alumni network strength, mentorship pairing success, and donation giving trends."""
    def __init__(self):
        super().__init__(agent_id="strategic_alumni_narrative", name="Strategic Alumni Narrative Agent",
                         description="Evaluates alumni network size, mentorship match success, donations, and career referrals.", icon="Users")

    async def evaluate(self, det: DeterministicAlumniPipelineResult) -> StrategicAlumniNarrative:
        fallback = {
            "alumni_summary": f"Highly engaged alumni network ({det.alumni_engagement_score:.1f}% score). {det.network_size.registered_alumni_count:,} registered alumni, {det.mentorship.active_mentorship_pairs:,} active mentorship pairs ({det.mentorship.match_success_rate_pct}% match success), ${det.donations.annual_alumni_donations_usd/1e6:.2f}M annual giving.",
            "key_alumni_strengths": [f"{det.career_transitions.alumni_hiring_students_count} students hired directly by alumni with {det.career_transitions.alumni_job_referrals_made:,} referrals made", f"{det.chapters.regional_chapters_count} regional chapters and {det.chapters.global_city_hubs_count} global city hubs"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("VP of Alumni Relations & Development", "alumni mentorship, annual giving, alumni networking, career referrals"),
                                          PromptBuilder.build_user_context({"score": det.alumni_engagement_score}), task_type="alumni_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicAlumniNarrative(alumni_summary=parsed.get("alumni_summary", fallback["alumni_summary"]),
                                            key_alumni_strengths=parsed.get("key_alumni_strengths", fallback["key_alumni_strengths"]))
        except Exception:
            return StrategicAlumniNarrative(**fallback)

class AlumniEngagementPlannerAgent(BaseAgent):
    """Agent 9: Generates alumni mentorship expansion programs and intelligent matching algorithms."""
    def __init__(self):
        super().__init__(agent_id="alumni_engagement_planner", name="Alumni Engagement Planner Agent",
                         description="Formulates alumni-student mentorship matching criteria and regional chapter expansion.", icon="UserCheck")

    async def plan_engagement(self, det: DeterministicAlumniPipelineResult) -> AlumniEngagementPlan:
        fallback = {
            "engagement_growth_actions": [f"Launch 'Alumni Career Spotlight' webinar series featuring top leaders from {det.chapters.global_city_hubs_count} global hubs", "Implement AI-powered micro-mentorship matching for 15-minute quick career advice calls"],
            "sample_mentorship_matching_rules": "MENTORSHIP MATCHING ALGORITHM:\nWeighting Matrix:\n  - Target Industry & Functional Domain: 40%\n  - Shared Academic Major / Department: 25%\n  - Geographic Proximity / Chapter Hub: 20%\n  - Shared Extracurricular Interests: 15%\nThreshold: Minimum match score of 80% required for auto-pairing recommendation"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Alumni Engagement Strategist", "mentorship algorithms, chapter events, donor engagement"),
                                          PromptBuilder.build_user_context({"pairs": det.mentorship.active_mentorship_pairs}), task_type="alumni_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return AlumniEngagementPlan(engagement_growth_actions=parsed.get("engagement_growth_actions", fallback["engagement_growth_actions"]),
                                        sample_mentorship_matching_rules=parsed.get("sample_mentorship_matching_rules", fallback["sample_mentorship_matching_rules"]))
        except Exception:
            return AlumniEngagementPlan(**fallback)
