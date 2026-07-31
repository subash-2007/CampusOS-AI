import pytest, asyncio
from departments.student_athletics_recreation.deterministic import (
    StudentAthleteHeadcountMeterAgent, NCAAAcademicProgressRateAuditorAgent, RecCenterFacilityUtilizationMeterAgent,
    AthleticScholarshipNILAuditorAgent, SportsMedicineInjuryPreventionAuditorAgent, IntramuralClubSportsLeagueMeterAgent, StudentAthleticsRecreationScorerAgent
)
from departments.student_athletics_recreation.orchestrator import StudentAthleticsRecreationOrchestratorAgent

def test_student_athlete_headcount_meter():
    res = StudentAthleteHeadcountMeterAgent().run(540)
    assert res.ncaa_student_athletes_count == 540
    assert res.varsity_teams_count >= 15

def test_ncaa_academic_progress_rate_auditor():
    res = NCAAAcademicProgressRateAuditorAgent().run()
    assert res.ncaa_apr_score_avg >= 950.0
    assert res.ncaa_academic_compliance_pct == 100.0

def test_rec_center_facility_utilization_meter():
    res = RecCenterFacilityUtilizationMeterAgent().run()
    assert res.fitness_equipment_uptime_pct >= 95.0

def test_athletic_scholarship_nil_auditor():
    res = AthleticScholarshipNILAuditorAgent().run()
    assert res.nil_compliance_rate_pct == 100.0
    assert res.athletic_scholarships_awarded_usd > 1000000.0

def test_sports_medicine_injury_prevention_auditor():
    res = SportsMedicineInjuryPreventionAuditorAgent().run()
    assert res.concussion_protocol_compliance_pct == 100.0

def test_intramural_club_sports_league_meter():
    res = IntramuralClubSportsLeagueMeterAgent().run()
    assert res.sportsmanship_rating_avg >= 4.0

def test_student_athletics_recreation_scorer():
    res = StudentAthleticsRecreationScorerAgent().run(540)
    assert res.athletics_score >= 90.0
    assert res.confidence_score >= 0.5

def test_student_athletics_recreation_orchestrator():
    report = asyncio.run(StudentAthleticsRecreationOrchestratorAgent().run_pipeline(540))
    assert report.department == "Student Athletics & Recreation"
    assert report.department_id == "dept_070"
    assert report.athletics_tier == "NCAA CHAMPIONSHIP EXCELLENCE PROGRAM"
    assert len(report.reasoning_steps) == 4
