from departments.shared.scoring import ScoringEngine
from departments.student_government_leadership.schemas import (
    StudentGovernmentElectionsVoterTurnoutMetric, SGABudgetAllocationAudit, StudentSenateLegislationMetric,
    StudentLeadershipAcademyMetric, StudentAdvocacyTownHallMetric, LeadershipCertificateBadgeAudit, DeterministicSGAPipelineResult
)

class StudentGovernmentElectionsVoterTurnoutMeterAgent:
    """Agent 1: Measures SGA election voter headcount, total eligible voters, and turnout percentage."""
    def run(self, voters: int = 8450) -> StudentGovernmentElectionsVoterTurnoutMetric:
        return StudentGovernmentElectionsVoterTurnoutMetric(total_eligible_voters=18500, student_voters_count=voters, sga_election_voter_turnout_pct=(voters / 18500.0) * 100)

class SGABudgetAllocationAuditorAgent:
    """Agent 2: Audits SGA activity fee budget (USD), club funding grants disbursed, and transparency percentage."""
    def run(self) -> SGABudgetAllocationAudit:
        return SGABudgetAllocationAudit(sga_activity_fee_budget_usd=2400000.0, club_funding_grants_disbursed=340, budget_disbursement_transparency_pct=100.0)

class StudentSenateLegislationMeterAgent:
    """Agent 3: Measures Senate bills introduced, resolutions passed, and university administration adoption rate."""
    def run(self) -> StudentSenateLegislationMetric:
        return StudentSenateLegislationMetric(senate_bills_introduced=48, resolutions_passed=38, administration_adoption_rate_pct=84.2)

class StudentLeadershipAcademyMeterAgent:
    """Agent 4: Measures Leadership Academy workshop graduates and certified student leaders."""
    def run(self) -> StudentLeadershipAcademyMetric:
        return StudentLeadershipAcademyMetric(leadership_workshop_graduates=420, student_leaders_certified=180)

class StudentAdvocacyTownHallMeterAgent:
    """Agent 5: Measures campus town halls hosted, student petitions addressed, and annual attendees."""
    def run(self) -> StudentAdvocacyTownHallMetric:
        return StudentAdvocacyTownHallMetric(campus_town_halls_hosted=8, student_petitions_addressed=24, town_hall_attendees_annual=2800)

class LeadershipCertificateBadgeAuditorAgent:
    """Agent 6: Audits digital leadership badges issued and leadership competency assessment score."""
    def run(self) -> LeadershipCertificateBadgeAudit:
        return LeadershipCertificateBadgeAudit(leadership_digital_badges_issued=650, leadership_competency_assessment_score=4.8)

class StudentGovernmentLeadershipScorerAgent:
    """Agent 7: Master deterministic aggregator for Student Government & Leadership."""
    def __init__(self):
        self.elections_agent = StudentGovernmentElectionsVoterTurnoutMeterAgent()
        self.budget_agent = SGABudgetAllocationAuditorAgent()
        self.senate_agent = StudentSenateLegislationMeterAgent()
        self.academy_agent = StudentLeadershipAcademyMeterAgent()
        self.town_hall_agent = StudentAdvocacyTownHallMeterAgent()
        self.badge_agent = LeadershipCertificateBadgeAuditorAgent()

    def run(self, voters: int = 8450) -> DeterministicSGAPipelineResult:
        elections = self.elections_agent.run(voters)
        budget = self.budget_agent.run()
        senate = self.senate_agent.run()
        academy = self.academy_agent.run()
        town_halls = self.town_hall_agent.run()
        badges = self.badge_agent.run()

        metrics = {
            "budget_transparency": budget.budget_disbursement_transparency_pct,
            "admin_adoption": senate.administration_adoption_rate_pct,
            "voter_turnout": elections.sga_election_voter_turnout_pct * 1.8,
            "leadership_assessment": (badges.leadership_competency_assessment_score / 5.0) * 100
        }
        weights = {"budget_transparency": 0.35, "admin_adoption": 0.30, "voter_turnout": 0.20, "leadership_assessment": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(elections.student_voters_count, 100)
        return DeterministicSGAPipelineResult(
            elections=elections, budget=budget, senate=senate,
            academy=academy, town_halls=town_halls, badges=badges,
            sga_score=score, confidence_score=confidence
        )
