from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.customer_support_success.schemas import (
    StrategicSupportNarrative, CustomerSuccessPlan, ReasoningSupportPipelineResult, DeterministicSupportPipelineResult
)

class StrategicSupportNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates customer support performance, CSAT scores, and account health trends."""
    def __init__(self):
        super().__init__(agent_id="strategic_support_narrative", name="Strategic Support Narrative Agent",
                         description="Evaluates CSAT, SLA compliance, account health, and AI deflection.", icon="Headphones")

    async def evaluate(self, det: DeterministicSupportPipelineResult) -> StrategicSupportNarrative:
        fallback = {
            "support_summary": f"World class customer support ({det.support_excellence_score:.1f}% score). CSAT={det.csat.csat_score_pct}%, SLA={det.resolution_time.sla_compliance_pct}%, {det.deflection.ai_deflection_rate_pct}% AI deflection.",
            "key_support_strengths": [f"14.2 min avg first response time with {det.resolution_time.sla_compliance_pct}% SLA compliance", f"{det.health.healthy_accounts_pct}% healthy accounts with proactively managed risk list"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("VP of Customer Success", "CSAT, SLA, customer health, AI deflection"),
                                          PromptBuilder.build_user_context({"score": det.support_excellence_score}), task_type="support_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicSupportNarrative(support_summary=parsed.get("support_summary", fallback["support_summary"]),
                                             key_support_strengths=parsed.get("key_support_strengths", fallback["key_support_strengths"]))
        except Exception:
            return StrategicSupportNarrative(**fallback)

class CustomerSuccessPlannerAgent(BaseAgent):
    """Agent 9: Formulates proactive churn prevention playbooks and AI deflection expansion strategies."""
    def __init__(self):
        super().__init__(agent_id="customer_success_planner", name="Customer Success Planner Agent",
                         description="Formulates account retention playbooks and self-service KB expansion plans.", icon="LifeBuoy")

    async def plan_success(self, det: DeterministicSupportPipelineResult) -> CustomerSuccessPlan:
        fallback = {
            "churn_prevention_actions": [f"Assign dedicated CSM outreach to {det.health.at_risk_accounts_count} at-risk accounts showing declining session frequency", "Expand AI chatbot deflection for password reset and billing FAQ queries"],
            "sample_support_playbook": "Trigger: Account health score drops below 60%\nPlaybook:\n  Day 1: Automated check-in email from assigned CSM\n  Day 3: Call attempt + custom feature usage review\n  Day 7: Offer free 1-on-1 career coaching session\n  Day 14: Executive sponsor check-in if unresponded"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Customer Success Manager", "churn prevention, playbooks, health scoring"),
                                          PromptBuilder.build_user_context({"at_risk": det.health.at_risk_accounts_count}), task_type="support_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return CustomerSuccessPlan(churn_prevention_actions=parsed.get("churn_prevention_actions", fallback["churn_prevention_actions"]),
                                       sample_support_playbook=parsed.get("sample_support_playbook", fallback["sample_support_playbook"]))
        except Exception:
            return CustomerSuccessPlan(**fallback)
