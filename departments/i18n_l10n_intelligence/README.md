# Department 044: Internationalization & Localization Intelligence
Locale coverage, translation completeness, RTL layout compliance, ICU date/number formatting, pseudo-localization audits, and translation BLEU quality scoring.
## 10-Agent Architecture
Deterministic(7): LocaleCoverageMeterAgent, TranslationCompletenessAuditorAgent, RTLSupportAuditorAgent, DateNumberFormatMeterAgent, PseudoLocalizationAuditorAgent, TranslationQualityMeterAgent, I18nReadinessScorerAgent
Reasoning(2): StrategicI18nNarrativeAgent, I18nExpansionPlannerAgent
Orchestrator(1): I18nL10nOrchestratorAgent
