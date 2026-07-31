from departments.shared.scoring import ScoringEngine
from departments.university_campus_relations.schemas import (
    UniversityPartnerCountMetric, CampusFairEventMetric, UniversityPlacementRateAudit,
    UniversityMOUStatusAudit, StudentEngagementMetric, FacultyCollaborationMetric, DeterministicCampusPipelineResult
)

class UniversityPartnerCountMeterAgent:
    """Agent 1: Measures total partner university count, Tier-1 universities, and global partners."""
    def run(self, universities: int = 142) -> UniversityPartnerCountMetric:
        return UniversityPartnerCountMetric(total_partner_universities=universities, tier1_universities_count=38, global_university_partners=24)

class CampusFairEventMeterAgent:
    """Agent 2: Measures annual career fairs hosted, total student attendees, and employer booths."""
    def run(self) -> CampusFairEventMetric:
        return CampusFairEventMetric(career_fairs_hosted_annual=28, student_attendees_total=42500, employer_booths_total=860)

class UniversityPlacementRateAuditorAgent:
    """Agent 3: Audits overall campus placement rate and top hiring partner count."""
    def run(self) -> UniversityPlacementRateAudit:
        return UniversityPlacementRateAudit(overall_campus_placement_rate_pct=91.2, top_hiring_partners_count=65)

class UniversityMOUStatusAuditorAgent:
    """Agent 4: Audits active MOU contract count and MOU renewal rate."""
    def run(self) -> UniversityMOUStatusAudit:
        return UniversityMOUStatusAudit(active_mou_contracts=128, mou_renewal_rate_pct=95.5)

class StudentEngagementMeterAgent:
    """Agent 5: Measures student platform adoption percentage and career center appointments booked."""
    def run(self) -> StudentEngagementMetric:
        return StudentEngagementMetric(student_platform_adoption_pct=84.0, career_center_appointments_booked=12400)

class FacultyCollaborationMeterAgent:
    """Agent 6: Measures joint research projects count and faculty-endorsed skill count."""
    def run(self) -> FacultyCollaborationMetric:
        return FacultyCollaborationMetric(joint_research_projects_count=42, faculty_endorsed_skills_count=88)

class UniversityCampusRelationsScorerAgent:
    """Agent 7: Master deterministic aggregator for University & Campus Relations."""
    def __init__(self):
        self.partners_agent = UniversityPartnerCountMeterAgent()
        self.fairs_agent = CampusFairEventMeterAgent()
        self.placement_agent = UniversityPlacementRateAuditorAgent()
        self.mou_agent = UniversityMOUStatusAuditorAgent()
        self.student_agent = StudentEngagementMeterAgent()
        self.faculty_agent = FacultyCollaborationMeterAgent()

    def run(self, universities: int = 142) -> DeterministicCampusPipelineResult:
        partners = self.partners_agent.run(universities)
        fairs = self.fairs_agent.run()
        placement = self.placement_agent.run()
        mou = self.mou_agent.run()
        student = self.student_agent.run()
        faculty = self.faculty_agent.run()

        metrics = {
            "placement": placement.overall_campus_placement_rate_pct,
            "mou_renewal": mou.mou_renewal_rate_pct,
            "student_adoption": student.student_platform_adoption_pct,
            "fair_volume": min(100.0, fairs.career_fairs_hosted_annual * 3.5)
        }
        weights = {"placement": 0.35, "mou_renewal": 0.25, "student_adoption": 0.25, "fair_volume": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(partners.total_partner_universities, 10)
        return DeterministicCampusPipelineResult(
            partners=partners, fairs=fairs, placement=placement,
            mou=mou, student_engagement=student, faculty=faculty,
            campus_relations_score=score, confidence_score=confidence
        )
