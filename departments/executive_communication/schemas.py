from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class BrevityConcisenessMetric(BaseModel):
    conciseness_score: float = 90.0
    word_count_reduction_pct: float = 35.0

class ExecutiveToneAudit(BaseModel):
    assertiveness_score: float = 88.0
    executive_presence_index: str = "HIGH PRESENCE"

class BoardDeckReadinessScore(BaseModel):
    deck_readiness_score: float = 85.0
    key_takeaway_clarity: str = "CRYSTAL CLEAR"

class ActiveListeningMeter(BaseModel):
    active_listening_score: float = 92.0
    empathy_rating: float = 88.0

class DataStorytellingScore(BaseModel):
    data_narrative_score: float = 90.0
    visual_clarity_rating: float = 85.0

class CrisisCommunicationAudit(BaseModel):
    crisis_response_speed: str = "FAST (< 2 HRS)"
    transparency_score: float = 95.0

class DeterministicExecutiveCommPipelineResult(BaseModel):
    brevity: BrevityConcisenessMetric
    tone: ExecutiveToneAudit
    deck: BoardDeckReadinessScore
    listening: ActiveListeningMeter
    storytelling: DataStorytellingScore
    crisis: CrisisCommunicationAudit
    executive_comm_score: float
    confidence_score: float

class StrategicExecutiveNarrative(BaseModel):
    communication_evaluation_summary: str
    key_presentation_strengths: List[str]

class ExecutiveBriefingDraft(BaseModel):
    executive_summary_bulletins: List[str]
    sample_c_suite_memo_draft: str

class ReasoningExecutiveCommPipelineResult(BaseModel):
    narrative: StrategicExecutiveNarrative
    briefing_draft: ExecutiveBriefingDraft
    reasoning_steps: List[str]

class ExecutiveCommunicationOrchestratorReport(BaseModel):
    department: str = "Executive Communication"
    department_id: str = "dept_022"
    communication_tier: str = "C-SUITE PERSUASIVE"
    executive_comm_score: float
    confidence_score: float
    deterministic_analysis: DeterministicExecutiveCommPipelineResult
    reasoning_analysis: ReasoningExecutiveCommPipelineResult
    reasoning_steps: List[str]
