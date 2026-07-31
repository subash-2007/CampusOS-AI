import pytest, asyncio
from departments.privacy_data_governance.deterministic import (
    GDPRComplianceAuditorAgent, DataRetentionPolicyAuditorAgent, ConsentManagementMeterAgent,
    DataEncryptionAuditorAgent, DataBreachDetectionMeterAgent, DataLineageAuditorAgent, PrivacyComplianceScorerAgent
)
from departments.privacy_data_governance.orchestrator import PrivacyDataGovernanceOrchestratorAgent

def test_gdpr_compliance_auditor():
    res = GDPRComplianceAuditorAgent().run()
    assert res.gdpr_compliant is True
    assert res.data_subject_rights_implemented >= 6

def test_data_retention_policy_auditor():
    res = DataRetentionPolicyAuditorAgent().run()
    assert res.expired_data_auto_purged is True
    assert res.retention_policies_defined >= 10

def test_consent_management_meter():
    res = ConsentManagementMeterAgent().run()
    assert res.consent_capture_rate_pct >= 95.0
    assert res.consent_withdrawal_latency_hours <= 2.0

def test_data_encryption_auditor():
    res = DataEncryptionAuditorAgent().run()
    assert "AES" in res.data_at_rest_encryption
    assert "TLS" in res.data_in_transit_encryption

def test_data_breach_detection_meter():
    res = DataBreachDetectionMeterAgent().run()
    assert res.breach_incidents_last_12m == 0
    assert res.incident_response_plan_tested is True

def test_data_lineage_auditor():
    res = DataLineageAuditorAgent().run()
    assert res.data_lineage_coverage_pct >= 85.0

def test_privacy_compliance_scorer():
    res = PrivacyComplianceScorerAgent().run()
    assert res.privacy_compliance_score >= 90.0
    assert res.confidence_score >= 0.5

def test_privacy_data_governance_orchestrator():
    report = asyncio.run(PrivacyDataGovernanceOrchestratorAgent().run_pipeline())
    assert report.department == "Privacy & Data Governance"
    assert report.department_id == "dept_041"
    assert report.privacy_tier == "FULL GDPR COMPLIANCE"
    assert len(report.reasoning_steps) == 4
