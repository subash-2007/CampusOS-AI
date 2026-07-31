from departments.shared.scoring import ScoringEngine
from departments.student_athletics_recreation.schemas import (
    StudentAthleteHeadcountMetric, NCAAAcademicProgressRateAudit, RecCenterFacilityUtilizationMetric,
    AthleticScholarshipNILAudit, SportsMedicineInjuryPreventionAudit, IntramuralClubSportsLeagueMetric, DeterministicAthleticsPipelineResult
)

class StudentAthleteHeadcountMeterAgent:
    """Agent 1: Measures NCAA varsity athletes count, varsity teams, and intramural participants."""
    def run(self, athletes: int = 540) -> StudentAthleteHeadcountMetric:
        return StudentAthleteHeadcountMetric(ncaa_student_athletes_count=athletes, varsity_teams_count=22, club_intramural_participants=4850)

class NCAAAcademicProgressRateAuditorAgent:
    """Agent 2: Audits NCAA Academic Progress Rate (APR) average, graduation success rate, and compliance."""
    def run(self) -> NCAAAcademicProgressRateAudit:
        return NCAAAcademicProgressRateAudit(ncaa_apr_score_avg=988.0, graduation_success_rate_pct=94.2, ncaa_academic_compliance_pct=100.0)

class RecCenterFacilityUtilizationMeterAgent:
    """Agent 3: Measures student rec center annual swipes, peak hour capacity, and equipment uptime."""
    def run(self) -> RecCenterFacilityUtilizationMetric:
        return RecCenterFacilityUtilizationMetric(rec_center_annual_swipes=420000, peak_hour_capacity_utilization_pct=84.5, fitness_equipment_uptime_pct=99.2)

class AthleticScholarshipNILAuditorAgent:
    """Agent 4: Audits athletic scholarship funding (USD), NIL disclosures, and NIL compliance rate."""
    def run(self) -> AthleticScholarshipNILAudit:
        return AthleticScholarshipNILAudit(athletic_scholarships_awarded_usd=4800000.0, nil_compliance_disclosures_processed=340, nil_compliance_rate_pct=100.0)

class SportsMedicineInjuryPreventionAuditorAgent:
    """Agent 5: Audits athletic trainer consultations, return-to-play timeline, and concussion protocols."""
    def run(self) -> SportsMedicineInjuryPreventionAudit:
        return SportsMedicineInjuryPreventionAudit(athletic_trainer_consultations=3200, avg_return_to_play_days=14.2, concussion_protocol_compliance_pct=100.0)

class IntramuralClubSportsLeagueMeterAgent:
    """Agent 6: Measures active intramural leagues, championship events, and sportsmanship ratings."""
    def run(self) -> IntramuralClubSportsLeagueMetric:
        return IntramuralClubSportsLeagueMetric(active_intramural_leagues=28, championship_events_hosted=14, sportsmanship_rating_avg=4.85)

class StudentAthleticsRecreationScorerAgent:
    """Agent 7: Master deterministic aggregator for Student Athletics & Recreation."""
    def __init__(self):
        self.headcount_agent = StudentAthleteHeadcountMeterAgent()
        self.apr_agent = NCAAAcademicProgressRateAuditorAgent()
        self.rec_agent = RecCenterFacilityUtilizationMeterAgent()
        self.nil_agent = AthleticScholarshipNILAuditorAgent()
        self.sports_med_agent = SportsMedicineInjuryPreventionAuditorAgent()
        self.intramural_agent = IntramuralClubSportsLeagueMeterAgent()

    def run(self, athletes: int = 540) -> DeterministicAthleticsPipelineResult:
        headcount = self.headcount_agent.run(athletes)
        ncaa_apr = self.apr_agent.run()
        rec_center = self.rec_agent.run()
        scholarships_nil = self.nil_agent.run()
        sports_medicine = self.sports_med_agent.run()
        intramurals = self.intramural_agent.run()

        metrics = {
            "ncaa_apr": (ncaa_apr.ncaa_apr_score_avg / 1000.0) * 100,
            "nil_compliance": scholarships_nil.nil_compliance_rate_pct,
            "concussion_compliance": sports_medicine.concussion_protocol_compliance_pct,
            "equipment_uptime": rec_center.fitness_equipment_uptime_pct
        }
        weights = {"ncaa_apr": 0.35, "nil_compliance": 0.30, "concussion_compliance": 0.20, "equipment_uptime": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(headcount.ncaa_student_athletes_count, 50)
        return DeterministicAthleticsPipelineResult(
            headcount=headcount, ncaa_apr=ncaa_apr, rec_center=rec_center,
            scholarships_nil=scholarships_nil, sports_medicine=sports_medicine, intramurals=intramurals,
            athletics_score=score, confidence_score=confidence
        )
