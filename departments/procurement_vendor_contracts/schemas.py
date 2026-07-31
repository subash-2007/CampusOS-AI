from typing import List
from pydantic import BaseModel

class PurchaseOrderVolumeComplianceAudit(BaseModel):
    purchase_orders_processed_annual: int = 38400
    po_policy_compliance_rate_pct: float = 98.6
    total_procurement_spend_millions: float = 248.0

class DiverseVendorMWBEParticipationMetric(BaseModel):
    mwbe_certified_vendors_active: int = 480
    mwbe_procurement_spend_pct: float = 24.8
    mwbe_spend_millions: float = 61.5

class CompetitiveBiddingRFPComplianceAudit(BaseModel):
    rfps_issued_annual: int = 124
    avg_rfp_cycle_time_days: float = 28.4
    competitive_bidding_compliance_pct: float = 100.0

class VendorPerformanceSLAAudit(BaseModel):
    active_vendor_contracts_managed: int = 1840
    vendor_sla_compliance_rate_pct: float = 94.2
    contract_dispute_incidents: int = 2

class ProcurementCostSavingsMetric(BaseModel):
    negotiated_cost_savings_millions: float = 18.4
    cost_savings_pct_of_total_spend: float = 7.4
    early_payment_discount_captured_usd: float = 480000.0

class PCardProgramAudit(BaseModel):
    active_pcard_holders_count: int = 1240
    pcard_transactions_annual: int = 84000
    pcard_audit_flagged_exceptions_pct: float = 0.42

class DeterministicProcurementVendorContractsPipelineResult(BaseModel):
    po: PurchaseOrderVolumeComplianceAudit
    mwbe: DiverseVendorMWBEParticipationMetric
    rfp: CompetitiveBiddingRFPComplianceAudit
    vendor_sla: VendorPerformanceSLAAudit
    savings: ProcurementCostSavingsMetric
    pcard: PCardProgramAudit
    procurement_score: float
    confidence_score: float

class StrategicProcurementNarrative(BaseModel):
    procurement_summary: str
    key_procurement_strengths: List[str]

class ProcurementOperationsPlan(BaseModel):
    procurement_actions: List[str]
    sample_schema_data: str

class ReasoningProcurementPipelineResult(BaseModel):
    narrative: StrategicProcurementNarrative
    plan: ProcurementOperationsPlan
    reasoning_steps: List[str]

class ProcurementVendorContractsOrchestratorReport(BaseModel):
    department: str = "Procurement Purchasing and Vendor Contracts"
    department_id: str = "dept_109"
    tier: str = "NATIONAL MODEL FOR STRATEGIC PROCUREMENT AND VENDOR DIVERSITY"
    procurement_score: float
    confidence_score: float
    deterministic_analysis: DeterministicProcurementVendorContractsPipelineResult
    reasoning_analysis: ReasoningProcurementPipelineResult
    reasoning_steps: List[str]
