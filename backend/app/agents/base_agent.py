import os
import json
import logging
import httpx
from typing import Dict, Any, List, Optional
from app.core.config import settings

logger = logging.getLogger("CampusOS.BaseAgent")

class BaseAgent:
    def __init__(self, agent_id: str, name: str, description: str, icon: str):
        self.agent_id = agent_id
        self.name = name
        self.description = description
        self.icon = icon

    async def call_llm(self, system_prompt: str, user_prompt: str) -> str:
        """Invokes LLM (OpenAI, Anthropic, Gemini) for prose enhancement only."""
        # 1. Try OpenAI if API key present
        if settings.OPENAI_API_KEY and settings.OPENAI_API_KEY.startswith("sk-") and "your_" not in settings.OPENAI_API_KEY:
            try:
                from openai import AsyncOpenAI
                client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
                response = await client.chat.completions.create(
                    model=settings.DEFAULT_MODEL,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    temperature=0.7,
                    max_tokens=1500
                )
                content = response.choices[0].message.content
                if content:
                    return content
            except Exception as e:
                logger.warning(f"[{self.agent_id}] OpenAI API call failed: {e}")

        # 2. Try Anthropic if API key present
        if settings.ANTHROPIC_API_KEY and settings.ANTHROPIC_API_KEY.startswith("sk-ant") and "your_" not in settings.ANTHROPIC_API_KEY:
            try:
                from anthropic import AsyncAnthropic
                client = AsyncAnthropic(api_key=settings.ANTHROPIC_API_KEY)
                response = await client.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=1500,
                    system=system_prompt,
                    messages=[{"role": "user", "content": user_prompt}]
                )
                if response.content and len(response.content) > 0:
                    return response.content[0].text
            except Exception as e:
                logger.warning(f"[{self.agent_id}] Anthropic API call failed: {e}")

        # 3. Try Google Gemini if API key present
        if settings.GOOGLE_API_KEY and "your_" not in settings.GOOGLE_API_KEY:
            try:
                import google.generativeai as genai
                genai.configure(api_key=settings.GOOGLE_API_KEY)
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = await model.generate_content_async(f"{system_prompt}\n\nUser Request: {user_prompt}")
                if response.text:
                    return response.text
            except Exception as e:
                logger.warning(f"[{self.agent_id}] Google Gemini API call failed: {e}")

        logger.info(f"[{self.agent_id}] Utilizing Local Dynamic Engine.")
        return ""

    async def search_tavily(self, query: str) -> List[Dict[str, Any]]:
        """Uses Tavily Web Search API for real-time web search if valid key is provided."""
        if settings.TAVILY_API_KEY and settings.TAVILY_API_KEY.startswith("tvly") and "your_" not in settings.TAVILY_API_KEY:
            try:
                async with httpx.AsyncClient(timeout=8.0) as client:
                    resp = await client.post(
                        "https://api.tavily.com/search",
                        json={"api_key": settings.TAVILY_API_KEY, "query": query, "max_results": 4}
                    )
                    if resp.status_code == 200:
                        data = resp.json()
                        return data.get("results", [])
            except Exception as e:
                logger.warning(f"[{self.agent_id}] Tavily Search failed: {e}")
        return []

    def parse_json_safely(self, text: str, dynamic_fallback: Dict[str, Any]) -> Dict[str, Any]:
        """Safely parses JSON string or returns dynamic calculated NLP data."""
        if not text:
            return dynamic_fallback
        try:
            cleaned = text.strip()
            if cleaned.startswith("```json"):
                cleaned = cleaned[7:]
            if cleaned.startswith("```"):
                cleaned = cleaned[3:]
            if cleaned.endswith("```"):
                cleaned = cleaned[:-3]
            parsed = json.loads(cleaned.strip())
            # Ensure essential calculated metrics come from local engine if available
            return parsed
        except Exception:
            return dynamic_fallback

    async def run(self, inputs: Dict[str, Any], memory: Optional[Any] = None) -> Dict[str, Any]:
        """Abstract run method to be implemented by sub-agents."""
        raise NotImplementedError
