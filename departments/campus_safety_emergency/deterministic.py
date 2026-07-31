from departments.shared.scoring import ScoringEngine
from departments.campus_safety_emergency.schemas import (
    EmergencyCallboxAudit, CampusSafetyAppMetric, EmergencyAlertBroadcastAudit,
    CleryActComplianceAudit, SecurityCameraCoverageMetric, CampusDisasterDrillMetric, DeterministicSafetyPipelineResult
)

class EmergencyCallboxAuditorAgent:
    """Agent 1: Audits emergency blue light callboxes, functional percentage, and average response speed."""
    def run(self, callboxes: int = 142) -> EmergencyCallboxAudit:
        return EmergencyCallboxAudit(callboxes_installed_count=callboxes, functional_callboxes_pct=99.3, avg_callbox_response_seconds=14.5)

class CampusSafetyAppMeterAgent:
    """Agent 2: Measures campus safety app downloads, active user percentage, and SafeWalk escorts."""
    def run(self) -> CampusSafetyAppMetric:
        return CampusSafetyAppMetric(app_downloads_count=18500, active_safety_app_users_pct=84.2, safe_walk_escorts_requested=1420)

class EmergencyAlertBroadcastAuditorAgent:
    """Agent 3: Audits mass notification alert delivery speed (seconds) and audience reach percentage."""
    def run(self) -> EmergencyAlertBroadcastAudit:
        return EmergencyAlertBroadcastAudit(mass_notification_channels=6, alert_delivery_time_seconds=3.2, delivery_reach_pct=98.8)

class CleryActComplianceAuditorAgent:
    """Agent 4: Audits Clery Act crime log statistics, annual security report publishing, and compliance score."""
    def run(self) -> CleryActComplianceAudit:
        return CleryActComplianceAudit(clery_act_crime_statistics_logged=24, annual_security_report_published=True, clery_compliance_score_pct=100.0)

class SecurityCameraCoverageMeterAgent:
    """Agent 5: Measures CCTV camera count, camera uptime percentage, and AI anomaly detection alerts."""
    def run(self) -> SecurityCameraCoverageMetric:
        return SecurityCameraCoverageMetric(security_cameras_active=840, camera_uptime_pct=99.6, ai_anomaly_alerts_triggered=34)

class CampusDisasterDrillMeterAgent:
    """Agent 6: Measures annual disaster drills, evacuation speed (minutes), and first responder rating."""
    def run(self) -> CampusDisasterDrillMetric:
        return CampusDisasterDrillMetric(disaster_drills_completed_annual=6, evacuation_time_avg_minutes=4.2, first_responder_coordination_rating=4.9)

class CampusSafetyEmergencyScorerAgent:
    """Agent 7: Master deterministic aggregator for Campus Safety & Emergency Response."""
    def __init__(self):
        self.callbox_agent = EmergencyCallboxAuditorAgent()
        self.safety_app_agent = CampusSafetyAppMeterAgent()
        self.alert_agent = EmergencyAlertBroadcastAuditorAgent()
        self.clery_agent = CleryActComplianceAuditorAgent()
        self.camera_agent = SecurityCameraCoverageMeterAgent()
        self.drill_agent = CampusDisasterDrillMeterAgent()

    def run(self, callboxes: int = 142) -> DeterministicSafetyPipelineResult:
        callbox_res = self.callbox_agent.run(callboxes)
        safety_app = self.safety_app_agent.run()
        alerts = self.alert_agent.run()
        clery = self.clery_agent.run()
        cameras = self.camera_agent.run()
        drills = self.drill_agent.run()

        metrics = {
            "clery_compliance": clery.clery_compliance_score_pct,
            "alert_reach": alerts.delivery_reach_pct,
            "callbox_functional": callbox_res.functional_callboxes_pct,
            "camera_uptime": cameras.camera_uptime_pct
        }
        weights = {"clery_compliance": 0.35, "alert_reach": 0.30, "callbox_functional": 0.20, "camera_uptime": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(callbox_res.callboxes_installed_count, 20)
        return DeterministicSafetyPipelineResult(
            callboxes=callbox_res, safety_app=safety_app, emergency_alerts=alerts,
            clery_act=clery, cameras=cameras, drills=drills,
            campus_safety_score=score, confidence_score=confidence
        )
