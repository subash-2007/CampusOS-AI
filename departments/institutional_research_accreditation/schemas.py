from typing import List
from pydantic import BaseModel

class IPEDSFederalComplianceReportingAudit(BaseModel):
    ipeds_reports_filed_annual: int = 12
    ipeds_data_accuracy_score_pct: float = 99.8
    federal_reporting_on_time_pct: float = 100.0

class RegionalAccreditationSACSSELFStudyAudit(BaseModel):
    sacs_coc_accreditation_status: str = "ACCREDITED"
    comprehensive_standards_met_count: int = 72
    comprehensive_standards_total_count: int = 72
    quality_enhancement_plan_on_track_pct: float = 100.0

class GraduationRetentionRateTrackingMetric(BaseModel):
    four_year_graduation_rate_pct: float = 68.4
    six_year_graduation_rate_pct: float = 82.6
    first_to_second_year_retention_rate_pct: float = 88.2

class ProgramOutcomesAssessmentCycleAudit(BaseModel):
    academic_programs_with_slo_assessment: int = 186
    total_academic_programs: int = 188
    slo_assessment_completion_rate_pct: float = 98.9

class FacultyQualificationsCredentialAudit(BaseModel):
    terminal_degree_faculty_pct: float = 92.4
    professionally_qualified_faculty_pct: float = 100.0

class InstitutionalEffectivenessDataAudit(BaseModel):
    strategic_plan_kpis_on_track_pct: float = 91.2
    institutional_dashboard_update_frequency_days: int = 30

class DeterministicResearchAccreditationPipelineResult(BaseModel):
    ipeds: IPEDSFederalComplianceReportingAudit
    accreditation: RegionalAccreditationSACSSELFStudyAudit
    graduation: GraduationRetentionRateTrackingMetric
    slo: ProgramOutcomesAssessmentCycleAudit
    faculty: FacultyQualificationsCredentialAudit
    effectiveness: InstitutionalEffectivenessDataAudit
    research_score: float
    confidence_score: float

class StrategicResearchNarrative(BaseModel):
    research_summary: str
    key_research_strengths: List[str]

class AccreditationCompliancePlan(BaseModel):
    accreditation_actions: List[str]
    sample_slo_assessment_schema: str

class ReasoningResearchPipelineResult(BaseModel):
    narrative: StrategicResearchNarrative
    accreditation_plan: AccreditationCompliancePlan
    reasoning_steps: List[str]

class InstitutionalResearchAccreditationOrchestratorReport(BaseModel):
    department: str = "Institutional Research & Accreditation"
    department_id: str = "dept_096"
    accreditation_tier: str = "GOLD STANDARD ACCREDITED INSTITUTION"
    research_score: float
    confidence_score: float
    deterministic_analysis: DeterministicResearchAccreditationPipelineResult
    reasoning_analysis: ReasoningResearchPipelineResult
    reasoning_steps: List[str]
