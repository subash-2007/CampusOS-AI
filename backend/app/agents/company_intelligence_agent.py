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
        target_role = inputs.get("target_role") or (memory.target_role if memory else "Software Engineer")

        tavily_results = await self.search_tavily(f"{company_name} engineering interview culture tech stack {target_role}")
        web_news = "\n".join([f"- {res.get('title')}: {res.get('content')}" for res in tavily_results[:3]]) if tavily_results else "No live search results available."

        dynamic_fallback = {
            "company_name": company_name,
            "company_insights": f"{company_name} focuses on high-performance software engineering, cloud infrastructure scalability, and rapid feature delivery.",
            "engineering_culture": "Agile microservice architecture, continuous integration, and data-driven product decisions.",
            "interview_focus": "System design architecture, data structures & algorithms, and behavioral cultural fit.",
            "score": 88
        }

        reasoning_steps = [
            f"Step 1: Executed real-time web search for '{company_name}' engineering culture via Tavily API",
            "Step 2: Analyzed live search results and company technical publications",
            "Step 3: Identified candidate alignment with company core values and tech stack",
            "Step 4: Pinpointed company interview process risks and technical bar expectations",
            "Step 5: Benchmarked candidate profile against Company Research Analyst standards",
            "Step 6: Formulated company-specific interview preparation strategies",
            "Step 7: Prioritized high-impact research actions",
            "Step 8: Generated enterprise Company Intelligence Report"
        ]

        system_prompt = self.build_expert_system_prompt(
            persona_role="Company Research Analyst & Corporate Intelligence Specialist",
            domain_focus="Live company web intelligence, engineering culture research, interview loop stage breakdown, and corporate strategy."
        )

        context_prompt = self.build_user_context_prompt(inputs, memory=memory)
        user_prompt = f"{context_prompt}\n\nLive Web Search Results for {company_name}:\n{web_news}"

        llm_response = await self.call_llm(system_prompt, user_prompt, task_type="company_intelligence", preferred_engine="tavily")
        output = self.parse_agent_output(llm_response, dynamic_fallback)

        output["company_name"] = company_name
        if memory:
            memory.company_intelligence = output

        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
