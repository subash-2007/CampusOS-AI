from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.high_school_outreach.schemas import (
    StrategicOutreachNarrative, OutreachExpansionPlan, ReasoningOutreachPipelineResult, DeterministicOutreachPipelineResult
)

class StrategicOutreachNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates K-12 pipeline strength, dual enrollment matriculation, and STEM diversity."""
    def __init__(self):
        super().__init__(agent_id="strategic_outreach_narrative", name="Strategic Outreach Narrative Agent",
                         description="Evaluates high school partnership counts, STEM camp participation, and dual enrollment conversion.", icon="Compass")

    async def evaluate(self, det: DeterministicOutreachPipelineResult) -> StrategicOutreachNarrative:
        fallback = {
            "outreach_summary": f"Strategic pipeline feeder network ({det.outreach_health_score:.1f}% score). {det.partnerships.partner_high_schools_count} partner high schools, {det.dual_enrollment.dual_enrollment_students_count} dual enrollment students ({det.dual_enrollment.matriculation_rate_post_hs_pct}% matriculation), {det.stem_programs.k12_student_participants:,} STEM camp participants.",
            "key_outreach_strengths": [f"{det.stem_programs.female_minority_stem_pct}% female & underrepresented minority participation in STEM camps", f"{det.tours.high_school_tours_hosted} campus tours reaching {det.tours.total_hs_visitors:,} high school visitors"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Director of K-12 Partnerships", "high school recruitment, STEM camps, dual enrollment, Title 1 outreach"),
                                          PromptBuilder.build_user_context({"score": det.outreach_health_score}), task_type="outreach_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicOutreachNarrative(outreach_summary=parsed.get("outreach_summary", fallback["outreach_summary"]),
                                             key_outreach_strengths=parsed.get("key_outreach_strengths", fallback["key_outreach_strengths"]))
        except Exception:
            return StrategicOutreachNarrative(**fallback)

class OutreachExpansionPlannerAgent(BaseAgent):
    """Agent 9: Generates high school outreach expansion roadmaps and dual enrollment MOU agreements."""
    def __init__(self):
        super().__init__(agent_id="outreach_expansion_planner", name="Outreach Expansion Planner Agent",
                         description="Formulates high school counselor summits, mobile STEM labs, and early college MOU frameworks.", icon="Award")

    async def plan_expansion(self, det: DeterministicOutreachPipelineResult) -> OutreachExpansionPlan:
        fallback = {
            "outreach_growth_actions": [f"Partner with 30 additional Title-1 high schools to expand STEM pipeline grants beyond ${det.scholarships.k12_outreach_grants_awarded_usd/1e3:.0f}K", "Launch Virtual Dual Enrollment Pathway for rural high school students"],
            "sample_dual_enrollment_mou": "DUAL ENROLLMENT ARTICULATION AGREEMENT\nBetween: CampusOS University & High School District\nAgreement:\n  1. Offered Courses: Intro to Programming (CS101), College Algebra (MATH110)\n  2. Tuition Subsidy: 100% covered by University K-12 Outreach Fund\n  3. Credit Transfer: Guaranteed transcripted college credit upon completion with C or better\n  4. Automatic Admissions: Guarantee of undergraduate admission if GPA >= 3.2"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Early College Program Director", "dual enrollment MOU, K-12 STEM, college access"),
                                          PromptBuilder.build_user_context({"schools": det.partnerships.partner_high_schools_count}), task_type="outreach_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return OutreachExpansionPlan(outreach_growth_actions=parsed.get("outreach_growth_actions", fallback["outreach_growth_actions"]),
                                         sample_dual_enrollment_mou=parsed.get("sample_dual_enrollment_mou", fallback["sample_dual_enrollment_mou"]))
        except Exception:
            return OutreachExpansionPlan(**fallback)
