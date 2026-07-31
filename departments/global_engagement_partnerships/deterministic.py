from departments.shared.scoring import ScoringEngine
from departments.global_engagement_partnerships.schemas import (
    InternationalStudentEnrollmentMetric, StudyAbroadParticipationMetric, GlobalMOUPartnershipAgreementAudit,
    ELIProgramEnglishLanguageAudit, InternationalFacultyExchangeMetric, CulturalExchangeLanguageProgramMetric, DeterministicGlobalEngagementPipelineResult
)

class InternationalStudentEnrollmentMeterAgent:
    """Agent 1: Measures students enrolled internationally, visa sponsorships, and international student GPA."""
    def run(self, int_students: int = 3840) -> InternationalStudentEnrollmentMetric:
        return InternationalStudentEnrollmentMetric(students_enrolled_from_international_countries=int_students)

class StudyAbroadParticipationMeterAgent:
    """Agent 2: Measures students studying abroad, program type distribution, and STEM participation."""
    def run(self) -> StudyAbroadParticipationMetric:
        return StudyAbroadParticipationMetric()

class GlobalMOUPartnershipAgreementAuditorAgent:
    """Agent 3: Audits bilateral MOU agreements, joint degree programs, and dual diploma enrollments."""
    def run(self) -> GlobalMOUPartnershipAgreementAudit:
        return GlobalMOUPartnershipAgreementAudit()

class ELIProgramEnglishLanguageAuditorAgent:
    """Agent 4: Audits English Language Intensive program enrollment, TOEFL/IELTS success rate, and graduate persistence."""
    def run(self) -> ELIProgramEnglishLanguageAudit:
        return ELIProgramEnglishLanguageAudit()

class InternationalFacultyExchangeMeterAgent:
    """Agent 5: Measures visiting international scholars hosted, outbound faculty sabbaticals, and joint research publications."""
    def run(self) -> InternationalFacultyExchangeMetric:
        return InternationalFacultyExchangeMetric()

class CulturalExchangeLanguageProgramMeterAgent:
    """Agent 6: Measures international cultural events, language exchange pairs, and global festival attendance."""
    def run(self) -> CulturalExchangeLanguageProgramMetric:
        return CulturalExchangeLanguageProgramMetric()

class GlobalEngagementPartnershipsScorerAgent:
    """Agent 7: Master deterministic aggregator for Global Engagement & International Partnerships."""
    def __init__(self):
        self.intl_agent = InternationalStudentEnrollmentMeterAgent()
        self.abroad_agent = StudyAbroadParticipationMeterAgent()
        self.mou_agent = GlobalMOUPartnershipAgreementAuditorAgent()
        self.eli_agent = ELIProgramEnglishLanguageAuditorAgent()
        self.faculty_agent = InternationalFacultyExchangeMeterAgent()
        self.cultural_agent = CulturalExchangeLanguageProgramMeterAgent()

    def run(self, int_students: int = 3840) -> DeterministicGlobalEngagementPipelineResult:
        intl_students = self.intl_agent.run(int_students)
        study_abroad = self.abroad_agent.run()
        mou = self.mou_agent.run()
        eli = self.eli_agent.run()
        faculty_exchange = self.faculty_agent.run()
        cultural = self.cultural_agent.run()
        metrics = {
            "intl_enrollment": min(100.0, (intl_students.students_enrolled_from_international_countries / 30) * 100),
            "mou_agreements": min(100.0, mou.active_bilateral_mou_agreements * 0.5),
            "study_abroad": min(100.0, (study_abroad.students_studying_abroad_annual / 18) * 100),
            "eli_success": eli.toefl_ielts_success_rate_pct
        }
        weights = {"intl_enrollment": 0.30, "mou_agreements": 0.25, "study_abroad": 0.25, "eli_success": 0.20}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(int_students, 100)
        return DeterministicGlobalEngagementPipelineResult(
            intl_students=intl_students, study_abroad=study_abroad, mou=mou,
            eli=eli, faculty_exchange=faculty_exchange, cultural=cultural,
            global_score=score, confidence_score=confidence
        )
