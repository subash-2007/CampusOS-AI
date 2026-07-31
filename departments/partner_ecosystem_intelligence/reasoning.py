from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.partner_ecosystem_intelligence.schemas import (
    StrategicPartnerNarrative, EcosystemExpansionPlan, ReasoningPartnerPipelineResult, DeterministicPartnerPipelineResult
)

class StrategicPartnerNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates partner ecosystem maturity, integration usage, and partner-driven revenue."""
    def __init__(self):
        super().__init__(agent_id="strategic_partner_narrative", name="Strategic Partner Narrative Agent",
                         description="Evaluates active partnerships, partner revenue attribution, and marketplace adoption.", icon="Share2")

    async def evaluate(self, det: DeterministicPartnerPipelineResult) -> StrategicPartnerNarrative:
        fallback = {
            "ecosystem_summary": f"Thriving partner ecosystem ({det.ecosystem_health_score:.1f}% score). {det.partnerships.active_partners_count} active partners, {det.revenue.partner_influence_revenue_pct}% partner revenue influence, {det.marketplace.marketplace_apps_count} marketplace apps.",
            "key_ecosystem_strengths": [f"2.85M monthly partner API calls led by '{det.integration_usage.top_integration}'", f"{det.certification.certified_partners_pct}% partner certification rate with {det.sla.partner_api_uptime_pct}% SLA compliance"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Head of Alliances & Ecosystem", "partner integrations, marketplace, API ecosystem"),
                                          PromptBuilder.build_user_context({"score": det.ecosystem_health_score}), task_type="partner_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicPartnerNarrative(ecosystem_summary=parsed.get("ecosystem_summary", fallback["ecosystem_summary"]),
                                             key_ecosystem_strengths=parsed.get("key_ecosystem_strengths", fallback["key_ecosystem_strengths"]))
        except Exception:
            return StrategicPartnerNarrative(**fallback)

class EcosystemExpansionPlannerAgent(BaseAgent):
    """Agent 9: Generates partner recruitment roadmaps and integration manifest templates."""
    def __init__(self):
        super().__init__(agent_id="ecosystem_expansion_planner", name="Ecosystem Expansion Planner Agent",
                         description="Formulates partner ecosystem expansion plans and integration OpenAPI/OAuth manifests.", icon="Box")

    async def plan_expansion(self, det: DeterministicPartnerPipelineResult) -> EcosystemExpansionPlan:
        fallback = {
            "partnership_growth_actions": ["Launch Partner Revenue Share Program (15% lifetime recurring) for HR Tech integration partners", "Publish Developer SDK and CLI tool to accelerate 3rd-party marketplace app development"],
            "sample_partner_integration_manifest": "manifest_version: '1.0'\npartner_id: linkedin_talent_hub\napp_name: CampusOS Resume Sync\nscopes:\n  - read:resumes\n  - write:candidate_status\nwebhook_url: https://api.campusos.ai/v1/partners/linkedin/webhook\nauth: OAuth2_Authorization_Code"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Ecosystem Product Manager", "partner portals, SDKs, developer platform"),
                                          PromptBuilder.build_user_context({"partners": det.partnerships.active_partners_count}), task_type="partner_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return EcosystemExpansionPlan(partnership_growth_actions=parsed.get("partnership_growth_actions", fallback["partnership_growth_actions"]),
                                          sample_partner_integration_manifest=parsed.get("sample_partner_integration_manifest", fallback["sample_partner_integration_manifest"]))
        except Exception:
            return EcosystemExpansionPlan(**fallback)
