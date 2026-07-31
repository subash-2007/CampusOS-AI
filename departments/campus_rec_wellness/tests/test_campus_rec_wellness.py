import pytest, asyncio
from departments.campus_rec_wellness.deterministic import (
    RecreationCenterCheckinTurnstileMeterAgent, GroupFitnessClassAttendanceAuditorAgent, IntramuralSportsLeagueParticipationMeterAgent,
    OutdoorAdventuresEquipmentRentalAuditorAgent, AquaticCenterPoolSafetyAuditorAgent, WellnessCoachingPersonalTrainingMeterAgent, CampusRecreationWellnessScorerAgent
)
from departments.campus_rec_wellness.orchestrator import CampusRecreationWellnessOrchestratorAgent

def test_recreation_center_checkin_turnstile_meter():
    res = RecreationCenterCheckinTurnstileMeterAgent().run(420000)
    assert res.rec_center_annual_turnstile_scans == 420000
    assert res.rec_center_student_body_utilization_pct >= 70.0

def test_group_fitness_class_attendance_auditor():
    res = GroupFitnessClassAttendanceAuditorAgent().run()
    assert res.class_capacity_fill_rate_pct >= 85.0

def test_intramural_sports_league_participation_meter():
    res = IntramuralSportsLeagueParticipationMeterAgent().run()
    assert res.intramural_teams_registered >= 200

def test_outdoor_adventures_equipment_rental_auditor():
    res = OutdoorAdventuresEquipmentRentalAuditorAgent().run()
    assert res.outdoor_gear_rentals_annual >= 1000

def test_aquatic_center_pool_safety_auditor():
    res = AquaticCenterPoolSafetyAuditorAgent().run()
    assert res.lifeguard_cpr_certifications_valid_pct == 100.0
    assert res.water_quality_chemical_audit_score_pct >= 95.0

def test_wellness_coaching_personal_training_meter():
    res = WellnessCoachingPersonalTrainingMeterAgent().run()
    assert res.personal_training_sessions_conducted >= 500

def test_campus_recreation_wellness_scorer():
    res = CampusRecreationWellnessScorerAgent().run(420000)
    assert res.rec_wellness_score >= 90.0
    assert res.confidence_score >= 0.5

def test_campus_recreation_wellness_orchestrator():
    report = asyncio.run(CampusRecreationWellnessOrchestratorAgent().run_pipeline(420000))
    assert report.department == "Campus Recreation & Wellness"
    assert report.department_id == "dept_085"
    assert report.rec_wellness_tier == "PREMIER CAMPUS FITNESS & RECREATION CENTER"
    assert len(report.reasoning_steps) == 4
