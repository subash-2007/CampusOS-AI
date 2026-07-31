from typing import List
from pydantic import BaseModel

class UniversityPartnerCountMetric(BaseModel):
    total_partner_universities: int = 142
    tier1_universities_count: int = 38
    global_university_partners: int = 24

class CampusFairEventMetric(BaseModel):
    career_fairs_hosted_annual: int = 28
    student_attendees_total: int = 42500
    employer_booths_total: int = 860

class UniversityPlacementRateAudit(BaseModel):
    overall_campus_placement_rate_pct: float = 91.2
    top_hiring_partners_count: int = 65

class UniversityMOUStatusAudit(BaseModel):
    active_mou_contracts: int = 128
    mou_renewal_rate_pct: float = 95.5

class StudentEngagementMetric(BaseModel):
    student_platform_adoption_pct: float = 84.0
    career_center_appointments_booked: int = 12400

class FacultyCollaborationMetric(BaseModel):
    joint_research_projects_count: int = 42
    faculty_endorsed_skills_count: int = 88

class DeterministicCampusPipelineResult(BaseModel):
    partners: UniversityPartnerCountMetric
    fairs: CampusFairEventMetric
    placement: UniversityPlacementRateAudit
    mou: UniversityMOUStatusAudit
    student_engagement: StudentEngagementMetric
    faculty: FacultyCollaborationMetric
    campus_relations_score: float
    confidence_score: float

class StrategicCampusNarrative(BaseModel):
    campus_summary: str
    key_campus_strengths: List[str]

class CampusRelationsPlan(BaseModel):
    university_expansion_actions: List[str]
    sample_mou_agreement_summary: str

class ReasoningCampusPipelineResult(BaseModel):
    narrative: StrategicCampusNarrative
    relations_plan: CampusRelationsPlan
    reasoning_steps: List[str]

class UniversityCampusRelationsOrchestratorReport(BaseModel):
    department: str = "University & Campus Relations"
    department_id: str = "dept_053"
    campus_tier: str = "STRATEGIC ACADEMIC PARTNER"
    campus_relations_score: float
    confidence_score: float
    deterministic_analysis: DeterministicCampusPipelineResult
    reasoning_analysis: ReasoningCampusPipelineResult
    reasoning_steps: List[str]
