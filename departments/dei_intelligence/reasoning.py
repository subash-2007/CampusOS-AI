from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.dei_intelligence.schemas import (
    StrategicDEINarrative, DEIActionPlan, ReasoningDEIPipelineResult, DeterministicDEIPipelineResult
)

class StrategicDEINarrativeAgent(BaseAgent):
    """Agent 8: Evaluates campus diversity equity representation, bias incident response, and inclusive curriculum integration."""
    def __init__(self):
        super().__init__(agent_id="strategic_dei_narrative", name="Strategic DEI Narrative Agent",
                         description="Evaluates underrepresented minority representation, faculty hiring diversity, bias response resolution, and inclusive pedagogy.", icon="Users")

    async def evaluate(self, det: DeterministicDEIPipelineResult) -> StrategicDEINarrative:
        fallback = {
            "dei_summary": f"National model for inclusive excellence ({det.dei_score:.1f}% score). {det.demographics.underrepresented_minority_students_pct}% underrepresented minority students, {det.demographics.first_gen_college_students_pct}% first-generation college students, {det.bias_response.bias_response_team_resolution_pct}% bias incident resolution rate within {det.bias_response.avg_resolution_days:.1f} days.",
            "key_dei_strengths": [f"${det.scholarships.dei_scholastic_funding_usd/1e6:.2f}M in diversity scholarship funding awarded to {det.scholarships.diversity_scholars_count} scholars", f"{det.inclusive_curriculum.courses_with_dei_designation} DEI-designated courses taught by {det.inclusive_curriculum.inclusive_pedagogy_trained_faculty} trained faculty members"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Vice President for Diversity Equity & Inclusion", "inclusive excellence, faculty diversity hiring, bias response, first-generation student success"),
                                          PromptBuilder.build_user_context({"score": det.dei_score}), task_type="dei_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicDEINarrative(dei_summary=parsed.get("dei_summary", fallback["dei_summary"]),
                                        key_dei_strengths=parsed.get("key_dei_strengths", fallback["key_dei_strengths"]))
        except Exception:
            return StrategicDEINarrative(**fallback)

class DEIActionPlannerAgent(BaseAgent):
    """Agent 9: Generates inclusive faculty hiring rubrics and campus climate survey response frameworks."""
    def __init__(self):
        super().__init__(agent_id="dei_action_planner", name="DEI Action Planner Agent",
                         description="Formulates inclusive faculty search protocols, cultural center expansion blueprints, and bias reporting transparency dashboards.", icon="CheckSquare")

    async def plan_dei(self, det: DeterministicDEIPipelineResult) -> DEIActionPlan:
        fallback = {
            "dei_improvement_actions": ["Establish Inclusive Excellence Faculty Fellowship to recruit and retain top underrepresented scholar-educators", "Launch Annual Campus Climate Survey & Real-Time Bias Transparency Dashboard"],
            "sample_inclusive_hiring_rubric": "FACULTY SEARCH COMMITTEE INCLUSIVE HIRING EVALUATION RUBRIC\nMandatory Criteria:\n  1. Inclusive Pedagogy Statement: Demonstrated track record of supporting diverse learners (Scored 1-5)\n  2. Diversity Search Training: 100% committee completion of implicit bias mitigation workshop\n  3. Diverse Shortlist Audit: Mandatory Dean review of candidate pool diversity before campus interviews\n  4. Mentorship Plan: Formal onboarding & tenure-track mentorship assignment upon hire"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("DEI Strategy Director", "inclusive hiring rubric, campus climate, bias transparency"),
                                          PromptBuilder.build_user_context({"urm_pct": det.demographics.underrepresented_minority_students_pct}), task_type="dei_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return DEIActionPlan(dei_improvement_actions=parsed.get("dei_improvement_actions", fallback["dei_improvement_actions"]),
                                 sample_inclusive_hiring_rubric=parsed.get("sample_inclusive_hiring_rubric", fallback["sample_inclusive_hiring_rubric"]))
        except Exception:
            return DEIActionPlan(**fallback)
