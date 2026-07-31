from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.resume_intelligence.schemas import (
    QualitativeEvaluation, EnhancementStrategy, ReasoningPipelineResult, DeterministicPipelineResult
)

class ImpactEvaluatorAgent(BaseAgent):
    """Agent 8: Evaluates qualitative resume narrative, impact, and leadership signals."""
    def __init__(self):
        super().__init__(
            agent_id="impact_evaluator",
            name="Impact Evaluator Agent",
            description="Evaluates resume bullet point impact narrative, leadership signals, and technical depth.",
            icon="TrendingUp"
        )

    async def evaluate(self, resume_text: str, det_result: DeterministicPipelineResult) -> QualitativeEvaluation:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Executive Resume Auditor & Tech Recruiter",
            domain_focus="Qualitative resume impact assessment, technical depth evaluation, and leadership signal detection."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"resume_text": resume_text, "action_verbs_found": det_result.action_verbs.action_verbs_found},
            extra_context=f"Quantification rate: {det_result.bullet_audit.quantification_rate}%"
        )
        
        fallback = {
            "impact_narrative": "Candidate demonstrates functional engineering experience with opportunities to highlight scalable impact and engineering ownership.",
            "leadership_signal": "Solid individual contributor metrics with clear task execution.",
            "key_strengths": [
                f"Uses {len(det_result.action_verbs.action_verbs_found)} strong action verbs",
                f"Identified {len(det_result.sections_found)} key structural resume sections"
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="impact_evaluation", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return QualitativeEvaluation(
                impact_narrative=parsed.get("impact_narrative", fallback["impact_narrative"]),
                leadership_signal=parsed.get("leadership_signal", fallback["leadership_signal"]),
                key_strengths=parsed.get("key_strengths", fallback["key_strengths"])
            )
        except Exception:
            return QualitativeEvaluation(**fallback)

class ResumeEnhancerAgent(BaseAgent):
    """Agent 9: Formulates actionable resume bullet point rewrites and strategic improvements."""
    def __init__(self):
        super().__init__(
            agent_id="resume_enhancer",
            name="Resume Enhancer Agent",
            description="Generates metric-driven bullet point rewrites and optimization strategies.",
            icon="Sparkles"
        )

    async def enhance(self, resume_text: str, det_result: DeterministicPipelineResult) -> EnhancementStrategy:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Principal Resume Strategist & Career Consultant",
            domain_focus="Formulating metric-driven bullet rewrites and ATS keyword optimization."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"missing_keywords": det_result.ats_match.missing_keywords[:5]},
            extra_context=f"ATS match: {det_result.ats_match.match_percentage}%"
        )
        
        fallback = {
            "top_recommendations": [
                f"Integrate missing target keywords: {', '.join(det_result.ats_match.missing_keywords[:3])}",
                "Increase metric quantification across bullet points (aim for > 60%)",
                "Ensure consistent date formatting across experience history"
            ],
            "suggested_bullet_rewrites": [
                {
                    "original": "Worked on backend microservices and database queries.",
                    "improved": "Architected high-throughput FastAPI microservices, reducing p99 API latency by 35% across 1M+ daily queries."
                }
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="resume_enhancement", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return EnhancementStrategy(
                top_recommendations=parsed.get("top_recommendations", fallback["top_recommendations"]),
                suggested_bullet_rewrites=parsed.get("suggested_bullet_rewrites", fallback["suggested_bullet_rewrites"])
            )
        except Exception:
            return EnhancementStrategy(**fallback)
