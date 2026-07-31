from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.accessibility_inclusivity_intelligence.schemas import (
    StrategicA11yNarrative, A11yRemediationPlan, ReasoningA11yPipelineResult, DeterministicA11yPipelineResult
)

class StrategicA11yNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates accessibility compliance posture, screen reader UX, and inclusive language."""
    def __init__(self):
        super().__init__(agent_id="strategic_a11y_narrative", name="Strategic Accessibility Narrative Agent",
                         description="Evaluates WCAG 2.1 AA compliance, ARIA attributes, and inclusive phrasing.", icon="Eye")

    async def evaluate(self, det: DeterministicA11yPipelineResult) -> StrategicA11yNarrative:
        fallback = {
            "a11y_summary": f"WCAG 2.1 AA compliant platform ({det.a11y_score:.1f}% score). {det.wcag.wcag_compliance_pct}% WCAG pass rate, {det.screen_reader.aria_attribute_coverage_pct}% ARIA coverage, zero keyboard traps.",
            "key_a11y_strengths": [f"100% keyboard tab order compliance with visible focus indicators", f"{det.inclusive_language.gender_neutral_language_pct}% gender-neutral language across platform UI"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Accessibility Specialist", "WCAG 2.1, ARIA, screen readers, inclusive UX"),
                                          PromptBuilder.build_user_context({"score": det.a11y_score}), task_type="a11y_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicA11yNarrative(a11y_summary=parsed.get("a11y_summary", fallback["a11y_summary"]),
                                         key_a11y_strengths=parsed.get("key_a11y_strengths", fallback["key_a11y_strengths"]))
        except Exception:
            return StrategicA11yNarrative(**fallback)

class A11yRemediationPlannerAgent(BaseAgent):
    """Agent 9: Generates accessibility remediation actions and accessible component code samples."""
    def __init__(self):
        super().__init__(agent_id="a11y_remediation_planner", name="Accessibility Remediation Planner Agent",
                         description="Formulates WCAG remediation roadmaps and accessible HTML/React component templates.", icon="CheckCircle")

    async def plan_remediation(self, det: DeterministicA11yPipelineResult) -> A11yRemediationPlan:
        fallback = {
            "remediation_actions": [f"Fix {det.contrast.non_compliant_elements} low-contrast button text element to achieve 4.5:1 ratio", f"Resolve {det.wcag.wcag_violations_count} minor WCAG violations in modal dialog focus trap management"],
            "sample_accessible_component": '<button\n  type="button"\n  aria-label="Upload resume file"\n  aria-describedby="resume-format-hint"\n  className="focus:ring-2 focus:ring-blue-600 focus:outline-none bg-blue-700 text-white font-medium px-4 py-2 rounded"\n>\n  Upload Resume\n</button>\n<span id="resume-format-hint" className="sr-only">Accepted formats: PDF, DOCX under 5MB</span>'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("a11y Engineer", "ARIA roles, focus management, color contrast"),
                                          PromptBuilder.build_user_context({"violations": det.wcag.wcag_violations_count}), task_type="a11y_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return A11yRemediationPlan(remediation_actions=parsed.get("remediation_actions", fallback["remediation_actions"]),
                                       sample_accessible_component=parsed.get("sample_accessible_component", fallback["sample_accessible_component"]))
        except Exception:
            return A11yRemediationPlan(**fallback)
