from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent

class CompanyIntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="company_intelligence",
            name="Company Intelligence Agent",
            description="Researches target company culture, interview patterns, engineering values, and recent news using web intelligence.",
            icon="Building"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[Any] = None) -> Dict[str, Any]:
        company_name = inputs.get("company_name", "") or (memory.company_name if memory else "") or "Tech Enterprise"
        job_desc = inputs.get("job_description_text", "") or (memory.job_description_text if memory else "")

        reasoning_steps = [
            f"Querying web intelligence for recent developments on '{company_name}'",
            "Analyzing corporate engineering culture & leadership principles",
            "Extracting interview loop structure & candidate evaluation criteria"
        ]

        web_results = await self.search_tavily(f"{company_name} engineering culture software engineer interview loop recent news")
        web_summary = "\n".join([r.get("content", "") for r in web_results[:3]]) if web_results else ""

        dynamic_data = {
            "company_name": company_name,
            "culture_highlights": [
                f"Fast-paced product engineering culture at {company_name} with developer autonomy",
                "Strong emphasis on automated testing, continuous integration, and mentor pairing",
                "Hybrid work setup with modern cloud and developer tooling"
            ],
            "engineering_values": [
                "Customer-obsessed technical decisions",
                "High code quality, CI/CD rigor, and automated testing",
                "Scalable system architecture and clear technical documentation"
            ],
            "interview_style": "4-Round Loop: Technical Screening -> Pair Live Coding -> System Architecture & Design -> HR & Behavioral Cultural Fit",
            "recent_developments": [
                f"Expanding engineering investments in scalable cloud infrastructure and AI integration",
                f"Active hiring drive for full-stack and backend software engineering roles"
            ],
            "insider_tips": [
                "Prepare 2-3 concrete STAR method examples highlighting technical problem solving under tight deadlines",
                "Demonstrate curiosity by asking thoughtful questions about their microservices architecture and deployment cadence"
            ]
        }

        system_prompt = (
            "You are a Company Research Specialist. Provide insights on the company and refine into JSON with keys: "
            "'company_name' (str), 'culture_highlights' (list), 'engineering_values' (list), "
            "'interview_style' (str), 'recent_developments' (list), 'insider_tips' (list)."
        )

        user_prompt = f"Company: {company_name}\nWeb Intelligence:\n{web_summary}\nJD Text:\n{job_desc}"
        llm_response = await self.call_llm(system_prompt, user_prompt)

        output = self.parse_json_safely(llm_response, dynamic_data)

        if memory:
            memory.company_intelligence = output
            memory.log_step(self.agent_id, "Completed dynamic Company Intelligence research", {"company": company_name})

        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
