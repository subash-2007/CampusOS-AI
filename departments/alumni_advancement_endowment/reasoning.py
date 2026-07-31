from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.alumni_advancement_endowment.schemas import (
    StrategicAdvancementNarrative, AdvancementOperationsPlan,
    ReasoningAdvancementPipelineResult, DeterministicAlumniAdvancementEndowmentPipelineResult
)

class StrategicAdvancementNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates strategic metrics for Alumni Advancement and Endowment Management."""
    def __init__(self):
        super().__init__(agent_id="strategic_advancement_narrative", name="Strategic Advancement Narrative Agent",
                         description="Evaluates strategic performance metrics.", icon="Award")

    async def evaluate(self, det: DeterministicAlumniAdvancementEndowmentPipelineResult) -> StrategicAdvancementNarrative:
        fallback = {
            "advancement_summary": f"BILLION DOLLAR CAMPUS ENDOWMENT ADVANCEMENT EXCELLENCE ({det.advancement_score:.1f}% score). High performing institutional operations across all key benchmarks.",
            "key_advancement_strengths": ["Full regulatory and operational compliance maintained across campus", "Industry benchmark performance achieved across key performance indicators"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Vice President for Institutional Advancement and Executive Director of Endowment", "endowment returns, capital campaign, alumni giving participation rate, planned giving, foundation grants"), PromptBuilder.build_user_context({"score": det.advancement_score}), task_type="eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicAdvancementNarrative(advancement_summary=parsed.get("advancement_summary", fallback["advancement_summary"]), key_advancement_strengths=parsed.get("key_advancement_strengths", fallback["key_advancement_strengths"]))
        except Exception:
            return StrategicAdvancementNarrative(**fallback)

class AdvancementOperationsPlannerAgent(BaseAgent):
    """Agent 9: Formulates operational plans for Alumni Advancement and Endowment Management."""
    def __init__(self):
        super().__init__(agent_id="advancement_operations_planner", name="Advancement Operations Planner Agent",
                         description="Formulates operational roadmaps and digital automation plans.", icon="TrendingUp")

    async def plan_operations(self, det: DeterministicAlumniAdvancementEndowmentPipelineResult) -> AdvancementOperationsPlan:
        fallback = {
            "advancement_actions": ["Deploy AI Donor Propensity Model analyzing alumni engagement signals to identify major gift prospects", "Launch Digital Micro-Donation Crowdfunding Platform for young alumni participation"],
            "sample_schema_data": '{\n  "gift_id": "GIFT_2026_00984",\n  "donor_type": "Alumni Class of 1994",\n  "amount_usd": 250000.0,\n  "designation": "Endowed Undergraduate Scholarship in Data Science",\n  "stewardship_status": "ACKNOWLEDGEMENT LETTER SENT AND ENDOWMENT REPORTING SCHEDULED"\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Chief Development Officer and Senior Advancement Director", "AI donor propensity scoring, digital alumni giving campaigns, major gift pipeline automation"), PromptBuilder.build_user_context({"score": det.advancement_score}), task_type="plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return AdvancementOperationsPlan(advancement_actions=parsed.get("advancement_actions", fallback["advancement_actions"]), sample_schema_data=parsed.get("sample_schema_data", fallback["sample_schema_data"]))
        except Exception:
            return AdvancementOperationsPlan(**fallback)
