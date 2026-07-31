import pytest, asyncio
from departments.learning_course_intelligence.deterministic import (
    CourseCompletionRateMeterAgent, LearningSkillGainMeterAgent, CourseCatalogAuditorAgent,
    LearnerEngagementMeterAgent, CourseRatingFeedbackAuditorAgent, AdaptiveLearningPathMeterAgent, LearningCourseScorerAgent
)
from departments.learning_course_intelligence.orchestrator import LearningCourseOrchestratorAgent

def test_course_completion_rate_meter():
    res = CourseCompletionRateMeterAgent().run(72.4)
    assert res.course_completion_rate_pct >= 50.0
    assert res.certificates_issued_count > 100

def test_learning_skill_gain_meter():
    res = LearningSkillGainMeterAgent().run()
    assert res.pre_post_assessment_gain_pct > 0.0
    assert res.assessment_pass_rate_pct >= 80.0

def test_course_catalog_auditor():
    res = CourseCatalogAuditorAgent().run()
    assert res.total_courses_count >= 10
    assert res.interactive_labs_count >= 50

def test_learner_engagement_meter():
    res = LearnerEngagementMeterAgent().run()
    assert res.active_learners_count > 1000

def test_course_rating_feedback_auditor():
    res = CourseRatingFeedbackAuditorAgent().run()
    assert res.avg_course_rating >= 4.0

def test_adaptive_learning_path_meter():
    res = AdaptiveLearningPathMeterAgent().run()
    assert res.path_personalization_accuracy_pct >= 85.0

def test_learning_course_scorer():
    res = LearningCourseScorerAgent().run(72.4)
    assert res.learning_quality_score >= 80.0
    assert res.confidence_score >= 0.5

def test_learning_course_orchestrator():
    report = asyncio.run(LearningCourseOrchestratorAgent().run_pipeline(72.4))
    assert report.department == "Learning & Course Intelligence"
    assert report.department_id == "dept_050"
    assert report.learning_tier == "HIGH IMPACT LEARNING PLATFORM"
    assert len(report.reasoning_steps) == 4
