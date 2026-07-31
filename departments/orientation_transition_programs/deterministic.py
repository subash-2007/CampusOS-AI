from departments.shared.scoring import ScoringEngine
from departments.orientation_transition_programs.schemas import (
    FreshmenOrientationAttendanceMetric, TransferStudentOrientationMetric, OrientationLeaderStaffingAudit,
    FirstYearExperienceFYECourseAudit, WelcomeWeekCampusEngagementMetric, ParentFamilyOrientationEngagementAudit, DeterministicOrientationPipelineResult
)

class FreshmenOrientationAttendanceMeterAgent:
    """Agent 1: Measures freshmen orientation attendees count, completion rate percentage, and family orientation participants."""
    def run(self, freshmen: int = 4850) -> FreshmenOrientationAttendanceMetric:
        return FreshmenOrientationAttendanceMetric(new_freshmen_attending_orientation=freshmen, freshmen_orientation_completion_pct=99.2, family_orientation_participants=3400)

class TransferStudentOrientationMeterAgent:
    """Agent 2: Measures new transfer student orientation attendees count and completion rate percentage."""
    def run(self) -> TransferStudentOrientationMetric:
        return TransferStudentOrientationMetric(new_transfer_students_attending=1420, transfer_orientation_completion_pct=98.4)

class OrientationLeaderStaffingAuditorAgent:
    """Agent 3: Audits active orientation leaders count, training hours completed, and OL-to-student ratio."""
    def run(self) -> OrientationLeaderStaffingAudit:
        return OrientationLeaderStaffingAudit(orientation_leaders_active=140, ol_training_hours_completed=40, ol_leader_to_student_ratio=34.6)

class FirstYearExperienceFYECourseAuditorAgent:
    """Agent 4: Audits FYE seminar sections offered, course enrollment percentage, and retention lift percentage."""
    def run(self) -> FirstYearExperienceFYECourseAudit:
        return FirstYearExperienceFYECourseAudit(fye_seminar_sections_offered=180, fye_course_enrollment_pct=96.5, fye_retention_lift_pct=6.4)

class WelcomeWeekCampusEngagementMeterAgent:
    """Agent 5: Measures Welcome Week events hosted, total event check-ins, and satisfaction rating."""
    def run(self) -> WelcomeWeekCampusEngagementMetric:
        return WelcomeWeekCampusEngagementMetric(welcome_week_events_hosted=64, welcome_week_event_checkins_total=28500, welcome_week_satisfaction_score=4.82)

class ParentFamilyOrientationEngagementAuditorAgent:
    """Agent 6: Audits Family Association members joined and parent orientation CSAT score rating."""
    def run(self) -> ParentFamilyOrientationEngagementAudit:
        return ParentFamilyOrientationEngagementAudit(family_association_members_joined=2400, parent_orientation_csat_score=4.76)

class StudentOrientationTransitionScorerAgent:
    """Agent 7: Master deterministic aggregator for Student Orientation & Transition Programs."""
    def __init__(self):
        self.freshmen_agent = FreshmenOrientationAttendanceMeterAgent()
        self.transfers_agent = TransferStudentOrientationMeterAgent()
        self.staffing_agent = OrientationLeaderStaffingAuditorAgent()
        self.fye_agent = FirstYearExperienceFYECourseAuditorAgent()
        self.welcome_week_agent = WelcomeWeekCampusEngagementMeterAgent()
        self.family_agent = ParentFamilyOrientationEngagementAuditorAgent()

    def run(self, freshmen: int = 4850) -> DeterministicOrientationPipelineResult:
        freshmen_metric = self.freshmen_agent.run(freshmen)
        transfers = self.transfers_agent.run()
        staffing = self.staffing_agent.run()
        fye_course = self.fye_agent.run()
        welcome_week = self.welcome_week_agent.run()
        family_engagement = self.family_agent.run()

        metrics = {
            "freshmen_completion": freshmen_metric.freshmen_orientation_completion_pct,
            "transfer_completion": transfers.transfer_orientation_completion_pct,
            "fye_enrollment": fye_course.fye_course_enrollment_pct,
            "welcome_week_csat": (welcome_week.welcome_week_satisfaction_score / 5.0) * 100
        }
        weights = {"freshmen_completion": 0.35, "transfer_completion": 0.30, "fye_enrollment": 0.20, "welcome_week_csat": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(freshmen_metric.new_freshmen_attending_orientation, 500)
        return DeterministicOrientationPipelineResult(
            freshmen=freshmen_metric, transfers=transfers, staffing=staffing,
            fye_course=fye_course, welcome_week=welcome_week, family_engagement=family_engagement,
            orientation_score=score, confidence_score=confidence
        )
