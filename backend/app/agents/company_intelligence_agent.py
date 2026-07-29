from typing import Dict, Any
from app.agents.base_agent import BaseAgent

class CompanyIntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="company_intelligence",
            name="Company Intelligence Agent",
            description="Researches target company culture, interview patterns, engineering values, and recent news using web intelligence.",
            icon="Building"
        )

    async def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        company_name = inputs.get("company_name", "") or inputs.get("prompt", "") or "Tech Enterprise"
        
        reasoning_steps = [
            f"Querying web intelligence for recent news on '{company_name}'",
            "Analyzing corporate engineering culture & leadership principles",
            "Extracting interview loop structure & candidate evaluation criteria"
        ]

        # Tavily search query
        web_results = await self.search_tavily(f"{company_name} engineering culture software engineer interview recent news 2026")
        web_summary = "\n".join([r.get("content", "") for r in web_results[:3]]) if web_results else ""

        system_prompt = (
            "You are a Company Research Specialist. Provide insights on the company and return JSON with keys: "
            "'company_name' (str), 'culture_highlights' (list), 'engineering_values' (list), "
            "'interview_style' (str), 'recent_developments' (list), 'insider_tips' (list)."
        )

        user_prompt = f"Company: {company_name}\nWeb Intelligence:\n{web_summary}"
        llm_response = await self.call_llm(system_prompt, user_prompt)

        fallback = {
            "company_name": company_name,
            "culture_highlights": [
                "Fast-paced product innovation culture with emphasis on engineering autonomy",
                "Strong focus on continuous learning, mentor pairings, and cross-functional hackathons",
                "Hybrid-friendly work environment with robust developer tooling"
            ],
            "engineering_values": [
                "Customer-first engineering mindset",
                "High code quality, comprehensive automated testing, and CI/CD rigor",
                "Scalable system design and data privacy by design"
            ],
            "interview_style": "4-Round Loop: Tech Screening (Data Structures/Algorithms) -> System Architecture -> Live Pair Coding -> Cultural Fit & Leadership Principles",
            "recent_developments": [
                f"Expanded engineering investments in cloud automation and AI agent integration",
                f"Active hiring drive for full-stack and cloud software engineers"
            ],
            "insider_tips": [
                "Prepare 2-3 concrete STAR method examples highlighting technical problem solving under tight deadlines",
                "Demonstrate curiosity by asking thoughtful questions about their microservices architecture and release cadence"
            ]
        }

        output = self.parse_json_safely(llm_response, fallback)
        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
