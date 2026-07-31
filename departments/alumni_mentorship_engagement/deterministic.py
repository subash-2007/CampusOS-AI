from departments.shared.scoring import ScoringEngine
from departments.alumni_mentorship_engagement.schemas import (
    AlumniNetworkSizeMetric, AlumniMentorshipPairingMetric, AlumniDonationGivingMetric,
    AlumniEventParticipationMetric, AlumniCareerTransitionMetric, AlumniChapterNetworkAudit, DeterministicAlumniPipelineResult
)

class AlumniNetworkSizeMeterAgent:
    """Agent 1: Measures registered alumni count, monthly active count, and engagement rate."""
    def run(self, registered: int = 18400) -> AlumniNetworkSizeMetric:
        active = 6800
        return AlumniNetworkSizeMetric(registered_alumni_count=registered, active_monthly_alumni_count=active, alumni_engagement_pct=(active / registered) * 100)

class AlumniMentorshipPairingMeterAgent:
    """Agent 2: Measures active mentorship pairs, satisfaction score, and match success rate."""
    def run(self) -> AlumniMentorshipPairingMetric:
        return AlumniMentorshipPairingMetric(active_mentorship_pairs=1250, mentorship_satisfaction_score=4.8, match_success_rate_pct=94.2)

class AlumniDonationGivingMeterAgent:
    """Agent 3: Tracks annual alumni donations (USD) and donor participation percentage."""
    def run(self) -> AlumniDonationGivingMetric:
        return AlumniDonationGivingMetric(annual_alumni_donations_usd=3450000.0, alumni_donor_participation_pct=14.8)

class AlumniEventParticipationMeterAgent:
    """Agent 4: Measures annual reunion events count and total alumni attendees."""
    def run(self) -> AlumniEventParticipationMetric:
        return AlumniEventParticipationMetric(reunion_events_count_annual=18, alumni_event_attendees_total=8400)

class AlumniCareerTransitionMeterAgent:
    """Agent 5: Tracks alumni hiring current students count and job referrals made."""
    def run(self) -> AlumniCareerTransitionMetric:
        return AlumniCareerTransitionMetric(alumni_hiring_students_count=420, alumni_job_referrals_made=1140)

class AlumniChapterNetworkAuditorAgent:
    """Agent 6: Audits regional chapters count and global city hub presence."""
    def run(self) -> AlumniChapterNetworkAudit:
        return AlumniChapterNetworkAudit(regional_chapters_count=24, global_city_hubs_count=12)

class AlumniEngagementScorerAgent:
    """Agent 7: Master deterministic aggregator for Alumni Mentorship & Engagement."""
    def __init__(self):
        self.size_agent = AlumniNetworkSizeMeterAgent()
        self.mentorship_agent = AlumniMentorshipPairingMeterAgent()
        self.donation_agent = AlumniDonationGivingMeterAgent()
        self.event_agent = AlumniEventParticipationMeterAgent()
        self.career_agent = AlumniCareerTransitionMeterAgent()
        self.chapter_agent = AlumniChapterNetworkAuditorAgent()

    def run(self, registered: int = 18400) -> DeterministicAlumniPipelineResult:
        size = self.size_agent.run(registered)
        mentorship = self.mentorship_agent.run()
        donations = self.donation_agent.run()
        events = self.event_agent.run()
        career = self.career_agent.run()
        chapters = self.chapter_agent.run()

        metrics = {
            "mentorship_match": mentorship.match_success_rate_pct,
            "alumni_engagement": size.alumni_engagement_pct * 2.2,
            "donor_participation": donations.alumni_donor_participation_pct * 5.0,
            "satisfaction": (mentorship.mentorship_satisfaction_score / 5.0) * 100
        }
        weights = {"mentorship_match": 0.35, "alumni_engagement": 0.25, "donor_participation": 0.20, "satisfaction": 0.20}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(mentorship.active_mentorship_pairs, 100)
        return DeterministicAlumniPipelineResult(
            network_size=size, mentorship=mentorship, donations=donations,
            events=events, career_transitions=career, chapters=chapters,
            alumni_engagement_score=score, confidence_score=confidence
        )
