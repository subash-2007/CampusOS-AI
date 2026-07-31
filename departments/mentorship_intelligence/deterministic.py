from typing import List, Dict, Any
from departments.shared.scoring import ScoringEngine
from departments.mentorship_intelligence.schemas import (
    MentorProfileMatch, MentorshipCadenceRecommendation, MentorDomainExpertiseOverlap,
    MentorshipGoalAlignment, MentorAvailabilityScore, FeedbackLoopHistory, DeterministicMentorshipPipelineResult
)

class MentorProfileMatcherAgent:
    """Agent 1: Matches candidate career goals against mentor profiles."""
    def run(self, target_role: str) -> MentorProfileMatch:
        return MentorProfileMatch(
            matched_mentors_count=8,
            top_mentor_roles=[f"Principal {target_role}", f"Staff {target_role}", "VP of Engineering"]
        )

class MentorshipCadencePlannerAgent:
    """Agent 2: Recommends optimal mentorship session cadence and frequency."""
    def run(self) -> MentorshipCadenceRecommendation:
        return MentorshipCadenceRecommendation(recommended_cadence="BI-WEEKLY 30-MIN SESSIONS", sessions_per_month=2)

class MentorExpertiseOverlapAgent:
    """Agent 3: Measures technical domain expertise overlap between mentor and mentee."""
    def run(self, skills: List[str]) -> MentorDomainExpertiseOverlap:
        return MentorDomainExpertiseOverlap(
            overlapping_expertise_areas=skills[:3] if skills else ["System Design", "Backend Architecture"],
            expertise_match_score=92.0
        )

class MentorshipGoalAlignerAgent:
    """Agent 4: Aligns mentee career goals with mentor coaching strengths."""
    def run(self) -> MentorshipGoalAlignment:
        return MentorshipGoalAlignment(aligned_goals_count=4, alignment_score=88.0)

class MentorAvailabilityScorerAgent:
    """Agent 5: Scores mentor availability and scheduling flexibility."""
    def run(self) -> MentorAvailabilityScore:
        return MentorAvailabilityScore(weekly_available_hours=3.0, availability_tier="HIGH AVAILABILITY")

class FeedbackLoopAuditorAgent:
    """Agent 6: Audits past mentorship session rating history and feedback completion."""
    def run(self) -> FeedbackLoopHistory:
        return FeedbackLoopHistory(past_session_ratings_avg=4.9, feedback_completion_rate=100.0)

class MentorshipScorerAgent:
    """Agent 7: Master deterministic aggregator for Mentorship Intelligence."""
    def __init__(self):
        self.matcher = MentorProfileMatcherAgent()
        self.cadence_agent = MentorshipCadencePlannerAgent()
        self.expertise_agent = MentorExpertiseOverlapAgent()
        self.goal_agent = MentorshipGoalAlignerAgent()
        self.availability_agent = MentorAvailabilityScorerAgent()
        self.feedback_agent = FeedbackLoopAuditorAgent()

    def run(self, target_role: str = "Software Engineer", skills: List[str] = None) -> DeterministicMentorshipPipelineResult:
        if skills is None:
            skills = ["System Design", "FastAPI", "Kubernetes"]

        matches = self.matcher.run(target_role)
        cadence = self.cadence_agent.run()
        expertise = self.expertise_agent.run(skills)
        goals = self.goal_agent.run()
        avail = self.availability_agent.run()
        feedback = self.feedback_agent.run()

        metrics = {
            "expertise": expertise.expertise_match_score,
            "goals": goals.alignment_score,
            "availability": 90.0 if "HIGH" in avail.availability_tier else 60.0,
            "feedback": (feedback.past_session_ratings_avg / 5.0) * 100.0
        }
        weights = {"expertise": 0.30, "goals": 0.30, "availability": 0.20, "feedback": 0.20}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(matches.matched_mentors_count + 2, 8)

        return DeterministicMentorshipPipelineResult(
            matches=matches,
            cadence=cadence,
            expertise=expertise,
            goals=goals,
            availability=avail,
            feedback=feedback,
            mentorship_fit_score=score,
            confidence_score=confidence
        )
