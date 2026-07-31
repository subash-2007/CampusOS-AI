from typing import List
from pydantic import BaseModel

class CourseCompletionRateMetric(BaseModel):
    course_completion_rate_pct: float = 72.4
    avg_learning_hours_per_week: float = 4.5
    certificates_issued_count: int = 1420

class LearningSkillGainMetric(BaseModel):
    pre_post_assessment_gain_pct: float = 34.0
    skills_mastered_per_course: float = 5.2
    assessment_pass_rate_pct: float = 88.5

class CourseCatalogAudit(BaseModel):
    total_courses_count: int = 84
    interactive_labs_count: int = 240
    catalog_freshness_score: float = 92.0

class LearnerEngagementMetric(BaseModel):
    active_learners_count: int = 3400
    video_retention_rate_pct: float = 78.0
    quiz_attempt_rate_pct: float = 94.0

class CourseRatingFeedbackAudit(BaseModel):
    avg_course_rating: float = 4.7
    total_reviews_count: int = 8500
    nps_learning_score: float = 62.0

class AdaptiveLearningPathMetric(BaseModel):
    adaptive_recommendations_count: int = 12
    path_personalization_accuracy_pct: float = 91.0

class DeterministicLearningPipelineResult(BaseModel):
    completion: CourseCompletionRateMetric
    skill_gain: LearningSkillGainMetric
    catalog: CourseCatalogAudit
    engagement: LearnerEngagementMetric
    feedback: CourseRatingFeedbackAudit
    adaptive: AdaptiveLearningPathMetric
    learning_quality_score: float
    confidence_score: float

class StrategicLearningNarrative(BaseModel):
    learning_summary: str
    key_learning_strengths: List[str]

class CurriculumOptimizationPlan(BaseModel):
    course_improvement_actions: List[str]
    sample_learning_path_schema: str

class ReasoningLearningPipelineResult(BaseModel):
    narrative: StrategicLearningNarrative
    curriculum_plan: CurriculumOptimizationPlan
    reasoning_steps: List[str]

class LearningCourseOrchestratorReport(BaseModel):
    department: str = "Learning & Course Intelligence"
    department_id: str = "dept_050"
    learning_tier: str = "HIGH IMPACT LEARNING PLATFORM"
    learning_quality_score: float
    confidence_score: float
    deterministic_analysis: DeterministicLearningPipelineResult
    reasoning_analysis: ReasoningLearningPipelineResult
    reasoning_steps: List[str]
