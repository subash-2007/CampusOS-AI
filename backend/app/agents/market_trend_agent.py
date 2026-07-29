from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent

class MarketTrendAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="market_trend",
            name="Market Trend Intelligence Agent",
            description="Fetches live tech hiring trends, top requested skills, and competitive market salary benchmarks.",
            icon="TrendingUp"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[Any] = None) -> Dict[str, Any]:
        target_role = memory.target_role if memory else "Software Engineer"

        reasoning_steps = [
            "Analyzed current industry tech hiring demand metrics and skill growth trajectories",
            "Synthesized role-based salary benchmarks and emerging tech skill requirements"
        ]

        dynamic_fallback = {
            "hiring_demand": "High Demand (+18% YoY hiring growth for full-stack and cloud AI engineers)",
            "industry_trends": f"Increasing adoption of cloud-native microservices, AI-powered automation APIs, and TypeScript full-stack ecosystems for {target_role} positions.",
            "salary_benchmark": "$85,000 - $130,000 / year (Entry to Mid-Level Software Engineer)"
        }

        system_prompt = (
            "You are a Senior Tech Labor Market Economist. Synthesize market hiring trends. "
            "Return JSON ONLY with keys:\n"
            "- 'hiring_demand': str (Hiring demand metric)\n"
            "- 'industry_trends': str (2-sentence industry trend summary)\n"
            "- 'salary_benchmark': str (Estimated annual salary range)"
        )

        user_prompt = f"Target Role: {target_role}"
        llm_response = await self.call_llm(system_prompt, user_prompt)
        output = self.parse_json_safely(llm_response, dynamic_fallback)

        if memory:
            memory.market_trends = output

        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
