import pytest, asyncio
from departments.academic_library_commons.deterministic import (
    LibraryPhysicalCollectionAuditorAgent, LibraryDatabaseEresourceAuditorAgent, LibraryReferenceResearchConsultationMeterAgent,
    LearningCommonsTutoringMeterAgent, LibraryHoursStudySpaceMeterAgent, DigitalRepositoryOpenAccessAuditorAgent, AcademicLibraryCommonsScorerAgent
)
from departments.academic_library_commons.orchestrator import AcademicLibraryCommonsOrchestratorAgent

def test_library_physical_collection_auditor():
    res = LibraryPhysicalCollectionAuditorAgent().run()
    assert res.physical_volumes_holdings >= 100000

def test_library_database_eresource_auditor():
    res = LibraryDatabaseEresourceAuditorAgent().run()
    assert res.licensed_databases_subscriptions >= 50
    assert res.database_cost_per_use_usd < 5.0

def test_library_reference_research_consultation_meter():
    res = LibraryReferenceResearchConsultationMeterAgent().run()
    assert res.research_librarian_satisfaction_score >= 4.0

def test_learning_commons_tutoring_meter():
    res = LearningCommonsTutoringMeterAgent().run()
    assert res.tutoring_sessions_facilitated_annual >= 5000
    assert res.tutoring_student_satisfaction_score >= 4.0

def test_library_hours_study_space_meter():
    res = LibraryHoursStudySpaceMeterAgent().run()
    assert res.library_open_hours_per_week >= 80

def test_digital_repository_open_access_auditor():
    res = DigitalRepositoryOpenAccessAuditorAgent().run()
    assert res.repository_uptime_pct >= 99.0

def test_academic_library_commons_scorer():
    res = AcademicLibraryCommonsScorerAgent().run()
    assert res.library_score >= 90.0
    assert res.confidence_score >= 0.5

def test_academic_library_commons_orchestrator():
    report = asyncio.run(AcademicLibraryCommonsOrchestratorAgent().run_pipeline())
    assert report.department == "Academic Library & Learning Commons"
    assert report.department_id == "dept_099"
    assert report.library_tier == "ARL RESEARCH LIBRARY DISTINCTION"
    assert len(report.reasoning_steps) == 4
