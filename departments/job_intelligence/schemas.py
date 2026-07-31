from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class TechStackExtraction(BaseModel):
    languages: List[str] = Field(default_factory=list)
    frameworks: List[str] = Field(default_factory=list)
    databases: List[str] = Field(default_factory=list)
    cloud_tools: List[str] = Field(default_factory=list)

class SenioritySignal(BaseModel):
    seniority_level: str = "Mid-Level"
    years_experience_required: int = 3
    is_management_role: bool = False

class ResponsibilityBreakdown(BaseModel):
    core_responsibilities: List[str] = Field(default_factory=list)
    secondary_duties: List[str] = Field(default_factory=list)

class SalaryBenchmarkResult(BaseModel):
    estimated_min_salary: int = 100000
    estimated_max_salary: int = 140000
    currency: str = "USD"

class WorkModelResult(BaseModel):
    work_model: str = "Remote"
    location: str = "United States"

class DomainComplexityResult(BaseModel):
    complexity_score: float = 75.0
    domain_tags: List[str] = Field(default_factory=list)

class DeterministicJobPipelineResult(BaseModel):
    tech_stack: TechStackExtraction
    seniority: SenioritySignal
    responsibilities: ResponsibilityBreakdown
    salary: SalaryBenchmarkResult
    work_model: WorkModelResult
    complexity: DomainComplexityResult
    confidence_score: float

class IdealCandidateProfile(BaseModel):
    ideal_background: str
    key_success_factors: List[str]
    must_have_skills: List[str]

class InterviewFocusStrategy(BaseModel):
    technical_eval_focus: List[str]
    behavioral_eval_focus: List[str]

class ReasoningJobPipelineResult(BaseModel):
    candidate_profile: IdealCandidateProfile
    interview_focus: InterviewFocusStrategy
    reasoning_steps: List[str]

class JobOrchestratorReport(BaseModel):
    department: str = "Job Intelligence"
    department_id: str = "dept_003"
    job_title: str
    seniority_level: str
    confidence_score: float
    deterministic_analysis: DeterministicJobPipelineResult
    reasoning_analysis: ReasoningJobPipelineResult
    reasoning_steps: List[str]
