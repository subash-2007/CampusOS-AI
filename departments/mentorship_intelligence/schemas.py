from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class MentorProfileMatch(BaseModel):
    matched_mentors_count: int = 8
    top_mentor_roles: List[str] = Field(default_factory=list)

class MentorshipCadenceRecommendation(BaseModel):
    recommended_cadence: str = "BI-WEEKLY 30-MIN SESSIONS"
    sessions_per_month: int = 2

class MentorDomainExpertiseOverlap(BaseModel):
    overlapping_expertise_areas: List[str] = Field(default_factory=list)
    expertise_match_score: float = 92.0

class MentorshipGoalAlignment(BaseModel):
    aligned_goals_count: int = 4
    alignment_score: float = 88.0

class MentorAvailabilityScore(BaseModel):
    weekly_available_hours: float = 3.0
    availability_tier: str = "HIGH AVAILABILITY"

class FeedbackLoopHistory(BaseModel):
    past_session_ratings_avg: float = 4.9
    feedback_completion_rate: float = 100.0

class DeterministicMentorshipPipelineResult(BaseModel):
    matches: MentorProfileMatch
    cadence: MentorshipCadenceRecommendation
    expertise: MentorDomainExpertiseOverlap
    goals: MentorshipGoalAlignment
    availability: MentorAvailabilityScore
    feedback: FeedbackLoopHistory
    mentorship_fit_score: float
    confidence_score: float

class QualitativeMentorshipNarrative(BaseModel):
    mentorship_strategy_summary: str
    key_mentor_pairings: List[str]

class SessionAgendaPlan(BaseModel):
    suggested_session_agendas: List[str]
    growth_milestones: List[str]

class ReasoningMentorshipPipelineResult(BaseModel):
    narrative: QualitativeMentorshipNarrative
    agenda_plan: SessionAgendaPlan
    reasoning_steps: List[str]

class MentorshipOrchestratorReport(BaseModel):
    department: str = "Mentorship Intelligence"
    department_id: str = "dept_018"
    mentorship_fit_tier: str = "HIGH COMPATIBILITY"
    mentorship_fit_score: float
    confidence_score: float
    deterministic_analysis: DeterministicMentorshipPipelineResult
    reasoning_analysis: ReasoningMentorshipPipelineResult
    reasoning_steps: List[str]
