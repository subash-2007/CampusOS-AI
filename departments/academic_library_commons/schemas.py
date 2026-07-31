from typing import List
from pydantic import BaseModel

class LibraryPhysicalCollectionAudit(BaseModel):
    physical_volumes_holdings: int = 1480000
    ebooks_digital_resources_count: int = 840000
    interlibrary_loan_requests_annual: int = 24800

class LibraryDatabaseEresourceAudit(BaseModel):
    licensed_databases_subscriptions: int = 480
    full_text_journal_subscriptions: int = 82000
    database_cost_per_use_usd: float = 0.38

class LibraryReferenceResearchConsultationMetric(BaseModel):
    research_consultations_annual: int = 8400
    research_librarian_satisfaction_score: float = 4.82
    library_instruction_sessions_annual: int = 840

class LearningCommonsTutoringMetric(BaseModel):
    tutoring_sessions_facilitated_annual: int = 42000
    writing_center_appointments_annual: int = 12400
    tutoring_student_satisfaction_score: float = 4.74

class LibraryHoursStudySpaceMetric(BaseModel):
    library_open_hours_per_week: int = 112
    individual_study_rooms_available: int = 84
    collaborative_group_study_rooms: int = 28

class DigitalRepositoryOpenAccessAudit(BaseModel):
    faculty_theses_in_digital_repository: int = 48000
    open_access_downloads_annual: int = 1240000
    repository_uptime_pct: float = 99.97

class DeterministicLibraryPipelineResult(BaseModel):
    collection: LibraryPhysicalCollectionAudit
    databases: LibraryDatabaseEresourceAudit
    research_support: LibraryReferenceResearchConsultationMetric
    learning_commons: LearningCommonsTutoringMetric
    hours: LibraryHoursStudySpaceMetric
    repository: DigitalRepositoryOpenAccessAudit
    library_score: float
    confidence_score: float

class StrategicLibraryNarrative(BaseModel):
    library_summary: str
    key_library_strengths: List[str]

class LibraryStrategicPlan(BaseModel):
    library_actions: List[str]
    sample_research_consultation_schema: str

class ReasoningLibraryPipelineResult(BaseModel):
    narrative: StrategicLibraryNarrative
    library_plan: LibraryStrategicPlan
    reasoning_steps: List[str]

class AcademicLibraryCommonsOrchestratorReport(BaseModel):
    department: str = "Academic Library & Learning Commons"
    department_id: str = "dept_099"
    library_tier: str = "ARL RESEARCH LIBRARY DISTINCTION"
    library_score: float
    confidence_score: float
    deterministic_analysis: DeterministicLibraryPipelineResult
    reasoning_analysis: ReasoningLibraryPipelineResult
    reasoning_steps: List[str]
