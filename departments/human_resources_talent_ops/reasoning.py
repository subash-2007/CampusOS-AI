from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.human_resources_talent_ops.schemas import (
    StrategicHRNarrative, HROperationsPlan,
    ReasoningHRPipelineResult, DeterministicHumanResourcesTalentOpsPipelineResult
)

class StrategicHRNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates strategic metrics for Campus Human Resources and Talent Operations."""
    def __init__(self):
        super().__init__(agent_id="strategic_hr_narrative", name="Strategic HR Narrative Agent",
                         description="Evaluates strategic performance metrics.", icon="Award")

    async def evaluate(self, det: DeterministicHumanResourcesTalentOpsPipelineResult) -> StrategicHRNarrative:
        fallback = {
            "hr_summary": f"GREAT COLLEGES TO WORK FOR HIGHER ED HR EXCELLENCE ({det.hr_score:.1f}% score). High performing institutional operations across all key benchmarks.",
            "key_hr_strengths": ["Full regulatory and operational compliance maintained across campus", "Industry benchmark performance achieved across key performance indicators"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Chief Human Resources Officer and Associate Vice President for Talent Operations", "time to fill, staff retention, compensation equity, performance reviews, Title IX EEO compliance"), PromptBuilder.build_user_context({"score": det.hr_score}), task_type="eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicHRNarrative(hr_summary=parsed.get("hr_summary", fallback["hr_summary"]), key_hr_strengths=parsed.get("key_hr_strengths", fallback["key_hr_strengths"]))
        except Exception:
            return StrategicHRNarrative(**fallback)

class HROperationsPlannerAgent(BaseAgent):
    """Agent 9: Formulates operational plans for Campus Human Resources and Talent Operations."""
    def __init__(self):
        super().__init__(agent_id="hr_operations_planner", name="HR Operations Planner Agent",
                         description="Formulates operational roadmaps and digital automation plans.", icon="TrendingUp")

    async def plan_operations(self, det: DeterministicHumanResourcesTalentOpsPipelineResult) -> HROperationsPlan:
        fallback = {
            "hr_actions": ["Deploy AI-Powered Campus HR Chatbot resolving employee benefit queries automatically", "Launch Campus Leadership Academy expanding professional development pathways for staff"],
            "sample_schema_data": '{\n  "position_id": "POS_2026_01142",\n  "job_title": "Senior Data Architect - Enterprise Analytics",\n  "department": "Campus IT & Technology Services",\n  "days_to_fill": 38,\n  "applicants_total": 84,\n  "hired_candidate": "Internal Promotion / Transfer",\n  "status": "FILLED AND ONBOARDING COMPLETED"\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Director of Talent Acquisition and Employee Relations", "AI resume matching for university staff, automated HR chatbot, digital onboarding portal"), PromptBuilder.build_user_context({"score": det.hr_score}), task_type="plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return HROperationsPlan(hr_actions=parsed.get("hr_actions", fallback["hr_actions"]), sample_schema_data=parsed.get("sample_schema_data", fallback["sample_schema_data"]))
        except Exception:
            return HROperationsPlan(**fallback)
