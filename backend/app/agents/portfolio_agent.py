from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent

class PortfolioAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="portfolio_intelligence",
            name="Portfolio Intelligence Agent",
            description="Evaluates GitHub & project portfolios, recommends high-impact projects, and auto-generates professional README files.",
            icon="FolderGit2"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[Any] = None) -> Dict[str, Any]:
        candidate_skills = memory.get_candidate_skills() if memory else ["Next.js", "FastAPI", "Python", "MongoDB"]
        target_role = memory.get_target_role() if memory else "Software Engineer"
        missing_skills = memory.get_missing_skills() if memory else ["Docker", "AWS"]

        reasoning_steps = [
            "Evaluated candidate project portfolio & tech stack breadth",
            "Conceptualized recruiter-magnet project blueprints addressing skill gaps",
            "Generated production GitHub README markdown specification"
        ]

        main_stack = candidate_skills[:4] if candidate_skills else ["Python", "FastAPI", "React", "MongoDB"]
        gap_skill = missing_skills[0] if missing_skills else "Cloud Architecture"

        dynamic_projects = [
            {
                "title": f"Production {target_role} Core Engine",
                "description": f"Full-stack scalable application built with {', '.join(main_stack[:3])} integrating {gap_skill}.",
                "tech_stack": main_stack + [gap_skill],
                "difficulty": "Advanced",
                "recruiter_appeal_score": 95,
                "key_features": ["JWT Authentication & Role Security", "Asynchronous Microservice Task Processing", "Automated Testing & CI/CD Pipelines"]
            }
        ]

        generated_readme = f"""# {target_role} Production Portfolio Project

![Build Status](https://img.shields.io/badge/Build-Passing-10b981?style=for-the-badge)
![Tech Stack](https://img.shields.io/badge/Stack-{'-'.join(main_stack[:3])}-7c3aed?style=for-the-badge)

## 🚀 Overview
High-performance full-stack application built for production workloads, featuring modern engineering best practices, modular architecture, and automated API documentation.

## 🛠️ Tech Stack
- **Frontend**: {main_stack[0] if len(main_stack)>0 else 'React/Next.js'}
- **Backend**: {main_stack[1] if len(main_stack)>1 else 'FastAPI/Python'}
- **Database**: {main_stack[2] if len(main_stack)>2 else 'MongoDB/PostgreSQL'}
- **Infrastructure**: {gap_skill}

## ⚡ Key Highlights
- Asynchronous non-blocking architecture processing concurrent API requests.
- End-to-end type safety, structured logging, and comprehensive unit tests.
- Docker containerization for seamless cloud deployment.
"""

        dynamic_data = {
            "portfolio_score": 88,
            "project_ideas": dynamic_projects,
            "generated_readme": generated_readme
        }

        system_prompt = (
            "You are a Senior Portfolio & Open Source Advisor. Return JSON with keys: "
            "'portfolio_score' (int), 'project_ideas' (list of dicts), 'generated_readme' (str)."
        )
        user_prompt = f"Candidate Stack: {main_stack}\nMissing Skill: {gap_skill}\nDynamic Data:\n{dynamic_data}"
        llm_response = await self.call_llm(system_prompt, user_prompt)

        output = self.parse_json_safely(llm_response, dynamic_data)

        if memory:
            memory.portfolio_recommendations = output
            memory.log_step(self.agent_id, "Completed dynamic Portfolio Analysis", {"score": output.get("portfolio_score", 88)})

        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
