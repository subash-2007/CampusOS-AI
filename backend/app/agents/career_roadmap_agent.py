from typing import Dict, Any
from app.agents.base_agent import BaseAgent

class CareerRoadmapAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="career_roadmap",
            name="Career Roadmap Agent",
            description="Generates actionable 30-60-90 day strategic execution plans, skill milestones, and target role progression.",
            icon="Compass"
        )

    async def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        target_role = inputs.get("target_role", "") or inputs.get("prompt", "") or "Full Stack Engineer"

        reasoning_steps = [
            "Structured multi-phase execution strategy (Days 1-30, 31-60, 61-90)",
            "Defined high-value portfolio milestones & resume target checkpoints",
            "Calculated market trajectory & target compensation ranges"
        ]

        system_prompt = (
            "You are a Strategic Career Roadmap Planner. Return JSON with keys: "
            "'target_role' (str), 'career_trajectory' (str), 'expected_salary_range' (str), "
            "'milestones' (list of dicts with 'phase', 'title', 'duration', 'goals', 'deliverables', 'key_metrics')."
        )

        user_prompt = f"Target Role: {target_role}"
        llm_response = await self.call_llm(system_prompt, user_prompt)

        fallback = {
            "target_role": target_role,
            "career_trajectory": "Junior Software Engineer -> Full Stack Developer -> Senior Architect / Tech Lead",
            "expected_salary_range": "$85,000 - $115,000 / year (Entry/Junior Level)",
            "milestones": [
                {
                    "phase": "Days 1 - 30",
                    "title": "Foundation & Skill Gap Blitz",
                    "duration": "Month 1",
                    "goals": [
                        "Master Next.js App Router and FastAPI production patterns",
                        "Build 1 production-grade full-stack project with authentication & DB",
                        "Optimize resume to 85%+ ATS score format"
                    ],
                    "deliverables": [
                        "Published GitHub repository with clean documentation",
                        "Validated ATS-compliant PDF resume",
                        "Completed 20 LeetCode Medium data structure problems"
                    ],
                    "key_metrics": "Resume ATS score >= 85%, 1 deployed live project"
                },
                {
                    "phase": "Days 31 - 60",
                    "title": "Portfolio Amplification & Outreach",
                    "duration": "Month 2",
                    "goals": [
                        "Integrate AI agent capabilities / third-party API into portfolio app",
                        "Launch targeted LinkedIn recruiter outreach campaign (15 messages/week)",
                        "Conduct 5 mock interview sessions with STAR responses"
                    ],
                    "deliverables": [
                        "Deployed full-stack app on Vercel/Render with custom domain",
                        "30 customized cold emails/LinkedIn applications submitted",
                        "Refined 5 STAR stories for behavioral interviews"
                    ],
                    "key_metrics": "5+ recruiter responses, 3 initial phone screens"
                },
                {
                    "phase": "Days 61 - 90",
                    "title": "Interview Execution & Offer Negotiation",
                    "duration": "Month 3",
                    "goals": [
                        "Ace technical coding assessments and system design loops",
                        "Execute final round onsite/virtual interviews",
                        "Negotiate job offers with target market benchmarks"
                    ],
                    "deliverables": [
                        "Completion of 3+ full interview loops",
                        "Offer evaluation matrix & counter-offer scripts",
                        "Signed offer letter for target software engineering role"
                    ],
                    "key_metrics": "1-2 formal job offers, successful contract execution"
                }
            ]
        }

        output = self.parse_json_safely(llm_response, fallback)
        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
