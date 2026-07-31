from typing import List
from pydantic import BaseModel

class ActivePartnershipsMetric(BaseModel):
    active_partners_count: int = 48
    strategic_partners_count: int = 12
    technology_integrations_count: int = 24

class PartnerAttributedRevenueMetric(BaseModel):
    partner_sourced_mrr_usd: float = 12400.0
    partner_influence_revenue_pct: float = 24.5

class IntegrationUsageMetric(BaseModel):
    monthly_api_calls_via_partners: int = 2850000
    top_integration: str = "LinkedIn Talent Hub"
    active_integration_users_pct: float = 68.0

class PartnerCertificationAudit(BaseModel):
    certified_partners_pct: float = 82.0
    partner_portal_active_users: int = 156

class EcosystemMarketplaceMetric(BaseModel):
    marketplace_apps_count: int = 34
    avg_app_rating: float = 4.8
    total_app_installations: int = 18400

class PartnerSLAComplianceAudit(BaseModel):
    partner_api_uptime_pct: float = 99.9
    partner_support_response_hours: float = 1.8

class DeterministicPartnerPipelineResult(BaseModel):
    partnerships: ActivePartnershipsMetric
    revenue: PartnerAttributedRevenueMetric
    integration_usage: IntegrationUsageMetric
    certification: PartnerCertificationAudit
    marketplace: EcosystemMarketplaceMetric
    sla: PartnerSLAComplianceAudit
    ecosystem_health_score: float
    confidence_score: float

class StrategicPartnerNarrative(BaseModel):
    ecosystem_summary: str
    key_ecosystem_strengths: List[str]

class EcosystemExpansionPlan(BaseModel):
    partnership_growth_actions: List[str]
    sample_partner_integration_manifest: str

class ReasoningPartnerPipelineResult(BaseModel):
    narrative: StrategicPartnerNarrative
    expansion_plan: EcosystemExpansionPlan
    reasoning_steps: List[str]

class PartnerEcosystemOrchestratorReport(BaseModel):
    department: str = "Partner & Ecosystem Intelligence"
    department_id: str = "dept_049"
    partner_tier: str = "THRIVING ECOSYSTEM"
    ecosystem_health_score: float
    confidence_score: float
    deterministic_analysis: DeterministicPartnerPipelineResult
    reasoning_analysis: ReasoningPartnerPipelineResult
    reasoning_steps: List[str]
