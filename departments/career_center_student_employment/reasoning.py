from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.career_center_student_employment.schemas import (
    StrategicCareerCenterNarrative, CareerDevelopmentPlan, ReasoningCareerCenterPipelineResult, DeterministicCareerCenterPipelineResult
)

class StrategicCareerCenterNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates career fair employer attendance, on-campus student employment, and NACE first destination outcome rates."""
    def __init__(self):
        super().__init__(agent_id="strategic_career_center_narrative", name="Strategic Career Center Narrative Agent",
                         description="Evaluates career fair employer engagement, Federal Work-Study payroll compliance, 1-on-1 career coaching volume, and 6-month post-grad placement rates.", icon="Briefcase")

    async def evaluate(self, det: DeterministicCareerCenterPipelineResult) -> StrategicCareerCenterNarrative:
        fallback = {
            "career_center_summary": f"Top-tier national career & employment center ({det.career_center_score:.1f}% score). {det.outcomes.employed_or_grad_school_at_6_months_pct}% 6-month placement rate (${det.outcomes.avg_starting_salary_usd:,.0f} average starting salary), {det.fairs.participating_employers_count} employers attending campus career fairs, {det.employment.student_employees_hired_on_campus:,} on-campus student employees hired.",
            "key_career_center_strengths": [f"100% student employment payroll compliance across ${det.employment.federal_work_study_fws_disbursed_usd/1e6:.1f}M in FWS disbursements", f"{det.advising.one_on_one_career_coaching_appointments:,} 1-on-1 career coaching appointments with {det.advising.advising_csat_score:.2f}/5.0 CSAT rating and {det.advising.resume_critique_turnaround_hours:.1f}-hour resume review turnaround"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Assistant Vice President for Student Career Success & Employment", "career fairs, FWS payroll, first destination outcomes, Handshake recruiting, mock interviews"),
                                          PromptBuilder.build_user_context({"score": det.career_center_score}), task_type="career_center_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicCareerCenterNarrative(career_center_summary=parsed.get("career_center_summary", fallback["career_center_summary"]),
                                                 key_career_center_strengths=parsed.get("key_career_center_strengths", fallback["key_career_center_strengths"]))
        except Exception:
            return StrategicCareerCenterNarrative(**fallback)

class CareerDevelopmentPlannerAgent(BaseAgent):
    """Agent 9: Formulates AI mock interview simulations and on-campus student worker onboarding roadmaps."""
    def __init__(self):
        super().__init__(agent_id="career_development_planner", name="Career Development Planner Agent",
                         description="Formulates AI-powered video interview practice tools, automated FWS timecard verification, and employer sponsorship career fair packages.", icon="Compass")

    async def plan_career_development(self, det: DeterministicCareerCenterPipelineResult) -> CareerDevelopmentPlan:
        fallback = {
            "career_actions": ["Deploy Smart AI Technical & Behavioral Mock Interview Simulator with real-time feedback", "Launch Instant On-Campus Student Worker Payroll Onboarding Portal"],
            "sample_first_destination_survey_schema": '{\n  "graduate_id": "grad_88190",\n  "graduation_term": "Spring 2026",\n  "degree": "BS Mechanical Engineering",\n  "primary_outcome": "EMPLOYED FULL-TIME",\n  "employer_details": {\n    "company_name": "Boeing Aerospace",\n    "job_title": "Systems Test Engineer",\n    "location": "Seattle, WA",\n    "starting_salary_usd": 84500.00,\n    "signing_bonus_usd": 7500.00,\n    "hiring_source": "CampusOS Spring Engineering Career Fair"\n  },\n  "survey_status": "VERIFIED & CONFIRMED AT 3 MONTHS POST-GRADUATION"\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Career Center Operations Director & Employer Relations Manager", "first destination survey, AI mock interview, student employment portal"),
                                          PromptBuilder.build_user_context({"employers": det.fairs.participating_employers_count}), task_type="career_center_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return CareerDevelopmentPlan(career_actions=parsed.get("career_actions", fallback["career_actions"]),
                                        sample_first_destination_survey_schema=parsed.get("sample_first_destination_survey_schema", fallback["sample_first_destination_survey_schema"]))
        except Exception:
            return CareerDevelopmentPlan(**fallback)
