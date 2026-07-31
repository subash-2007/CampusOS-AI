from departments.shared.scoring import ScoringEngine
from departments.dei_intelligence.schemas import (
    DiversityDemographicsRepresentationMetric, FacultyStaffDiversityAudit, CulturalCenterEngagementMetric,
    InclusiveCurriculumAudit, BiasIncidentReportingResolutionAudit, DiversityScholarshipMetric, DeterministicDEIPipelineResult
)

class DiversityDemographicsRepresentationMeterAgent:
    """Agent 1: Measures underrepresented minority percentage, first-gen percentage, and Pell Grant eligible percentage."""
    def run(self, urm_pct: float = 34.8) -> DiversityDemographicsRepresentationMetric:
        return DiversityDemographicsRepresentationMetric(underrepresented_minority_students_pct=urm_pct, first_gen_college_students_pct=28.5, pell_grant_eligible_students_pct=31.2)

class FacultyStaffDiversityAuditorAgent:
    """Agent 2: Audits diverse faculty count, diverse faculty percentage, and inclusive search committee training compliance."""
    def run(self) -> FacultyStaffDiversityAudit:
        return FacultyStaffDiversityAudit(diversity_faculty_count=420, diverse_faculty_pct=28.4, inclusive_search_committee_training_pct=100.0)

class CulturalCenterEngagementMeterAgent:
    """Agent 3: Measures cultural resource centers, annual cultural event attendance, and affinity graduation celebrations."""
    def run(self) -> CulturalCenterEngagementMetric:
        return CulturalCenterEngagementMetric(cultural_resource_centers_count=6, annual_cultural_event_attendees=14500, affinity_graduation_celebrations=12)

class InclusiveCurriculumAuditorAgent:
    """Agent 4: Audits DEI designated courses count, inclusive pedagogy trained faculty, and curriculum audit score."""
    def run(self) -> InclusiveCurriculumAudit:
        return InclusiveCurriculumAudit(courses_with_dei_designation=420, inclusive_pedagogy_trained_faculty=680, dei_curriculum_audit_score_pct=94.5)

class BiasIncidentReportingResolutionAuditorAgent:
    """Agent 5: Audits bias incident reports annual volume, response team resolution percentage, and resolution speed (days)."""
    def run(self) -> BiasIncidentReportingResolutionAudit:
        return BiasIncidentReportingResolutionAudit(bias_incidents_reported_annual=34, bias_response_team_resolution_pct=97.0, avg_resolution_days=3.5)

class DiversityScholarshipMeterAgent:
    """Agent 6: Measures DEI scholarship funding (USD) and diversity scholar recipient counts."""
    def run(self) -> DiversityScholarshipMetric:
        return DiversityScholarshipMetric(dei_scholastic_funding_usd=1850000.0, diversity_scholars_count=420)

class DiversityEquityInclusionScorerAgent:
    """Agent 7: Master deterministic aggregator for Diversity Equity & Inclusion."""
    def __init__(self):
        self.demographics_agent = DiversityDemographicsRepresentationMeterAgent()
        self.faculty_agent = FacultyStaffDiversityAuditorAgent()
        self.cultural_agent = CulturalCenterEngagementMeterAgent()
        self.curriculum_agent = InclusiveCurriculumAuditorAgent()
        self.bias_agent = BiasIncidentReportingResolutionAuditorAgent()
        self.scholarship_agent = DiversityScholarshipMeterAgent()

    def run(self, urm_pct: float = 34.8) -> DeterministicDEIPipelineResult:
        demographics = self.demographics_agent.run(urm_pct)
        faculty_diversity = self.faculty_agent.run()
        cultural_centers = self.cultural_agent.run()
        inclusive_curriculum = self.curriculum_agent.run()
        bias_response = self.bias_agent.run()
        scholarships = self.scholarship_agent.run()

        metrics = {
            "search_training": faculty_diversity.inclusive_search_committee_training_pct,
            "bias_resolution": bias_response.bias_response_team_resolution_pct,
            "curriculum_score": inclusive_curriculum.dei_curriculum_audit_score_pct,
            "urm_representation": min(100.0, demographics.underrepresented_minority_students_pct * 2.5)
        }
        weights = {"search_training": 0.35, "bias_resolution": 0.30, "curriculum_score": 0.20, "urm_representation": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(int(demographics.underrepresented_minority_students_pct), 10)
        return DeterministicDEIPipelineResult(
            demographics=demographics, faculty_diversity=faculty_diversity,
            cultural_centers=cultural_centers, inclusive_curriculum=inclusive_curriculum,
            bias_response=bias_response, scholarships=scholarships,
            dei_score=score, confidence_score=confidence
        )
