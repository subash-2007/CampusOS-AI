from typing import List
from pydantic import BaseModel

class StudentAthleteHeadcountMetric(BaseModel):
    ncaa_student_athletes_count: int = 540
    varsity_teams_count: int = 22
    club_intramural_participants: int = 4850

class NCAAAcademicProgressRateAudit(BaseModel):
    ncaa_apr_score_avg: float = 988.0
    graduation_success_rate_pct: float = 94.2
    ncaa_academic_compliance_pct: float = 100.0

class RecCenterFacilityUtilizationMetric(BaseModel):
    rec_center_annual_swipes: int = 420000
    peak_hour_capacity_utilization_pct: float = 84.5
    fitness_equipment_uptime_pct: float = 99.2

class AthleticScholarshipNILAudit(BaseModel):
    athletic_scholarships_awarded_usd: float = 4800000.0
    nil_compliance_disclosures_processed: int = 340
    nil_compliance_rate_pct: float = 100.0

class SportsMedicineInjuryPreventionAudit(BaseModel):
    athletic_trainer_consultations: int = 3200
    avg_return_to_play_days: float = 14.2
    concussion_protocol_compliance_pct: float = 100.0

class IntramuralClubSportsLeagueMetric(BaseModel):
    active_intramural_leagues: int = 28
    championship_events_hosted: int = 14
    sportsmanship_rating_avg: float = 4.85

class DeterministicAthleticsPipelineResult(BaseModel):
    headcount: StudentAthleteHeadcountMetric
    ncaa_apr: NCAAAcademicProgressRateAudit
    rec_center: RecCenterFacilityUtilizationMetric
    scholarships_nil: AthleticScholarshipNILAudit
    sports_medicine: SportsMedicineInjuryPreventionAudit
    intramurals: IntramuralClubSportsLeagueMetric
    athletics_score: float
    confidence_score: float

class StrategicAthleticsNarrative(BaseModel):
    athletics_summary: str
    key_athletics_strengths: List[str]

class CampusAthleticsPlan(BaseModel):
    athletics_program_actions: List[str]
    sample_nil_disclosure_schema: str

class ReasoningAthleticsPipelineResult(BaseModel):
    narrative: StrategicAthleticsNarrative
    athletics_plan: CampusAthleticsPlan
    reasoning_steps: List[str]

class StudentAthleticsRecreationOrchestratorReport(BaseModel):
    department: str = "Student Athletics & Recreation"
    department_id: str = "dept_070"
    athletics_tier: str = "NCAA CHAMPIONSHIP EXCELLENCE PROGRAM"
    athletics_score: float
    confidence_score: float
    deterministic_analysis: DeterministicAthleticsPipelineResult
    reasoning_analysis: ReasoningAthleticsPipelineResult
    reasoning_steps: List[str]
