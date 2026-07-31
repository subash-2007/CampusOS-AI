from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class MilestoneGoal(BaseModel):
    timeframe: str  # e.g. "30 Days", "60 Days", "90 Days"
    objectives: List[str] = Field(default_factory=list)
    key_results: List[str] = Field(default_factory=list)

class SalaryTrajectory(BaseModel):
    current_estimate: int = 100000
    target_role_estimate: int = 150000
    expected_increase_pct: float = 50.0

class RoleProgressionPath(BaseModel):
    current_level: str = "Mid-Level Software Engineer"
    next_level: str = "Senior Software Engineer"
    long_term_level: str = "Staff Engineer / Engineering Manager"

class WeeklyTaskPlan(BaseModel):
    week_number: int
    focus_area: str
    action_items: List[str] = Field(default_factory=list)

class RiskMitigationFactor(BaseModel):
    risk_item: str
    mitigation_strategy: str

class FeasibilityScore(BaseModel):
    feasibility_index: float = 88.0

class DeterministicRoadmapPipelineResult(BaseModel):
    milestones: List[MilestoneGoal]
    salary_trajectory: SalaryTrajectory
    progression_path: RoleProgressionPath
    weekly_plan: List[WeeklyTaskPlan]
    risk_factors: List[RiskMitigationFactor]
    feasibility: FeasibilityScore
    confidence_score: float

class StrategicCareerAdvice(BaseModel):
    executive_narrative: str
    networking_strategy: List[str]

class LongTermCareerVision(BaseModel):
    five_year_vision: str
    key_career_pivots: List[str]

class ReasoningRoadmapPipelineResult(BaseModel):
    career_advice: StrategicCareerAdvice
    long_term_vision: LongTermCareerVision
    reasoning_steps: List[str]

class RoadmapOrchestratorReport(BaseModel):
    department: str = "Career Roadmap"
    department_id: str = "dept_007"
    target_role: str
    timeframe_months: int = 3
    confidence_score: float
    deterministic_analysis: DeterministicRoadmapPipelineResult
    reasoning_analysis: ReasoningRoadmapPipelineResult
    reasoning_steps: List[str]
