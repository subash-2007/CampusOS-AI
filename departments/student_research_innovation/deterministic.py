from departments.shared.scoring import ScoringEngine
from departments.student_research_innovation.schemas import (
    UndergraduateResearchProgramMetric, StartupIncubatorVentureMetric, PatentTechTransferAudit,
    MakerspaceFabLabUsageMetric, InnovationChallengeGrantMetric, IndustryPartnershipResearchAgreementAudit, DeterministicInnovationPipelineResult
)

class UndergraduateResearchProgramMeterAgent:
    """Agent 1: Measures undergraduate researchers active, faculty-mentored projects, and symposium presenters."""
    def run(self) -> UndergraduateResearchProgramMetric:
        return UndergraduateResearchProgramMetric()

class StartupIncubatorVentureMeterAgent:
    """Agent 2: Measures student startups in incubator, seed funding awarded (USD), and startups that raised external funding."""
    def run(self) -> StartupIncubatorVentureMetric:
        return StartupIncubatorVentureMetric()

class PatentTechTransferAuditorAgent:
    """Agent 3: Audits patents filed annually, technology licenses executed, and tech transfer royalties (USD)."""
    def run(self) -> PatentTechTransferAudit:
        return PatentTechTransferAudit()

class MakerspaceFabLabUsageMeterAgent:
    """Agent 4: Measures makerspace active users, equipment utilization percentage, and project prototypes completed."""
    def run(self) -> MakerspaceFabLabUsageMetric:
        return MakerspaceFabLabUsageMetric()

class InnovationChallengeGrantMeterAgent:
    """Agent 5: Measures innovation challenge entries, grants awarded, and average grant award (USD)."""
    def run(self) -> InnovationChallengeGrantMetric:
        return InnovationChallengeGrantMetric()

class IndustryPartnershipResearchAgreementAuditorAgent:
    """Agent 6: Audits industry research partnership agreements, sponsored research revenue, and collaborative publications."""
    def run(self) -> IndustryPartnershipResearchAgreementAudit:
        return IndustryPartnershipResearchAgreementAudit()

class StudentResearchInnovationScorerAgent:
    """Agent 7: Master deterministic aggregator for Student Research & Innovation Incubator."""
    def __init__(self):
        self.research_agent = UndergraduateResearchProgramMeterAgent()
        self.incubator_agent = StartupIncubatorVentureMeterAgent()
        self.patent_agent = PatentTechTransferAuditorAgent()
        self.makerspace_agent = MakerspaceFabLabUsageMeterAgent()
        self.innovation_agent = InnovationChallengeGrantMeterAgent()
        self.industry_agent = IndustryPartnershipResearchAgreementAuditorAgent()

    def run(self) -> DeterministicInnovationPipelineResult:
        undergrad_research = self.research_agent.run()
        incubator = self.incubator_agent.run()
        patents = self.patent_agent.run()
        makerspace = self.makerspace_agent.run()
        innovation_grants = self.innovation_agent.run()
        industry = self.industry_agent.run()
        metrics = {
            "makerspace_utilization": makerspace.makerspace_equipment_utilization_pct,
            "research_participation": min(100.0, (undergrad_research.undergraduate_researchers_active / 20) * 100),
            "startup_success": min(100.0, (incubator.incubator_startups_raised_external_funding / incubator.student_startups_in_incubator) * 100 * 3) if incubator.student_startups_in_incubator > 0 else 0.0,
            "industry_partnerships": min(100.0, industry.industry_research_partnership_agreements * 1.2)
        }
        weights = {"makerspace_utilization": 0.25, "research_participation": 0.30, "startup_success": 0.25, "industry_partnerships": 0.20}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(undergrad_research.undergraduate_researchers_active, 100)
        return DeterministicInnovationPipelineResult(
            undergrad_research=undergrad_research, incubator=incubator, patents=patents,
            makerspace=makerspace, innovation_grants=innovation_grants, industry=industry,
            innovation_score=score, confidence_score=confidence
        )
