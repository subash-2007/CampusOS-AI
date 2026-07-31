import pytest, asyncio
from departments.procurement_vendor_contracts.deterministic import (PurchaseOrderVolumeComplianceAuditorAgent, DiverseVendorMWBEParticipationMeterAgent, CompetitiveBiddingRFPComplianceAuditorAgent, VendorPerformanceSLAAuditorAgent, ProcurementCostSavingsMeterAgent, PCardProgramAuditorAgent, ProcurementVendorContractsScorerAgent)
from departments.procurement_vendor_contracts.orchestrator import ProcurementVendorContractsOrchestratorAgent

def test_purchase_order_volume_compliance_auditor_agent():
    res = PurchaseOrderVolumeComplianceAuditorAgent().run()
    assert res is not None

def test_diverse_vendor_m_w_b_e_participation_meter_agent():
    res = DiverseVendorMWBEParticipationMeterAgent().run()
    assert res is not None

def test_competitive_bidding_r_f_p_compliance_auditor_agent():
    res = CompetitiveBiddingRFPComplianceAuditorAgent().run()
    assert res is not None

def test_vendor_performance_s_l_a_auditor_agent():
    res = VendorPerformanceSLAAuditorAgent().run()
    assert res is not None

def test_procurement_cost_savings_meter_agent():
    res = ProcurementCostSavingsMeterAgent().run()
    assert res is not None

def test_p_card_program_auditor_agent():
    res = PCardProgramAuditorAgent().run()
    assert res is not None

def test_procurement_vendor_contracts_scorer():
    res = ProcurementVendorContractsScorerAgent().run()
    assert res.procurement_score >= 50.0
    assert res.confidence_score >= 0.5

def test_procurement_vendor_contracts_orchestrator():
    report = asyncio.run(ProcurementVendorContractsOrchestratorAgent().run_pipeline())
    assert report.department == "Procurement Purchasing and Vendor Contracts"
    assert report.department_id == "dept_109"
    assert report.tier == "NATIONAL MODEL FOR STRATEGIC PROCUREMENT AND VENDOR DIVERSITY"
    assert len(report.reasoning_steps) == 4
