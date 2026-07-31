from departments.shared.scoring import ScoringEngine
from departments.institutional_research_accreditation.schemas import (
    IPEDSFederalComplianceReportingAudit, RegionalAccreditationSACSSELFStudyAudit, GraduationRetentionRateTrackingMetric,
    ProgramOutcomesAssessmentCycleAudit, FacultyQualificationsCredentialAudit, InstitutionalEffectivenessDataAudit, DeterministicResearchAccreditationPipelineResult
)

class IPEDSFederalComplianceReportingAuditorAgent:
    """Agent 1: Audits IPEDS reports filed, data accuracy score, and federal on-time reporting percentage."""
    def run(self) -> IPEDSFederalComplianceReportingAudit:
        return IPEDSFederalComplianceReportingAudit()

class RegionalAccreditationSACSSELFStudyAuditorAgent:
    """Agent 2: Audits SACSCOC accreditation status, comprehensive standards met count, and QEP on-track percentage."""
    def run(self) -> RegionalAccreditationSACSSELFStudyAudit:
        return RegionalAccreditationSACSSELFStudyAudit()

class GraduationRetentionRateTrackingMeterAgent:
    """Agent 3: Measures 4-year and 6-year graduation rates and first-to-second year retention rate."""
    def run(self) -> GraduationRetentionRateTrackingMetric:
        return GraduationRetentionRateTrackingMetric()

class ProgramOutcomesAssessmentCycleAuditorAgent:
    """Agent 4: Audits academic programs with SLO assessments completed, total programs, and completion rate percentage."""
    def run(self) -> ProgramOutcomesAssessmentCycleAudit:
        return ProgramOutcomesAssessmentCycleAudit()

class FacultyQualificationsCredentialAuditorAgent:
    """Agent 5: Audits terminal degree faculty percentage and professionally qualified faculty percentage."""
    def run(self) -> FacultyQualificationsCredentialAudit:
        return FacultyQualificationsCredentialAudit()

class InstitutionalEffectivenessDataAuditorAgent:
    """Agent 6: Audits strategic plan KPIs on-track percentage and institutional dashboard update frequency."""
    def run(self) -> InstitutionalEffectivenessDataAudit:
        return InstitutionalEffectivenessDataAudit()

class InstitutionalResearchAccreditationScorerAgent:
    """Agent 7: Master deterministic aggregator for Institutional Research & Accreditation."""
    def __init__(self):
        self.ipeds_agent = IPEDSFederalComplianceReportingAuditorAgent()
        self.accreditation_agent = RegionalAccreditationSACSSELFStudyAuditorAgent()
        self.graduation_agent = GraduationRetentionRateTrackingMeterAgent()
        self.slo_agent = ProgramOutcomesAssessmentCycleAuditorAgent()
        self.faculty_agent = FacultyQualificationsCredentialAuditorAgent()
        self.effectiveness_agent = InstitutionalEffectivenessDataAuditorAgent()

    def run(self) -> DeterministicResearchAccreditationPipelineResult:
        ipeds = self.ipeds_agent.run()
        accreditation = self.accreditation_agent.run()
        graduation = self.graduation_agent.run()
        slo = self.slo_agent.run()
        faculty = self.faculty_agent.run()
        effectiveness = self.effectiveness_agent.run()
        metrics = {
            "ipeds_accuracy": ipeds.ipeds_data_accuracy_score_pct,
            "slo_completion": slo.slo_assessment_completion_rate_pct,
            "faculty_qualified": faculty.professionally_qualified_faculty_pct,
            "strategic_kpis": effectiveness.strategic_plan_kpis_on_track_pct
        }
        weights = {"ipeds_accuracy": 0.30, "slo_completion": 0.30, "faculty_qualified": 0.25, "strategic_kpis": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(slo.academic_programs_with_slo_assessment, 10)
        return DeterministicResearchAccreditationPipelineResult(
            ipeds=ipeds, accreditation=accreditation, graduation=graduation,
            slo=slo, faculty=faculty, effectiveness=effectiveness,
            research_score=score, confidence_score=confidence
        )
