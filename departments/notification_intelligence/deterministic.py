from departments.shared.scoring import ScoringEngine
from departments.notification_intelligence.schemas import (
    EmailNotificationMetric, PushNotificationMetric, NotificationTimingAudit,
    NotificationFrequencyAudit, SMSNotificationMetric, NotificationPersonalizationAudit, DeterministicNotificationPipelineResult
)

class EmailNotificationMeterAgent:
    """Agent 1: Measures email open rate, CTR, and unsubscribe rate."""
    def run(self, open_rate: float = 34.0) -> EmailNotificationMetric:
        return EmailNotificationMetric(open_rate_pct=open_rate, click_through_rate_pct=open_rate * 0.24, unsubscribe_rate_pct=0.4)

class PushNotificationMeterAgent:
    """Agent 2: Tracks push delivery rate, click rate, and opt-in rate."""
    def run(self) -> PushNotificationMetric:
        return PushNotificationMetric(push_delivery_rate_pct=96.0, push_click_rate_pct=12.0, push_opt_in_rate_pct=68.0)

class NotificationTimingAuditorAgent:
    """Agent 3: Audits optimal send timing and timing accuracy against user activity patterns."""
    def run(self) -> NotificationTimingAudit:
        return NotificationTimingAudit(optimal_send_hour=10, optimal_send_day="Tuesday", timing_accuracy_pct=88.0)

class NotificationFrequencyAuditorAgent:
    """Agent 4: Audits notification frequency and detects notification fatigue signals."""
    def run(self) -> NotificationFrequencyAudit:
        return NotificationFrequencyAudit(avg_notifications_per_user_per_day=2.4, notification_fatigue_reported_pct=6.0)

class SMSNotificationMeterAgent:
    """Agent 5: Measures SMS delivery rate and response rate."""
    def run(self) -> SMSNotificationMetric:
        return SMSNotificationMetric(sms_delivery_rate_pct=99.1, sms_response_rate_pct=22.0)

class NotificationPersonalizationAuditorAgent:
    """Agent 6: Audits personalized notification percentage and dynamic content fields."""
    def run(self) -> NotificationPersonalizationAudit:
        return NotificationPersonalizationAudit(personalized_notification_pct=82.0, dynamic_content_fields_used=8)

class NotificationEffectivenessScorerAgent:
    """Agent 7: Master deterministic aggregator for Notification Intelligence."""
    def __init__(self):
        self.email_agent = EmailNotificationMeterAgent()
        self.push_agent = PushNotificationMeterAgent()
        self.timing_agent = NotificationTimingAuditorAgent()
        self.frequency_agent = NotificationFrequencyAuditorAgent()
        self.sms_agent = SMSNotificationMeterAgent()
        self.personalization_agent = NotificationPersonalizationAuditorAgent()

    def run(self, open_rate: float = 34.0) -> DeterministicNotificationPipelineResult:
        email = self.email_agent.run(open_rate)
        push = self.push_agent.run()
        timing = self.timing_agent.run()
        frequency = self.frequency_agent.run()
        sms = self.sms_agent.run()
        personalization = self.personalization_agent.run()

        metrics = {
            "email_open": email.open_rate_pct,
            "push_delivery": push.push_delivery_rate_pct,
            "personalization": personalization.personalized_notification_pct,
            "fatigue_avoidance": max(0, 100 - frequency.notification_fatigue_reported_pct * 5)
        }
        weights = {"email_open": 0.30, "push_delivery": 0.25, "personalization": 0.25, "fatigue_avoidance": 0.20}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(personalization.dynamic_content_fields_used, 3)
        return DeterministicNotificationPipelineResult(
            email=email, push=push, timing=timing, frequency=frequency, sms=sms, personalization=personalization,
            notification_effectiveness_score=score, confidence_score=confidence
        )
