from typing import List
from pydantic import BaseModel

class AlumniNetworkSizeMetric(BaseModel):
    registered_alumni_count: int = 18400
    active_monthly_alumni_count: int = 6800
    alumni_engagement_pct: float = 36.9

class AlumniMentorshipPairingMetric(BaseModel):
    active_mentorship_pairs: int = 1250
    mentorship_satisfaction_score: float = 4.8
    match_success_rate_pct: float = 94.2

class AlumniDonationGivingMetric(BaseModel):
    annual_alumni_donations_usd: float = 3450000.0
    alumni_donor_participation_pct: float = 14.8

class AlumniEventParticipationMetric(BaseModel):
    reunion_events_count_annual: int = 18
    alumni_event_attendees_total: int = 8400

class AlumniCareerTransitionMetric(BaseModel):
    alumni_hiring_students_count: int = 420
    alumni_job_referrals_made: int = 1140

class AlumniChapterNetworkAudit(BaseModel):
    regional_chapters_count: int = 24
    global_city_hubs_count: int = 12

class DeterministicAlumniPipelineResult(BaseModel):
    network_size: AlumniNetworkSizeMetric
    mentorship: AlumniMentorshipPairingMetric
    donations: AlumniDonationGivingMetric
    events: AlumniEventParticipationMetric
    career_transitions: AlumniCareerTransitionMetric
    chapters: AlumniChapterNetworkAudit
    alumni_engagement_score: float
    confidence_score: float

class StrategicAlumniNarrative(BaseModel):
    alumni_summary: str
    key_alumni_strengths: List[str]

class AlumniEngagementPlan(BaseModel):
    engagement_growth_actions: List[str]
    sample_mentorship_matching_rules: str

class ReasoningAlumniPipelineResult(BaseModel):
    narrative: StrategicAlumniNarrative
    engagement_plan: AlumniEngagementPlan
    reasoning_steps: List[str]

class AlumniMentorshipOrchestratorReport(BaseModel):
    department: str = "Alumni Mentorship & Engagement"
    department_id: str = "dept_060"
    alumni_tier: str = "HIGHLY ENGAGED ALUMNI NETWORK"
    alumni_engagement_score: float
    confidence_score: float
    deterministic_analysis: DeterministicAlumniPipelineResult
    reasoning_analysis: ReasoningAlumniPipelineResult
    reasoning_steps: List[str]
