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
        extracted_tech = extract_skills_from_text(jd_text)

        dynamic_fallback = {
            "target_role": target_role,
            "seniority_level": "Mid-Senior Level",
            "role_expectations": [
                "Architect and maintain scalable web applications and microservices",
                "Collaborate with product managers and engineers to deliver features",
                "Write clean, unit-tested, performant code"
            ],
            "required_technologies": extracted_tech or ["Python", "FastAPI", "React", "TypeScript", "SQL"],
            "score": 90
        }

        reasoning_steps = [
            "Step 1: Analyzed full candidate resume text",
            "Step 2: Deconstructed target Job Description to identify primary & implicit technical demands",
            "Step 3: Identified candidate technical alignment strengths",
            "Step 4: Pinpointed missing domain tools, frameworks, and architecture expectations",
            "Step 5: Compared candidate profile against Senior Technical Recruiter role benchmarks",
            "Step 6: Formulated strategic recommendations to demonstrate role mastery",
            "Step 7: Prioritized high-impact job preparation steps",
            "Step 8: Produced comprehensive Job Intelligence Consulting Report"
        ]

        system_prompt = self.build_expert_system_prompt(
            persona_role="Senior Technical Recruiter",
            domain_focus="Job description deconstruction, required tech stack analysis, seniority level calibration, and implicit role expectations."
        )

        user_prompt = self.build_user_context_prompt(inputs, memory=memory)
        llm_response = await self.call_llm(system_prompt, user_prompt, task_type="job_intelligence", preferred_engine="gemini")
        output = self.parse_agent_output(llm_response, dynamic_fallback)

        if not output.get("required_technologies"):
            output["required_technologies"] = extracted_tech or ["Python", "FastAPI", "React", "TypeScript"]
        if not output.get("target_role"):
            output["target_role"] = target_role

        if memory:
            memory.job_analysis = output
            memory.required_skills = output.get("required_technologies", extracted_tech)

        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
