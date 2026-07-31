import logging
from typing import Dict, Any, Optional
from app.services.llm_service import llm_service

logger = logging.getLogger("CampusOS.ModelRouter")

class AIModelRouter:
    """Cloud AI Model Router determining optimal cloud AI provider (Anthropic Claude, Gemini, OpenAI, Tavily) per agent task."""

    # Tasks mapped primarily to Anthropic Claude
    CLAUDE_TASKS = {
        "resume_intelligence",
        "ats_optimization",
        "skill_gap_intelligence",
        "interview_intelligence",
        "career_roadmap",
        "portfolio_intelligence",
        "communication_intelligence",
        "career_analytics",
        "recruiter_simulation",
        "behavioral_intelligence",
        "career_risk_assessment",
        "ai_mentor",
        "professional_branding",
        "project_innovation",
        "technical_architecture_review",
        "ai_hiring_manager",
        "industry_benchmark",
        "offer_evaluation",
        "career_success_prediction",
        "supervisor_evaluation"
    }

    # Fast generation & document extraction mapped primarily to Gemini
    GEMINI_TASKS = {
        "document_verification",
        "learning_resource",
        "certification_advisor",
        "coding_assessment",
        "job_intelligence"
    }

    # Web search tasks mapped primarily to Tavily + Gemini/Claude synthesis
    TAVILY_TASKS = {
        "company_intelligence",
        "market_trend"
    }

    @classmethod
    def get_preferred_provider(cls, task_type: str, preferred_engine: Optional[str] = None) -> str:
        """Determines the primary provider for a given agent task."""
        if preferred_engine:
            return preferred_engine.lower()
        if task_type in cls.TAVILY_TASKS:
            return "tavily"
        if task_type in cls.GEMINI_TASKS:
            return "gemini"
        return "anthropic"

    @classmethod
    async def invoke_model(
        cls,
        task_type: str,
        system_prompt: str,
        user_prompt: str,
        preferred_engine: Optional[str] = None
    ) -> Dict[str, Any]:
        """Routes task to primary cloud provider with automatic fallback (Anthropic -> Gemini -> OpenAI)."""
        provider = cls.get_preferred_provider(task_type, preferred_engine)
        
        # 1. Handle Web Research tasks with Tavily
        if provider == "tavily" or task_type in cls.TAVILY_TASKS:
            web_results = await llm_service.search_tavily(user_prompt[:200])
            context_str = f"User Prompt: {user_prompt}\n\nLive Web Search Results:\n{web_results}"
            gen_res = await llm_service.generate(
                provider="anthropic",
                prompt=context_str,
                system_prompt=system_prompt,
                fallback_providers=["anthropic", "gemini", "openai"]
            )
            gen_res["web_results"] = web_results
            return gen_res

        # 2. Standard LLM Task Generation
        if provider == "gemini":
            fallbacks = ["gemini", "anthropic", "openai"]
        else:
            fallbacks = ["anthropic", "openai", "gemini"]

        res = await llm_service.generate(
            provider=provider,
            prompt=user_prompt,
            system_prompt=system_prompt,
            fallback_providers=fallbacks
        )
        return res

model_router = AIModelRouter()
