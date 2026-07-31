from departments.shared.scoring import ScoringEngine
from departments.intercollegiate_athletics_ncaa.schemas import (NCAAAcademicProgressRateAPRMetric, NCAAComplianceRulesViolationAudit, StudentAthleteNILNameImageLikenessAudit, AthleticFacilitiesFanAttendanceMetric, SportsMedicineAthleticTrainingAudit, SportsInformationMediaBroadcastingMetric, DeterministicIntercollegiateAthleticsNCAAPipelineResult)

class NCAAAcademicProgressRateAPRMeterAgent:
    """Agent 1: Evaluates NCAAAcademicProgressRateAPRMetric."""
    def run(self) -> NCAAAcademicProgressRateAPRMetric:
        return NCAAAcademicProgressRateAPRMetric()

class NCAAComplianceRulesViolationAuditorAgent:
    """Agent 2: Evaluates NCAAComplianceRulesViolationAudit."""
    def run(self) -> NCAAComplianceRulesViolationAudit:
        return NCAAComplianceRulesViolationAudit()

class StudentAthleteNILNameImageLikenessAuditorAgent:
    """Agent 3: Evaluates StudentAthleteNILNameImageLikenessAudit."""
    def run(self) -> StudentAthleteNILNameImageLikenessAudit:
        return StudentAthleteNILNameImageLikenessAudit()

class AthleticFacilitiesFanAttendanceMeterAgent:
    """Agent 4: Evaluates AthleticFacilitiesFanAttendanceMetric."""
    def run(self) -> AthleticFacilitiesFanAttendanceMetric:
        return AthleticFacilitiesFanAttendanceMetric()

class SportsMedicineAthleticTrainingAuditorAgent:
    """Agent 5: Evaluates SportsMedicineAthleticTrainingAudit."""
    def run(self) -> SportsMedicineAthleticTrainingAudit:
        return SportsMedicineAthleticTrainingAudit()

class SportsInformationMediaBroadcastingMeterAgent:
    """Agent 6: Evaluates SportsInformationMediaBroadcastingMetric."""
    def run(self) -> SportsInformationMediaBroadcastingMetric:
        return SportsInformationMediaBroadcastingMetric()

class IntercollegiateAthleticsNCAAScorerAgent:
    """Agent 7: Master deterministic aggregator for Intercollegiate Athletics and NCAA Compliance."""
    def __init__(self):
        self.apr_agent = NCAAAcademicProgressRateAPRMeterAgent()
        self.compliance_agent = NCAAComplianceRulesViolationAuditorAgent()
        self.nil_agent = StudentAthleteNILNameImageLikenessAuditorAgent()
        self.attendance_agent = AthleticFacilitiesFanAttendanceMeterAgent()
        self.medicine_agent = SportsMedicineAthleticTrainingAuditorAgent()
        self.media_agent = SportsInformationMediaBroadcastingMeterAgent()

    def run(self) -> DeterministicIntercollegiateAthleticsNCAAPipelineResult:
        apr = self.apr_agent.run()
        compliance = self.compliance_agent.run()
        nil = self.nil_agent.run()
        attendance = self.attendance_agent.run()
        medicine = self.medicine_agent.run()
        media = self.media_agent.run()
        metrics = {
            "apr_score": (apr.overall_department_apr_score / 1000.0) * 100,
            "gsr_rate": apr.student_athlete_graduation_success_rate_pct,
            "concussion_compliance": medicine.concussion_protocol_compliance_pct,
            "ncaa_compliance": max(0.0, 100.0 - (compliance.ncaa_level_1_2_violations_count * 50))
        }
        weights = {"apr_score": 0.35, "gsr_rate": 0.30, "concussion_compliance": 0.20, "ncaa_compliance": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(apr.overall_department_apr_score, 10)
        return DeterministicIntercollegiateAthleticsNCAAPipelineResult(
            apr=apr,
            compliance=compliance,
            nil=nil,
            attendance=attendance,
            medicine=medicine,
            media=media,
            athletics_score=score, confidence_score=confidence
        )
