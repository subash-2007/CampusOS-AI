from typing import List, Dict, Any
from departments.shared.keywords import KeywordMatcher
from departments.shared.scoring import ScoringEngine
from departments.skill_gap_intelligence.schemas import (
    CandidateSkillInventory, MissingSkillMatrix, SkillPriorityRanking,
    CourseRecommendation, LearningTimelineEstimate, SkillMasteryScore, DeterministicSkillGapPipelineResult
)

class SkillInventoryAuditorAgent:
    """Agent 1: Extracts candidate skills into structured inventory."""
    def run(self, candidate_skills: List[str]) -> CandidateSkillInventory:
        return CandidateSkillInventory(
            mastered_hard_skills=[s for s in candidate_skills if s.strip()],
            mastered_soft_skills=["Leadership", "Communication"]
        )

class GapMatrixCalculatorAgent:
    """Agent 2: Identifies critical and secondary missing skills."""
    def run(self, candidate_skills: List[str], required_skills: List[str]) -> MissingSkillMatrix:
        overlap = KeywordMatcher.calculate_overlap(candidate_skills, required_skills)
        missing = overlap["missing"]
        gap_pct = 100.0 - overlap["match_percentage"]
        return MissingSkillMatrix(
            critical_missing_skills=missing[:3],
            secondary_missing_skills=missing[3:],
            skill_gap_percentage=round(gap_pct, 2)
        )

class SkillPriorityRankerAgent:
    """Agent 3: Ranks missing skills by learning urgency and career impact."""
    def run(self, missing_skills: List[str]) -> SkillPriorityRanking:
        return SkillPriorityRanking(
            high_priority_skills=missing_skills[:2],
            medium_priority_skills=missing_skills[2:]
        )

class CourseRecommendationEngineAgent:
    """Agent 4: Maps missing skills to course recommendations."""
    def run(self, missing_skills: List[str]) -> List[CourseRecommendation]:
        courses = []
        for skill in missing_skills[:4]:
            courses.append(CourseRecommendation(
                skill=skill,
                course_name=f"Mastering {skill} for Enterprise Applications",
                platform="Coursera / Udemy",
                estimated_hours=12
            ))
        return courses

class LearningTimelineEstimatorAgent:
    """Agent 5: Estimates time required to bridge skill gaps."""
    def run(self, missing_skills_count: int) -> LearningTimelineEstimate:
        weeks = max(missing_skills_count * 2, 2)
        return LearningTimelineEstimate(estimated_weeks_to_bridge=weeks, weekly_hours_required=10)

class SkillReadinessScorerAgent:
    """Agent 6: Calculates overall technical readiness index score."""
    def run(self, gap_pct: float) -> SkillMasteryScore:
        readiness = round(max(100.0 - gap_pct, 0.0), 2)
        return SkillMasteryScore(readiness_index=readiness)

class SkillGapScorerAgent:
    """Agent 7: Master deterministic aggregator for Skill Gap Intelligence."""
    def __init__(self):
        self.inventory_agent = SkillInventoryAuditorAgent()
        self.gap_agent = GapMatrixCalculatorAgent()
        self.priority_agent = SkillPriorityRankerAgent()
        self.course_agent = CourseRecommendationEngineAgent()
        self.timeline_agent = LearningTimelineEstimatorAgent()
        self.readiness_agent = SkillReadinessScorerAgent()

    def run(self, candidate_skills: List[str], required_skills: List[str] = None) -> DeterministicSkillGapPipelineResult:
        if required_skills is None:
            required_skills = ["Python", "FastAPI", "React", "Docker", "Kubernetes", "AWS"]

        inventory = self.inventory_agent.run(candidate_skills)
        gap = self.gap_agent.run(candidate_skills, required_skills)
        priority = self.priority_agent.run(gap.critical_missing_skills + gap.secondary_missing_skills)
        courses = self.course_agent.run(gap.critical_missing_skills + gap.secondary_missing_skills)
        timeline = self.timeline_agent.run(len(gap.critical_missing_skills) + len(gap.secondary_missing_skills))
        readiness = self.readiness_agent.run(gap.skill_gap_percentage)

        confidence = ScoringEngine.calculate_confidence_score(
            len(inventory.mastered_hard_skills) + len(required_skills), 10
        )

        return DeterministicSkillGapPipelineResult(
            candidate_skills=inventory,
            gap_matrix=gap,
            priority_ranking=priority,
            course_recommendations=courses,
            timeline=timeline,
            mastery_score=readiness,
            confidence_score=confidence
        )
