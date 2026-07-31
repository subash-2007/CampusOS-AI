from typing import List, Dict, Any
from departments.shared.scoring import ScoringEngine
from departments.memory_personalization.schemas import (
    UserPreferencesProfile, HistoricalSessionMemory, SkillMasteryTrajectory,
    PersonalizationVector, ContextRetentionScore, UserPersonaProfile, DeterministicMemoryPipelineResult
)

class UserPreferencesAuditorAgent:
    """Agent 1: Audits user career preferences and target roles."""
    def run(self, user_id: str, target_roles: List[str]) -> UserPreferencesProfile:
        return UserPreferencesProfile(
            user_id=user_id,
            target_roles=target_roles if target_roles else ["Software Engineer"],
            preferred_locations=["Remote (US)", "San Francisco, CA"]
        )

class HistoricalMemoryTrackerAgent:
    """Agent 2: Tracks session memory history and interaction logs."""
    def run(self, user_id: str) -> HistoricalSessionMemory:
        return HistoricalSessionMemory(
            total_sessions_count=12,
            recent_interactions=[
                "Completed Resume Intelligence Audit",
                "Generated 30-60-90 Day Career Roadmap",
                "Ran ATS Optimization Scanner"
            ]
        )

class SkillTrajectoryAnalyzerAgent:
    """Agent 3: Tracks skill mastery trajectory over time."""
    def run(self) -> SkillMasteryTrajectory:
        return SkillMasteryTrajectory(
            mastered_skills=["Python", "FastAPI", "Docker"],
            in_progress_skills=["Kubernetes", "System Design", "AWS"]
        )

class PersonalizationVectorBuilderAgent:
    """Agent 4: Builds user domain interest weighting vectors."""
    def run(self) -> PersonalizationVector:
        return PersonalizationVector(domain_interest_weights={
            "backend_engineering": 0.90,
            "cloud_architecture": 0.85,
            "frontend_react": 0.60
        })

class ContextRetentionScorerAgent:
    """Agent 5: Calculates context memory retention score."""
    def run(self, interaction_count: int) -> ContextRetentionScore:
        score = min(75.0 + (interaction_count * 2.0), 98.0)
        return ContextRetentionScore(retention_score=round(score, 1))

class UserPersonaClassifierAgent:
    """Agent 6: Classifies user persona archetype and career stage."""
    def run(self, target_roles: List[str]) -> UserPersonaProfile:
        role = target_roles[0] if target_roles else "Software Engineer"
        return UserPersonaProfile(
            persona_archetype=f"High-Growth {role}",
            career_stage="Mid-Career / Senior Track"
        )

class MemoryScorerAgent:
    """Agent 7: Master deterministic aggregator for Memory & Personalization."""
    def __init__(self):
        self.pref_auditor = UserPreferencesAuditorAgent()
        self.history_tracker = HistoricalMemoryTrackerAgent()
        self.trajectory_analyzer = SkillTrajectoryAnalyzerAgent()
        self.vector_builder = PersonalizationVectorBuilderAgent()
        self.retention_scorer = ContextRetentionScorerAgent()
        self.persona_classifier = UserPersonaClassifierAgent()

    def run(self, user_id: str = "usr_99812", target_roles: List[str] = None) -> DeterministicMemoryPipelineResult:
        if target_roles is None:
            target_roles = ["Senior Backend Engineer"]

        pref = self.pref_auditor.run(user_id, target_roles)
        history = self.history_tracker.run(user_id)
        traj = self.trajectory_analyzer.run()
        vector = self.vector_builder.run()
        retention = self.retention_scorer.run(history.total_sessions_count)
        persona = self.persona_classifier.run(target_roles)

        confidence = ScoringEngine.calculate_confidence_score(
            len(pref.target_roles) + len(history.recent_interactions), 8
        )

        return DeterministicMemoryPipelineResult(
            preferences=pref,
            history=history,
            skill_trajectory=traj,
            vector=vector,
            retention=retention,
            persona=persona,
            confidence_score=confidence
        )
