from departments.shared.scoring import ScoringEngine
from departments.research_publication_intelligence.schemas import (
    PublicationOutputMetric, CitationImpactMetric, ResearchGrantFundingMetric,
    PatentTechTransferAudit, OpenAccessComplianceAudit, CoAuthorshipNetworkMetric, DeterministicResearchPipelineResult
)

class PublicationOutputMeterAgent:
    """Agent 1: Measures total published papers, peer-reviewed journals, and conference proceedings."""
    def run(self, papers: int = 340) -> PublicationOutputMetric:
        return PublicationOutputMetric(published_papers_total=papers, peer_reviewed_journals_count=280, conference_proceedings_count=60)

class CitationImpactMeterAgent:
    """Agent 2: Measures total citation count, h-index, and i10-index average across research faculty."""
    def run(self) -> CitationImpactMetric:
        return CitationImpactMetric(total_citations_count=8400, h_index_avg=18.5, i10_index_avg=32.0)

class ResearchGrantFundingMeterAgent:
    """Agent 3: Tracks active grant funding value, grant win rate percentage, and granting agency count."""
    def run(self) -> ResearchGrantFundingMetric:
        return ResearchGrantFundingMetric(active_grants_value_usd=8500000.0, grant_win_rate_pct=24.8, grant_agencies_count=14)

class PatentTechTransferAuditorAgent:
    """Agent 4: Audits patents filed/granted and tech transfer commercialization licensing agreements."""
    def run(self) -> PatentTechTransferAudit:
        return PatentTechTransferAudit(patents_filed_count=18, patents_granted_count=12, tech_transfer_licensing_agreements=6)

class OpenAccessComplianceAuditorAgent:
    """Agent 5: Audits open access publication percentage and preprint repository uploads."""
    def run(self) -> OpenAccessComplianceAudit:
        return OpenAccessComplianceAudit(open_access_publications_pct=92.0, arxiv_biorxiv_preprints_count=145)

class CoAuthorshipNetworkMeterAgent:
    """Agent 6: Measures international co-authorship rate and industry collaborative research percentage."""
    def run(self) -> CoAuthorshipNetworkMetric:
        return CoAuthorshipNetworkMetric(international_coauthor_pct=44.0, industry_collaborative_papers_pct=28.0)

class ResearchExcellenceScorerAgent:
    """Agent 7: Master deterministic aggregator for Research & Publication Intelligence."""
    def __init__(self):
        self.pub_agent = PublicationOutputMeterAgent()
        self.citation_agent = CitationImpactMeterAgent()
        self.grant_agent = ResearchGrantFundingMeterAgent()
        self.patent_agent = PatentTechTransferAuditorAgent()
        self.oa_agent = OpenAccessComplianceAuditorAgent()
        self.coauthor_agent = CoAuthorshipNetworkMeterAgent()

    def run(self, papers: int = 340) -> DeterministicResearchPipelineResult:
        pubs = self.pub_agent.run(papers)
        citation = self.citation_agent.run()
        grants = self.grant_agent.run()
        patents = self.patent_agent.run()
        oa = self.oa_agent.run()
        coauthor = self.coauthor_agent.run()

        metrics = {
            "h_index": min(100.0, citation.h_index_avg * 4.5),
            "open_access": oa.open_access_publications_pct,
            "grant_win_rate": grants.grant_win_rate_pct * 3.5,
            "international_coauthorship": coauthor.international_coauthor_pct * 2.0
        }
        weights = {"h_index": 0.35, "open_access": 0.25, "grant_win_rate": 0.20, "international_coauthorship": 0.20}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(pubs.published_papers_total, 50)
        return DeterministicResearchPipelineResult(
            publications=pubs, citation=citation, grants=grants,
            patents=patents, open_access=oa, coauthorship=coauthor,
            research_excellence_score=score, confidence_score=confidence
        )
