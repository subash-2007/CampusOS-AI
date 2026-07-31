from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class AccessibilityWCAGMetric(BaseModel):
    wcag_compliance_tier: str = "AAA STANDARD"
    contrast_ratio: float = 7.5
    aria_compliance_score: float = 98.0

class DesignSystemTokenCoverage(BaseModel):
    token_usage_pct: float = 94.0
    hardcoded_styles_count: int = 0

class UsabilityTaskSuccessRate(BaseModel):
    task_completion_rate_pct: float = 96.5
    average_task_duration_seconds: int = 18

class UserFlowFrictionScore(BaseModel):
    friction_index_score: float = 12.0
    drop_off_step: Optional[str] = None

class TypographyGridAlignment(BaseModel):
    grid_system_type: str = "8-POINT BASE GRID"
    type_scale_ratio: float = 1.25

class MicroAnimationPerformance(BaseModel):
    animation_frame_rate: int = 60
    gpu_hardware_acceleration: bool = True

class DeterministicDesignPipelineResult(BaseModel):
    wcag: AccessibilityWCAGMetric
    tokens: DesignSystemTokenCoverage
    usability: UsabilityTaskSuccessRate
    friction: UserFlowFrictionScore
    grid: TypographyGridAlignment
    animation: MicroAnimationPerformance
    design_quality_score: float
    confidence_score: float

class StrategicDesignNarrative(BaseModel):
    design_evaluation_summary: str
    key_ux_highlights: List[str]

class DesignSystemAuditPlan(BaseModel):
    figma_token_sync_recommendations: List[str]
    sample_design_system_tokens_json: str

class ReasoningDesignPipelineResult(BaseModel):
    narrative: StrategicDesignNarrative
    audit_plan: DesignSystemAuditPlan
    reasoning_steps: List[str]

class UIUXDesignOrchestratorReport(BaseModel):
    department: str = "UI/UX Design Intelligence"
    department_id: str = "dept_029"
    design_tier: str = "PREMIUM AAA DESIGN"
    design_quality_score: float
    confidence_score: float
    deterministic_analysis: DeterministicDesignPipelineResult
    reasoning_analysis: ReasoningDesignPipelineResult
    reasoning_steps: List[str]
