from typing import Dict, Any, List, Optional
from app.agents.base_agent import BaseAgent
from departments.company_intelligence.deterministic import CompanyScorerAgent
from departments.company_intelligence.reasoning import CompanyCultureAnalyzerAgent, CompanyPrepStrategistAgent
from departments.company_intelligence.schemas import (
    CompanyOrchestratorReport, ReasoningCompanyPipelineResult
)

class CompanyOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator Agent for the Company Intelligence Department."""
    def __init__(self):
        super().__init__(
            agent_id="company_orchestrator",
            name="Company Intelligence Master Orchestrator",
            description="Coordinates all 9 sub-agents to deliver a comprehensive Company Intelligence Report.",
            icon="Building"
        )
        self.company_scorer = CompanyScorerAgent()
        self.culture_analyzer = CompanyCultureAnalyzerAgent()
        self.prep_strategist = CompanyPrepStrategistAgent()

    async def run_pipeline(self, company_name: str) -> CompanyOrchestratorReport:
        reasoning_steps = []
        
        # Step 1: Execute Deterministic Pipeline
        reasoning_steps.append("Step 1: Running deterministic Company Intelligence pipeline (Firmographics, Tech culture, Interview signals, News sentiment, Compensation benchmarks, Competitive landscape).")
        det_result = self.company_scorer.run(company_name)
        
        # Step 2: Execute Culture Analyzer Agent
        reasoning_steps.append("Step 2: Executing Company Culture Analyzer Agent to evaluate engineering values and workplace culture.")
        culture = await self.culture_analyzer.analyze(company_name, det_result)
        
        # Step 3: Execute Prep Strategist Agent
        reasoning_steps.append("Step 3: Executing Company Prep Strategist Agent to formulate interview preparation tips and sample questions.")
        strategy = await self.prep_strategist.strategize(company_name, det_result)
        
        # Step 4: Synthesize Report
        reasoning_steps.append("Step 4: Compiling Company Intelligence Report.")
        reasoning_result = ReasoningCompanyPipelineResult(
            culture_analysis=culture,
            prep_strategy=strategy,
            reasoning_steps=reasoning_steps
        )
        
        return CompanyOrchestratorReport(
            company_name=company_name,
            confidence_score=det_result.confidence_score,
            deterministic_analysis=det_result,
            reasoning_analysis=reasoning_result,
            reasoning_steps=reasoning_steps
        )
