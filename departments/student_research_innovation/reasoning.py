from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.student_research_innovation.schemas import (
    StrategicInnovationNarrative, InnovationIncubatorPlan, ReasoningInnovationPipelineResult, DeterministicInnovationPipelineResult
)

class StrategicInnovationNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates undergraduate research program depth, student startup incubator outcomes, and patent/tech transfer productivity."""
    def __init__(self):
        super().__init__(agent_id="strategic_innovation_narrative", name="Strategic Innovation Narrative Agent",
                         description="Evaluates undergraduate research mentoring, startup incubator seed funding, patent filing output, makerspace utilization, and industry research partnership revenue.", icon="Zap")

    async def evaluate(self, det: DeterministicInnovationPipelineResult) -> StrategicInnovationNarrative:
        fallback = {
            "innovation_summary": f"Nationally ranked student innovation ecosystem ({det.innovation_score:.1f}% score). Supporting {det.undergrad_research.undergraduate_researchers_active:,} active undergraduate researchers across {det.undergrad_research.faculty_mentored_research_projects} faculty-mentored projects, {det.incubator.student_startups_in_incubator} student startups with ${det.incubator.seed_funding_awarded_total_usd:,.0f} total seed funding.",
            "key_innovation_strengths": [f"{det.patents.patents_filed_annual} patents filed generating ${det.patents.tech_transfer_royalties_usd:,.0f} tech transfer royalties from {det.patents.technology_licenses_executed} technology licenses", f"{det.industry.industry_research_partnership_agreements} industry research partnerships generating ${det.industry.sponsored_research_revenue_millions:.1f}M sponsored research revenue with {det.industry.collaborative_publications_with_industry} collaborative publications"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Vice Provost for Research & Innovation Ecosystems", "undergraduate research, startup incubator, patents, tech transfer, makerspace, industry partnerships"),
                                          PromptBuilder.build_user_context({"score": det.innovation_score}), task_type="innovation_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicInnovationNarrative(innovation_summary=parsed.get("innovation_summary", fallback["innovation_summary"]),
                                               key_innovation_strengths=parsed.get("key_innovation_strengths", fallback["key_innovation_strengths"]))
        except Exception:
            return StrategicInnovationNarrative(**fallback)

class InnovationIncubatorPlannerAgent(BaseAgent):
    """Agent 9: Formulates AI-powered startup ideation tools and industry co-innovation lab investment strategies."""
    def __init__(self):
        super().__init__(agent_id="innovation_incubator_planner", name="Innovation Incubator Planner Agent",
                         description="Formulates AI venture evaluation tools, corporate innovation partnership programs, and student IP portfolio management frameworks.", icon="TrendingUp")

    async def plan_innovation(self, det: DeterministicInnovationPipelineResult) -> InnovationIncubatorPlan:
        fallback = {
            "innovation_actions": ["Launch AI Startup Viability Assessment Tool evaluating market size, competitive landscape, and IP landscape for all incubator applicants", "Deploy Industry Co-Innovation Lab Partnership bringing corporate R&D engineers into campus maker facilities"],
            "sample_startup_pitch_deck_schema": '{\n  "startup_id": "INC_2026_0042",\n  "startup_name": "NeuralFarm AI",\n  "founders": ["Alex Chen (CS, Senior)", "Priya Patel (Data Science, Junior)"],\n  "sector": "AgriTech / Precision Agriculture AI",\n  "problem": "Small-scale farmers lose 32% of crop yield annually to preventable disease and pest outbreaks",\n  "solution": "Computer vision drone AI detecting crop disease 14 days earlier than visual inspection",\n  "traction": "$48K pre-revenue LOIs from 3 regional farm cooperatives",\n  "seed_funding_requested": "$75,000",\n  "incubator_status": "ACCEPTED - Innovation Lab Cohort 4 (Spring 2027)"\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Chief Innovation Officer & Venture Development Director", "startup incubator, tech transfer, AI evaluation, industry co-innovation lab"),
                                          PromptBuilder.build_user_context({"startups": det.incubator.student_startups_in_incubator}), task_type="innovation_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return InnovationIncubatorPlan(innovation_actions=parsed.get("innovation_actions", fallback["innovation_actions"]),
                                           sample_startup_pitch_deck_schema=parsed.get("sample_startup_pitch_deck_schema", fallback["sample_startup_pitch_deck_schema"]))
        except Exception:
            return InnovationIncubatorPlan(**fallback)
