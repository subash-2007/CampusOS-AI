from typing import Dict, Any, List, Optional
from app.agents.base_agent import BaseAgent
from departments.ats_optimization.deterministic import ATSScorerAgent
from departments.ats_optimization.reasoning import ATSQualitativeAuditorAgent, ATSKeywordOptimizerAgent
from departments.ats_optimization.schemas import (
    ATSOrchestratorReport, ReasoningATSPipelineResult
)

class ATSOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator Agent for the ATS Optimization Department."""
    def __init__(self):
        super().__init__(
            agent_id="ats_orchestrator",
            name="ATS Optimization Master Orchestrator",
            description="Coordinates all 9 sub-agents to deliver a unified, production-grade ATS Optimization Report.",
            icon="Target"
        )
        self.ats_scorer = ATSScorerAgent()
        self.qual_auditor = ATSQualitativeAuditorAgent()
        self.optimizer = ATSKeywordOptimizerAgent()

    async def run_pipeline(
        self,
        resume_text: str,
        target_hard_skills: Optional[List[str]] = None,
        target_soft_skills: Optional[List[str]] = None
    ) -> ATSOrchestratorReport:
        reasoning_steps = []
        
        # Step 1: Execute Deterministic Pipeline
        reasoning_steps.append("Step 1: Running deterministic ATS audit (Hard skill matching, Soft skill matching, Format safety, Section audit, Weak phrase detection, Quantification metering).")
        det_result = self.ats_scorer.run(resume_text, target_hard_skills, target_soft_skills)
        
        # Step 2: Execute Qualitative Auditor Agent
        reasoning_steps.append("Step 2: Executing ATS Qualitative Auditor Agent to determine scanner pass probability and recruiter readability.")
        qual_report = await self.qual_auditor.evaluate(resume_text, det_result)
        
        # Step 3: Execute Keyword Optimizer Agent
        reasoning_steps.append("Step 3: Executing ATS Keyword Optimizer Agent to produce bullet rewrites and placement guidelines.")
        strategy = await self.optimizer.optimize(resume_text, det_result)
        
        # Step 4: Synthesize Reasoning Pipeline
        reasoning_steps.append("Step 4: Synthesizing deterministic scores and LLM recommendations into final ATS report.")
        reasoning_result = ReasoningATSPipelineResult(
            qualitative_report=qual_report,
            strategy=strategy,
            reasoning_steps=reasoning_steps
        )
        
        return ATSOrchestratorReport(
            overall_ats_score=det_result.overall_ats_score,
            confidence_score=det_result.confidence_score,
            deterministic_analysis=det_result,
            reasoning_analysis=reasoning_result,
            reasoning_steps=reasoning_steps
        )
