from typing import List
from pydantic import BaseModel

class InternationalStudentDemographicsMetric(BaseModel):
    international_students_count: int = 2450
    represented_countries_count: int = 94
    top_origin_countries: List[str] = ["India", "China", "South Korea", "Brazil", "Germany"]

class SEVISComplianceAudit(BaseModel):
    sevis_records_maintained: int = 2450
    sevis_reporting_compliance_pct: float = 100.0
    i20_ds2019_issuance_speed_days: float = 2.4

class CPTOPTWorkAuthorizationAudit(BaseModel):
    cpt_authorizations_approved: int = 840
    opt_applications_endorsed: int = 620
    stem_opt_extensions_processed: int = 380

class InternationalHostFamilyCultureMetric(BaseModel):
    host_family_pairs: int = 240
    cultural_exchange_events_annual: int = 32
    event_attendance_total: int = 5800

class EnglishProficiencySupportMetric(BaseModel):
    esl_tutoring_hours_delivered: int = 4200
    toefl_ielts_waiver_audits: int = 650

class InternationalTaxHealthInsuranceAudit(BaseModel):
    non_resident_tax_software_utilization_pct: float = 94.5
    health_insurance_waiver_compliance_pct: float = 98.8

class DeterministicISSSPipelineResult(BaseModel):
    demographics: InternationalStudentDemographicsMetric
    sevis: SEVISComplianceAudit
    work_auth: CPTOPTWorkAuthorizationAudit
    culture: InternationalHostFamilyCultureMetric
    english_support: EnglishProficiencySupportMetric
    tax_insurance: InternationalTaxHealthInsuranceAudit
    isss_score: float
    confidence_score: float

class StrategicISSSNarrative(BaseModel):
    isss_summary: str
    key_isss_strengths: List[str]

class InternationalStudentPlan(BaseModel):
    support_actions: List[str]
    sample_cpt_recommendation_letter: str

class ReasoningISSSPipelineResult(BaseModel):
    narrative: StrategicISSSNarrative
    student_plan: InternationalStudentPlan
    reasoning_steps: List[str]

class InternationalStudentServicesOrchestratorReport(BaseModel):
    department: str = "International Student & Scholar Services"
    department_id: str = "dept_068"
    isss_tier: str = "GLOBAL HUB OF EXCELLENCE"
    isss_score: float
    confidence_score: float
    deterministic_analysis: DeterministicISSSPipelineResult
    reasoning_analysis: ReasoningISSSPipelineResult
    reasoning_steps: List[str]
