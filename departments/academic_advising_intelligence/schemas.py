from typing import List
from pydantic import BaseModel

class DegreeAuditProgressMetric(BaseModel):
    on_track_graduation_pct: float = 88.5
    avg_credits_completed: float = 78.4
    total_credits_required: int = 120

class EarlyWarningRiskAudit(BaseModel):
    at_risk_students_count: int = 42
    academic_probation_risk_pct: float = 3.2
    early_warning_alerts_triggered: int = 18

class CoursePrerequisiteComplianceAudit(BaseModel):
    prerequisite_violations_count: int = 0
    override_requests_approved: int = 14

class AdvisingSessionFrequencyMetric(BaseModel):
    avg_advising_sessions_per_year: float = 2.8
    advisor_satisfaction_score: float = 91.5

class DegreePlanCustomizationMetric(BaseModel):
    custom_degree_plans_created: int = 1420
    double_major_minor_plans_pct: float = 24.0

class GPAAnalyticsMetric(BaseModel):
    avg_gpa: float = 3.42
    gpa_improvement_post_advising_pct: float = 12.4

class DeterministicAdvisingPipelineResult(BaseModel):
    degree_audit: DegreeAuditProgressMetric
    early_warning: EarlyWarningRiskAudit
    prerequisites: CoursePrerequisiteComplianceAudit
    session_frequency: AdvisingSessionFrequencyMetric
    customization: DegreePlanCustomizationMetric
    gpa_analytics: GPAAnalyticsMetric
    advising_health_score: float
    confidence_score: float

class StrategicAdvisingNarrative(BaseModel):
    advising_summary: str
    key_advising_strengths: List[str]

class AcademicRetentionPlan(BaseModel):
    retention_improvement_actions: List[str]
    sample_degree_roadmap: str

class ReasoningAdvisingPipelineResult(BaseModel):
    narrative: StrategicAdvisingNarrative
    retention_plan: AcademicRetentionPlan
    reasoning_steps: List[str]

class AcademicAdvisingOrchestratorReport(BaseModel):
    department: str = "Academic Advising Intelligence"
    department_id: str = "dept_054"
    advising_tier: str = "PROACTIVE ACADEMIC RETENTION"
    advising_health_score: float
    confidence_score: float
    deterministic_analysis: DeterministicAdvisingPipelineResult
    reasoning_analysis: ReasoningAdvisingPipelineResult
    reasoning_steps: List[str]
