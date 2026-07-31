from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.company_intelligence.schemas import (
    CompanyCultureAnalysis, CompanyInterviewPrepStrategy, ReasoningCompanyPipelineResult, DeterministicCompanyPipelineResult
)

class CompanyCultureAnalyzerAgent(BaseAgent):
    """Agent 8: Performs qualitative evaluation of company culture and engineering values."""
    def __init__(self):
        super().__init__(
            agent_id="company_culture_analyzer",
            name="Company Culture Analyzer Agent",
            description="Evaluates engineering culture, leadership principles, and workplace values.",
            icon="Building2"
        )

    async def analyze(self, company_name: str, det_result: DeterministicCompanyPipelineResult) -> CompanyCultureAnalysis:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Senior Technology Culture Consultant",
            domain_focus="Engineering culture assessment and corporate values auditing."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"company_name": company_name, "values": det_result.tech_culture.engineering_values}
        )
        
        fallback = {
            "culture_summary": f"{company_name} maintains an engineering-centric culture emphasizing rapid deployment, code quality, and architectural autonomy.",
            "engineering_principles": det_result.tech_culture.engineering_values
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="culture_analysis", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return CompanyCultureAnalysis(
                culture_summary=parsed.get("culture_summary", fallback["culture_summary"]),
                engineering_principles=parsed.get("engineering_principles", fallback["engineering_principles"])
            )
        except Exception:
            return CompanyCultureAnalysis(**fallback)

class CompanyPrepStrategistAgent(BaseAgent):
    """Agent 9: Formulates tailored company interview strategy and sample questions."""
    def __init__(self):
        super().__init__(
            agent_id="company_prep_strategist",
            name="Company Prep Strategist Agent",
            description="Generates tailored company interview preparation guides and question banks.",
            icon="Lightbulb"
        )

    async def strategize(self, company_name: str, det_result: DeterministicCompanyPipelineResult) -> CompanyInterviewPrepStrategy:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Executive Interview Coach",
            domain_focus="Company-specific technical and behavioral interview preparation."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"company_name": company_name, "system_design_emphasis": det_result.interview_signals.system_design_emphasis}
        )
        
        fallback = {
            "top_interview_tips": [
                f"Focus heavily on system scalability and microservices design for {company_name}",
                "Prepare STAR-method examples demonstrating cross-functional collaboration",
                "Familiarize yourself with the latest tech stack tools (Python, Go, Kubernetes)"
            ],
            "sample_questions": [
                f"How would you design a distributed rate-limiter for {company_name}'s API infrastructure?",
                "Tell me about a time you handled a production incident under strict SLAs."
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="company_interview_prep", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return CompanyInterviewPrepStrategy(
                top_interview_tips=parsed.get("top_interview_tips", fallback["top_interview_tips"]),
                sample_questions=parsed.get("sample_questions", fallback["sample_questions"])
            )
        except Exception:
            return CompanyInterviewPrepStrategy(**fallback)
