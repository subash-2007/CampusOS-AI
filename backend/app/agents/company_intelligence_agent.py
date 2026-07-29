from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent

class CompanyIntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="company_intelligence",
            name="Company Intelligence Agent",
            description="Researches target company culture, engineering stack, interview patterns, and live web news via Tavily API.",
            icon="Building"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[Any] = None) -> Dict[str, Any]:
        company_name = inputs.get("company_name", "") or (memory.company_name if memory else "Target Enterprise")

        reasoning_steps = [
            f"Executed real-time web search for '{company_name}' engineering culture via Tavily API",
            "Synthesized company tech stack, interview loop focus, and core values"
        ]

        tavily_results = await self.search_tavily(f"{company_name} engineering interview questions tech stack")
        news_summary = " ".join([res.get("content", "") for res in tavily_results[:2]]) if tavily_results else ""

        dynamic_fallback = {
            "company_name": company_name,
            "company_insights": f"{company_name} focuses on high-performance software engineering, cloud infrastructure scalability, and rapid feature delivery.",
            "engineering_culture": "Agile microservice architecture, continuous integration, and data-driven product decisions.",
            "interview_focus": "System design architecture, data structures & algorithms, and behavioral cultural fit."
        }

        system_prompt = (
            "You are a Corporate Technical Recruiter. Synthesize target company insights. "
            "Return JSON ONLY with keys:\n"
            "- 'company_name': str\n"
            "- 'company_insights': str (2-sentence company summary)\n"
            "- 'engineering_culture': str (Summary of tech culture)\n"
            "- 'interview_focus': str (Primary technical interview topics)"
        )

        user_prompt = f"Company: {company_name}\nSearch Results:\n{news_summary}"
        llm_response = await self.call_llm(system_prompt, user_prompt)
        output = self.parse_json_safely(llm_response, dynamic_fallback)

        if memory:
            memory.company_intelligence = output

        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
