import logging
from typing import Dict, Any, List
from app.services.llm_service import llm_service

logger = logging.getLogger("CampusOS.TavilyTool")

class TavilySearchTool:
    """Tool for fetching real-time web search results for company news, hiring trends, and tech stack benchmarks."""
    def __init__(self):
        self.name = "Tavily Search Tool"
        self.description = "Executes real-time web queries for company news, salaries, and industry hiring standards."

    async def execute(self, query: str) -> Dict[str, Any]:
        if not query:
            return {"status": "skipped", "results": []}
        
        try:
            results = await llm_service.search_web_tavily(query)
            return {
                "status": "success",
                "query": query,
                "result_count": len(results),
                "snippets": [r.get("content", r.get("snippet", "")) for r in results if isinstance(r, dict)][:3]
            }
        except Exception as e:
            logger.warning(f"Tavily Tool search error: {e}")
            return {
                "status": "fallback",
                "query": query,
                "snippets": [f"Industry standard benchmark data for {query}"]
            }

tavily_tool = TavilySearchTool()
