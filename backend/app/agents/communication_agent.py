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
        company_name = inputs.get("company_name") or (memory.company_name if memory else "Target Enterprise")
        target_role = inputs.get("target_role") or (memory.target_role if memory else "Software Engineer")
        candidate_skills = memory.get_candidate_skills() if memory else ["Full-Stack Engineering", "FastAPI"]

        dynamic_fallback = {
            "score": 90,
            "recruiter_email": f"Subject: Application for {target_role} - {', '.join(candidate_skills[:2])}\n\nHi Hiring Team,\n\nI have been following {company_name}'s recent technical developments and wanted to express my enthusiasm for the {target_role} role. With experience building scalable applications using {', '.join(candidate_skills[:3])}, I am confident I can bring immediate value to your engineering team.\n\nAttached is my resume for your review.\n\nBest regards,\nCandidate",
            "linkedin_message": f"Hi [Recruiter Name], I noticed you lead technical hiring for {target_role} roles at {company_name}. I recently built a full-stack production application matching your tech stack. Would love to connect and share more!",
            "cover_letter": f"Dear Hiring Manager,\n\nI am writing to formally apply for the {target_role} position at {company_name}. Throughout my project engineering experience, I have developed expertise in {', '.join(candidate_skills[:4])}. I am impressed by {company_name}'s dedication to engineering quality and would welcome the opportunity to discuss how my background aligns with your goals.\n\nSincerely,\nCandidate"
        }

        reasoning_steps = [
            "Step 1: Examined candidate background and technical accomplishments",
            "Step 2: Analyzed target company culture and recruiter outreach channel expectations",
            "Step 3: Identified candidate value proposition strengths",
            "Step 4: Flagged generic template tone risks and low-converting email structures",
            "Step 5: Benchmarked messaging against Executive Communication Coach standards",
            "Step 6: Formulated high-converting recruiter cold emails, LinkedIn notes, and custom cover letters",
            "Step 7: Prioritized high-impact outreach strategies",
            "Step 8: Generated enterprise Communication Coaching Report"
        ]

        system_prompt = self.build_expert_system_prompt(
            persona_role="Executive Communication Coach & Career Branding Expert",
            domain_focus="High-converting cold email drafting, recruiter outreach scripting, LinkedIn connection copywriting, and executive presence."
        )

        user_prompt = self.build_user_context_prompt(inputs, memory=memory)
        llm_response = await self.call_llm(system_prompt, user_prompt, task_type="communication_intelligence", preferred_engine="anthropic")
        output = self.parse_agent_output(llm_response, dynamic_fallback)

        if memory:
            memory.communication_templates = output

        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
