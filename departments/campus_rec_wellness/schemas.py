from typing import List
from pydantic import BaseModel

class RecreationCenterCheckinTurnstileMetric(BaseModel):
    rec_center_annual_turnstile_scans: int = 420000
    daily_unique_student_visitors: int = 3400
    rec_center_student_body_utilization_pct: float = 78.4

class GroupFitnessClassAttendanceAudit(BaseModel):
    group_fitness_classes_weekly: int = 84
    annual_group_fitness_participants: int = 24500
    class_capacity_fill_rate_pct: float = 91.2

class IntramuralSportsLeagueParticipationMetric(BaseModel):
    intramural_teams_registered: int = 420
    intramural_league_athletes_count: int = 4800
    intramural_sports_offered_count: int = 24

class OutdoorAdventuresEquipmentRentalAudit(BaseModel):
    outdoor_expeditions_hosted: int = 48
    outdoor_gear_rentals_annual: int = 3400
    outdoor_safety_certified_guides_count: int = 28

class AquaticCenterPoolSafetyAudit(BaseModel):
    aquatic_center_weekly_visitors: int = 2800
    lifeguard_cpr_certifications_valid_pct: float = 100.0
    water_quality_chemical_audit_score_pct: float = 99.4

class WellnessCoachingPersonalTrainingMetric(BaseModel):
    personal_training_sessions_conducted: int = 1850
    wellness_coaching_participants: int = 940

class DeterministicCampusRecPipelineResult(BaseModel):
    turnstiles: RecreationCenterCheckinTurnstileMetric
    group_fitness: GroupFitnessClassAttendanceAudit
    intramurals: IntramuralSportsLeagueParticipationMetric
    outdoors: OutdoorAdventuresEquipmentRentalAudit
    aquatics: AquaticCenterPoolSafetyAudit
    personal_training: WellnessCoachingPersonalTrainingMetric
    rec_wellness_score: float
    confidence_score: float

class StrategicCampusRecNarrative(BaseModel):
    rec_wellness_summary: str
    key_rec_strengths: List[str]

class CampusRecOperationsPlan(BaseModel):
    rec_actions: List[str]
    sample_intramural_league_bracket_schema: str

class ReasoningCampusRecPipelineResult(BaseModel):
    narrative: StrategicCampusRecNarrative
    rec_plan: CampusRecOperationsPlan
    reasoning_steps: List[str]

class CampusRecreationWellnessOrchestratorReport(BaseModel):
    department: str = "Campus Recreation & Wellness"
    department_id: str = "dept_085"
    rec_wellness_tier: str = "PREMIER CAMPUS FITNESS & RECREATION CENTER"
    rec_wellness_score: float
    confidence_score: float
    deterministic_analysis: DeterministicCampusRecPipelineResult
    reasoning_analysis: ReasoningCampusRecPipelineResult
    reasoning_steps: List[str]
