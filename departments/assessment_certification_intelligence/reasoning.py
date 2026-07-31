from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.assessment_certification_intelligence.schemas import (
    StrategicAssessmentNarrative, CertificationExpansionPlan, ReasoningAssessmentPipelineResult, DeterministicAssessmentPipelineResult
)

class StrategicAssessmentNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates certification engine reliability, proctoring security, and badge adoption."""
    def __init__(self):
        super().__init__(agent_id="strategic_assessment_narrative", name="Strategic Assessment Narrative Agent",
                         description="Evaluates certification validity, proctoring integrity, IRT calibration, and badge sharing.", icon="Award")

    async def evaluate(self, det: DeterministicAssessmentPipelineResult) -> StrategicAssessmentNarrative:
        fallback = {
            "assessment_summary": f"Enterprise certification engine ({det.assessment_health_score:.1f}% score). {det.validity.validity_pct:.1f}% validity, {det.proctoring.ai_proctoring_integrity_score}% proctoring integrity, {det.verification.blockchain_verified_certs_pct}% blockchain verified.",
            "key_assessment_strengths": [f"IRT calibrated assessments with {det.difficulty.cronbach_alpha_reliability} Cronbach's alpha reliability", f"{det.issuance.digital_badges_issued} digital badges issued with {det.issuance.linkedin_share_rate_pct}% LinkedIn share rate"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Head of Psychometrics & Certification", "IRT, proctoring, digital badges, skill taxonomy"),
                                          PromptBuilder.build_user_context({"score": det.assessment_health_score}), task_type="assessment_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicAssessmentNarrative(assessment_summary=parsed.get("assessment_summary", fallback["assessment_summary"]),
                                                key_assessment_strengths=parsed.get("key_assessment_strengths", fallback["key_assessment_strengths"]))
        except Exception:
            return StrategicAssessmentNarrative(**fallback)

class CertificationExpansionPlannerAgent(BaseAgent):
    """Agent 9: Generates certification program expansion plans and Open Badges v3 JSON schemas."""
    def __init__(self):
        super().__init__(agent_id="certification_expansion_planner", name="Certification Expansion Planner Agent",
                         description="Formulates digital credentialing roadmaps and Open Badges v3 JSON-LD specs.", icon="CheckCircle")

    async def plan_expansion(self, det: DeterministicAssessmentPipelineResult) -> CertificationExpansionPlan:
        fallback = {
            "certification_roadmap_actions": [f"Transition remaining {100 - det.verification.blockchain_verified_certs_pct:.0f}% certs to W3C Verifiable Credentials standard", "Implement adaptive cat-testing algorithm to reduce assessment duration by 40%"],
            "sample_certificate_schema": '{\n  "@context": "https://w3id.org/openbadges/v3",\n  "type": "OpenBadgeCredential",\n  "name": "Certified AI Systems Architect",\n  "issuer": "CampusOS AI Certification Board",\n  "criteria": "Passed 3-hour proctored practical exam on multi-agent architectures",\n  "recipient": "did:example:user123"\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Credentialing Standards Architect", "Open Badges v3, Verifiable Credentials, W3C"),
                                          PromptBuilder.build_user_context({"certs": det.validity.total_certifications_tracked}), task_type="assessment_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return CertificationExpansionPlan(certification_roadmap_actions=parsed.get("certification_roadmap_actions", fallback["certification_roadmap_actions"]),
                                              sample_certificate_schema=parsed.get("sample_certificate_schema", fallback["sample_certificate_schema"]))
        except Exception:
            return CertificationExpansionPlan(**fallback)
