import pytest, asyncio
from departments.orientation_transition_programs.deterministic import (
    FreshmenOrientationAttendanceMeterAgent, TransferStudentOrientationMeterAgent, OrientationLeaderStaffingAuditorAgent,
    FirstYearExperienceFYECourseAuditorAgent, WelcomeWeekCampusEngagementMeterAgent, ParentFamilyOrientationEngagementAuditorAgent, StudentOrientationTransitionScorerAgent
)
from departments.orientation_transition_programs.orchestrator import StudentOrientationTransitionOrchestratorAgent

def test_freshmen_orientation_attendance_meter():
    res = FreshmenOrientationAttendanceMeterAgent().run(4850)
    assert res.new_freshmen_attending_orientation == 4850
    assert res.freshmen_orientation_completion_pct >= 95.0

def test_transfer_student_orientation_meter():
    res = TransferStudentOrientationMeterAgent().run()
    assert res.transfer_orientation_completion_pct >= 90.0

def test_orientation_leader_staffing_auditor():
    res = OrientationLeaderStaffingAuditorAgent().run()
    assert res.ol_training_hours_completed >= 30

def test_first_year_experience_fye_course_auditor():
    res = FirstYearExperienceFYECourseAuditorAgent().run()
    assert res.fye_course_enrollment_pct >= 90.0
    assert res.fye_retention_lift_pct > 0.0

def test_welcome_week_campus_engagement_meter():
    res = WelcomeWeekCampusEngagementMeterAgent().run()
    assert res.welcome_week_events_hosted >= 30
    assert res.welcome_week_satisfaction_score >= 4.0

def test_parent_family_orientation_engagement_auditor():
    res = ParentFamilyOrientationEngagementAuditorAgent().run()
    assert res.parent_orientation_csat_score >= 4.0

def test_student_orientation_transition_scorer():
    res = StudentOrientationTransitionScorerAgent().run(4850)
    assert res.orientation_score >= 90.0
    assert res.confidence_score >= 0.5

def test_student_orientation_transition_orchestrator():
    report = asyncio.run(StudentOrientationTransitionOrchestratorAgent().run_pipeline(4850))
    assert report.department == "Student Orientation & Transition Programs"
    assert report.department_id == "dept_090"
    assert report.orientation_tier == "NATIONAL MODEL FOR STUDENT TRANSITION & RETENTION"
    assert len(report.reasoning_steps) == 4
