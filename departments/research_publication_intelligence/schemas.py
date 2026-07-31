from typing import List
from pydantic import BaseModel

class PublicationOutputMetric(BaseModel):
    published_papers_total: int = 340
    peer_reviewed_journals_count: int = 280
    conference_proceedings_count: int = 60

class CitationImpactMetric(BaseModel):
    total_citations_count: int = 8400
    h_index_avg: float = 18.5
    i10_index_avg: float = 32.0

class ResearchGrantFundingMetric(BaseModel):
    active_grants_value_usd: float = 8500000.0
    grant_win_rate_pct: float = 24.8
    grant_agencies_count: int = 14

class PatentTechTransferAudit(BaseModel):
    patents_filed_count: int = 18
    patents_granted_count: int = 12
    tech_transfer_licensing_agreements: int = 6

class OpenAccessComplianceAudit(BaseModel):
    open_access_publications_pct: float = 92.0
    arxiv_biorxiv_preprints_count: int = 145

class CoAuthorshipNetworkMetric(BaseModel):
    international_coauthor_pct: float = 44.0
    industry_collaborative_papers_pct: float = 28.0

class DeterministicResearchPipelineResult(BaseModel):
    publications: PublicationOutputMetric
    citation: CitationImpactMetric
    grants: ResearchGrantFundingMetric
    patents: PatentTechTransferAudit
    open_access: OpenAccessComplianceAudit
    coauthorship: CoAuthorshipNetworkMetric
    research_excellence_score: float
    confidence_score: float

class StrategicResearchNarrative(BaseModel):
    research_summary: str
    key_research_strengths: List[str]

class CommercializationPlan(BaseModel):
    tech_transfer_actions: List[str]
    sample_grant_proposal_summary: str

class ReasoningResearchPipelineResult(BaseModel):
    narrative: StrategicResearchNarrative
    commercialization_plan: CommercializationPlan
    reasoning_steps: List[str]

class ResearchPublicationOrchestratorReport(BaseModel):
    department: str = "Research & Publication Intelligence"
    department_id: str = "dept_056"
    research_tier: str = "HIGH IMPACT RESEARCH INSTITUTION"
    research_excellence_score: float
    confidence_score: float
    deterministic_analysis: DeterministicResearchPipelineResult
    reasoning_analysis: ReasoningResearchPipelineResult
    reasoning_steps: List[str]
