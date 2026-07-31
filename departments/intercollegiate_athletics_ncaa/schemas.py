from typing import List
from pydantic import BaseModel

class NCAAAcademicProgressRateAPRMetric(BaseModel):
    overall_department_apr_score: float = 988.0
    teams_meeting_ncaa_apr_benchmark_pct: float = 100.0
    student_athlete_graduation_success_rate_pct: float = 92.4

class NCAAComplianceRulesViolationAudit(BaseModel):
    ncaa_level_1_2_violations_count: int = 0
    ncaa_level_3_secondary_violations_reported: int = 4
    compliance_rules_education_workshops: int = 24

class StudentAthleteNILNameImageLikenessAudit(BaseModel):
    active_nil_deals_disclosed: int = 480
    total_nil_compensation_millions: float = 3.8
    nil_financial_literacy_workshop_completions: int = 520

class AthleticFacilitiesFanAttendanceMetric(BaseModel):
    varsity_sports_teams_count: int = 22
    annual_home_game_attendance_total: int = 384000
    ticket_sales_revenue_millions: float = 18.6

class SportsMedicineAthleticTrainingAudit(BaseModel):
    licensed_athletic_trainers_count: int = 18
    sports_medicine_injury_rehab_cases: int = 2840
    concussion_protocol_compliance_pct: float = 100.0

class SportsInformationMediaBroadcastingMetric(BaseModel):
    live_streamed_athletic_broadcasts: int = 180
    athletic_social_media_followers_total: int = 480000
    media_rights_licensing_revenue_millions: float = 8.4

class DeterministicIntercollegiateAthleticsNCAAPipelineResult(BaseModel):
    apr: NCAAAcademicProgressRateAPRMetric
    compliance: NCAAComplianceRulesViolationAudit
    nil: StudentAthleteNILNameImageLikenessAudit
    attendance: AthleticFacilitiesFanAttendanceMetric
    medicine: SportsMedicineAthleticTrainingAudit
    media: SportsInformationMediaBroadcastingMetric
    athletics_score: float
    confidence_score: float

class StrategicAthleticsNarrative(BaseModel):
    athletics_summary: str
    key_athletics_strengths: List[str]

class AthleticsOperationsPlan(BaseModel):
    athletics_actions: List[str]
    sample_schema_data: str

class ReasoningAthleticsPipelineResult(BaseModel):
    narrative: StrategicAthleticsNarrative
    plan: AthleticsOperationsPlan
    reasoning_steps: List[str]

class IntercollegiateAthleticsNCAAOrchestratorReport(BaseModel):
    department: str = "Intercollegiate Athletics and NCAA Compliance"
    department_id: str = "dept_107"
    tier: str = "NCAA DIVISION I CHAMPIONSHIP ATHLETICS PROGRAM"
    athletics_score: float
    confidence_score: float
    deterministic_analysis: DeterministicIntercollegiateAthleticsNCAAPipelineResult
    reasoning_analysis: ReasoningAthleticsPipelineResult
    reasoning_steps: List[str]
