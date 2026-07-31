from typing import List
from pydantic import BaseModel

class WCAGComplianceAudit(BaseModel):
    wcag_level: str = "AA"
    wcag_compliance_pct: float = 96.5
    wcag_violations_count: int = 2

class ScreenReaderAudit(BaseModel):
    aria_attribute_coverage_pct: float = 98.0
    alt_text_coverage_pct: float = 99.1
    screen_reader_compatibility: str = "EXCELLENT"

class ColorContrastAudit(BaseModel):
    min_contrast_ratio: float = 4.8
    contrast_pass_rate_pct: float = 97.4
    non_compliant_elements: int = 1

class KeyboardNavigationAudit(BaseModel):
    tab_order_compliant_pct: float = 100.0
    focus_indicator_visible: bool = True
    keyboard_traps_count: int = 0

class InclusiveLanguageAudit(BaseModel):
    gender_neutral_language_pct: float = 98.6
    bias_free_phrasing_score: float = 99.0
    flagged_phrases_count: int = 0

class CognitiveAccessibilityMetric(BaseModel):
    readability_level_ok: bool = True
    distraction_free_mode_available: bool = True

class DeterministicA11yPipelineResult(BaseModel):
    wcag: WCAGComplianceAudit
    screen_reader: ScreenReaderAudit
    contrast: ColorContrastAudit
    keyboard: KeyboardNavigationAudit
    inclusive_language: InclusiveLanguageAudit
    cognitive: CognitiveAccessibilityMetric
    a11y_score: float
    confidence_score: float

class StrategicA11yNarrative(BaseModel):
    a11y_summary: str
    key_a11y_strengths: List[str]

class A11yRemediationPlan(BaseModel):
    remediation_actions: List[str]
    sample_accessible_component: str

class ReasoningA11yPipelineResult(BaseModel):
    narrative: StrategicA11yNarrative
    remediation_plan: A11yRemediationPlan
    reasoning_steps: List[str]

class AccessibilityInclusivityOrchestratorReport(BaseModel):
    department: str = "Accessibility & Inclusivity Intelligence"
    department_id: str = "dept_045"
    a11y_tier: str = "WCAG 2.1 AA COMPLIANT"
    a11y_score: float
    confidence_score: float
    deterministic_analysis: DeterministicA11yPipelineResult
    reasoning_analysis: ReasoningA11yPipelineResult
    reasoning_steps: List[str]
