from typing import List, Dict, Any
from departments.shared.scoring import ScoringEngine
from departments.leadership_management_intelligence.schemas import (
    TeamSizeCapacityMetric, LeadershipStyleAnalysis, ConflictResolutionMetric,
    StrategicVisionScore, CrossFunctionalInfluence, RetentionPerformanceMetric, DeterministicLeadershipPipelineResult
)

class TeamSizeCapacityMeterAgent:
    """Agent 1: Measures managed team size and direct report span of control."""
    def run(self, team_size: int = 12) -> TeamSizeCapacityMetric:
        tier = "LARGE ORG" if team_size > 20 else ("MID-SIZE TEAM" if team_size >= 8 else "SMALL TEAM")
        return TeamSizeCapacityMetric(managed_team_size=team_size, direct_reports_count=min(team_size, 6), capacity_tier=tier)

class LeadershipStyleAnalyzerAgent:
    """Agent 2: Analyzes leadership style traits and delegation scores."""
    def run(self) -> LeadershipStyleAnalysis:
        return LeadershipStyleAnalysis(dominant_style="SERVANT & STRATEGIC", delegation_score=88.0)

class ConflictResolutionScorerAgent:
    """Agent 3: Evaluates conflict resolution and mediation tactics."""
    def run(self) -> ConflictResolutionMetric:
        return ConflictResolutionMetric(
            conflict_resolution_score=90.0,
            deescalation_tactics=["Active Listening", "Interest-Based Relational Approach", "Root Cause Mediation"]
        )

class StrategicVisionScorerAgent:
    """Agent 4: Scores strategic vision clarity and OKR goal alignment."""
    def run(self) -> StrategicVisionScore:
        return StrategicVisionScore(vision_clarity_score=85.0, okr_alignment_rate=92.0)

class CrossFunctionalInfluenceAgent:
    """Agent 5: Measures stakeholder influence across partner departments."""
    def run(self) -> CrossFunctionalInfluence:
        return CrossFunctionalInfluence(
            stakeholder_influence_score=88.0,
            key_partner_departments=["Product", "Design", "Sales Engineering", "Operations"]
        )

class RetentionPerformanceAuditorAgent:
    """Agent 6: Audits team retention rate and voluntary attrition metrics."""
    def run(self) -> RetentionPerformanceMetric:
        return RetentionPerformanceMetric(team_retention_rate=95.0, voluntary_attrition_pct=5.0)

class LeadershipScorerAgent:
    """Agent 7: Master deterministic aggregator for Leadership & Management Intelligence."""
    def __init__(self):
        self.capacity_agent = TeamSizeCapacityMeterAgent()
        self.style_agent = LeadershipStyleAnalyzerAgent()
        self.conflict_agent = ConflictResolutionScorerAgent()
        self.vision_agent = StrategicVisionScorerAgent()
        self.influence_agent = CrossFunctionalInfluenceAgent()
        self.retention_agent = RetentionPerformanceAuditorAgent()

    def run(self, team_size: int = 12) -> DeterministicLeadershipPipelineResult:
        capacity = self.capacity_agent.run(team_size)
        style = self.style_agent.run()
        conflict = self.conflict_agent.run()
        vision = self.vision_agent.run()
        influence = self.influence_agent.run()
        retention = self.retention_agent.run()

        metrics = {
            "delegation": style.delegation_score,
            "conflict": conflict.conflict_resolution_score,
            "vision": vision.vision_clarity_score,
            "retention": retention.team_retention_rate
        }
        weights = {"delegation": 0.25, "conflict": 0.25, "vision": 0.25, "retention": 0.25}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(team_size, 10)

        return DeterministicLeadershipPipelineResult(
            capacity=capacity,
            style=style,
            conflict=conflict,
            vision=vision,
            influence=influence,
            retention=retention,
            leadership_readiness_score=score,
            confidence_score=confidence
        )
