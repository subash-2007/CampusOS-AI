from typing import List
from pydantic import BaseModel

class EmailNotificationMetric(BaseModel):
    open_rate_pct: float = 34.0
    click_through_rate_pct: float = 8.2
    unsubscribe_rate_pct: float = 0.4

class PushNotificationMetric(BaseModel):
    push_delivery_rate_pct: float = 96.0
    push_click_rate_pct: float = 12.0
    push_opt_in_rate_pct: float = 68.0

class NotificationTimingAudit(BaseModel):
    optimal_send_hour: int = 10
    optimal_send_day: str = "Tuesday"
    timing_accuracy_pct: float = 88.0

class NotificationFrequencyAudit(BaseModel):
    avg_notifications_per_user_per_day: float = 2.4
    notification_fatigue_reported_pct: float = 6.0

class SMSNotificationMetric(BaseModel):
    sms_delivery_rate_pct: float = 99.1
    sms_response_rate_pct: float = 22.0

class NotificationPersonalizationAudit(BaseModel):
    personalized_notification_pct: float = 82.0
    dynamic_content_fields_used: int = 8

class DeterministicNotificationPipelineResult(BaseModel):
    email: EmailNotificationMetric
    push: PushNotificationMetric
    timing: NotificationTimingAudit
    frequency: NotificationFrequencyAudit
    sms: SMSNotificationMetric
    personalization: NotificationPersonalizationAudit
    notification_effectiveness_score: float
    confidence_score: float

class StrategicNotificationNarrative(BaseModel):
    notification_strategy_summary: str
    key_notification_strengths: List[str]

class NotificationOptimizationPlan(BaseModel):
    engagement_improvement_actions: List[str]
    sample_notification_template: str

class ReasoningNotificationPipelineResult(BaseModel):
    narrative: StrategicNotificationNarrative
    optimization_plan: NotificationOptimizationPlan
    reasoning_steps: List[str]

class NotificationIntelligenceOrchestratorReport(BaseModel):
    department: str = "Notification Intelligence"
    department_id: str = "dept_040"
    notification_tier: str = "HIGH ENGAGEMENT NOTIFICATIONS"
    notification_effectiveness_score: float
    confidence_score: float
    deterministic_analysis: DeterministicNotificationPipelineResult
    reasoning_analysis: ReasoningNotificationPipelineResult
    reasoning_steps: List[str]
