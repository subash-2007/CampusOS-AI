from typing import List
from pydantic import BaseModel

class LocaleCoverageMetric(BaseModel):
    supported_locales_count: int = 32
    primary_locales_coverage_pct: float = 98.0
    rtl_locales_supported: int = 4

class TranslationCompletenessAudit(BaseModel):
    missing_keys_count: int = 0
    translation_completion_pct: float = 99.4
    untranslated_string_tokens: int = 12

class RTLSupportAudit(BaseModel):
    rtl_layout_compliance_pct: float = 96.0
    bidi_rendering_errors: int = 0

class DateNumberFormatMetric(BaseModel):
    icu_formatting_compliant: bool = True
    timezone_aware_formatting: bool = True

class PseudoLocalizationAudit(BaseModel):
    hardcoded_strings_count: int = 2
    text_expansion_clipping_risks: int = 1

class TranslationQualityMetric(BaseModel):
    human_verified_locales_pct: float = 75.0
    bleu_score_avg: float = 0.88

class DeterministicI18nPipelineResult(BaseModel):
    locale_coverage: LocaleCoverageMetric
    translation: TranslationCompletenessAudit
    rtl: RTLSupportAudit
    formatting: DateNumberFormatMetric
    pseudo_l10n: PseudoLocalizationAudit
    quality: TranslationQualityMetric
    i18n_readiness_score: float
    confidence_score: float

class StrategicI18nNarrative(BaseModel):
    i18n_summary: str
    key_i18n_strengths: List[str]

class I18nExpansionPlan(BaseModel):
    localization_actions: List[str]
    sample_i18n_json: str

class ReasoningI18nPipelineResult(BaseModel):
    narrative: StrategicI18nNarrative
    expansion_plan: I18nExpansionPlan
    reasoning_steps: List[str]

class I18nL10nOrchestratorReport(BaseModel):
    department: str = "Internationalization & Localization Intelligence"
    department_id: str = "dept_044"
    i18n_tier: str = "GLOBAL READY PLATFORM"
    i18n_readiness_score: float
    confidence_score: float
    deterministic_analysis: DeterministicI18nPipelineResult
    reasoning_analysis: ReasoningI18nPipelineResult
    reasoning_steps: List[str]
