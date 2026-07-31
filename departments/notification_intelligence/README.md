# Department 040: Notification Intelligence (`notification_intelligence`)
Email open/CTR/unsubscribe metrics, push delivery and click rates, send-time optimization, notification fatigue detection, SMS delivery, and personalization depth analysis.
## 10-Agent Architecture
Deterministic(7): EmailNotificationMeterAgent, PushNotificationMeterAgent, NotificationTimingAuditorAgent, NotificationFrequencyAuditorAgent, SMSNotificationMeterAgent, NotificationPersonalizationAuditorAgent, NotificationEffectivenessScorerAgent
Reasoning(2): StrategicNotificationNarrativeAgent, NotificationOptimizationPlannerAgent
Orchestrator(1): NotificationIntelligenceOrchestratorAgent
