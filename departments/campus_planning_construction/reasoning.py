from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.campus_planning_construction.schemas import (
    StrategicPlanningNarrative, PlanningOperationsPlan,
    ReasoningPlanningPipelineResult, DeterministicCampusPlanningConstructionPipelineResult
)

class StrategicPlanningNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates strategic metrics for Campus Planning and Capital Construction."""
    def __init__(self):
        super().__init__(agent_id="strategic_planning_narrative", name="Strategic Planning Narrative Agent",
                         description="Evaluates strategic performance metrics.", icon="Award")

    async def evaluate(self, det: DeterministicCampusPlanningConstructionPipelineResult) -> StrategicPlanningNarrative:
        fallback = {
            "planning_summary": f"LEED PLATINUM CAMPUS MASTER PLAN INSTITUTION ({det.planning_score:.1f}% score). High performing institutional operations across all key benchmarks.",
            "key_planning_strengths": ["Full regulatory and operational compliance maintained across campus", "Industry benchmark performance achieved across key performance indicators"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Vice President for Facilities and Campus Planning", "capital projects, LEED certification, master plan, deferred maintenance, universal design"), PromptBuilder.build_user_context({"score": det.planning_score}), task_type="eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicPlanningNarrative(planning_summary=parsed.get("planning_summary", fallback["planning_summary"]), key_planning_strengths=parsed.get("key_planning_strengths", fallback["key_planning_strengths"]))
        except Exception:
            return StrategicPlanningNarrative(**fallback)

class PlanningOperationsPlannerAgent(BaseAgent):
    """Agent 9: Formulates operational plans for Campus Planning and Capital Construction."""
    def __init__(self):
        super().__init__(agent_id="planning_operations_planner", name="Planning Operations Planner Agent",
                         description="Formulates operational roadmaps and digital automation plans.", icon="TrendingUp")

    async def plan_operations(self, det: DeterministicCampusPlanningConstructionPipelineResult) -> PlanningOperationsPlan:
        fallback = {
            "planning_actions": ["Deploy BIM (Building Information Modeling) 3D Twin for all capital construction projects", "Implement Smart Building IoT Sensor Mesh optimizing HVAC and lighting energy consumption"],
            "sample_schema_data": '{\n  "project_id": "CAP_2026_0048",\n  "project_name": "Interdisciplinary Science & Engineering Complex",\n  "budget_millions": 84.5,\n  "completion_pct": 78.4,\n  "leed_target": "LEED Platinum",\n  "status": "ON BUDGET AND ON SCHEDULE"\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Capital Construction Director and Campus Architect", "BIM 3D modeling, smart building IoT sensors, LEED Platinum, deferred maintenance reduction"), PromptBuilder.build_user_context({"score": det.planning_score}), task_type="plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return PlanningOperationsPlan(planning_actions=parsed.get("planning_actions", fallback["planning_actions"]), sample_schema_data=parsed.get("sample_schema_data", fallback["sample_schema_data"]))
        except Exception:
            return PlanningOperationsPlan(**fallback)
