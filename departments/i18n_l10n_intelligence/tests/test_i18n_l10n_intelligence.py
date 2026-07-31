import pytest, asyncio
from departments.i18n_l10n_intelligence.deterministic import (
    LocaleCoverageMeterAgent, TranslationCompletenessAuditorAgent, RTLSupportAuditorAgent,
    DateNumberFormatMeterAgent, PseudoLocalizationAuditorAgent, TranslationQualityMeterAgent, I18nReadinessScorerAgent
)
from departments.i18n_l10n_intelligence.orchestrator import I18nL10nOrchestratorAgent

def test_locale_coverage_meter():
    res = LocaleCoverageMeterAgent().run(32)
    assert res.supported_locales_count >= 10
    assert res.rtl_locales_supported >= 1

def test_translation_completeness_auditor():
    res = TranslationCompletenessAuditorAgent().run()
    assert res.translation_completion_pct >= 95.0

def test_rtl_support_auditor():
    res = RTLSupportAuditorAgent().run()
    assert res.rtl_layout_compliance_pct >= 90.0

def test_date_number_format_meter():
    res = DateNumberFormatMeterAgent().run()
    assert res.icu_formatting_compliant is True

def test_pseudo_localization_auditor():
    res = PseudoLocalizationAuditorAgent().run()
    assert res.hardcoded_strings_count < 10

def test_translation_quality_meter():
    res = TranslationQualityMeterAgent().run()
    assert res.bleu_score_avg >= 0.70

def test_i18n_readiness_scorer():
    res = I18nReadinessScorerAgent().run(32)
    assert res.i18n_readiness_score >= 80.0
    assert res.confidence_score >= 0.5

def test_i18n_l10n_orchestrator():
    report = asyncio.run(I18nL10nOrchestratorAgent().run_pipeline(32))
    assert report.department == "Internationalization & Localization Intelligence"
    assert report.department_id == "dept_044"
    assert report.i18n_tier == "GLOBAL READY PLATFORM"
    assert len(report.reasoning_steps) == 4
