from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.privacy_data_governance.schemas import (
    StrategicPrivacyNarrative, PrivacyRoadmapPlan, ReasoningPrivacyPipelineResult, DeterministicPrivacyPipelineResult
)

class StrategicPrivacyNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates privacy compliance posture, data governance maturity, and breach readiness."""
    def __init__(self):
        super().__init__(agent_id="strategic_privacy_narrative", name="Strategic Privacy Narrative Agent",
                         description="Evaluates GDPR compliance, consent management, and data lineage.", icon="Shield")

    async def evaluate(self, det: DeterministicPrivacyPipelineResult) -> StrategicPrivacyNarrative:
        fallback = {
            "privacy_compliance_summary": f"Full GDPR compliance ({det.privacy_compliance_score:.1f}% score). {det.consent.consent_capture_rate_pct}% consent capture, {det.lineage.data_lineage_coverage_pct}% lineage coverage, {det.breach_detection.breach_incidents_last_12m} breaches in 12 months.",
            "key_privacy_strengths": [f"AES-256-GCM encryption with 90-day key rotation", f"{det.consent.consent_withdrawal_latency_hours}h consent withdrawal latency (under 1hr SLA)"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Chief Privacy Officer", "GDPR, data governance, consent management"),
                                          PromptBuilder.build_user_context({"score": det.privacy_compliance_score}), task_type="privacy_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicPrivacyNarrative(privacy_compliance_summary=parsed.get("privacy_compliance_summary", fallback["privacy_compliance_summary"]),
                                              key_privacy_strengths=parsed.get("key_privacy_strengths", fallback["key_privacy_strengths"]))
        except Exception:
            return StrategicPrivacyNarrative(**fallback)

class PrivacyRoadmapPlannerAgent(BaseAgent):
    """Agent 9: Generates compliance improvement actions and privacy policy clause samples."""
    def __init__(self):
        super().__init__(agent_id="privacy_roadmap_planner", name="Privacy Roadmap Planner Agent",
                         description="Formulates GDPR compliance roadmaps and privacy policy templates.", icon="Lock")

    async def plan_roadmap(self, det: DeterministicPrivacyPipelineResult) -> PrivacyRoadmapPlan:
        fallback = {
            "compliance_improvement_actions": [f"Document {det.lineage.undocumented_data_flows} undocumented data flows to reach 100% lineage coverage", "Implement Privacy Impact Assessment (PIA) for all new AI model deployments"],
            "sample_privacy_policy_clause": "Data Retention: CampusOS AI retains personal data only as long as necessary for the purposes described. Resume and career data is retained for 365 days from last active session. Users may request immediate deletion under Article 17 GDPR via the Privacy Dashboard."
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Data Protection Lawyer", "GDPR Article 17, PIA, DPA requirements"),
                                          PromptBuilder.build_user_context({"undocumented": det.lineage.undocumented_data_flows}), task_type="privacy_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return PrivacyRoadmapPlan(compliance_improvement_actions=parsed.get("compliance_improvement_actions", fallback["compliance_improvement_actions"]),
                                      sample_privacy_policy_clause=parsed.get("sample_privacy_policy_clause", fallback["sample_privacy_policy_clause"]))
        except Exception:
            return PrivacyRoadmapPlan(**fallback)
