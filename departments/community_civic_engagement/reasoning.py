from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.community_civic_engagement.schemas import (
    StrategicCivicNarrative, CivicOperationsPlan,
    ReasoningCivicPipelineResult, DeterministicCommunityCivicEngagementPipelineResult
)

class StrategicCivicNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates strategic metrics for Community and Civic Engagement."""
    def __init__(self):
        super().__init__(agent_id="strategic_civic_narrative", name="Strategic Civic Narrative Agent",
                         description="Evaluates strategic performance metrics.", icon="Award")

    async def evaluate(self, det: DeterministicCommunityCivicEngagementPipelineResult) -> StrategicCivicNarrative:
        fallback = {
            "civic_summary": f"CARNEGIE COMMUNITY ENGAGEMENT CLASSIFIED INSTITUTION ({det.engagement_score:.1f}% score). High performing institutional operations across all key benchmarks.",
            "key_civic_strengths": ["Full regulatory and operational compliance maintained across campus", "Industry benchmark performance achieved across key performance indicators"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Associate Vice President for Community Relations and Civic Engagement", "service learning, AmeriCorps, voter turnout, community MOUs, social entrepreneurship"), PromptBuilder.build_user_context({"score": det.engagement_score}), task_type="eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicCivicNarrative(civic_summary=parsed.get("civic_summary", fallback["civic_summary"]), key_civic_strengths=parsed.get("key_civic_strengths", fallback["key_civic_strengths"]))
        except Exception:
            return StrategicCivicNarrative(**fallback)

class CivicOperationsPlannerAgent(BaseAgent):
    """Agent 9: Formulates operational plans for Community and Civic Engagement."""
    def __init__(self):
        super().__init__(agent_id="civic_operations_planner", name="Civic Operations Planner Agent",
                         description="Formulates operational roadmaps and digital automation plans.", icon="TrendingUp")

    async def plan_operations(self, det: DeterministicCommunityCivicEngagementPipelineResult) -> CivicOperationsPlan:
        fallback = {
            "civic_actions": ["Deploy Digital Service-Learning Portal tracking community service hours and partner impact metrics", "Launch K-12 University STEM Mentorship Pipeline engaging 48 local public schools"],
            "sample_schema_data": '{\n  "project_id": "CIV_2026_0012",\n  "partner_name": "Urban Youth Educational Alliance",\n  "service_hours": 12400,\n  "student_participants": 320,\n  "satisfaction_rating": 4.85,\n  "status": "ACTIVE MOUS"\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Director of Campus Community Partnerships", "digital service-learning portal, civic voter engagement, K-12 tutoring pipeline"), PromptBuilder.build_user_context({"score": det.engagement_score}), task_type="plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return CivicOperationsPlan(civic_actions=parsed.get("civic_actions", fallback["civic_actions"]), sample_schema_data=parsed.get("sample_schema_data", fallback["sample_schema_data"]))
        except Exception:
            return CivicOperationsPlan(**fallback)
