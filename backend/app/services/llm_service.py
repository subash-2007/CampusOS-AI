import logging
import asyncio
import httpx
from typing import Dict, Any, List, Optional
from app.core.config import settings

logger = logging.getLogger("CampusOS.LLMService")

class LLMService:
    """Unified Cloud LLM Service Layer orchestrating Anthropic Claude, Gemini, OpenAI, and Tavily with per-request timeouts and automatic provider fallbacks."""

    def __init__(self):
        self.anthropic_client = None
        self.openai_client = None
        self._init_clients()

    def _init_clients(self):
        """Initializes API clients using existing environment keys."""
        # 1. Anthropic Claude Client
        anthropic_key = settings.ANTHROPIC_API_KEY
        if anthropic_key and anthropic_key.startswith("sk-ant") and "your_" not in anthropic_key:
            try:
                from anthropic import AsyncAnthropic
                self.anthropic_client = AsyncAnthropic(api_key=anthropic_key, timeout=15.0)
                logger.info("Initialized Anthropic Async Client (Primary Model Engine)")
            except Exception as e:
                logger.warning(f"Failed to initialize Anthropic client: {e}")

        # 2. OpenAI Client
        openai_key = settings.OPENAI_API_KEY
        if openai_key and openai_key.startswith("sk-") and "your_" not in openai_key:
            try:
                from openai import AsyncOpenAI
                self.openai_client = AsyncOpenAI(api_key=openai_key, timeout=15.0)
                logger.info("Initialized OpenAI Async Client (Secondary/Fallback Model Engine)")
            except Exception as e:
                logger.warning(f"Failed to initialize OpenAI client: {e}")

    async def generate_anthropic(self, prompt: str, system_prompt: str = "") -> Optional[str]:
        """Calls Anthropic Claude 3.5 Sonnet / Haiku."""
        if not self.anthropic_client:
            self._init_clients()
        if not self.anthropic_client:
            return None

        models_to_try = ["claude-3-5-sonnet-20241022", "claude-3-5-sonnet-latest", "claude-3-haiku-20240307"]
        sys_p = system_prompt if system_prompt else "You are an elite career intelligence AI specialist creating comprehensive consulting reports."

        for m in models_to_try:
            try:
                response = await asyncio.wait_for(
                    self.anthropic_client.messages.create(
                        model=m,
                        max_tokens=3500,
                        system=sys_p,
                        messages=[{"role": "user", "content": prompt}]
                    ),
                    timeout=25.0
                )
                if response.content and len(response.content) > 0:
                    return response.content[0].text
            except Exception as e:
                logger.warning(f"Anthropic Claude ({m}) call failed/timed out: {e}")
        return None

    async def generate_gemini(self, prompt: str, system_prompt: str = "") -> Optional[str]:
        """Calls Google Gemini API with automatic model name fallback."""
        gemini_key = settings.GEMINI_API_KEY or settings.GOOGLE_API_KEY
        if gemini_key and "your_" not in gemini_key and len(gemini_key) > 10:
            models_to_try = ["gemini-3.6-flash", "gemini-3.5-flash", "gemini-2.0-flash", "gemini-flash-latest"]
            try:
                import google.generativeai as genai
                genai.configure(api_key=gemini_key)
                full_prompt = f"{system_prompt}\n\nUser Query:\n{prompt}" if system_prompt else prompt

                for m in models_to_try:
                    try:
                        model = genai.GenerativeModel(m)
                        resp = await asyncio.wait_for(
                            model.generate_content_async(full_prompt),
                            timeout=22.0
                        )
                        if resp and resp.text:
                            return resp.text
                    except Exception as inner_e:
                        logger.warning(f"Gemini model {m} failed: {inner_e}")
            except Exception as e:
                logger.warning(f"Gemini API call failed: {e}")
        return None

    async def generate_openai(self, prompt: str, system_prompt: str = "") -> Optional[str]:
        """Calls OpenAI Chat Completions API."""
        if not self.openai_client:
            self._init_clients()
        if not self.openai_client:
            return None

        try:
            messages = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
            messages.append({"role": "user", "content": prompt})

            resp = await asyncio.wait_for(
                self.openai_client.chat.completions.create(
                    model=settings.DEFAULT_MODEL or "gpt-4o-mini",
                    messages=messages,
                    temperature=0.7,
                    max_tokens=3500
                ),
                timeout=22.0
            )
            if resp.choices and resp.choices[0].message.content:
                return resp.choices[0].message.content
        except Exception as e:
            logger.warning(f"OpenAI API call failed/timed out: {e}")
        return None

    async def search_tavily(self, query: str) -> List[Dict[str, Any]]:
        """Uses Tavily Web Search API for real-time web research."""
        tavily_key = settings.TAVILY_API_KEY
        if tavily_key and tavily_key.startswith("tvly") and "your_" not in tavily_key:
            try:
                async with httpx.AsyncClient(timeout=8.0) as client:
                    resp = await client.post(
                        "https://api.tavily.com/search",
                        json={"api_key": tavily_key, "query": query, "max_results": 4}
                    )
                    if resp.status_code == 200:
                        data = resp.json()
                        return data.get("results", [])
            except Exception as e:
                logger.warning(f"Tavily web search call failed: {e}")
        return []

    async def generate(
        self,
        provider: str = "anthropic",
        prompt: str = "",
        system_prompt: str = "",
        fallback_providers: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Unified generation method trying specified provider first, then automatic fallback chain.
        Providers: 'anthropic', 'gemini', 'openai', 'tavily'
        """
        fallbacks = fallback_providers or ["anthropic", "gemini", "openai"]
        if provider not in fallbacks:
            fallbacks = [provider] + [p for p in fallbacks if p != provider]

        for p in fallbacks:
            res_text = None
            if p == "anthropic":
                res_text = await self.generate_anthropic(prompt, system_prompt)
                if res_text:
                    return {"content": res_text, "provider": "Anthropic Claude 3.5", "model_used": "Claude 3.5 Sonnet"}
            elif p == "gemini":
                res_text = await self.generate_gemini(prompt, system_prompt)
                if res_text:
                    return {"content": res_text, "provider": "Google Gemini", "model_used": "Gemini 1.5 Flash"}
            elif p == "openai":
                res_text = await self.generate_openai(prompt, system_prompt)
                if res_text:
                    return {"content": res_text, "provider": "OpenAI", "model_used": settings.DEFAULT_MODEL or "gpt-4o-mini"}

        return {
            "content": "",
            "provider": "dynamic_nlp_engine",
            "model_used": "CampusOS Dynamic NLP Engine"
        }

llm_service = LLMService()
