from departments.shared.scoring import ScoringEngine
from departments.campus_rec_wellness.schemas import (
    RecreationCenterCheckinTurnstileMetric, GroupFitnessClassAttendanceAudit, IntramuralSportsLeagueParticipationMetric,
    OutdoorAdventuresEquipmentRentalAudit, AquaticCenterPoolSafetyAudit, WellnessCoachingPersonalTrainingMetric, DeterministicCampusRecPipelineResult
)

class RecreationCenterCheckinTurnstileMeterAgent:
    """Agent 1: Measures turnstile scans, daily unique visitors, and student body utilization percentage."""
    def run(self, scans: int = 420000) -> RecreationCenterCheckinTurnstileMetric:
        return RecreationCenterCheckinTurnstileMetric(rec_center_annual_turnstile_scans=scans, daily_unique_student_visitors=3400, rec_center_student_body_utilization_pct=78.4)

class GroupFitnessClassAttendanceAuditorAgent:
    """Agent 2: Audits weekly group fitness classes count, annual participants, and class fill rate percentage."""
    def run(self) -> GroupFitnessClassAttendanceAudit:
        return GroupFitnessClassAttendanceAudit(group_fitness_classes_weekly=84, annual_group_fitness_participants=24500, class_capacity_fill_rate_pct=91.2)

class IntramuralSportsLeagueParticipationMeterAgent:
    """Agent 3: Measures intramural teams registered, participating athletes count, and sports leagues offered."""
    def run(self) -> IntramuralSportsLeagueParticipationMetric:
        return IntramuralSportsLeagueParticipationMetric(intramural_teams_registered=420, intramural_league_athletes_count=4800, intramural_sports_offered_count=24)

class OutdoorAdventuresEquipmentRentalAuditorAgent:
    """Agent 4: Audits outdoor expeditions hosted, annual gear rentals count, and certified wilderness guides."""
    def run(self) -> OutdoorAdventuresEquipmentRentalAudit:
        return OutdoorAdventuresEquipmentRentalAudit(outdoor_expeditions_hosted=48, outdoor_gear_rentals_annual=3400, outdoor_safety_certified_guides_count=28)

class AquaticCenterPoolSafetyAuditorAgent:
    """Agent 5: Audits aquatic center weekly visitors, lifeguard certification compliance, and pool water chemical audit score."""
    def run(self) -> AquaticCenterPoolSafetyAudit:
        return AquaticCenterPoolSafetyAudit(aquatic_center_weekly_visitors=2800, lifeguard_cpr_certifications_valid_pct=100.0, water_quality_chemical_audit_score_pct=99.4)

class WellnessCoachingPersonalTrainingMeterAgent:
    """Agent 6: Measures personal training sessions conducted and wellness coaching participants count."""
    def run(self) -> WellnessCoachingPersonalTrainingMetric:
        return WellnessCoachingPersonalTrainingMetric(personal_training_sessions_conducted=1850, wellness_coaching_participants=940)

class CampusRecreationWellnessScorerAgent:
    """Agent 7: Master deterministic aggregator for Campus Recreation & Wellness."""
    def __init__(self):
        self.turnstiles_agent = RecreationCenterCheckinTurnstileMeterAgent()
        self.fitness_agent = GroupFitnessClassAttendanceAuditorAgent()
        self.intramurals_agent = IntramuralSportsLeagueParticipationMeterAgent()
        self.outdoors_agent = OutdoorAdventuresEquipmentRentalAuditorAgent()
        self.aquatics_agent = AquaticCenterPoolSafetyAuditorAgent()
        self.pt_agent = WellnessCoachingPersonalTrainingMeterAgent()

    def run(self, scans: int = 420000) -> DeterministicCampusRecPipelineResult:
        turnstiles = self.turnstiles_agent.run(scans)
        group_fitness = self.fitness_agent.run()
        intramurals = self.intramurals_agent.run()
        outdoors = self.outdoors_agent.run()
        aquatics = self.aquatics_agent.run()
        personal_training = self.pt_agent.run()

        metrics = {
            "lifeguard_certs": aquatics.lifeguard_cpr_certifications_valid_pct,
            "fill_rate": group_fitness.class_capacity_fill_rate_pct,
            "utilization": turnstiles.rec_center_student_body_utilization_pct * 1.15,
            "pool_chemical": aquatics.water_quality_chemical_audit_score_pct
        }
        weights = {"lifeguard_certs": 0.35, "fill_rate": 0.30, "utilization": 0.20, "pool_chemical": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(int(turnstiles.rec_center_annual_turnstile_scans / 1000.0), 100)
        return DeterministicCampusRecPipelineResult(
            turnstiles=turnstiles, group_fitness=group_fitness, intramurals=intramurals,
            outdoors=outdoors, aquatics=aquatics, personal_training=personal_training,
            rec_wellness_score=score, confidence_score=confidence
        )
