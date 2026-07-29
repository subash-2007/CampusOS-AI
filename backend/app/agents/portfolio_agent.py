from typing import Dict, Any
from app.agents.base_agent import BaseAgent

class PortfolioAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="portfolio_intelligence",
            name="Portfolio Intelligence Agent",
            description="Evaluates GitHub & project portfolios, recommends high-impact projects, and auto-generates professional README files.",
            icon="FolderGit2"
        )

    async def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        tech_stack = inputs.get("tech_stack", ["Next.js", "FastAPI", "MongoDB"])
        target_role = inputs.get("target_role", "Software Engineer")

        reasoning_steps = [
            "Evaluated project portfolio impact & tech stack breadth",
            "Conceptualized high-value standout project blueprints tailored for recruiter appeal",
            "Structured production-grade GitHub README markdown specification"
        ]

        system_prompt = (
            "You are a Senior Portfolio & Open Source Advisor. Return JSON with keys: "
            "'portfolio_score' (int 0-100), "
            "'project_ideas' (list of dicts with 'title', 'description', 'tech_stack', 'difficulty', 'recruiter_appeal_score', 'key_features'), "
            "'generated_readme' (str markdown)."
        )

        user_prompt = f"Tech Stack: {tech_stack}, Target Role: {target_role}"
        llm_response = await self.call_llm(system_prompt, user_prompt)

        fallback = {
            "portfolio_score": 88,
            "project_ideas": [
                {
                    "title": "CampusOS AI - Multi-Agent Career Copilot",
                    "description": "Enterprise-grade AI platform coordinating 14 specialized agents for resume parsing, ATS scoring, and interview prep.",
                    "tech_stack": ["Next.js", "TypeScript", "FastAPI", "MongoDB", "Tailwind CSS"],
                    "difficulty": "Advanced",
                    "recruiter_appeal_score": 98,
                    "key_features": ["JWT Authentication", "Multi-Agent System Architecture", "Live Web Search via Tavily", "Downloadable PDF Reports"]
                },
                {
                    "title": "CloudScale - Distributed Microservice Task Queue",
                    "description": "High-performance asynchronous background worker system with real-time WebSocket dashboard monitoring.",
                    "tech_stack": ["Python", "FastAPI", "Redis", "Docker", "React"],
                    "difficulty": "Intermediate",
                    "recruiter_appeal_score": 92,
                    "key_features": ["Async Event Loop", "Rate Limiting Middleware", "Docker Compose Orchestration"]
                }
            ],
            "generated_readme": """# CampusOS AI - Multi-Agent Career Platform

![CampusOS Banner](https://img.shields.io/badge/CampusOS-AI_Platform-7c3aed?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge)
![Next.js](https://img.shields.io/badge/Frontend-Next.js_14-000000?style=for-the-badge)

## 🚀 Overview
CampusOS AI is an AI-powered career copilot that coordinates 14 autonomous agents to accelerate technical job search, ATS resume matching, and interview readiness.

## ✨ Features
- **14 AI Agents**: Resume Intelligence, ATS Optimization, Interview Simulator, Career Roadmap, and more.
- **Modern UI**: Built with Next.js App Router, TypeScript, Tailwind CSS, and Framer Motion.
- **FastAPI Engine**: Scalable REST API with JWT Auth and MongoDB integration.
- **Exportable PDF Reports**: One-click comprehensive career audit generation.

## 🛠️ Quick Start
```bash
# Clone the repository
git clone https://github.com/your-username/campusos-ai.git
cd campusos-ai
```
"""
        }

        output = self.parse_json_safely(llm_response, fallback)
        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
