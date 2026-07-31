from departments.shared.scoring import ScoringEngine
from departments.campus_safety_security.schemas import (
    CampusPolicePatrolResponseMetric, CrimePreventionAwarenessProgramMetric, CampusCCTVAccessControlAudit,
    EmergencyMassNotificationAudit, CampusParkingCitationEnforcementMetric, SafetyEscortNightRideServiceMetric, DeterministicCampusSafetyPipelineResult
)

class CampusPolicePatrolResponseMeterAgent:
    """Agent 1: Measures sworn campus officers, average emergency response time, and Clery Act incident reports."""
    def run(self) -> CampusPolicePatrolResponseMetric:
        return CampusPolicePatrolResponseMetric()

class CrimePreventionAwarenessProgramMeterAgent:
    """Agent 2: Measures RAD workshop participants, crime prevention programs offered, and bystander intervention completions."""
    def run(self) -> CrimePreventionAwarenessProgramMetric:
        return CrimePreventionAwarenessProgramMetric()

class CampusCCTVAccessControlAuditorAgent:
    """Agent 3: Audits CCTV cameras operational, blue light station uptime percentage, and access control doors managed."""
    def run(self) -> CampusCCTVAccessControlAudit:
        return CampusCCTVAccessControlAudit()

class EmergencyMassNotificationAuditorAgent:
    """Agent 4: Audits mass notification tests conducted, average notification delivery speed, and opt-in enrollment rate."""
    def run(self) -> EmergencyMassNotificationAudit:
        return EmergencyMassNotificationAudit()

class CampusParkingCitationEnforcementMeterAgent:
    """Agent 5: Measures registered parking permits, citations issued, and parking violation appeal success rate."""
    def run(self) -> CampusParkingCitationEnforcementMetric:
        return CampusParkingCitationEnforcementMetric()

class SafetyEscortNightRideServiceMeterAgent:
    """Agent 6: Measures Safe Walk escort requests fulfilled, NightRide shuttle trips, and escort satisfaction score."""
    def run(self) -> SafetyEscortNightRideServiceMetric:
        return SafetyEscortNightRideServiceMetric()

class CampusSafetySecurityScorerAgent:
    """Agent 7: Master deterministic aggregator for Campus Safety and Security Operations."""
    def __init__(self):
        self.patrol_agent = CampusPolicePatrolResponseMeterAgent()
        self.crime_agent = CrimePreventionAwarenessProgramMeterAgent()
        self.cctv_agent = CampusCCTVAccessControlAuditorAgent()
        self.notification_agent = EmergencyMassNotificationAuditorAgent()
        self.parking_agent = CampusParkingCitationEnforcementMeterAgent()
        self.escort_agent = SafetyEscortNightRideServiceMeterAgent()

    def run(self) -> DeterministicCampusSafetyPipelineResult:
        patrol = self.patrol_agent.run()
        crime_prevention = self.crime_agent.run()
        cctv = self.cctv_agent.run()
        notification = self.notification_agent.run()
        parking = self.parking_agent.run()
        escort = self.escort_agent.run()
        metrics = {
            "blue_light_uptime": cctv.blue_light_station_uptime_pct,
            "notification_opt_in": notification.opt_in_enrollment_rate_pct,
            "response_speed": max(0.0, 100.0 - (patrol.avg_emergency_response_time_minutes * 5)),
            "escort_satisfaction": (escort.escort_service_satisfaction_score / 5.0) * 100
        }
        weights = {"blue_light_uptime": 0.35, "notification_opt_in": 0.25, "response_speed": 0.25, "escort_satisfaction": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(patrol.sworn_campus_officers_count, 10)
        return DeterministicCampusSafetyPipelineResult(
            patrol=patrol, crime_prevention=crime_prevention, cctv=cctv,
            notification=notification, parking=parking, escort=escort,
            safety_score=score, confidence_score=confidence
        )
