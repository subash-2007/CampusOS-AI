from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.ats_optimization.schemas import (
    QualitativeATSReport, ATSOptimizationStrategy, ReasoningATSPipelineResult, DeterministicATSPipelineResult
)

class ATSQualitativeAuditorAgent(BaseAgent):
    """Agent 8: Evaluates ATS pass probability and qualitative match narrative."""
    def __init__(self):
        super().__init__(
            agent_id="ats_qualitative_auditor",
            name="ATS Qualitative Auditor Agent",
            description="Evaluates ATS scanner compliance, recruiter readability, and pass probability.",
            icon="Search"
        )

    async def evaluate(self, resume_text: str, det_result: DeterministicATSPipelineResult) -> QualitativeATSReport:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Principal ATS Systems Architect & Recruiter Operations Lead",
            domain_focus="ATS scanner pass probability, recruiter readability, and parser compliance."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"overall_ats_score": det_result.overall_ats_score, "missing_keywords": det_result.keyword_match.missing_critical_keywords},
            extra_context=f"Format Safety Score: {det_result.format_compat.font_safety_score}%"
        )
        
        prob = "HIGH" if det_result.overall_ats_score >= 80 else ("MEDIUM" if det_result.overall_ats_score >= 60 else "LOW")
        fallback = {
            "executive_summary": f"Resume demonstrates a {det_result.overall_ats_score}% ATS match score with {prob} scanner pass probability.",
            "ats_pass_probability": prob,
            "strategic_recommendations": [
                f"Insert missing critical hard skills: {', '.join(det_result.keyword_match.missing_critical_keywords[:3])}",
                "Replace weak phrasing with high-impact action verbs"
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="ats_qualitative_eval", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return QualitativeATSReport(
                executive_summary=parsed.get("executive_summary", fallback["executive_summary"]),
                ats_pass_probability=parsed.get("ats_pass_probability", fallback["ats_pass_probability"]),
                strategic_recommendations=parsed.get("strategic_recommendations", fallback["strategic_recommendations"])
            )
        except Exception:
            return QualitativeATSReport(**fallback)

class ATSKeywordOptimizerAgent(BaseAgent):
    """Agent 9: Generates strategic keyword placement guide and bullet point rewrites."""
    def __init__(self):
        super().__init__(
            agent_id="ats_keyword_optimizer",
            name="ATS Keyword Optimizer Agent",
            description="Formulates keyword insertion strategies and ATS-optimized bullet rewrites.",
            icon="Sliders"
        )

    async def optimize(self, resume_text: str, det_result: DeterministicATSPipelineResult) -> ATSOptimizationStrategy:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Senior ATS Optimization Strategist",
            domain_focus="Keyword insertion optimization and ATS bullet rewrites."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"missing_keywords": det_result.keyword_match.missing_critical_keywords}
        )
        
        fallback = {
            "top_priority_rewrites": [
                {
                    "original": "Worked on python scripts and Docker containers.",
                    "improved": "Developed automated Python scripts deployed within Docker containers, improving deployment velocity by 40%."
                }
            ],
            "keyword_insertion_guide": [
                f"Add '{kw}' into the Skills section or bullet descriptions." for kw in det_result.keyword_match.missing_critical_keywords[:3]
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="ats_optimization", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return ATSOptimizationStrategy(
                top_priority_rewrites=parsed.get("top_priority_rewrites", fallback["top_priority_rewrites"]),
                keyword_insertion_guide=parsed.get("keyword_insertion_guide", fallback["keyword_insertion_guide"])
            )
        except Exception:
            return ATSOptimizationStrategy(**fallback)
