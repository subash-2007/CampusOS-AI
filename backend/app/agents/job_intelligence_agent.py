from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from app.nlp import extract_skills_from_text

class JobIntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="job_intelligence",
            name="Job Intelligence Agent",
            description="Deconstructs Job Descriptions into core domain requirements, target tech stacks, and engineering expectations.",
            icon="Briefcase"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[Any] = None) -> Dict[str, Any]:
        jd_text = inputs.get("job_description_text", "") or (memory.job_description_text if memory else "")
        target_role = inputs.get("target_role", "") or (memory.target_role if memory else "Software Engineer")

        reasoning_steps = [
            "Parsed Job Description body for tech stack requirements",
            "Extracted domain expectations, team structure signals, and seniority level"
        ]

        extracted_tech = extract_skills_from_text(jd_text)

        dynamic_fallback = {
            "target_role": target_role,
            "seniority_level": "Mid-Senior Level",
            "role_expectations": [
                "Architect and maintain scalable web applications and microservices",
                "Collaborate with product managers and engineers to deliver features",
                "Write clean, unit-tested, performant code"
            ],
            "required_technologies": extracted_tech or ["Python", "FastAPI", "React", "TypeScript", "SQL"]
        }

        system_prompt = (
            "You are a Technical Job Market Analyst. Deconstruct the Job Description into specific requirements. "
            "Return JSON ONLY with keys:\n"
            "- 'target_role': str\n"
            "- 'seniority_level': str (e.g. Entry Level, Mid Level, Senior)\n"
            "- 'role_expectations': list of 3 specific job responsibilities\n"
            "- 'required_technologies': list of strings (technologies/frameworks specified in JD)"
        )

        user_prompt = f"Target Role: {target_role}\nJob Description:\n{jd_text}"
        llm_response = await self.call_llm(system_prompt, user_prompt)
        output = self.parse_json_safely(llm_response, dynamic_fallback)

        if memory:
            memory.job_analysis = output
            memory.required_skills = output.get("required_technologies", extracted_tech)

        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
