from typing import List
from pydantic import BaseModel

class TicketResolutionTimeMetric(BaseModel):
    avg_first_response_time_minutes: float = 14.2
    avg_resolution_time_hours: float = 3.8
    sla_compliance_pct: float = 96.8

class CustomerSatisfactionMetric(BaseModel):
    csat_score_pct: float = 94.5
    ces_score: float = 6.2
    nps_score: float = 64.0

class TicketDeflectionRateAudit(BaseModel):
    ai_deflection_rate_pct: float = 42.0
    self_service_kb_views: int = 14200
    deflection_savings_usd: float = 18500.0

class CustomerHealthScoreAudit(BaseModel):
    healthy_accounts_pct: float = 84.0
    at_risk_accounts_count: int = 8
    critical_risk_accounts_count: int = 1

class SupportChannelVolumeAudit(BaseModel):
    chat_tickets_pct: float = 58.0
    email_tickets_pct: float = 34.0
    phone_tickets_pct: float = 8.0
    total_tickets_last_30d: int = 2450

class SupportAgentPerformanceMetric(BaseModel):
    active_support_agents: int = 14
    avg_tickets_resolved_per_agent_day: float = 24.5
    agent_satisfaction_score: float = 88.0

class DeterministicSupportPipelineResult(BaseModel):
    resolution_time: TicketResolutionTimeMetric
    csat: CustomerSatisfactionMetric
    deflection: TicketDeflectionRateAudit
    health: CustomerHealthScoreAudit
    volume: SupportChannelVolumeAudit
    agent_performance: SupportAgentPerformanceMetric
    support_excellence_score: float
    confidence_score: float

class StrategicSupportNarrative(BaseModel):
    support_summary: str
    key_support_strengths: List[str]

class CustomerSuccessPlan(BaseModel):
    churn_prevention_actions: List[str]
    sample_support_playbook: str

class ReasoningSupportPipelineResult(BaseModel):
    narrative: StrategicSupportNarrative
    success_plan: CustomerSuccessPlan
    reasoning_steps: List[str]

class CustomerSupportSuccessOrchestratorReport(BaseModel):
    department: str = "Customer Support & Success Intelligence"
    department_id: str = "dept_047"
    support_tier: str = "WORLD CLASS CUSTOMER SUPPORT"
    support_excellence_score: float
    confidence_score: float
    deterministic_analysis: DeterministicSupportPipelineResult
    reasoning_analysis: ReasoningSupportPipelineResult
    reasoning_steps: List[str]
