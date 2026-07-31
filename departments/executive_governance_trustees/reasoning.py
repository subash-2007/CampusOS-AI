from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.executive_governance_trustees.schemas import (
    StrategicGovernanceNarrative, GovernanceOperationsPlan,
    ReasoningGovernancePipelineResult, DeterministicExecutiveGovernanceTrusteesPipelineResult
)

class StrategicGovernanceNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates strategic metrics for Executive Governance and Board of Trustees Intelligence."""
    def __init__(self):
        super().__init__(agent_id="strategic_governance_narrative", name="Strategic Governance Narrative Agent",
                         description="Evaluates strategic performance metrics.", icon="Award")

    async def evaluate(self, det: DeterministicExecutiveGovernanceTrusteesPipelineResult) -> StrategicGovernanceNarrative:
        fallback = {
            "governance_summary": f"GOLD STANDARD HIGHER EDUCATION GOVERNANCE AND EXECUTIVE LEADERSHIP ({det.governance_score:.1f}% score). High performing institutional operations across all key benchmarks.",
            "key_governance_strengths": ["Full regulatory and operational compliance maintained across campus", "Industry benchmark performance achieved across key performance indicators"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Secretary of the University and Chief Governance Officer to the Board of Trustees", "Board of Trustees resolutions, presidential KPIs, ERM risk register, state appropriations, fiduciary audits"), PromptBuilder.build_user_context({"score": det.governance_score}), task_type="eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicGovernanceNarrative(governance_summary=parsed.get("governance_summary", fallback["governance_summary"]), key_governance_strengths=parsed.get("key_governance_strengths", fallback["key_governance_strengths"]))
        except Exception:
            return StrategicGovernanceNarrative(**fallback)

class GovernanceOperationsPlannerAgent(BaseAgent):
    """Agent 9: Formulates operational plans for Executive Governance and Board of Trustees Intelligence."""
    def __init__(self):
        super().__init__(agent_id="governance_operations_planner", name="Governance Operations Planner Agent",
                         description="Formulates operational roadmaps and digital automation plans.", icon="TrendingUp")

    async def plan_operations(self, det: DeterministicExecutiveGovernanceTrusteesPipelineResult) -> GovernanceOperationsPlan:
        fallback = {
            "governance_actions": ["Deploy Board of Trustees AI Executive Portal delivering real-time institutional KPI dashboards", "Launch ERM Predictive Risk Analytics Engine monitoring higher education regulatory changes"],
            "sample_schema_data": '{\n  "resolution_id": "RES_2026_0068",\n  "title": "Approval of Campus Master Plan 2026-2036 and $500M Capital Campaign",\n  "vote_tally": "UNANIMOUS (18-0)",\n  "date_adopted": "2026-10-15",\n  "signatory": "Chair, Board of Trustees",\n  "audit_opinion": "UNQUALIFIED CLEAN AUDIT OPINION"\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Chief of Staff to the President and General Counsel", "AI board portal governance dashboard, ERM risk prediction, state legislative policy tracker"), PromptBuilder.build_user_context({"score": det.governance_score}), task_type="plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return GovernanceOperationsPlan(governance_actions=parsed.get("governance_actions", fallback["governance_actions"]), sample_schema_data=parsed.get("sample_schema_data", fallback["sample_schema_data"]))
        except Exception:
            return GovernanceOperationsPlan(**fallback)
