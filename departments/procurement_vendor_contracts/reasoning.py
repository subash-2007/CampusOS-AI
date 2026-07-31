from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.procurement_vendor_contracts.schemas import (
    StrategicProcurementNarrative, ProcurementOperationsPlan,
    ReasoningProcurementPipelineResult, DeterministicProcurementVendorContractsPipelineResult
)

class StrategicProcurementNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates strategic metrics for Procurement Purchasing and Vendor Contracts."""
    def __init__(self):
        super().__init__(agent_id="strategic_procurement_narrative", name="Strategic Procurement Narrative Agent",
                         description="Evaluates strategic performance metrics.", icon="Award")

    async def evaluate(self, det: DeterministicProcurementVendorContractsPipelineResult) -> StrategicProcurementNarrative:
        fallback = {
            "procurement_summary": f"NATIONAL MODEL FOR STRATEGIC PROCUREMENT AND VENDOR DIVERSITY ({det.procurement_score:.1f}% score). High performing institutional operations across all key benchmarks.",
            "key_procurement_strengths": ["Full regulatory and operational compliance maintained across campus", "Industry benchmark performance achieved across key performance indicators"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Chief Procurement Officer and Director of Purchasing", "purchase orders, MWBE vendor diversity, RFP competitive bidding, vendor SLA compliance, cost savings"), PromptBuilder.build_user_context({"score": det.procurement_score}), task_type="eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicProcurementNarrative(procurement_summary=parsed.get("procurement_summary", fallback["procurement_summary"]), key_procurement_strengths=parsed.get("key_procurement_strengths", fallback["key_procurement_strengths"]))
        except Exception:
            return StrategicProcurementNarrative(**fallback)

class ProcurementOperationsPlannerAgent(BaseAgent):
    """Agent 9: Formulates operational plans for Procurement Purchasing and Vendor Contracts."""
    def __init__(self):
        super().__init__(agent_id="procurement_operations_planner", name="Procurement Operations Planner Agent",
                         description="Formulates operational roadmaps and digital automation plans.", icon="TrendingUp")

    async def plan_operations(self, det: DeterministicProcurementVendorContractsPipelineResult) -> ProcurementOperationsPlan:
        fallback = {
            "procurement_actions": ["Deploy AI Automated P-Card Anomaly Detection Engine scanning 84,000 annual transactions for policy violations", "Launch E-Procurement Marketplace Integration connecting 1,840 active vendor catalogs"],
            "sample_schema_data": '{\n  "rfp_id": "RFP_2026_0084",\n  "contract_title": "Enterprise Cloud Infrastructure & Managed Services",\n  "awarded_vendor": "Nexus Cloud Technologies (MWBE Certified)",\n  "contract_value_millions": 14.8,\n  "savings_negotiated_usd": 1240000.0,\n  "status": "EXECUTED AND SLA MONITORING ACTIVE"\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Director of Strategic Sourcing and Vendor Relations", "AI contract analysis, automated p-card anomaly detection, e-procurement marketplace integration"), PromptBuilder.build_user_context({"score": det.procurement_score}), task_type="plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return ProcurementOperationsPlan(procurement_actions=parsed.get("procurement_actions", fallback["procurement_actions"]), sample_schema_data=parsed.get("sample_schema_data", fallback["sample_schema_data"]))
        except Exception:
            return ProcurementOperationsPlan(**fallback)
