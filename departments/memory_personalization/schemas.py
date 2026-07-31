from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class UserPreferencesProfile(BaseModel):
    user_id: str
    target_roles: List[str] = Field(default_factory=list)
    preferred_locations: List[str] = Field(default_factory=list)

class HistoricalSessionMemory(BaseModel):
    total_sessions_count: int = 1
    recent_interactions: List[str] = Field(default_factory=list)

class SkillMasteryTrajectory(BaseModel):
    mastered_skills: List[str] = Field(default_factory=list)
    in_progress_skills: List[str] = Field(default_factory=list)

class PersonalizationVector(BaseModel):
    domain_interest_weights: Dict[str, float] = Field(default_factory=dict)

class ContextRetentionScore(BaseModel):
    retention_score: float = 95.0

class UserPersonaProfile(BaseModel):
    persona_archetype: str = "Ambitious Senior Software Engineer"
    career_stage: str = "Mid-Career"

class DeterministicMemoryPipelineResult(BaseModel):
    preferences: UserPreferencesProfile
    history: HistoricalSessionMemory
    skill_trajectory: SkillMasteryTrajectory
    vector: PersonalizationVector
    retention: ContextRetentionScore
    persona: UserPersonaProfile
    confidence_score: float

class PersonalizationSynthesis(BaseModel):
    tailored_advice: str
    recommended_next_actions: List[str]

class AdaptiveLearningPath(BaseModel):
    adapted_milestones: List[str]

class ReasoningMemoryPipelineResult(BaseModel):
    synthesis: PersonalizationSynthesis
    adaptive_path: AdaptiveLearningPath
    reasoning_steps: List[str]

class MemoryOrchestratorReport(BaseModel):
    department: str = "Memory & Personalization"
    department_id: str = "dept_009"
    user_id: str
    retention_score: float
    confidence_score: float
    deterministic_analysis: DeterministicMemoryPipelineResult
    reasoning_analysis: ReasoningMemoryPipelineResult
    reasoning_steps: List[str]
