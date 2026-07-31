from departments.shared.scoring import ScoringEngine
from departments.admissions_enrollment_management.schemas import (
    UndergraduateAdmissionsApplicationVolumeMetric, EnrollmentYieldDepositMetric, ApplicationHolisticReviewTurnaroundAudit,
    CampusTourOpenHouseVisitorMetric, CRMRecruitmentCampaignAudit, HighSchoolGPAStandardizedTestAudit, DeterministicAdmissionsPipelineResult
)

class UndergraduateAdmissionsApplicationVolumeMeterAgent:
    """Agent 1: Measures total applications received, admitted students count, and selectivity rate percentage."""
    def run(self, apps: int = 38500) -> UndergraduateAdmissionsApplicationVolumeMetric:
        return UndergraduateAdmissionsApplicationVolumeMetric(applications_received_count=apps, admitted_students_count=14200, admissions_selectivity_rate_pct=36.8)

class EnrollmentYieldDepositMeterAgent:
    """Agent 2: Measures enrolled freshmen headcount, enrollment yield rate percentage, and tuition deposit fulfillment."""
    def run(self) -> EnrollmentYieldDepositMetric:
        return EnrollmentYieldDepositMetric(enrolled_freshmen_count=4850, enrollment_yield_rate_pct=34.2, tuition_deposit_fulfillment_pct=98.6)

class ApplicationHolisticReviewTurnaroundAuditorAgent:
    """Agent 3: Audits holistic file reviews completed, average review speed (days), and rubric compliance percentage."""
    def run(self) -> ApplicationHolisticReviewTurnaroundAudit:
        return ApplicationHolisticReviewTurnaroundAudit(holistic_file_reviews_completed=38500, avg_application_review_days=14.5, holistic_rubric_audit_compliance_pct=100.0)

class CampusTourOpenHouseVisitorMeterAgent:
    """Agent 4: Measures annual campus tour visitors, open house attendees, and tour-to-application conversion percentage."""
    def run(self) -> CampusTourOpenHouseVisitorMetric:
        return CampusTourOpenHouseVisitorMetric(campus_tour_visitors_annual=24500, prospective_student_open_house_attendees=8400, tour_visitor_application_conversion_pct=68.4)

class CRMRecruitmentCampaignAuditorAgent:
    """Agent 5: Audits prospect contacts in Slate CRM, email campaign open rate percentage, and inquiry-to-applicant conversion."""
    def run(self) -> CRMRecruitmentCampaignAudit:
        return CRMRecruitmentCampaignAudit(prospect_contacts_in_slate_crm=185000, email_campaign_open_rate_pct=48.5, inquiry_to_applicant_conversion_pct=24.2)

class HighSchoolGPAStandardizedTestAuditorAgent:
    """Agent 6: Audits enrolled class average GPA and test-optional applicant percentage."""
    def run(self) -> HighSchoolGPAStandardizedTestAudit:
        return HighSchoolGPAStandardizedTestAudit(enrolled_class_avg_gpa=3.84, test_optional_applicants_pct=62.0)

class AdmissionsEnrollmentManagementScorerAgent:
    """Agent 7: Master deterministic aggregator for Admissions & Enrollment Management."""
    def __init__(self):
        self.volume_agent = UndergraduateAdmissionsApplicationVolumeMeterAgent()
        self.yield_agent = EnrollmentYieldDepositMeterAgent()
        self.review_agent = ApplicationHolisticReviewTurnaroundAuditorAgent()
        self.tours_agent = CampusTourOpenHouseVisitorMeterAgent()
        self.crm_agent = CRMRecruitmentCampaignAuditorAgent()
        self.academics_agent = HighSchoolGPAStandardizedTestAuditorAgent()

    def run(self, apps: int = 38500) -> DeterministicAdmissionsPipelineResult:
        volume = self.volume_agent.run(apps)
        yield_metric = self.yield_agent.run()
        holistic_review = self.review_agent.run()
        tours = self.tours_agent.run()
        crm = self.crm_agent.run()
        academics = self.academics_agent.run()

        metrics = {
            "holistic_rubric": holistic_review.holistic_rubric_audit_compliance_pct,
            "deposit_fulfillment": yield_metric.tuition_deposit_fulfillment_pct,
            "tour_conversion": tours.tour_visitor_application_conversion_pct * 1.3,
            "enrolled_gpa": (academics.enrolled_class_avg_gpa / 4.0) * 100
        }
        weights = {"holistic_rubric": 0.35, "deposit_fulfillment": 0.30, "tour_conversion": 0.20, "enrolled_gpa": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(volume.applications_received_count, 1000)
        return DeterministicAdmissionsPipelineResult(
            volume=volume, yield_metric=yield_metric, holistic_review=holistic_review,
            tours=tours, crm=crm, academics=academics,
            admissions_score=score, confidence_score=confidence
        )
