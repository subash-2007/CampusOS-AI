from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent

class CommunicationAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="communication_intelligence",
            name="Communication Intelligence Agent",
            description="Drafts personalized recruiter cold emails, LinkedIn connection notes, and custom cover letters.",
            icon="Send"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[Any] = None) -> Dict[str, Any]:
        company_name = memory.company_name if memory else "Target Enterprise"
        target_role = memory.target_role if memory else "Software Engineer"
        candidate_skills = memory.get_candidate_skills() if memory else ["Full-Stack Engineering"]

        reasoning_steps = [
            "Analyzed candidate experience and target company specs",
            "Generated high-converting recruiter cold email, LinkedIn note, and targeted cover letter"
        ]

        dynamic_fallback = {
            "recruiter_email": f"Subject: Application for {target_role} - {', '.join(candidate_skills[:2])}\n\nHi Hiring Team,\n\nI have been following {company_name}'s recent technical developments and wanted to express my enthusiasm for the {target_role} role. With experience building scalable applications using {', '.join(candidate_skills[:3])}, I am confident I can bring immediate value to your engineering team.\n\nAttached is my resume for your review.\n\nBest regards,\nCandidate",
            "linkedin_message": f"Hi [Recruiter Name], I noticed you lead technical hiring for {target_role} roles at {company_name}. I recently built a full-stack production application matching your tech stack. Would love to connect and share more!",
            "cover_letter": f"Dear Hiring Manager,\n\nI am writing to formally apply for the {target_role} position at {company_name}. Throughout my academic and project engineering experience, I have developed expertise in {', '.join(candidate_skills[:4])}. I am impressed by {company_name}'s dedication to engineering quality and would welcome the opportunity to discuss how my background aligns with your goals.\n\nSincerely,\nCandidate"
        }

        system_prompt = (
            "You are an Executive Communication & Career Coach. Draft recruiter outreach messages. "
            "Return JSON ONLY with keys:\n"
            "- 'recruiter_email': str (Full cold email template)\n"
            "- 'linkedin_message': str (Short LinkedIn connection note <300 chars)\n"
            "- 'cover_letter': str (3-paragraph tailored cover letter)"
        )

        user_prompt = f"Company: {company_name}\nTarget Role: {target_role}\nCandidate Skills: {candidate_skills}"
        llm_response = await self.call_llm(system_prompt, user_prompt)
        output = self.parse_json_safely(llm_response, dynamic_fallback)

        if memory:
            memory.communication_templates = output

        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
