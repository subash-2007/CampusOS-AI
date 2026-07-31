from typing import Dict, Any, List, Optional
from app.agents.base_agent import BaseAgent
from departments.shared.scoring import ScoringEngine
from departments.resume_intelligence.deterministic import ResumeParserAgent
from departments.resume_intelligence.reasoning import ImpactEvaluatorAgent, ResumeEnhancerAgent
from departments.resume_intelligence.schemas import (
    ResumeOrchestratorReport, ReasoningPipelineResult
)

class ResumeOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator Agent for the Resume Intelligence Department."""
    def __init__(self):
        super().__init__(
            agent_id="resume_orchestrator",
            name="Resume Intelligence Master Orchestrator",
            description="Coordinates all 9 sub-agents to deliver a unified, production-grade Resume Intelligence Report.",
            icon="Briefcase"
        )
        self.parser_agent = ResumeParserAgent()
        self.impact_agent = ImpactEvaluatorAgent()
        self.enhancer_agent = ResumeEnhancerAgent()

    async def run_pipeline(self, resume_text: str, target_keywords: Optional[List[str]] = None) -> ResumeOrchestratorReport:
        reasoning_steps = []
        
        # Step 1: Execute Deterministic Pipeline
        reasoning_steps.append("Step 1: Running deterministic parsing pipeline (Regex contact extraction, Section auditing, Action verb analysis, Date gap detection, Bullet metrics, ATS keyword matching).")
        det_result = self.parser_agent.run(resume_text, target_keywords)
        
        # Step 2: Execute Reasoning Pipeline Agent 8 (Impact Evaluation)
        reasoning_steps.append("Step 2: Executing Impact Evaluator Agent to audit qualitative impact narrative and leadership signals.")
        qual_eval = await self.impact_agent.evaluate(resume_text, det_result)
        
        # Step 3: Execute Reasoning Pipeline Agent 9 (Resume Enhancer)
        reasoning_steps.append("Step 3: Executing Resume Enhancer Agent to generate metric-driven bullet point rewrites and recommendations.")
        enhancements = await self.enhancer_agent.enhance(resume_text, det_result)
        
        # Step 4: Scoring Engine Computation
        reasoning_steps.append("Step 4: Computing overall composite score using weighted metrics (ATS Match: 40%, Quantification Rate: 30%, Verb Density: 30%).")
        metrics = {
            "ats_match": det_result.ats_match.match_percentage,
            "quantification": det_result.bullet_audit.quantification_rate,
            "verb_density": min(det_result.action_verbs.verb_density_score * 10.0, 100.0)
        }
        weights = {"ats_match": 0.40, "quantification": 0.30, "verb_density": 0.30}
        overall_score = ScoringEngine.calculate_weighted_score(metrics, weights)
        
        # Step 5: Construct Final Orchestrator Report
        reasoning_steps.append("Step 5: Synthesizing deterministic data, qualitative evaluations, and recommendations into final report.")
        reasoning_result = ReasoningPipelineResult(
            qualitative_eval=qual_eval,
            enhancements=enhancements,
            reasoning_steps=reasoning_steps
        )
        
        return ResumeOrchestratorReport(
            overall_score=overall_score,
            confidence_score=det_result.confidence_score,
            deterministic_analysis=det_result,
            reasoning_analysis=reasoning_result,
            reasoning_steps=reasoning_steps
        )
