from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class CompanyOverview(BaseModel):
    company_name: str
    industry: str = "Technology"
    estimated_size: str = "1,000 - 5,000 employees"
    headquarters: str = "San Francisco, CA"

class TechStackCultureResult(BaseModel):
    primary_tech_stack: List[str] = Field(default_factory=list)
    engineering_values: List[str] = Field(default_factory=list)

class InterviewFocusSignals(BaseModel):
    system_design_emphasis: float = 85.0
    coding_ds_algo_emphasis: float = 90.0
    behavioral_culture_emphasis: float = 75.0

class NewsSentimentResult(BaseModel):
    recent_news_events: List[str] = Field(default_factory=list)
    overall_sentiment: str = "POSITIVE"

class CompensationCultureResult(BaseModel):
    pay_transparency_score: float = 80.0
    work_life_balance_rating: float = 4.2

class CompetitiveLandscapeResult(BaseModel):
    key_competitors: List[str] = Field(default_factory=list)
    market_position: str = "Market Leader"

class DeterministicCompanyPipelineResult(BaseModel):
    overview: CompanyOverview
    tech_culture: TechStackCultureResult
    interview_signals: InterviewFocusSignals
    news_sentiment: NewsSentimentResult
    comp_culture: CompensationCultureResult
    competition: CompetitiveLandscapeResult
    confidence_score: float

class CompanyCultureAnalysis(BaseModel):
    culture_summary: str
    engineering_principles: List[str]

class CompanyInterviewPrepStrategy(BaseModel):
    top_interview_tips: List[str]
    sample_questions: List[str]

class ReasoningCompanyPipelineResult(BaseModel):
    culture_analysis: CompanyCultureAnalysis
    prep_strategy: CompanyInterviewPrepStrategy
    reasoning_steps: List[str]

class CompanyOrchestratorReport(BaseModel):
    department: str = "Company Intelligence"
    department_id: str = "dept_004"
    company_name: str
    confidence_score: float
    deterministic_analysis: DeterministicCompanyPipelineResult
    reasoning_analysis: ReasoningCompanyPipelineResult
    reasoning_steps: List[str]
