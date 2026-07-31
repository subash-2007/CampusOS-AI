from departments.shared.scoring import ScoringEngine
from departments.campus_childcare_services.schemas import (
    ChildcareEnrollmentCapacityMetric, ChildcareSubsidyFinancialAidAudit, StateChildcareLicensingAudit,
    StudentParentAcademicRetentionMetric, FamilyFriendlyCampusInfrastructureAudit, AfterSchoolDropInCareMetric, DeterministicChildcarePipelineResult
)

class ChildcareEnrollmentCapacityMeterAgent:
    """Agent 1: Measures enrolled children headcount, center capacity percentage, and slot distribution."""
    def run(self, children: int = 340) -> ChildcareEnrollmentCapacityMetric:
        return ChildcareEnrollmentCapacityMetric(enrolled_children_count=children, childcare_center_capacity_pct=94.2, infant_toddler_preschool_slots=360)

class ChildcareSubsidyFinancialAidAuditorAgent:
    """Agent 2: Audits student-parent childcare subsidies awarded (USD), recipient counts, and fulfillment rate."""
    def run(self) -> ChildcareSubsidyFinancialAidAudit:
        return ChildcareSubsidyFinancialAidAudit(childcare_subsidies_awarded_usd=480000.0, student_parent_subsidy_recipients=142, subsidy_fulfillment_rate_pct=98.5)

class StateChildcareLicensingAuditorAgent:
    """Agent 3: Audits state childcare licensing compliance, staff-to-child ratio, and certified staff percentage."""
    def run(self) -> StateChildcareLicensingAudit:
        return StateChildcareLicensingAudit(licensing_compliance_score_pct=100.0, staff_to_child_ratio_avg=4.2, early_childhood_certified_staff_pct=96.0)

class StudentParentAcademicRetentionMeterAgent:
    """Agent 4: Measures student-parent academic retention percentage and average GPA."""
    def run(self) -> StudentParentAcademicRetentionMetric:
        return StudentParentAcademicRetentionMetric(student_parent_retention_rate_pct=91.8, student_parent_avg_gpa=3.32)

class FamilyFriendlyCampusInfrastructureAuditorAgent:
    """Agent 5: Audits lactation/nursing rooms count, family study lounges, and family housing units occupied."""
    def run(self) -> FamilyFriendlyCampusInfrastructureAudit:
        return FamilyFriendlyCampusInfrastructureAudit(lactation_nursing_rooms_count=24, family_study_lounges_count=8, family_housing_units_occupied=180)

class AfterSchoolDropInCareMeterAgent:
    """Agent 6: Measures after-school care participants and emergency drop-in childcare hours provided."""
    def run(self) -> AfterSchoolDropInCareMetric:
        return AfterSchoolDropInCareMetric(after_school_care_participants=180, drop_in_emergency_childcare_hours=2400)

class CampusChildcareServicesScorerAgent:
    """Agent 7: Master deterministic aggregator for Campus Childcare & Family Services."""
    def __init__(self):
        self.enrollment_agent = ChildcareEnrollmentCapacityMeterAgent()
        self.subsidy_agent = ChildcareSubsidyFinancialAidAuditorAgent()
        self.licensing_agent = StateChildcareLicensingAuditorAgent()
        self.retention_agent = StudentParentAcademicRetentionMeterAgent()
        self.infra_agent = FamilyFriendlyCampusInfrastructureAuditorAgent()
        self.after_school_agent = AfterSchoolDropInCareMeterAgent()

    def run(self, children: int = 340) -> DeterministicChildcarePipelineResult:
        enrollment = self.enrollment_agent.run(children)
        subsidies = self.subsidy_agent.run()
        licensing = self.licensing_agent.run()
        retention = self.retention_agent.run()
        infrastructure = self.infra_agent.run()
        after_school = self.after_school_agent.run()

        metrics = {
            "licensing_compliance": licensing.licensing_compliance_score_pct,
            "subsidy_fulfillment": subsidies.subsidy_fulfillment_rate_pct,
            "student_parent_retention": retention.student_parent_retention_rate_pct,
            "certified_staff": licensing.early_childhood_certified_staff_pct
        }
        weights = {"licensing_compliance": 0.35, "subsidy_fulfillment": 0.30, "student_parent_retention": 0.20, "certified_staff": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(enrollment.enrolled_children_count, 50)
        return DeterministicChildcarePipelineResult(
            enrollment=enrollment, subsidies=subsidies, licensing=licensing,
            retention=retention, infrastructure=infrastructure, after_school=after_school,
            childcare_score=score, confidence_score=confidence
        )
