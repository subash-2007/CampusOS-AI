from typing import List
from pydantic import BaseModel

class FreshmenOrientationAttendanceMetric(BaseModel):
    new_freshmen_attending_orientation: int = 4850
    freshmen_orientation_completion_pct: float = 99.2
    family_orientation_participants: int = 3400

class TransferStudentOrientationMetric(BaseModel):
    new_transfer_students_attending: int = 1420
    transfer_orientation_completion_pct: float = 98.4

class OrientationLeaderStaffingAudit(BaseModel):
    orientation_leaders_active: int = 140
    ol_training_hours_completed: int = 40
    ol_leader_to_student_ratio: float = 34.6

class FirstYearExperienceFYECourseAudit(BaseModel):
    fye_seminar_sections_offered: int = 180
    fye_course_enrollment_pct: float = 96.5
    fye_retention_lift_pct: float = 6.4

class WelcomeWeekCampusEngagementMetric(BaseModel):
    welcome_week_events_hosted: int = 64
    welcome_week_event_checkins_total: int = 28500
    welcome_week_satisfaction_score: float = 4.82

class ParentFamilyOrientationEngagementAudit(BaseModel):
    family_association_members_joined: int = 2400
    parent_orientation_csat_score: float = 4.76

class DeterministicOrientationPipelineResult(BaseModel):
    freshmen: FreshmenOrientationAttendanceMetric
    transfers: TransferStudentOrientationMetric
    staffing: OrientationLeaderStaffingAudit
    fye_course: FirstYearExperienceFYECourseAudit
    welcome_week: WelcomeWeekCampusEngagementMetric
    family_engagement: ParentFamilyOrientationEngagementAudit
    orientation_score: float
    confidence_score: float

class StrategicOrientationNarrative(BaseModel):
    orientation_summary: str
    key_orientation_strengths: List[str]

class TransitionProgramPlan(BaseModel):
    orientation_actions: List[str]
    sample_orientation_schedule_schema: str

class ReasoningOrientationPipelineResult(BaseModel):
    narrative: StrategicOrientationNarrative
    transition_plan: TransitionProgramPlan
    reasoning_steps: List[str]

class StudentOrientationTransitionOrchestratorReport(BaseModel):
    department: str = "Student Orientation & Transition Programs"
    department_id: str = "dept_090"
    orientation_tier: str = "NATIONAL MODEL FOR STUDENT TRANSITION & RETENTION"
    orientation_score: float
    confidence_score: float
    deterministic_analysis: DeterministicOrientationPipelineResult
    reasoning_analysis: ReasoningOrientationPipelineResult
    reasoning_steps: List[str]
