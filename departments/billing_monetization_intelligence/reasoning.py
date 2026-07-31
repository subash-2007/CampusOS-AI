from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.billing_monetization_intelligence.schemas import (
    StrategicBillingNarrative, MonetizationOptimizationPlan, ReasoningBillingPipelineResult, DeterministicBillingPipelineResult
)

class StrategicBillingNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates SaaS monetization health, unit economics, and churn dynamics."""
    def __init__(self):
        super().__init__(agent_id="strategic_billing_narrative", name="Strategic Billing Narrative Agent",
                         description="Evaluates MRR/ARR, NRR, LTV/CAC, and dunning performance.", icon="DollarSign")

    async def evaluate(self, det: DeterministicBillingPipelineResult) -> StrategicBillingNarrative:
        fallback = {
            "billing_summary": f"High growth monetization platform (${det.arr.mrr_usd:,.0f} MRR / ${det.arr.arr_usd:,.0f} ARR). NRR={det.churn.net_revenue_retention_pct}%, LTV/CAC={det.ltv.ltv_to_cac_ratio:.1f}x, {det.churn.user_churn_rate_pct}% user churn.",
            "key_billing_strengths": [f"LTV/CAC ratio of {det.ltv.ltv_to_cac_ratio:.1f}x (${det.ltv.ltv_usd} LTV vs ${det.ltv.cac_usd} CAC)", f"Dunning automation recovering {det.payment_gateway.failed_payment_recovery_pct}% of failed payments"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Chief Revenue Officer", "SaaS metrics, ARR, NRR, LTV, pricing strategy"),
                                          PromptBuilder.build_user_context({"score": det.billing_health_score}), task_type="billing_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicBillingNarrative(billing_summary=parsed.get("billing_summary", fallback["billing_summary"]),
                                             key_billing_strengths=parsed.get("key_billing_strengths", fallback["key_billing_strengths"]))
        except Exception:
            return StrategicBillingNarrative(**fallback)

class MonetizationOptimizationPlannerAgent(BaseAgent):
    """Agent 9: Generates pricing strategy improvements and Stripe webhook integration code samples."""
    def __init__(self):
        super().__init__(agent_id="monetization_optimization_planner", name="Monetization Optimization Planner Agent",
                         description="Formulates SaaS pricing tier strategies and Stripe integration handlers.", icon="TrendingUp")

    async def plan_monetization(self, det: DeterministicBillingPipelineResult) -> MonetizationOptimizationPlan:
        fallback = {
            "pricing_improvement_actions": ["Introduce Annual Billing discount (20% off) to increase upfront cash flow and lower churn", "Add Enterprise custom tier with SSO and dedicated SLA support"],
            "sample_stripe_webhook_handler": 'import stripe\nfrom fastapi import APIRouter, Request, HTTPException\n\nrouter = APIRouter()\n\n@router.post("/webhooks/stripe")\nasync def stripe_webhook(request: Request):\n    payload = await request.body()\n    sig_header = request.headers.get("stripe-signature")\n    try:\n        event = stripe.Webhook.construct_event(payload, sig_header, STRIPE_WEBHOOK_SECRET)\n        if event["type"] == "invoice.payment_succeeded":\n            handle_payment_success(event["data"]["object"])\n        elif event["type"] == "invoice.payment_failed":\n            trigger_dunning_flow(event["data"]["object"])\n        return {"status": "success"}\n    except Exception as e:\n        raise HTTPException(status_code=400, detail=str(e))'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Monetization Product Manager", "Stripe API, subscription tiers, dunning"),
                                          PromptBuilder.build_user_context({"arr": det.arr.arr_usd}), task_type="billing_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return MonetizationOptimizationPlan(pricing_improvement_actions=parsed.get("pricing_improvement_actions", fallback["pricing_improvement_actions"]),
                                                sample_stripe_webhook_handler=parsed.get("sample_stripe_webhook_handler", fallback["sample_stripe_webhook_handler"]))
        except Exception:
            return MonetizationOptimizationPlan(**fallback)
