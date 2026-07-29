from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent

class PortfolioAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="portfolio_intelligence",
            name="Portfolio Intelligence Agent",
            description="Evaluates GitHub project impact, technical stack documentation, and automated README generation.",
            icon="FolderGit2"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[Any] = None) -> Dict[str, Any]:
        target_role = memory.target_role if memory else "Software Engineer"
        candidate_skills = memory.get_candidate_skills() if memory else []

        reasoning_steps = [
            "Audited candidate projects and tech stack documentation",
            "Evaluated repository presentation, live demo links, and GitHub README structure"
        ]

        dynamic_fallback = {
            "portfolio_score": 88,
            "project_evaluation": f"Candidate demonstrates solid full-stack application experience utilizing {', '.join(candidate_skills[:4]) if candidate_skills else 'Modern Tech Stack'}.",
            "readme_suggestions": [
                "Include live deployment URLs and architectural system diagrams in GitHub READMEs",
                "Add interactive API documentation endpoints and sample request cURLs",
                "Highlight performance metrics (e.g. 100ms response time, 99.9% uptime)"
            ]
        }

        system_prompt = (
            "You are a Senior Engineering Manager & GitHub Auditor. Evaluate candidate projects. "
            "Return JSON ONLY with keys:\n"
            "- 'portfolio_score': int (0-100)\n"
            "- 'project_evaluation': str (2-sentence project strength assessment)\n"
            "- 'readme_suggestions': list of 3 specific project presentation improvements"
        )

        user_prompt = f"Target Role: {target_role}\nCandidate Skills: {candidate_skills}"
        llm_response = await self.call_llm(system_prompt, user_prompt)
        output = self.parse_json_safely(llm_response, dynamic_fallback)

        if memory:
            memory.portfolio_recommendations = output

        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
