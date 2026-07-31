from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.greek_life_student_orgs.schemas import (
    StrategicGreekLifeNarrative, StudentOrgManagementPlan, ReasoningGreekLifePipelineResult, DeterministicGreekLifePipelineResult
)

class StrategicGreekLifeNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates fraternity/sorority chapter safety, anti-hazing compliance, and student organization philanthropy impact."""
    def __init__(self):
        super().__init__(agent_id="strategic_greek_life_narrative", name="Strategic Greek Life Narrative Agent",
                         description="Evaluates Greek Life chapter GPA, anti-hazing education compliance, annual philanthropy fundraising, and event risk management.", icon="Shield")

    async def evaluate(self, det: DeterministicGreekLifePipelineResult) -> StrategicGreekLifeNarrative:
        fallback = {
            "org_summary": f"Exemplary campus life involvement ({det.org_health_score:.1f}% score). Supporting {det.registration.registered_student_orgs_count} registered student organizations and {det.greek_compliance.greek_chapters_active} Greek chapters ({det.registration.active_org_members_total:,} members), {det.greek_compliance.hazing_prevention_training_compliance_pct}% anti-hazing training compliance.",
            "key_org_strengths": [f"${det.philanthropy.philanthropy_funds_raised_usd:,.0f} in charitable philanthropy raised and {det.philanthropy.community_service_hours_logged:,} community service hours logged", f"{det.greek_compliance.greek_chapter_avg_gpa:.2f} average Greek chapter GPA (exceeding all-undergraduate average)"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Director of Fraternity & Sorority Life and Student Involvement", "Greek Life compliance, anti-hazing policies, student organization risk management, philanthropy"),
                                          PromptBuilder.build_user_context({"score": det.org_health_score}), task_type="greek_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicGreekLifeNarrative(org_summary=parsed.get("org_summary", fallback["org_summary"]),
                                              key_org_strengths=parsed.get("key_org_strengths", fallback["key_org_strengths"]))
        except Exception:
            return StrategicGreekLifeNarrative(**fallback)

class StudentOrgManagementPlannerAgent(BaseAgent):
    """Agent 9: Generates digital event risk registration portals and anti-hazing compliance verification roadmaps."""
    def __init__(self):
        super().__init__(agent_id="student_org_management_planner", name="Student Org Management Planner Agent",
                         description="Formulates student organization leadership transition toolkits, digital budget auditing platforms, and risk management guidelines.", icon="UserCheck")

    async def plan_management(self, det: DeterministicGreekLifePipelineResult) -> StudentOrgManagementPlan:
        fallback = {
            "management_actions": ["Deploy Smart Event Risk Assessment Matrix required for all student org events with > 100 attendees", "Launch Annual Greek Excellence Accreditation Standards Dashboard"],
            "sample_hazing_compliance_declaration": "ANNUAL ANTI-HAZING POLICY COMPLIANCE DECLARATION\nOrganization: Alpha Beta Gamma Fraternity\nChapter Officers Verified: President, Vice President, New Member Educator, Advisor\nPolicy Affirmation:\n  1. 100% of new members completed University Anti-Hazing Training Workshop\n  2. Zero tolerance for alcohol/drug usage during new member onboarding\n  3. Mandatory adherence to Timothy J. Piazza Anti-Hazing Law standards\nStatus: FULLY COMPLIANT & APPROVED FOR FALL RECRUITMENT"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Campus Student Organization Operations Manager", "anti-hazing policy, event risk registration, Greek accreditation"),
                                          PromptBuilder.build_user_context({"orgs": det.registration.registered_student_orgs_count}), task_type="greek_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StudentOrgManagementPlan(management_actions=parsed.get("management_actions", fallback["management_actions"]),
                                            sample_hazing_compliance_declaration=parsed.get("sample_hazing_compliance_declaration", fallback["sample_hazing_compliance_declaration"]))
        except Exception:
            return StudentOrgManagementPlan(**fallback)
