import pytest, asyncio
from departments.institutional_advancement_fundraising.deterministic import (
    CapitalCampaignDonationMeterAgent, MajorGiftsProspectPipelineAuditorAgent, EndowmentFundAssetMeterAgent,
    AnnualGivingDonorParticipationAuditorAgent, DonorStewardshipNamingRightsAuditorAgent, FoundationGrantProposalMeterAgent, InstitutionalAdvancementFundraisingScorerAgent
)
from departments.institutional_advancement_fundraising.orchestrator import InstitutionalAdvancementFundraisingOrchestratorAgent

def test_capital_campaign_donation_meter():
    res = CapitalCampaignDonationMeterAgent().run(48500000.0)
    assert res.annual_fundraising_total_usd == 48500000.0
    assert res.campaign_progress_pct >= 50.0

def test_major_gifts_prospect_pipeline_auditor():
    res = MajorGiftsProspectPipelineAuditorAgent().run()
    assert res.proposals_submitted_usd > 10000000.0
    assert res.major_gift_closing_rate_pct >= 30.0

def test_endowment_fund_asset_meter():
    res = EndowmentFundAssetMeterAgent().run()
    assert res.total_endowment_assets_usd > 100000000.0

def test_annual_giving_donor_participation_auditor():
    res = AnnualGivingDonorParticipationAuditorAgent().run()
    assert res.total_donors_count >= 10000

def test_donor_stewardship_naming_rights_auditor():
    res = DonorStewardshipNamingRightsAuditorAgent().run()
    assert res.stewardship_report_fulfillment_pct >= 95.0

def test_foundation_grant_proposal_meter():
    res = FoundationGrantProposalMeterAgent().run()
    assert res.foundation_grants_awarded_usd > 5000000.0

def test_institutional_advancement_fundraising_scorer():
    res = InstitutionalAdvancementFundraisingScorerAgent().run(48500000.0)
    assert res.advancement_score >= 85.0
    assert res.confidence_score >= 0.5

def test_institutional_advancement_fundraising_orchestrator():
    report = asyncio.run(InstitutionalAdvancementFundraisingOrchestratorAgent().run_pipeline(48500000.0))
    assert report.department == "Institutional Advancement & Fundraising"
    assert report.department_id == "dept_080"
    assert report.advancement_tier == "MAJOR ENDOWMENT CAPITAL LEADER"
    assert len(report.reasoning_steps) == 4
