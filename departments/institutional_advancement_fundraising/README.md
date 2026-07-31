# Department 080: Institutional Advancement & Fundraising
Annual fundraising totals, capital campaign goals & progress, major gift prospect pipeline closing rates, total endowment assets & investment returns, annual alumni donor participation, donor stewardship fulfillment, and foundation grant success.
## 10-Agent Architecture
Deterministic(7): CapitalCampaignDonationMeterAgent, MajorGiftsProspectPipelineAuditorAgent, EndowmentFundAssetMeterAgent, AnnualGivingDonorParticipationAuditorAgent, DonorStewardshipNamingRightsAuditorAgent, FoundationGrantProposalMeterAgent, InstitutionalAdvancementFundraisingScorerAgent
Reasoning(2): StrategicAdvancementNarrativeAgent, DevelopmentCampaignPlannerAgent
Orchestrator(1): InstitutionalAdvancementFundraisingOrchestratorAgent
