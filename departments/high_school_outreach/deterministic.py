from departments.shared.scoring import ScoringEngine
from departments.high_school_outreach.schemas import (
    HighSchoolPartnerCountMetric, K12STEMProgramParticipationMetric, DualEnrollmentCreditAudit,
    CampusTourVisitMetric, CounselorRelationshipAudit, OutreachScholarshipMetric, DeterministicOutreachPipelineResult
)

class HighSchoolPartnerCountMeterAgent:
    """Agent 1: Measures partner high school count, feeder high schools, and Title-1 support percentage."""
    def run(self, schools: int = 184) -> HighSchoolPartnerCountMetric:
        return HighSchoolPartnerCountMetric(partner_high_schools_count=schools, feeder_high_schools_count=42, title_1_schools_supported_pct=38.0)

class K12STEMProgramParticipationMeterAgent:
    """Agent 2: Measures STEM camps hosted, K-12 participants, and underrepresented minority STEM percentage."""
    def run(self) -> K12STEMProgramParticipationMetric:
        return K12STEMProgramParticipationMetric(stem_camps_hosted=14, k12_student_participants=3850, female_minority_stem_pct=68.0)

class DualEnrollmentCreditAuditorAgent:
    """Agent 3: Audits dual enrollment student counts, credits earned, and post-HS matriculation rate."""
    def run(self) -> DualEnrollmentCreditAudit:
        return DualEnrollmentCreditAudit(dual_enrollment_students_count=840, credits_earned_total=5040, matriculation_rate_post_hs_pct=52.0)

class CampusTourVisitMeterAgent:
    """Agent 4: Measures high school campus tours hosted, visitor counts, and satisfaction scores."""
    def run(self) -> CampusTourVisitMetric:
        return CampusTourVisitMetric(high_school_tours_hosted=68, total_hs_visitors=6200, tour_satisfaction_score=4.8)

class CounselorRelationshipAuditorAgent:
    """Agent 5: Audits registered high school counselor count and counselor portal activity."""
    def run(self) -> CounselorRelationshipAudit:
        return CounselorRelationshipAudit(registered_hs_counselors=320, counselor_portal_active_users=272)

class OutreachScholarshipMeterAgent:
    """Agent 6: Measures K-12 outreach grants awarded (USD) and recipient student count."""
    def run(self) -> OutreachScholarshipMetric:
        return OutreachScholarshipMetric(k12_outreach_grants_awarded_usd=240000.0, scholarship_recipients_count=120)

class HighSchoolOutreachScorerAgent:
    """Agent 7: Master deterministic aggregator for High School & K-12 Outreach."""
    def __init__(self):
        self.partner_agent = HighSchoolPartnerCountMeterAgent()
        self.stem_agent = K12STEMProgramParticipationMeterAgent()
        self.dual_agent = DualEnrollmentCreditAuditorAgent()
        self.tour_agent = CampusTourVisitMeterAgent()
        self.counselor_agent = CounselorRelationshipAuditorAgent()
        self.scholarship_agent = OutreachScholarshipMeterAgent()

    def run(self, schools: int = 184) -> DeterministicOutreachPipelineResult:
        partnerships = self.partner_agent.run(schools)
        stem_programs = self.stem_agent.run()
        dual_enrollment = self.dual_agent.run()
        tours = self.tour_agent.run()
        counselors = self.counselor_agent.run()
        scholarships = self.scholarship_agent.run()

        metrics = {
            "dual_matriculation": dual_enrollment.matriculation_rate_post_hs_pct * 1.8,
            "stem_diversity": stem_programs.female_minority_stem_pct,
            "tour_satisfaction": (tours.tour_satisfaction_score / 5.0) * 100,
            "counselor_active": (counselors.counselor_portal_active_users / counselors.registered_hs_counselors) * 100
        }
        weights = {"dual_matriculation": 0.35, "stem_diversity": 0.25, "tour_satisfaction": 0.20, "counselor_active": 0.20}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(partnerships.partner_high_schools_count, 20)
        return DeterministicOutreachPipelineResult(
            partnerships=partnerships, stem_programs=stem_programs, dual_enrollment=dual_enrollment,
            tours=tours, counselors=counselors, scholarships=scholarships,
            outreach_health_score=score, confidence_score=confidence
        )
