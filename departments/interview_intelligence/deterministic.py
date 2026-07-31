from typing import List, Dict, Any
from departments.shared.scoring import ScoringEngine
from departments.interview_intelligence.schemas import (
    TechQuestionBank, BehavioralQuestionBank, SystemDesignTopics,
    DifficultyDistribution, RubricCriteria, InterviewDurationEstimate, DeterministicInterviewPipelineResult
)

class TechQuestionGeneratorAgent:
    """Agent 1: Generates tailored technical coding and domain questions."""
    def run(self, tech_stack: List[str]) -> TechQuestionBank:
        questions = []
        for tech in tech_stack[:4]:
            questions.append({
                "category": tech,
                "question": f"Explain key concurrency mechanisms and performance optimization strategies in {tech}.",
                "expected_key_concepts": "Async I/O, thread safety, memory management, profiling tools."
            })
        return TechQuestionBank(questions=questions)

class BehavioralSTARGeneratorAgent:
    """Agent 2: Generates STAR-method behavioral interview questions."""
    def run(self, target_role: str) -> BehavioralQuestionBank:
        return BehavioralQuestionBank(star_questions=[
            {
                "topic": "Conflict Resolution",
                "question": "Tell me about a time you disagreed with a senior architect on system design. How did you resolve it?"
            },
            {
                "topic": "Production Incident",
                "question": "Describe a critical production outage you led the resolution for. What root cause analysis steps did you perform?"
            }
        ])

class SystemDesignPromptGeneratorAgent:
    """Agent 3: Generates system design scenario prompts."""
    def run(self, target_role: str) -> SystemDesignTopics:
        return SystemDesignTopics(design_prompts=[
            "Design a distributed rate-limiter supporting 1M+ requests per second",
            "Design a real-time notification engine with guaranteed delivery"
        ])

class DifficultyDistributionAgent:
    """Agent 4: Maps interview question difficulty distribution."""
    def run(self, seniority: str) -> DifficultyDistribution:
        if "Senior" in seniority or "Staff" in seniority:
            return DifficultyDistribution(easy_count=1, medium_count=4, hard_count=5)
        return DifficultyDistribution(easy_count=3, medium_count=5, hard_count=2)

class RubricCriteriaBuilderAgent:
    """Agent 5: Builds interview scoring rubric criteria."""
    def run(self) -> RubricCriteria:
        return RubricCriteria(scoring_dimensions=[
            "Technical Correctness & Code Hygiene",
            "System Architecture & Scalability",
            "Communication & Problem-Solving Clarity",
            "Behavioral & Culture Fit (STAR Method)"
        ])

class InterviewDurationCalculatorAgent:
    """Agent 6: Estimates interview loop duration and rounds."""
    def run(self, seniority: str) -> InterviewDurationEstimate:
        rounds = 5 if "Senior" in seniority else 4
        return InterviewDurationEstimate(estimated_rounds=rounds, total_minutes=rounds * 60)

class InterviewScorerAgent:
    """Agent 7: Master deterministic aggregator for Interview Intelligence."""
    def __init__(self):
        self.tech_gen = TechQuestionGeneratorAgent()
        self.star_gen = BehavioralSTARGeneratorAgent()
        self.design_gen = SystemDesignPromptGeneratorAgent()
        self.diff_agent = DifficultyDistributionAgent()
        self.rubric_builder = RubricCriteriaBuilderAgent()
        self.duration_calc = InterviewDurationCalculatorAgent()

    def run(self, tech_stack: List[str], target_role: str = "Software Engineer", seniority: str = "Senior") -> DeterministicInterviewPipelineResult:
        tech = self.tech_gen.run(tech_stack)
        star = self.star_gen.run(target_role)
        design = self.design_gen.run(target_role)
        diff = self.diff_agent.run(seniority)
        rubric = self.rubric_builder.run()
        duration = self.duration_calc.run(seniority)

        confidence = ScoringEngine.calculate_confidence_score(
            len(tech.questions) + len(star.star_questions) + len(design.design_prompts), 8
        )

        return DeterministicInterviewPipelineResult(
            tech_questions=tech,
            behavioral_questions=star,
            design_topics=design,
            difficulty=diff,
            rubric=rubric,
            duration=duration,
            confidence_score=confidence
        )
