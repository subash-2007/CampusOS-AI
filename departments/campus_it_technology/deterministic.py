from departments.shared.scoring import ScoringEngine
from departments.campus_it_technology.schemas import (
    NetworkInfrastructureUptimeMetric, ITHelpdeskTicketResolutionAudit, CampusCybersecuritySOCAudit,
    SoftwareLicenseComplianceAudit, ClassroomAVTechnologyReadinessMetric, ITServiceContinuityDRPAudit, DeterministicITPipelineResult
)

class NetworkInfrastructureUptimeMeterAgent:
    """Agent 1: Measures campus WiFi access points managed, network uptime SLA percentage, and average WiFi speed."""
    def run(self, access_points: int = 3800) -> NetworkInfrastructureUptimeMetric:
        return NetworkInfrastructureUptimeMetric(campus_wifi_access_points_managed=access_points, network_uptime_sla_pct=99.97, avg_campus_wifi_speed_mbps=980.0)

class ITHelpdeskTicketResolutionAuditorAgent:
    """Agent 2: Audits helpdesk tickets resolved, first-call resolution rate percentage, and average resolution hours."""
    def run(self) -> ITHelpdeskTicketResolutionAudit:
        return ITHelpdeskTicketResolutionAudit(helpdesk_tickets_resolved_annual=48000, first_call_resolution_rate_pct=84.6, avg_ticket_resolution_hours=3.8)

class CampusCybersecuritySOCAuditorAgent:
    """Agent 3: Audits security incidents detected, mean time to contain (hours), and student data breach incidents."""
    def run(self) -> CampusCybersecuritySOCAudit:
        return CampusCybersecuritySOCAudit(security_incidents_detected_annual=2840, mean_time_to_contain_hours=1.8, student_data_breach_incidents=0)

class SoftwareLicenseComplianceAuditorAgent:
    """Agent 4: Audits enterprise software licenses managed, Microsoft/Google Workspace seats, and compliance audit score."""
    def run(self) -> SoftwareLicenseComplianceAudit:
        return SoftwareLicenseComplianceAudit(enterprise_software_licenses_managed=145000, microsoft_google_workspace_seats=42000, license_compliance_audit_score_pct=99.2)

class ClassroomAVTechnologyReadinessMeterAgent:
    """Agent 5: Measures smart classrooms equipped, AV technology uptime percentage, and hybrid learning rooms count."""
    def run(self) -> ClassroomAVTechnologyReadinessMetric:
        return ClassroomAVTechnologyReadinessMetric(smart_classrooms_equipped=620, av_technology_uptime_pct=99.1, hybrid_learning_rooms_count=220)

class ITServiceContinuityDRPAuditorAgent:
    """Agent 6: Audits disaster recovery RTO (minutes), backup completion rate percentage, and annual DRP test exercises."""
    def run(self) -> ITServiceContinuityDRPAudit:
        return ITServiceContinuityDRPAudit(disaster_recovery_rto_minutes=12.0, backup_completion_rate_pct=100.0, drp_test_exercises_annual=4)

class CampusITTechnologyScorerAgent:
    """Agent 7: Master deterministic aggregator for Campus IT & Technology Services."""
    def __init__(self):
        self.network_agent = NetworkInfrastructureUptimeMeterAgent()
        self.helpdesk_agent = ITHelpdeskTicketResolutionAuditorAgent()
        self.cybersecurity_agent = CampusCybersecuritySOCAuditorAgent()
        self.software_agent = SoftwareLicenseComplianceAuditorAgent()
        self.av_agent = ClassroomAVTechnologyReadinessMeterAgent()
        self.drp_agent = ITServiceContinuityDRPAuditorAgent()

    def run(self, access_points: int = 3800) -> DeterministicITPipelineResult:
        network = self.network_agent.run(access_points)
        helpdesk = self.helpdesk_agent.run()
        cybersecurity = self.cybersecurity_agent.run()
        software = self.software_agent.run()
        classroom_av = self.av_agent.run()
        drp = self.drp_agent.run()
        metrics = {
            "network_uptime": network.network_uptime_sla_pct,
            "license_compliance": software.license_compliance_audit_score_pct,
            "av_uptime": classroom_av.av_technology_uptime_pct,
            "backup_rate": drp.backup_completion_rate_pct
        }
        weights = {"network_uptime": 0.35, "license_compliance": 0.25, "av_uptime": 0.25, "backup_rate": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(access_points, 100)
        return DeterministicITPipelineResult(
            network=network, helpdesk=helpdesk, cybersecurity=cybersecurity,
            software=software, classroom_av=classroom_av, drp=drp,
            it_score=score, confidence_score=confidence
        )
