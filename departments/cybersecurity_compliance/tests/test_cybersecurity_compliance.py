import pytest
import asyncio
from departments.cybersecurity_compliance.deterministic import (
    VulnerabilityScanMeterAgent, SOC2ComplianceStatusAgent, EncryptionStrengthAuditorAgent,
    IAMRolePermissionMeterAgent, IncidentResponseSpeedMeterAgent, GDPRPrivacyComplianceAuditorAgent, CybersecurityScorerAgent
)
from departments.cybersecurity_compliance.orchestrator import CybersecurityComplianceOrchestratorAgent

CRITICAL_VULNERABILITIES = 0

def test_vulnerability_scan_meter():
    agent = VulnerabilityScanMeterAgent()
    res = agent.run(CRITICAL_VULNERABILITIES)
    assert res.vulnerability_security_score >= 90.0

def test_soc2_compliance_status():
    agent = SOC2ComplianceStatusAgent()
    res = agent.run()
    assert res.soc2_type2_certified is True

def test_encryption_strength_auditor():
    agent = EncryptionStrengthAuditorAgent()
    res = agent.run()
    assert res.encryption_compliance_score == 100.0

def test_iam_role_permission_meter():
    agent = IAMRolePermissionMeterAgent()
    res = agent.run()
    assert res.least_privilege_score >= 80.0

def test_incident_response_speed_meter():
    agent = IncidentResponseSpeedMeterAgent()
    res = agent.run(4, 12)
    assert res.mean_time_to_detect_minutes == 4

def test_gdpr_privacy_compliance_auditor():
    agent = GDPRPrivacyComplianceAuditorAgent()
    res = agent.run()
    assert res.gdpr_compliant is True

def test_cybersecurity_scorer():
    agent = CybersecurityScorerAgent()
    res = agent.run(CRITICAL_VULNERABILITIES)
    assert res.cybersecurity_posture_score >= 85.0
    assert res.confidence_score > 0.5

def test_cybersecurity_orchestrator_pipeline():
    orchestrator = CybersecurityComplianceOrchestratorAgent()
    report = asyncio.run(orchestrator.run_pipeline(CRITICAL_VULNERABILITIES))
    
    assert report.department == "Cybersecurity & Compliance"
    assert report.department_id == "dept_026"
    assert report.security_tier == "ENTERPRISE HARDENED"
    assert report.confidence_score > 0
    assert len(report.reasoning_steps) == 4
    assert len(report.reasoning_analysis.mitigation_plan.zero_trust_action_items) > 0
