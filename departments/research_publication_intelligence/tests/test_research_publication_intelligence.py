import pytest, asyncio
from departments.research_publication_intelligence.deterministic import (
    PublicationOutputMeterAgent, CitationImpactMeterAgent, ResearchGrantFundingMeterAgent,
    PatentTechTransferAuditorAgent, OpenAccessComplianceAuditorAgent, CoAuthorshipNetworkMeterAgent, ResearchExcellenceScorerAgent
)
from departments.research_publication_intelligence.orchestrator import ResearchPublicationOrchestratorAgent

def test_publication_output_meter():
    res = PublicationOutputMeterAgent().run(340)
    assert res.published_papers_total >= 100
    assert res.peer_reviewed_journals_count > 50

def test_citation_impact_meter():
    res = CitationImpactMeterAgent().run()
    assert res.total_citations_count > 1000
    assert res.h_index_avg >= 10.0

def test_research_grant_funding_meter():
    res = ResearchGrantFundingMeterAgent().run()
    assert res.active_grants_value_usd > 1000000.0

def test_patent_tech_transfer_auditor():
    res = PatentTechTransferAuditorAgent().run()
    assert res.patents_filed_count >= 5

def test_open_access_compliance_auditor():
    res = OpenAccessComplianceAuditorAgent().run()
    assert res.open_access_publications_pct >= 80.0

def test_coauthorship_network_meter():
    res = CoAuthorshipNetworkMeterAgent().run()
    assert res.international_coauthor_pct >= 30.0

def test_research_excellence_scorer():
    res = ResearchExcellenceScorerAgent().run(340)
    assert res.research_excellence_score >= 80.0
    assert res.confidence_score >= 0.5

def test_research_publication_orchestrator():
    report = asyncio.run(ResearchPublicationOrchestratorAgent().run_pipeline(340))
    assert report.department == "Research & Publication Intelligence"
    assert report.department_id == "dept_056"
    assert report.research_tier == "HIGH IMPACT RESEARCH INSTITUTION"
    assert len(report.reasoning_steps) == 4
