from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from app.nlp import extract_skills_from_text, extract_key_phrases

class JobIntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="job_intelligence",
            name="Job Intelligence Agent",
            description="Deconstructs Job Descriptions into core domain requirements, tech stacks, seniority signals, and unspoken expectations.",
            icon="Briefcase"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[Any] = None) -> Dict[str, Any]:
        job_desc = inputs.get("job_description_text", "") or (memory.job_description_text if memory else "")
        target_role = inputs.get("target_role", "") or (memory.target_role if memory else "")

        reasoning_steps = [
            "Deconstructed Job Description taxonomy & role requirements",
            "Extracted required technical stack & domain key phrases",
            "Assessed seniority indicators and candidate profile expectations"
        ]

        # Dynamic Extraction
        extracted_skills = extract_skills_from_text(job_desc)
        key_phrases = extract_key_phrases(job_desc, 10)

        # Seniority signals
        text_lower = job_desc.lower()
        if any(w in text_lower for w in ["senior", "lead", "principal", "5+ years", "7+ years"]):
            seniority = "Senior / Lead (5+ YOE)"
        elif any(w in text_lower for w in ["mid", "3+ years", "2+ years"]):
            seniority = "Mid-Level (2-4 YOE)"
        else:
            seniority = "Junior / Entry-Level / Student (0-2 YOE)"

        role_title = target_role or (key_phrases[0] if key_phrases else "Software Engineer")

        dynamic_data = {
            "role_title": role_title,
            "seniority_level": seniority,
            "required_skills": extracted_skills if extracted_skills else key_phrases[:6],
            "preferred_skills": key_phrases[6:] if len(key_phrases) > 6 else ["Cloud Infrastructure", "System Architecture"],
            "key_responsibilities": [
                f"Develop and maintain high-quality features matching {role_title} requirements",
                "Participate in code reviews, technical architecture planning, and deployment pipelines",
                "Optimize performance, scalability, and system reliability"
            ],
            "domain_focus": f"{role_title} & Scalable Systems"
        }

        system_prompt = (
            "You are a Job Intelligence Analyst. Parse the Job Description and refine into JSON with keys: "
            "'role_title' (str), 'seniority_level' (str), 'required_skills' (list), 'preferred_skills' (list), "
            "'key_responsibilities' (list), 'domain_focus' (str)."
        )
        user_prompt = f"Job Description:\n{job_desc}\nDynamic Extracted Data:\n{dynamic_data}"
        llm_response = await self.call_llm(system_prompt, user_prompt)

        output = self.parse_json_safely(llm_response, dynamic_data)
        output["required_skills"] = dynamic_data["required_skills"]

        if memory:
            memory.job_analysis = output
            memory.log_step(self.agent_id, "Completed dynamic Job Description analysis", {"role": output["role_title"]})

        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
