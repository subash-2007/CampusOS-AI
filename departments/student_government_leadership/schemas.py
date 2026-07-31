from typing import List
from pydantic import BaseModel

class StudentGovernmentElectionsVoterTurnoutMetric(BaseModel):
    total_eligible_voters: int = 18500
    student_voters_count: int = 8450
    sga_election_voter_turnout_pct: float = 45.7

class SGABudgetAllocationAudit(BaseModel):
    sga_activity_fee_budget_usd: float = 2400000.0
    club_funding_grants_disbursed: int = 340
    budget_disbursement_transparency_pct: float = 100.0

class StudentSenateLegislationMetric(BaseModel):
    senate_bills_introduced: int = 48
    resolutions_passed: int = 38
    administration_adoption_rate_pct: float = 84.2

class StudentLeadershipAcademyMetric(BaseModel):
    leadership_workshop_graduates: int = 420
    student_leaders_certified: int = 180

class StudentAdvocacyTownHallMetric(BaseModel):
    campus_town_halls_hosted: int = 8
    student_petitions_addressed: int = 24
    town_hall_attendees_annual: int = 2800

class LeadershipCertificateBadgeAudit(BaseModel):
    leadership_digital_badges_issued: int = 650
    leadership_competency_assessment_score: float = 4.8

class DeterministicSGAPipelineResult(BaseModel):
    elections: StudentGovernmentElectionsVoterTurnoutMetric
    budget: SGABudgetAllocationAudit
    senate: StudentSenateLegislationMetric
    academy: StudentLeadershipAcademyMetric
    town_halls: StudentAdvocacyTownHallMetric
    badges: LeadershipCertificateBadgeAudit
    sga_score: float
    confidence_score: float

class StrategicSGANarrative(BaseModel):
    sga_summary: str
    key_sga_strengths: List[str]

class StudentGovernancePlan(BaseModel):
    governance_actions: List[str]
    sample_sga_bill_schema: str

class ReasoningSGAPipelineResult(BaseModel):
    narrative: StrategicSGANarrative
    governance_plan: StudentGovernancePlan
    reasoning_steps: List[str]

class StudentGovernmentLeadershipOrchestratorReport(BaseModel):
    department: str = "Student Government & Leadership"
    department_id: str = "dept_076"
    governance_tier: str = "HIGH-ENGAGEMENT STUDENT DEMOCRACY"
    sga_score: float
    confidence_score: float
    deterministic_analysis: DeterministicSGAPipelineResult
    reasoning_analysis: ReasoningSGAPipelineResult
    reasoning_steps: List[str]
