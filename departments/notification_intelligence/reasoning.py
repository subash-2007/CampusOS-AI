from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.notification_intelligence.schemas import (
    StrategicNotificationNarrative, NotificationOptimizationPlan, ReasoningNotificationPipelineResult, DeterministicNotificationPipelineResult
)

class StrategicNotificationNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates notification strategy effectiveness, fatigue risk, and personalization depth."""
    def __init__(self):
        super().__init__(agent_id="strategic_notification_narrative", name="Strategic Notification Narrative Agent",
                         description="Evaluates email, push, SMS performance and notification personalization.", icon="Bell")

    async def evaluate(self, det: DeterministicNotificationPipelineResult) -> StrategicNotificationNarrative:
        fallback = {
            "notification_strategy_summary": f"High-engagement notification platform ({det.notification_effectiveness_score:.1f}% score). {det.email.open_rate_pct}% email open rate, {det.push.push_delivery_rate_pct}% push delivery, {det.personalization.personalized_notification_pct}% personalized.",
            "key_notification_strengths": [f"{det.push.push_opt_in_rate_pct}% push opt-in rate with {det.push.push_delivery_rate_pct}% delivery", f"Low {det.frequency.notification_fatigue_reported_pct}% fatigue rate with {det.frequency.avg_notifications_per_user_per_day} daily avg"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Growth Marketing Lead", "email marketing, push notifications, SMS"),
                                          PromptBuilder.build_user_context({"open_rate": det.email.open_rate_pct}), task_type="notification_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicNotificationNarrative(notification_strategy_summary=parsed.get("notification_strategy_summary", fallback["notification_strategy_summary"]),
                                                   key_notification_strengths=parsed.get("key_notification_strengths", fallback["key_notification_strengths"]))
        except Exception:
            return StrategicNotificationNarrative(**fallback)

class NotificationOptimizationPlannerAgent(BaseAgent):
    """Agent 9: Generates engagement improvement actions and notification template samples."""
    def __init__(self):
        super().__init__(agent_id="notification_optimization_planner", name="Notification Optimization Planner Agent",
                         description="Formulates notification timing, frequency, and personalization improvements.", icon="Sliders")

    async def plan_optimization(self, det: DeterministicNotificationPipelineResult) -> NotificationOptimizationPlan:
        fallback = {
            "engagement_improvement_actions": ["Implement send-time optimization (STO) using individual user activity windows", "Add emoji subject lines A/B test for 5% open rate lift"],
            "sample_notification_template": "Subject: 🎯 3 new {role} jobs match your profile!\nPreview: {company} is hiring — your match score: {match_score}%\nBody: Hi {first_name}, based on your {skill} skills and {experience} years experience, we found {job_count} new matches this week."
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("CRM Manager", "email templates, push optimization, personalization"),
                                          PromptBuilder.build_user_context({"personalization_pct": det.personalization.personalized_notification_pct}), task_type="notification_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return NotificationOptimizationPlan(engagement_improvement_actions=parsed.get("engagement_improvement_actions", fallback["engagement_improvement_actions"]),
                                                 sample_notification_template=parsed.get("sample_notification_template", fallback["sample_notification_template"]))
        except Exception:
            return NotificationOptimizationPlan(**fallback)
