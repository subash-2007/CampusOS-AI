from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class TeamSizeCapacityMetric(BaseModel):
    managed_team_size: int = 12
    direct_reports_count: int = 6
    capacity_tier: str = "MID-SIZE TEAM"

class LeadershipStyleAnalysis(BaseModel):
    dominant_style: str = "SERVANT & STRATEGIC"
    delegation_score: float = 88.0

class ConflictResolutionMetric(BaseModel):
    conflict_resolution_score: float = 90.0
    deescalation_tactics: List[str] = Field(default_factory=list)

class StrategicVisionScore(BaseModel):
    vision_clarity_score: float = 85.0
    okr_alignment_rate: float = 92.0

class CrossFunctionalInfluence(BaseModel):
    stakeholder_influence_score: float = 88.0
    key_partner_departments: List[str] = Field(default_factory=list)

class RetentionPerformanceMetric(BaseModel):
    team_retention_rate: float = 95.0
    voluntary_attrition_pct: float = 5.0

class DeterministicLeadershipPipelineResult(BaseModel):
    capacity: TeamSizeCapacityMetric
    style: LeadershipStyleAnalysis
    conflict: ConflictResolutionMetric
    vision: StrategicVisionScore
    influence: CrossFunctionalInfluence
    retention: RetentionPerformanceMetric
    leadership_readiness_score: float
    confidence_score: float

class StrategicLeadershipNarrative(BaseModel):
    leadership_evaluation_summary: str
    key_management_strengths: List[str]

class ExecutiveCoachingPlan(BaseModel):
    leadership_development_goals: List[str]
    coaching_action_items: List[str]

class ReasoningLeadershipPipelineResult(BaseModel):
    narrative: StrategicLeadershipNarrative
    coaching_plan: ExecutiveCoachingPlan
    reasoning_steps: List[str]

class LeadershipManagementOrchestratorReport(BaseModel):
    department: str = "Leadership & Management Intelligence"
    department_id: str = "dept_021"
    leadership_tier: str = "EXECUTIVE READY"
    leadership_readiness_score: float
    confidence_score: float
    deterministic_analysis: DeterministicLeadershipPipelineResult
    reasoning_analysis: ReasoningLeadershipPipelineResult
    reasoning_steps: List[str]
