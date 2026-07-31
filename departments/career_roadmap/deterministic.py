from typing import List, Dict, Any
from departments.shared.scoring import ScoringEngine
from departments.career_roadmap.schemas import (
    MilestoneGoal, SalaryTrajectory, RoleProgressionPath,
    WeeklyTaskPlan, RiskMitigationFactor, FeasibilityScore, DeterministicRoadmapPipelineResult
)

class MilestoneGeneratorAgent:
    """Agent 1: Formulates 30-60-90 day structured milestone objectives."""
    def run(self, target_role: str) -> List[MilestoneGoal]:
        return [
            MilestoneGoal(
                timeframe="30 Days",
                objectives=["Audit skill gaps and complete core certification modules"],
                key_results=["100% completion of foundational Python & FastAPI courses"]
            ),
            MilestoneGoal(
                timeframe="60 Days",
                objectives=["Build production portfolio application and optimize GitHub & resume"],
                key_results=["Deploy full-stack microservices app with live demo link"]
            ),
            MilestoneGoal(
                timeframe="90 Days",
                objectives=["Execute targeted interview applications and mock simulations"],
                key_results=["Complete 10 top-tier company interviews with 80%+ pass rate"]
            )
        ]

class SalaryTrajectoryCalculatorAgent:
    """Agent 2: Calculates salary progression metrics and expected increase %."""
    def run(self, current_salary: int = 100000, target_salary: int = 150000) -> SalaryTrajectory:
        increase_pct = round(((target_salary - current_salary) / max(current_salary, 1)) * 100.0, 2)
        return SalaryTrajectory(
            current_estimate=current_salary,
            target_role_estimate=target_salary,
            expected_increase_pct=increase_pct
        )

class RoleProgressionMapperAgent:
    """Agent 3: Maps role progression trajectory across career levels."""
    def run(self, target_role: str) -> RoleProgressionPath:
        return RoleProgressionPath(
            current_level="Software Engineer",
            next_level=f"Senior {target_role}",
            long_term_level=f"Lead Architect / Staff {target_role}"
        )

class WeeklyPlanGeneratorAgent:
    """Agent 4: Breaks milestones down into weekly execution task items."""
    def run(self) -> List[WeeklyTaskPlan]:
        plans = []
        for w in range(1, 5):
            plans.append(WeeklyTaskPlan(
                week_number=w,
                focus_area="Core Skill Mastery & System Architecture",
                action_items=[f"Complete week {w} backend modules", f"Build feature milestone #{w}"]
            ))
        return plans

class RiskMitigationAnalyzerAgent:
    """Agent 5: Identifies execution risks and mitigation strategies."""
    def run(self) -> List[RiskMitigationFactor]:
        return [
            RiskMitigationFactor(
                risk_item="Interview scheduling conflicts with current job duties",
                mitigation_strategy="Block dedicated 2-hour morning windows for interview prep and calls."
            ),
            RiskMitigationFactor(
                risk_item="System design interview gaps",
                mitigation_strategy="Conduct weekly mock system design simulations."
            )
        ]

class FeasibilityScorerAgent:
    """Agent 6: Calculates overall roadmap feasibility index score."""
    def run(self, expected_increase_pct: float) -> FeasibilityScore:
        score = max(100.0 - (expected_increase_pct * 0.3), 60.0)
        return FeasibilityScore(feasibility_index=round(score, 2))

class RoadmapScorerAgent:
    """Agent 7: Master deterministic aggregator for Career Roadmap."""
    def __init__(self):
        self.milestone_gen = MilestoneGeneratorAgent()
        self.salary_calc = SalaryTrajectoryCalculatorAgent()
        self.prog_mapper = RoleProgressionMapperAgent()
        self.weekly_gen = WeeklyPlanGeneratorAgent()
        self.risk_analyzer = RiskMitigationAnalyzerAgent()
        self.feasibility_scorer = FeasibilityScorerAgent()

    def run(self, target_role: str = "Senior Software Engineer", current_salary: int = 100000, target_salary: int = 150000) -> DeterministicRoadmapPipelineResult:
        milestones = self.milestone_gen.run(target_role)
        salary = self.salary_calc.run(current_salary, target_salary)
        prog = self.prog_mapper.run(target_role)
        weekly = self.weekly_gen.run()
        risks = self.risk_analyzer.run()
        feasibility = self.feasibility_scorer.run(salary.expected_increase_pct)

        confidence = ScoringEngine.calculate_confidence_score(
            len(milestones) + len(weekly) + len(risks), 10
        )

        return DeterministicRoadmapPipelineResult(
            milestones=milestones,
            salary_trajectory=salary,
            progression_path=prog,
            weekly_plan=weekly,
            risk_factors=risks,
            feasibility=feasibility,
            confidence_score=confidence
        )
