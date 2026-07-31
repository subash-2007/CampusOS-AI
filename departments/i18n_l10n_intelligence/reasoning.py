from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.i18n_l10n_intelligence.schemas import (
    StrategicI18nNarrative, I18nExpansionPlan, ReasoningI18nPipelineResult, DeterministicI18nPipelineResult
)

class StrategicI18nNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates internationalization readiness, RTL support, and localization quality."""
    def __init__(self):
        super().__init__(agent_id="strategic_i18n_narrative", name="Strategic i18n Narrative Agent",
                         description="Evaluates locale coverage, translation completeness, and ICU formatting.", icon="Globe")

    async def evaluate(self, det: DeterministicI18nPipelineResult) -> StrategicI18nNarrative:
        fallback = {
            "i18n_summary": f"Global ready platform ({det.i18n_readiness_score:.1f}% readiness). {det.locale_coverage.supported_locales_count} locales supported, {det.translation.translation_completion_pct}% completion, {det.locale_coverage.rtl_locales_supported} RTL locales.",
            "key_i18n_strengths": [f"ICU compliant formatting with {det.rtl.rtl_layout_compliance_pct}% RTL compliance", f"{det.quality.human_verified_locales_pct}% human-verified locales with {det.quality.bleu_score_avg} BLEU score"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Localization Architect", "i18n, l10n, RTL, ICU formatting"),
                                          PromptBuilder.build_user_context({"score": det.i18n_readiness_score}), task_type="i18n_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicI18nNarrative(i18n_summary=parsed.get("i18n_summary", fallback["i18n_summary"]),
                                         key_i18n_strengths=parsed.get("key_i18n_strengths", fallback["key_i18n_strengths"]))
        except Exception:
            return StrategicI18nNarrative(**fallback)

class I18nExpansionPlannerAgent(BaseAgent):
    """Agent 9: Generates localization expansion actions and sample translation JSON schemas."""
    def __init__(self):
        super().__init__(agent_id="i18n_expansion_planner", name="i18n Expansion Planner Agent",
                         description="Formulates international market expansion plans and translation JSON templates.", icon="Languages")

    async def plan_expansion(self, det: DeterministicI18nPipelineResult) -> I18nExpansionPlan:
        fallback = {
            "localization_actions": [f"Extract {det.pseudo_l10n.hardcoded_strings_count} remaining hardcoded strings to i18n translation files", "Add automated pseudo-localization test step in CI pipeline"],
            "sample_i18n_json": '{\n  "app": {\n    "title": "CampusOS AI",\n    "welcome": "Welcome back, {name}!",\n    "resume": {\n      "upload": "Upload Resume",\n      "score": "Match Score: {score, number, percent}"\n    }\n  }\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Globalization Manager", "i18next, react-intl, translation management"),
                                          PromptBuilder.build_user_context({"locales": det.locale_coverage.supported_locales_count}), task_type="i18n_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return I18nExpansionPlan(localization_actions=parsed.get("localization_actions", fallback["localization_actions"]),
                                     sample_i18n_json=parsed.get("sample_i18n_json", fallback["sample_i18n_json"]))
        except Exception:
            return I18nExpansionPlan(**fallback)
