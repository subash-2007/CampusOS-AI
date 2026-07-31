import pytest, asyncio
from departments.campus_safety_emergency.deterministic import (
    EmergencyCallboxAuditorAgent, CampusSafetyAppMeterAgent, EmergencyAlertBroadcastAuditorAgent,
    CleryActComplianceAuditorAgent, SecurityCameraCoverageMeterAgent, CampusDisasterDrillMeterAgent, CampusSafetyEmergencyScorerAgent
)
from departments.campus_safety_emergency.orchestrator import CampusSafetyEmergencyOrchestratorAgent

def test_emergency_callbox_auditor():
    res = EmergencyCallboxAuditorAgent().run(142)
    assert res.callboxes_installed_count == 142
    assert res.functional_callboxes_pct >= 95.0

def test_campus_safety_app_meter():
    res = CampusSafetyAppMeterAgent().run()
    assert res.app_downloads_count >= 10000
    assert res.safe_walk_escorts_requested >= 1000

def test_emergency_alert_broadcast_auditor():
    res = EmergencyAlertBroadcastAuditorAgent().run()
    assert res.alert_delivery_time_seconds <= 10.0
    assert res.delivery_reach_pct >= 95.0

def test_clery_act_compliance_auditor():
    res = CleryActComplianceAuditorAgent().run()
    assert res.clery_compliance_score_pct == 100.0
    assert res.annual_security_report_published is True

def test_security_camera_coverage_meter():
    res = SecurityCameraCoverageMeterAgent().run()
    assert res.camera_uptime_pct >= 98.0

def test_campus_disaster_drill_meter():
    res = CampusDisasterDrillMeterAgent().run()
    assert res.disaster_drills_completed_annual >= 4

def test_campus_safety_emergency_scorer():
    res = CampusSafetyEmergencyScorerAgent().run(142)
    assert res.campus_safety_score >= 90.0
    assert res.confidence_score >= 0.5

def test_campus_safety_emergency_orchestrator():
    report = asyncio.run(CampusSafetyEmergencyOrchestratorAgent().run_pipeline(142))
    assert report.department == "Campus Safety & Emergency Response"
    assert report.department_id == "dept_065"
    assert report.safety_tier == "GOLD-STANDARD SAFE CAMPUS"
    assert len(report.reasoning_steps) == 4
