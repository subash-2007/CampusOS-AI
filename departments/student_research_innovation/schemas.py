from typing import List
from pydantic import BaseModel

class UndergraduateResearchProgramMetric(BaseModel):
    undergraduate_researchers_active: int = 1840
    faculty_mentored_research_projects: int = 420
    undergrad_research_symposium_presenters: int = 680

class StartupIncubatorVentureMetric(BaseModel):
    student_startups_in_incubator: int = 84
    seed_funding_awarded_total_usd: float = 1840000.0
    incubator_startups_raised_external_funding: int = 28

class PatentTechTransferAudit(BaseModel):
    patents_filed_annual: int = 48
    technology_licenses_executed: int = 18
    tech_transfer_royalties_usd: float = 2840000.0

class MakerspaceFabLabUsageMetric(BaseModel):
    makerspace_student_active_users: int = 3840
    makerspace_equipment_utilization_pct: float = 74.8
    project_prototypes_completed_annual: int = 1240

class InnovationChallengeGrantMetric(BaseModel):
    innovation_challenge_entries_annual: int = 840
    innovation_grants_awarded: int = 124
    avg_innovation_grant_award_usd: float = 4800.0

class IndustryPartnershipResearchAgreementAudit(BaseModel):
    industry_research_partnership_agreements: int = 68
    sponsored_research_revenue_millions: float = 24.8
    collaborative_publications_with_industry: int = 184

class DeterministicInnovationPipelineResult(BaseModel):
    undergrad_research: UndergraduateResearchProgramMetric
    incubator: StartupIncubatorVentureMetric
    patents: PatentTechTransferAudit
    makerspace: MakerspaceFabLabUsageMetric
    innovation_grants: InnovationChallengeGrantMetric
    industry: IndustryPartnershipResearchAgreementAudit
    innovation_score: float
    confidence_score: float

class StrategicInnovationNarrative(BaseModel):
    innovation_summary: str
    key_innovation_strengths: List[str]

class InnovationIncubatorPlan(BaseModel):
    innovation_actions: List[str]
    sample_startup_pitch_deck_schema: str

class ReasoningInnovationPipelineResult(BaseModel):
    narrative: StrategicInnovationNarrative
    innovation_plan: InnovationIncubatorPlan
    reasoning_steps: List[str]

class StudentResearchInnovationOrchestratorReport(BaseModel):
    department: str = "Student Research & Innovation Incubator"
    department_id: str = "dept_100"
    innovation_tier: str = "NATIONALLY RANKED STUDENT INNOVATION ECOSYSTEM"
    innovation_score: float
    confidence_score: float
    deterministic_analysis: DeterministicInnovationPipelineResult
    reasoning_analysis: ReasoningInnovationPipelineResult
    reasoning_steps: List[str]
