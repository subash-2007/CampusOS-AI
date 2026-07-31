from typing import List
from pydantic import BaseModel

class DiversityDemographicsRepresentationMetric(BaseModel):
    underrepresented_minority_students_pct: float = 34.8
    first_gen_college_students_pct: float = 28.5
    pell_grant_eligible_students_pct: float = 31.2

class FacultyStaffDiversityAudit(BaseModel):
    diversity_faculty_count: int = 420
    diverse_faculty_pct: float = 28.4
    inclusive_search_committee_training_pct: float = 100.0

class CulturalCenterEngagementMetric(BaseModel):
    cultural_resource_centers_count: int = 6
    annual_cultural_event_attendees: int = 14500
    affinity_graduation_celebrations: int = 12

class InclusiveCurriculumAudit(BaseModel):
    courses_with_dei_designation: int = 420
    inclusive_pedagogy_trained_faculty: int = 680
    dei_curriculum_audit_score_pct: float = 94.5

class BiasIncidentReportingResolutionAudit(BaseModel):
    bias_incidents_reported_annual: int = 34
    bias_response_team_resolution_pct: float = 97.0
    avg_resolution_days: float = 3.5

class DiversityScholarshipMetric(BaseModel):
    dei_scholastic_funding_usd: float = 1850000.0
    diversity_scholars_count: int = 420

class DeterministicDEIPipelineResult(BaseModel):
    demographics: DiversityDemographicsRepresentationMetric
    faculty_diversity: FacultyStaffDiversityAudit
    cultural_centers: CulturalCenterEngagementMetric
    inclusive_curriculum: InclusiveCurriculumAudit
    bias_response: BiasIncidentReportingResolutionAudit
    scholarships: DiversityScholarshipMetric
    dei_score: float
    confidence_score: float

class StrategicDEINarrative(BaseModel):
    dei_summary: str
    key_dei_strengths: List[str]

class DEIActionPlan(BaseModel):
    dei_improvement_actions: List[str]
    sample_inclusive_hiring_rubric: str

class ReasoningDEIPipelineResult(BaseModel):
    narrative: StrategicDEINarrative
    action_plan: DEIActionPlan
    reasoning_steps: List[str]

class DiversityEquityInclusionOrchestratorReport(BaseModel):
    department: str = "Diversity Equity & Inclusion"
    department_id: str = "dept_075"
    dei_tier: str = "NATIONAL MODEL FOR INCLUSIVE EXCELLENCE"
    dei_score: float
    confidence_score: float
    deterministic_analysis: DeterministicDEIPipelineResult
    reasoning_analysis: ReasoningDEIPipelineResult
    reasoning_steps: List[str]
