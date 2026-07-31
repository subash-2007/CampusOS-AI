from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class CandidateSkillInventory(BaseModel):
    mastered_hard_skills: List[str] = Field(default_factory=list)
    mastered_soft_skills: List[str] = Field(default_factory=list)

class MissingSkillMatrix(BaseModel):
    critical_missing_skills: List[str] = Field(default_factory=list)
    secondary_missing_skills: List[str] = Field(default_factory=list)
    skill_gap_percentage: float = 0.0

class SkillPriorityRanking(BaseModel):
    high_priority_skills: List[str] = Field(default_factory=list)
    medium_priority_skills: List[str] = Field(default_factory=list)

class CourseRecommendation(BaseModel):
    skill: str
    course_name: str
    platform: str = "Coursera / Udemy"
    estimated_hours: int = 15

class LearningTimelineEstimate(BaseModel):
    estimated_weeks_to_bridge: int = 4
    weekly_hours_required: int = 10

class SkillMasteryScore(BaseModel):
    readiness_index: float = 75.0

class DeterministicSkillGapPipelineResult(BaseModel):
    candidate_skills: CandidateSkillInventory
    gap_matrix: MissingSkillMatrix
    priority_ranking: SkillPriorityRanking
    course_recommendations: List[CourseRecommendation]
    timeline: LearningTimelineEstimate
    mastery_score: SkillMasteryScore
    confidence_score: float

class LearningRoadmapStrategy(BaseModel):
    learning_path: List[str]
    project_ideas: List[str]

class QualitativeSkillReport(BaseModel):
    readiness_summary: str
    competitive_edge_analysis: str

class ReasoningSkillGapPipelineResult(BaseModel):
    qualitative_report: QualitativeSkillReport
    roadmap_strategy: LearningRoadmapStrategy
    reasoning_steps: List[str]

class SkillGapOrchestratorReport(BaseModel):
    department: str = "Skill Gap Intelligence"
    department_id: str = "dept_005"
    target_role: str
    readiness_index: float
    confidence_score: float
    deterministic_analysis: DeterministicSkillGapPipelineResult
    reasoning_analysis: ReasoningSkillGapPipelineResult
    reasoning_steps: List[str]
