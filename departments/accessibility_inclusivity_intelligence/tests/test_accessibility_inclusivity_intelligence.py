import pytest, asyncio
from departments.accessibility_inclusivity_intelligence.deterministic import (
    WCAGComplianceAuditorAgent, ScreenReaderAuditorAgent, ColorContrastAuditorAgent,
    KeyboardNavigationAuditorAgent, InclusiveLanguageAuditorAgent, CognitiveAccessibilityMeterAgent, AccessibilityScorerAgent
)
from departments.accessibility_inclusivity_intelligence.orchestrator import AccessibilityInclusivityOrchestratorAgent

def test_wcag_compliance_auditor():
    res = WCAGComplianceAuditorAgent().run(96.5)
    assert res.wcag_level == "AA"
    assert res.wcag_compliance_pct >= 90.0

def test_screen_reader_auditor():
    res = ScreenReaderAuditorAgent().run()
    assert res.aria_attribute_coverage_pct >= 95.0

def test_color_contrast_auditor():
    res = ColorContrastAuditorAgent().run()
    assert res.min_contrast_ratio >= 4.5

def test_keyboard_navigation_auditor():
    res = KeyboardNavigationAuditorAgent().run()
    assert res.keyboard_traps_count == 0
    assert res.focus_indicator_visible is True

def test_inclusive_language_auditor():
    res = InclusiveLanguageAuditorAgent().run()
    assert res.gender_neutral_language_pct >= 95.0

def test_cognitive_accessibility_meter():
    res = CognitiveAccessibilityMeterAgent().run()
    assert res.readability_level_ok is True

def test_accessibility_scorer():
    res = AccessibilityScorerAgent().run(96.5)
    assert res.a11y_score >= 90.0
    assert res.confidence_score >= 0.5

def test_accessibility_inclusivity_orchestrator():
    report = asyncio.run(AccessibilityInclusivityOrchestratorAgent().run_pipeline(96.5))
    assert report.department == "Accessibility & Inclusivity Intelligence"
    assert report.department_id == "dept_045"
    assert report.a11y_tier == "WCAG 2.1 AA COMPLIANT"
    assert len(report.reasoning_steps) == 4
