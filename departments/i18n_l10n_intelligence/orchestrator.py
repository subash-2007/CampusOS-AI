from app.agents.base_agent import BaseAgent
from departments.i18n_l10n_intelligence.deterministic import I18nReadinessScorerAgent
from departments.i18n_l10n_intelligence.reasoning import StrategicI18nNarrativeAgent, I18nExpansionPlannerAgent
from departments.i18n_l10n_intelligence.schemas import I18nL10nOrchestratorReport, ReasoningI18nPipelineResult

class I18nL10nOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Internationalization & Localization Intelligence Department."""
    def __init__(self):
        super().__init__(agent_id="i18n_l10n_orchestrator", name="Internationalization & Localization Intelligence Master Orchestrator",
                         description="Coordinates all 9 i18n/l10n intelligence sub-agents.", icon="Globe")
        self.scorer = I18nReadinessScorerAgent()
        self.narrative_agent = StrategicI18nNarrativeAgent()
        self.expansion_planner = I18nExpansionPlannerAgent()

    async def run_pipeline(self, locales_count: int = 32) -> I18nL10nOrchestratorReport:
        steps = ["Step 1: Running deterministic i18n pipeline (locale coverage, translation completeness, RTL support, ICU formatting, pseudo-l10n, translation quality)."]
        det = self.scorer.run(locales_count)
        steps.append("Step 2: Executing Strategic i18n Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing i18n Expansion Planner Agent.")
        expansion = await self.expansion_planner.plan_expansion(det)
        steps.append("Step 4: Compiling i18n/l10n Intelligence Master Report.")
        tier = "GLOBAL READY PLATFORM" if det.i18n_readiness_score >= 85 else "STANDARD LOCALIZATION"
        return I18nL10nOrchestratorReport(
            i18n_tier=tier, i18n_readiness_score=det.i18n_readiness_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningI18nPipelineResult(narrative=narrative, expansion_plan=expansion, reasoning_steps=steps),
            reasoning_steps=steps
        )
