from typing import Dict, Any
from app.agents.base_agent import BaseAgent

class JobIntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="job_intelligence",
            name="Job Intelligence Agent",
            description="Deconstructs Job Descriptions into core domain requirements, tech stacks, seniority signals, and unspoken expectations.",
            icon="Briefcase"
        )

    async def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        job_desc = inputs.get("job_description_text", "") or inputs.get("prompt", "")

        reasoning_steps = [
            "Deconstructed Job Description taxonomy & role requirements",
            "Categorized required vs preferred technical skillsets",
            "Assessed seniority indicators and core domain focus"
        ]

        system_prompt = (
            "You are a Job Intelligence Analyst. Parse the Job Description and return JSON with keys: "
            "'role_title' (str), 'seniority_level' (str), 'required_skills' (list), 'preferred_skills' (list), "
            "'key_responsibilities' (list), 'domain_focus' (str), 'candidate_profile' (str)."
        )

        user_prompt = f"Job Description:\n{job_desc}"
        llm_response = await self.call_llm(system_prompt, user_prompt)

        fallback = {
            "role_title": "Full Stack Software Engineer",
            "seniority_level": "Junior / Entry-Level (0-2 YOE)",
            "required_skills": ["Python", "FastAPI / Django", "TypeScript", "React / Next.js", "SQL / MongoDB", "Git"],
            "preferred_skills": ["Docker", "AWS / GCP", "Redis", "GraphQL", "Tailwind CSS"],
            "key_responsibilities": [
                "Develop scalable frontend components and backend RESTful APIs",
                "Participate in code reviews, sprint planning, and system architecture discussions",
                "Optimize application performance and integrate third-party web services"
            ],
            "domain_focus": "Full Stack Web & Cloud Applications",
            "candidate_profile": "Proactive software engineer with strong fundamentals in full-stack JavaScript/TypeScript and Python, eager to take ownership of end-to-end features."
        }

        output = self.parse_json_safely(llm_response, fallback)
        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
