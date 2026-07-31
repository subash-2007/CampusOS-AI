from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class TechQuestionBank(BaseModel):
    questions: List[Dict[str, str]] = Field(default_factory=list)

class BehavioralQuestionBank(BaseModel):
    star_questions: List[Dict[str, str]] = Field(default_factory=list)

class SystemDesignTopics(BaseModel):
    design_prompts: List[str] = Field(default_factory=list)

class DifficultyDistribution(BaseModel):
    easy_count: int = 2
    medium_count: int = 5
    hard_count: int = 3

class RubricCriteria(BaseModel):
    scoring_dimensions: List[str] = Field(default_factory=list)

class InterviewDurationEstimate(BaseModel):
    estimated_rounds: int = 4
    total_minutes: int = 240

class DeterministicInterviewPipelineResult(BaseModel):
    tech_questions: TechQuestionBank
    behavioral_questions: BehavioralQuestionBank
    design_topics: SystemDesignTopics
    difficulty: DifficultyDistribution
    rubric: RubricCriteria
    duration: InterviewDurationEstimate
    confidence_score: float

class STARResponseGuide(BaseModel):
    situation_tips: str
    task_tips: str
    action_tips: str
    result_tips: str

class MockSimulationStrategy(BaseModel):
    mock_session_plan: List[str]
    critical_pitfalls_to_avoid: List[str]

class ReasoningInterviewPipelineResult(BaseModel):
    star_guide: STARResponseGuide
    simulation_strategy: MockSimulationStrategy
    reasoning_steps: List[str]

class InterviewOrchestratorReport(BaseModel):
    department: str = "Interview Intelligence"
    department_id: str = "dept_006"
    target_role: str
    target_company: str
    confidence_score: float
    deterministic_analysis: DeterministicInterviewPipelineResult
    reasoning_analysis: ReasoningInterviewPipelineResult
    reasoning_steps: List[str]
