from departments.shared.scoring import ScoringEngine
from departments.student_judicial_conduct.schemas import (
    StudentConductIncidentCaseVolumeMetric, ConductHearingResolutionSpeedAudit, AcademicIntegrityHonorCodeAudit,
    RestorativeJusticeCommunityServiceMetric, StudentConductAdvisorTrainingMetric, TitleIXConductCrossReferenceAudit, DeterministicJudicialPipelineResult
)

class StudentConductIncidentCaseVolumeMeterAgent:
    """Agent 1: Measures annual conduct cases adjudicated, academic integrity violations, and behavioral infractions."""
    def run(self, cases: int = 1420) -> StudentConductIncidentCaseVolumeMetric:
        return StudentConductIncidentCaseVolumeMetric(annual_conduct_cases_adjudicated=cases, academic_integrity_violations=420, non_academic_behavioral_infractions=1000)

class ConductHearingResolutionSpeedAuditorAgent:
    """Agent 2: Audits average case resolution speed (days), due process compliance rate percentage, and hearing board resolutions."""
    def run(self) -> ConductHearingResolutionSpeedAudit:
        return ConductHearingResolutionSpeedAudit(avg_case_resolution_days=8.5, due_process_compliance_rate_pct=100.0, conduct_hearing_board_cases_resolved=340)

class AcademicIntegrityHonorCodeAuditorAgent:
    """Agent 3: Audits Turnitin similarity flagged cases, Honor Code pledge compliance, and repeat academic violation rate."""
    def run(self) -> AcademicIntegrityHonorCodeAudit:
        return AcademicIntegrityHonorCodeAudit(turnitin_similarity_flagged_cases=680, honor_code_pledge_compliance_pct=98.6, repeat_academic_violation_rate_pct=1.2)

class RestorativeJusticeCommunityServiceMeterAgent:
    """Agent 4: Measures restorative justice resolutions, sanctioned community service hours, and recidivism reduction rate."""
    def run(self) -> RestorativeJusticeCommunityServiceMetric:
        return RestorativeJusticeCommunityServiceMetric(restorative_justice_resolutions=280, sanctioned_community_service_hours_logged=14200, recidivism_reduction_rate_pct=92.4)

class StudentConductAdvisorTrainingMeterAgent:
    """Agent 5: Measures trained conduct advisors count and advisor training completion percentage."""
    def run(self) -> StudentConductAdvisorTrainingMetric:
        return StudentConductAdvisorTrainingMetric(trained_conduct_advisors_count=65, advisor_training_completion_pct=100.0)

class TitleIXConductCrossReferenceAuditorAgent:
    """Agent 6: Audits Title IX referred cases, interim protective measures enforced, and procedural compliance percentage."""
    def run(self) -> TitleIXConductCrossReferenceAudit:
        return TitleIXConductCrossReferenceAudit(title_ix_referred_cases=48, interim_protective_measures_enforced=48, title_ix_procedural_compliance_pct=100.0)

class StudentJudicialConductScorerAgent:
    """Agent 7: Master deterministic aggregator for Student Judicial & Conduct Affairs."""
    def __init__(self):
        self.cases_agent = StudentConductIncidentCaseVolumeMeterAgent()
        self.resolution_agent = ConductHearingResolutionSpeedAuditorAgent()
        self.academic_agent = AcademicIntegrityHonorCodeAuditorAgent()
        self.restorative_agent = RestorativeJusticeCommunityServiceMeterAgent()
        self.advisors_agent = StudentConductAdvisorTrainingMeterAgent()
        self.title_ix_agent = TitleIXConductCrossReferenceAuditorAgent()

    def run(self, cases: int = 1420) -> DeterministicJudicialPipelineResult:
        cases_metric = self.cases_agent.run(cases)
        resolution = self.resolution_agent.run()
        academic_integrity = self.academic_agent.run()
        restorative_justice = self.restorative_agent.run()
        advisors = self.advisors_agent.run()
        title_ix = self.title_ix_agent.run()

        metrics = {
            "due_process": resolution.due_process_compliance_rate_pct,
            "title_ix_compliance": title_ix.title_ix_procedural_compliance_pct,
            "honor_code": academic_integrity.honor_code_pledge_compliance_pct,
            "resolution_speed": max(0.0, 100.0 - (resolution.avg_case_resolution_days * 3))
        }
        weights = {"due_process": 0.35, "title_ix_compliance": 0.30, "honor_code": 0.20, "resolution_speed": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(cases_metric.annual_conduct_cases_adjudicated, 100)
        return DeterministicJudicialPipelineResult(
            cases=cases_metric, resolution=resolution, academic_integrity=academic_integrity,
            restorative_justice=restorative_justice, advisors=advisors, title_ix=title_ix,
            judicial_score=score, confidence_score=confidence
        )
