from departments.shared.scoring import ScoringEngine
from departments.academic_library_commons.schemas import (
    LibraryPhysicalCollectionAudit, LibraryDatabaseEresourceAudit, LibraryReferenceResearchConsultationMetric,
    LearningCommonsTutoringMetric, LibraryHoursStudySpaceMetric, DigitalRepositoryOpenAccessAudit, DeterministicLibraryPipelineResult
)

class LibraryPhysicalCollectionAuditorAgent:
    """Agent 1: Audits physical volumes, digital e-books/resources count, and interlibrary loan requests."""
    def run(self) -> LibraryPhysicalCollectionAudit:
        return LibraryPhysicalCollectionAudit()

class LibraryDatabaseEresourceAuditorAgent:
    """Agent 2: Audits licensed database subscriptions, full-text journal subscriptions, and cost-per-use."""
    def run(self) -> LibraryDatabaseEresourceAudit:
        return LibraryDatabaseEresourceAudit()

class LibraryReferenceResearchConsultationMeterAgent:
    """Agent 3: Measures research consultations annual, research librarian satisfaction, and instruction sessions."""
    def run(self) -> LibraryReferenceResearchConsultationMetric:
        return LibraryReferenceResearchConsultationMetric()

class LearningCommonsTutoringMeterAgent:
    """Agent 4: Measures tutoring sessions, writing center appointments, and tutoring satisfaction score."""
    def run(self) -> LearningCommonsTutoringMetric:
        return LearningCommonsTutoringMetric()

class LibraryHoursStudySpaceMeterAgent:
    """Agent 5: Measures open hours per week, individual study rooms, and collaborative group study rooms."""
    def run(self) -> LibraryHoursStudySpaceMetric:
        return LibraryHoursStudySpaceMetric()

class DigitalRepositoryOpenAccessAuditorAgent:
    """Agent 6: Audits faculty theses in digital repository, open access downloads, and repository uptime."""
    def run(self) -> DigitalRepositoryOpenAccessAudit:
        return DigitalRepositoryOpenAccessAudit()

class AcademicLibraryCommonsScorerAgent:
    """Agent 7: Master deterministic aggregator for Academic Library & Learning Commons."""
    def __init__(self):
        self.collection_agent = LibraryPhysicalCollectionAuditorAgent()
        self.db_agent = LibraryDatabaseEresourceAuditorAgent()
        self.research_agent = LibraryReferenceResearchConsultationMeterAgent()
        self.tutoring_agent = LearningCommonsTutoringMeterAgent()
        self.hours_agent = LibraryHoursStudySpaceMeterAgent()
        self.repo_agent = DigitalRepositoryOpenAccessAuditorAgent()

    def run(self) -> DeterministicLibraryPipelineResult:
        collection = self.collection_agent.run()
        databases = self.db_agent.run()
        research_support = self.research_agent.run()
        learning_commons = self.tutoring_agent.run()
        hours = self.hours_agent.run()
        repository = self.repo_agent.run()
        metrics = {
            "librarian_satisfaction": (research_support.research_librarian_satisfaction_score / 5.0) * 100,
            "tutoring_satisfaction": (learning_commons.tutoring_student_satisfaction_score / 5.0) * 100,
            "repo_uptime": repository.repository_uptime_pct,
            "cost_per_use": max(0.0, 100.0 - (databases.database_cost_per_use_usd * 50))
        }
        weights = {"librarian_satisfaction": 0.30, "tutoring_satisfaction": 0.30, "repo_uptime": 0.25, "cost_per_use": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(research_support.research_consultations_annual, 100)
        return DeterministicLibraryPipelineResult(
            collection=collection, databases=databases, research_support=research_support,
            learning_commons=learning_commons, hours=hours, repository=repository,
            library_score=score, confidence_score=confidence
        )
