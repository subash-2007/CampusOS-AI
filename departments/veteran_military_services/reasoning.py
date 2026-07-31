from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.veteran_military_services.schemas import (
    StrategicVeteranNarrative, VeteranTransitionPlan, ReasoningVeteranServicesPipelineResult, DeterministicVeteranServicesPipelineResult
)

class StrategicVeteranNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates military student support, GI Bill processing accuracy, and civilian career transition outcomes."""
    def __init__(self):
        super().__init__(agent_id="strategic_veteran_narrative", name="Strategic Veteran Narrative Agent",
                         description="Evaluates veteran enrollment, GI Bill certification speed, Yellow Ribbon funding, and military career placement.", icon="Award")

    async def evaluate(self, det: DeterministicVeteranServicesPipelineResult) -> StrategicVeteranNarrative:
        fallback = {
            "veteran_summary": f"Military friendly top-ten campus ({det.veteran_services_score:.1f}% score). Serving {det.enrollment.veteran_students_count} veteran students and {det.enrollment.active_duty_military_count} active duty military personnel with {det.gi_bill.gi_bill_compliance_pct}% GI Bill compliance ({det.gi_bill.avg_certification_speed_days:.1f}-day certification turnaround).",
            "key_veteran_strengths": [f"${det.yellow_ribbon.yellow_ribbon_funding_usd:,.0f} in Yellow Ribbon institutional tuition support granted to {det.yellow_ribbon.yellow_ribbon_recipients_count} recipients", f"{det.outcomes.veteran_career_placement_rate_pct}% 6-month career placement rate with average {det.jst.military_credits_awarded_avg:.1f} JST transfer credits awarded"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Director of Military & Veteran Student Services", "GI Bill, Yellow Ribbon, JST credit transfer, military career transition"),
                                          PromptBuilder.build_user_context({"score": det.veteran_services_score}), task_type="veteran_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicVeteranNarrative(veteran_summary=parsed.get("veteran_summary", fallback["veteran_summary"]),
                                            key_veteran_strengths=parsed.get("key_veteran_strengths", fallback["key_veteran_strengths"]))
        except Exception:
            return StrategicVeteranNarrative(**fallback)

class VeteranTransitionPlannerAgent(BaseAgent):
    """Agent 9: Generates military-to-civilian career transition roadmaps and GI Bill automated certification forms."""
    def __init__(self):
        super().__init__(agent_id="veteran_transition_planner", name="Veteran Transition Planner Agent",
                         description="Formulates military credit conversion rubrics, defense industry networking events, and VA benefit workflows.", icon="Compass")

    async def plan_transition(self, det: DeterministicVeteranServicesPipelineResult) -> VeteranTransitionPlan:
        fallback = {
            "transition_actions": ["Establish Defense & Aerospace Industry Veteran Career Accelerator Program", "Implement Automated VA Certifying Official Portal to process GI Bill claims in under 24 hours"],
            "sample_gi_bill_verification_form": "VA FORM 22-1999 ENROLLMENT CERTIFICATION\nStudent ID: vet_90124\nService Branch: US Marine Corps (Veteran)\nBenefit Program: Post-9/11 GI Bill (Chapter 33) - 100% Rate\nTerm: Fall Semester 2026 (15 Credit Hours)\nTuition & Fees: $12,450.00 USD\nYellow Ribbon Match: $3,250.00 USD (University) / $3,250.00 USD (VA)\nCertification Status: APPROVED & SUBMITTED TO VA"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("VA Certifying Official & Veteran Career Advisor", "GI Bill certification, military resume translation, veteran mentoring"),
                                          PromptBuilder.build_user_context({"veterans": det.enrollment.veteran_students_count}), task_type="veteran_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return VeteranTransitionPlan(transition_actions=parsed.get("transition_actions", fallback["transition_actions"]),
                                        sample_gi_bill_verification_form=parsed.get("sample_gi_bill_verification_form", fallback["sample_gi_bill_verification_form"]))
        except Exception:
            return VeteranTransitionPlan(**fallback)
