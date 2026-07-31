from typing import List
from pydantic import BaseModel

class AlumniNetworkMentorshipEngagementMetric(BaseModel):
    registered_alumni_mentors_count: int = 8450
    active_alumni_student_matches: int = 3420
    mentorship_satisfaction_rate_pct: float = 96.4

class AlumniMidCareerTransitionCoachingAudit(BaseModel):
    alumni_coaching_sessions_held: int = 1850
    career_pivot_success_rate_pct: float = 88.5
    resume_linkedin_review_requests: int = 2400

class RegionalAlumniChapterEventMetric(BaseModel):
    active_regional_chapters_count: int = 42
    annual_alumni_networking_events: int = 380
    chapter_event_attendees_annual: int = 24500

class AlumniJobBoardHiringReferralAudit(BaseModel):
    alumni_posted_job_openings: int = 4800
    alumni_referrals_submitted: int = 1250
    alumni_hire_conversion_rate_pct: float = 34.2

class LifelongLearningAlumniUpskillingMetric(BaseModel):
    alumni_enrolled_in_micro_credentials: int = 3200
    alumni_tuition_discount_utilized_usd: float = 640000.0

class AlumniDirectoryDataFreshnessAudit(BaseModel):
    alumni_profiles_updated_annual_pct: float = 78.4
    linkedin_sync_accuracy_pct: float = 94.2

class DeterministicAlumniCareerPipelineResult(BaseModel):
    mentorship: AlumniNetworkMentorshipEngagementMetric
    coaching: AlumniMidCareerTransitionCoachingAudit
    chapters: RegionalAlumniChapterEventMetric
    job_board: AlumniJobBoardHiringReferralAudit
    lifelong_learning: LifelongLearningAlumniUpskillingMetric
    directory: AlumniDirectoryDataFreshnessAudit
    alumni_career_score: float
    confidence_score: float

class StrategicAlumniCareerNarrative(BaseModel):
    alumni_career_summary: str
    key_alumni_career_strengths: List[str]

class AlumniCareerPlan(BaseModel):
    alumni_career_actions: List[str]
    sample_alumni_mentor_matching_schema: str

class ReasoningAlumniCareerPipelineResult(BaseModel):
    narrative: StrategicAlumniCareerNarrative
    alumni_career_plan: AlumniCareerPlan
    reasoning_steps: List[str]

class AlumniCareerNetworkingOrchestratorReport(BaseModel):
    department: str = "Alumni Career Services & Networking"
    department_id: str = "dept_081"
    alumni_career_tier: str = "GLOBAL ALUMNI CAREER POWERHOUSE"
    alumni_career_score: float
    confidence_score: float
    deterministic_analysis: DeterministicAlumniCareerPipelineResult
    reasoning_analysis: ReasoningAlumniCareerPipelineResult
    reasoning_steps: List[str]
