from typing import Dict, Any, List, Optional
from app.agents.base_agent import BaseAgent
from departments.job_intelligence.deterministic import JobScorerAgent
from departments.job_intelligence.reasoning import IdealCandidateProfilerAgent, InterviewFocusStrategistAgent
from departments.job_intelligence.schemas import (
    JobOrchestratorReport, ReasoningJobPipelineResult
)

class JobOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator Agent for the Job Intelligence Department."""
    def __init__(self):
        super().__init__(
            agent_id="job_orchestrator",
            name="Job Intelligence Master Orchestrator",
            description="Coordinates all 9 sub-agents to analyze Job Descriptions into structured intelligence reports.",
            icon="Briefcase"
        )
        self.job_scorer = JobScorerAgent()
        self.profiler = IdealCandidateProfilerAgent()
        self.strategist = InterviewFocusStrategistAgent()

    async def run_pipeline(self, jd_text: str, job_title: str = "Software Engineer") -> JobOrchestratorReport:
        reasoning_steps = []
        
        # Step 1: Execute Deterministic Pipeline
        reasoning_steps.append("Step 1: Running deterministic Job Intelligence pipeline (Tech stack extraction, Seniority classification, Responsibility parsing, Salary benchmarking, Work model identification, Domain complexity scoring).")
        det_result = self.job_scorer.run(jd_text)
        
        # Step 2: Execute Ideal Candidate Profiler Agent
        reasoning_steps.append("Step 2: Executing Ideal Candidate Profiler Agent to synthesize target profile and key success factors.")
        profile = await self.profiler.profile(jd_text, det_result)
        
        # Step 3: Execute Interview Focus Strategist Agent
        reasoning_steps.append("Step 3: Executing Interview Focus Strategist Agent to formulate technical and behavioral assessment rubrics.")
        strategy = await self.strategist.strategize(jd_text, det_result)
        
        # Step 4: Synthesize Report
        reasoning_steps.append("Step 4: Compiling Job Intelligence Report.")
        reasoning_result = ReasoningJobPipelineResult(
            candidate_profile=profile,
            interview_focus=strategy,
            reasoning_steps=reasoning_steps
        )
        
        return JobOrchestratorReport(
            job_title=job_title,
            seniority_level=det_result.seniority.seniority_level,
            confidence_score=det_result.confidence_score,
            deterministic_analysis=det_result,
            reasoning_analysis=reasoning_result,
            reasoning_steps=reasoning_steps
        )
