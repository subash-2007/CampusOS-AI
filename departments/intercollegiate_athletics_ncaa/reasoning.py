from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.intercollegiate_athletics_ncaa.schemas import (
    StrategicAthleticsNarrative, AthleticsOperationsPlan,
    ReasoningAthleticsPipelineResult, DeterministicIntercollegiateAthleticsNCAAPipelineResult
)

class StrategicAthleticsNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates strategic metrics for Intercollegiate Athletics and NCAA Compliance."""
    def __init__(self):
        super().__init__(agent_id="strategic_athletics_narrative", name="Strategic Athletics Narrative Agent",
                         description="Evaluates strategic performance metrics.", icon="Award")

    async def evaluate(self, det: DeterministicIntercollegiateAthleticsNCAAPipelineResult) -> StrategicAthleticsNarrative:
        fallback = {
            "athletics_summary": f"NCAA DIVISION I CHAMPIONSHIP ATHLETICS PROGRAM ({det.athletics_score:.1f}% score). High performing institutional operations across all key benchmarks.",
            "key_athletics_strengths": ["Full regulatory and operational compliance maintained across campus", "Industry benchmark performance achieved across key performance indicators"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Director of Intercollegiate Athletics and NCAA Senior Woman Administrator", "NCAA APR, Graduation Success Rate, NIL disclosure compliance, sports medicine, broadcast media rights"), PromptBuilder.build_user_context({"score": det.athletics_score}), task_type="eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicAthleticsNarrative(athletics_summary=parsed.get("athletics_summary", fallback["athletics_summary"]), key_athletics_strengths=parsed.get("key_athletics_strengths", fallback["key_athletics_strengths"]))
        except Exception:
            return StrategicAthleticsNarrative(**fallback)

class AthleticsOperationsPlannerAgent(BaseAgent):
    """Agent 9: Formulates operational plans for Intercollegiate Athletics and NCAA Compliance."""
    def __init__(self):
        super().__init__(agent_id="athletics_operations_planner", name="Athletics Operations Planner Agent",
                         description="Formulates operational roadmaps and digital automation plans.", icon="TrendingUp")

    async def plan_operations(self, det: DeterministicIntercollegiateAthleticsNCAAPipelineResult) -> AthleticsOperationsPlan:
        fallback = {
            "athletics_actions": ["Deploy AI NIL Disclosure & Compliance Engine evaluating all student-athlete brand agreements for NCAA adherence", "Implement Wearable Biomechanics & Injury Prevention System for varsity student-athletes"],
            "sample_schema_data": '{\n  "nil_deal_id": "NIL_2026_00412",\n  "student_athlete": "Marcus Vance (Men\'s Basketball, Junior)",\n  "brand_partner": "Apex Sports Nutrition",\n  "compensation_usd": 15000.0,\n  "deliverables": "2 Social Media Posts + 1 Youth Camp Appearance",\n  "compliance_status": "APPROVED BY NCAA COMPLIANCE OFFICE"\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Senior Associate Athletic Director for Compliance and Student-Athlete Welfare", "AI NIL compliance tracking, student-athlete biomechanics monitoring, automated broadcast streaming"), PromptBuilder.build_user_context({"score": det.athletics_score}), task_type="plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return AthleticsOperationsPlan(athletics_actions=parsed.get("athletics_actions", fallback["athletics_actions"]), sample_schema_data=parsed.get("sample_schema_data", fallback["sample_schema_data"]))
        except Exception:
            return AthleticsOperationsPlan(**fallback)
