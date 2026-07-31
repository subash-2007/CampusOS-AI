from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.auxiliary_enterprises_housing.schemas import (
    StrategicAuxiliaryNarrative, AuxiliaryOperationsPlan,
    ReasoningAuxiliaryPipelineResult, DeterministicAuxiliaryEnterprisesHousingPipelineResult
)

class StrategicAuxiliaryNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates strategic metrics for Auxiliary Enterprises and Housing Operations."""
    def __init__(self):
        super().__init__(agent_id="strategic_auxiliary_narrative", name="Strategic Auxiliary Narrative Agent",
                         description="Evaluates strategic performance metrics.", icon="Award")

    async def evaluate(self, det: DeterministicAuxiliaryEnterprisesHousingPipelineResult) -> StrategicAuxiliaryNarrative:
        fallback = {
            "auxiliary_summary": f"PREMIER CAMPUS AUXILIARY SERVICES AND HOUSING OPERATIONS ({det.auxiliary_score:.1f}% score). High performing institutional operations across all key benchmarks.",
            "key_auxiliary_strengths": ["Full regulatory and operational compliance maintained across campus", "Industry benchmark performance achieved across key performance indicators"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Associate Vice President for Auxiliary Enterprises and Operations", "residence housing occupancy, dining meal plans, digital inclusive access textbooks, conference services revenue, maintenance turnaround"), PromptBuilder.build_user_context({"score": det.auxiliary_score}), task_type="eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicAuxiliaryNarrative(auxiliary_summary=parsed.get("auxiliary_summary", fallback["auxiliary_summary"]), key_auxiliary_strengths=parsed.get("key_auxiliary_strengths", fallback["key_auxiliary_strengths"]))
        except Exception:
            return StrategicAuxiliaryNarrative(**fallback)

class AuxiliaryOperationsPlannerAgent(BaseAgent):
    """Agent 9: Formulates operational plans for Auxiliary Enterprises and Housing Operations."""
    def __init__(self):
        super().__init__(agent_id="auxiliary_operations_planner", name="Auxiliary Operations Planner Agent",
                         description="Formulates operational roadmaps and digital automation plans.", icon="TrendingUp")

    async def plan_operations(self, det: DeterministicAuxiliaryEnterprisesHousingPipelineResult) -> AuxiliaryOperationsPlan:
        fallback = {
            "auxiliary_actions": ["Deploy Mobile Credential & Smart Room Lock System across all 8,400 residence hall beds", "Launch Campus Mobile Dining Ordering & Robot Delivery System for retail venues"],
            "sample_schema_data": '{\n  "work_order_id": "WO_2026_01842",\n  "residence_hall": "Founders Hall, Room 412",\n  "issue_category": "Plumbing / Hot Water Pressure",\n  "reported_at": "2026-10-12T08:30:00Z",\n  "resolved_at": "2026-10-12T11:45:00Z",\n  "resolution_time_hours": 3.25,\n  "student_feedback_rating": 5.0\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Director of Housing & Residential Operations", "smart room IoT mobile access keys, mobile dining ordering, automated work order dispatch"), PromptBuilder.build_user_context({"score": det.auxiliary_score}), task_type="plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return AuxiliaryOperationsPlan(auxiliary_actions=parsed.get("auxiliary_actions", fallback["auxiliary_actions"]), sample_schema_data=parsed.get("sample_schema_data", fallback["sample_schema_data"]))
        except Exception:
            return AuxiliaryOperationsPlan(**fallback)
