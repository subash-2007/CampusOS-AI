from departments.shared.scoring import ScoringEngine
from departments.procurement_vendor_contracts.schemas import (PurchaseOrderVolumeComplianceAudit, DiverseVendorMWBEParticipationMetric, CompetitiveBiddingRFPComplianceAudit, VendorPerformanceSLAAudit, ProcurementCostSavingsMetric, PCardProgramAudit, DeterministicProcurementVendorContractsPipelineResult)

class PurchaseOrderVolumeComplianceAuditorAgent:
    """Agent 1: Evaluates PurchaseOrderVolumeComplianceAudit."""
    def run(self) -> PurchaseOrderVolumeComplianceAudit:
        return PurchaseOrderVolumeComplianceAudit()

class DiverseVendorMWBEParticipationMeterAgent:
    """Agent 2: Evaluates DiverseVendorMWBEParticipationMetric."""
    def run(self) -> DiverseVendorMWBEParticipationMetric:
        return DiverseVendorMWBEParticipationMetric()

class CompetitiveBiddingRFPComplianceAuditorAgent:
    """Agent 3: Evaluates CompetitiveBiddingRFPComplianceAudit."""
    def run(self) -> CompetitiveBiddingRFPComplianceAudit:
        return CompetitiveBiddingRFPComplianceAudit()

class VendorPerformanceSLAAuditorAgent:
    """Agent 4: Evaluates VendorPerformanceSLAAudit."""
    def run(self) -> VendorPerformanceSLAAudit:
        return VendorPerformanceSLAAudit()

class ProcurementCostSavingsMeterAgent:
    """Agent 5: Evaluates ProcurementCostSavingsMetric."""
    def run(self) -> ProcurementCostSavingsMetric:
        return ProcurementCostSavingsMetric()

class PCardProgramAuditorAgent:
    """Agent 6: Evaluates PCardProgramAudit."""
    def run(self) -> PCardProgramAudit:
        return PCardProgramAudit()

class ProcurementVendorContractsScorerAgent:
    """Agent 7: Master deterministic aggregator for Procurement Purchasing and Vendor Contracts."""
    def __init__(self):
        self.po_agent = PurchaseOrderVolumeComplianceAuditorAgent()
        self.mwbe_agent = DiverseVendorMWBEParticipationMeterAgent()
        self.rfp_agent = CompetitiveBiddingRFPComplianceAuditorAgent()
        self.vendor_sla_agent = VendorPerformanceSLAAuditorAgent()
        self.savings_agent = ProcurementCostSavingsMeterAgent()
        self.pcard_agent = PCardProgramAuditorAgent()

    def run(self) -> DeterministicProcurementVendorContractsPipelineResult:
        po = self.po_agent.run()
        mwbe = self.mwbe_agent.run()
        rfp = self.rfp_agent.run()
        vendor_sla = self.vendor_sla_agent.run()
        savings = self.savings_agent.run()
        pcard = self.pcard_agent.run()
        metrics = {
            "po_compliance": po.po_policy_compliance_rate_pct,
            "mwbe_spend_pct": min(100.0, mwbe.mwbe_procurement_spend_pct * 3.5),
            "vendor_sla": vendor_sla.vendor_sla_compliance_rate_pct,
            "pcard_clean_rate": max(0.0, 100.0 - (pcard.pcard_audit_flagged_exceptions_pct * 20))
        }
        weights = {"po_compliance": 0.30, "mwbe_spend_pct": 0.30, "vendor_sla": 0.25, "pcard_clean_rate": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(po.purchase_orders_processed_annual, 10)
        return DeterministicProcurementVendorContractsPipelineResult(
            po=po,
            mwbe=mwbe,
            rfp=rfp,
            vendor_sla=vendor_sla,
            savings=savings,
            pcard=pcard,
            procurement_score=score, confidence_score=confidence
        )
