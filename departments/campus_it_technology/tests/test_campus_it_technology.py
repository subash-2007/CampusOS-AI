import pytest, asyncio
from departments.campus_it_technology.deterministic import (
    NetworkInfrastructureUptimeMeterAgent, ITHelpdeskTicketResolutionAuditorAgent, CampusCybersecuritySOCAuditorAgent,
    SoftwareLicenseComplianceAuditorAgent, ClassroomAVTechnologyReadinessMeterAgent, ITServiceContinuityDRPAuditorAgent, CampusITTechnologyScorerAgent
)
from departments.campus_it_technology.orchestrator import CampusITTechnologyOrchestratorAgent

def test_network_infrastructure_uptime_meter():
    res = NetworkInfrastructureUptimeMeterAgent().run(3800)
    assert res.campus_wifi_access_points_managed == 3800
    assert res.network_uptime_sla_pct >= 99.9

def test_it_helpdesk_ticket_resolution_auditor():
    res = ITHelpdeskTicketResolutionAuditorAgent().run()
    assert res.first_call_resolution_rate_pct >= 70.0

def test_campus_cybersecurity_soc_auditor():
    res = CampusCybersecuritySOCAuditorAgent().run()
    assert res.student_data_breach_incidents == 0

def test_software_license_compliance_auditor():
    res = SoftwareLicenseComplianceAuditorAgent().run()
    assert res.license_compliance_audit_score_pct >= 95.0

def test_classroom_av_technology_readiness_meter():
    res = ClassroomAVTechnologyReadinessMeterAgent().run()
    assert res.av_technology_uptime_pct >= 95.0

def test_it_service_continuity_drp_auditor():
    res = ITServiceContinuityDRPAuditorAgent().run()
    assert res.backup_completion_rate_pct == 100.0

def test_campus_it_technology_scorer():
    res = CampusITTechnologyScorerAgent().run(3800)
    assert res.it_score >= 90.0
    assert res.confidence_score >= 0.5

def test_campus_it_technology_orchestrator():
    report = asyncio.run(CampusITTechnologyOrchestratorAgent().run_pipeline(3800))
    assert report.department == "Campus IT & Technology Services"
    assert report.department_id == "dept_095"
    assert report.it_tier == "AWARD-WINNING DIGITAL CAMPUS TECHNOLOGY INFRASTRUCTURE"
    assert len(report.reasoning_steps) == 4
