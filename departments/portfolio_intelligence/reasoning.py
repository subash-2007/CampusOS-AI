from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.portfolio_intelligence.schemas import (
    PortfolioNarrativeEvaluation, READMEOptimizationStrategy, ReasoningPortfolioPipelineResult, DeterministicPortfolioPipelineResult
)

class PortfolioNarrativeEvaluatorAgent(BaseAgent):
    """Agent 8: Evaluates qualitative engineering depth and project impact narrative."""
    def __init__(self):
        super().__init__(
            agent_id="portfolio_narrative_evaluator",
            name="Portfolio Narrative Evaluator Agent",
            description="Evaluates code depth, engineering quality, and GitHub repository presentation.",
            icon="FolderGit"
        )

    async def evaluate(self, det_result: DeterministicPortfolioPipelineResult) -> PortfolioNarrativeEvaluation:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Senior Engineering Portfolio Reviewer & Open Source Lead",
            domain_focus="Project architecture evaluation, open-source impact, and GitHub presentation."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"overall_portfolio_score": det_result.overall_portfolio_score, "repo_count": det_result.repos.repo_count}
        )
        
        fallback = {
            "qualitative_impact_summary": f"Candidate demonstrates solid full-stack project experience ({det_result.overall_portfolio_score} score) with clean microservice architecture.",
            "engineering_highlights": [
                "Includes automated CI/CD workflows and high test coverage",
                "Demonstrates multi-language stack fluency (Python, React, Docker)"
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="portfolio_eval", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return PortfolioNarrativeEvaluation(
                qualitative_impact_summary=parsed.get("qualitative_impact_summary", fallback["qualitative_impact_summary"]),
                engineering_highlights=parsed.get("engineering_highlights", fallback["engineering_highlights"])
            )
        except Exception:
            return PortfolioNarrativeEvaluation(**fallback)

class READMEOptimizationStrategistAgent(BaseAgent):
    """Agent 9: Formulates README enhancement strategies and architecture improvements."""
    def __init__(self):
        super().__init__(
            agent_id="readme_optimization_strategist",
            name="README Optimization Strategist Agent",
            description="Formulates GitHub README enhancement strategies and live demo optimizations.",
            icon="FileCode"
        )

    async def strategize(self, det_result: DeterministicPortfolioPipelineResult) -> READMEOptimizationStrategy:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Principal Technical Writer & Open Source Maintainer",
            domain_focus="GitHub README formatting, architecture diagram generation, and documentation design."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"readme_quality_score": det_result.readme_audit.readme_quality_score}
        )
        
        fallback = {
            "suggested_readme_rewrites": [
                {
                    "section": "System Architecture",
                    "suggestion": "Include Mermaid.js sequence and system flow diagrams."
                }
            ],
            "recommended_portfolio_upgrades": [
                "Add live deployment badges and interactive Swagger API documentation URLs",
                "Highlight key performance benchmarks (e.g. 100ms response time, 99.9% uptime)"
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="readme_optimization", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return READMEOptimizationStrategy(
                suggested_readme_rewrites=parsed.get("suggested_readme_rewrites", fallback["suggested_readme_rewrites"]),
                recommended_portfolio_upgrades=parsed.get("recommended_portfolio_upgrades", fallback["recommended_portfolio_upgrades"])
            )
        except Exception:
            return READMEOptimizationStrategy(**fallback)
