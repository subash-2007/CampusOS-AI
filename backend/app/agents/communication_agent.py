from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent

class CommunicationAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="communication_intelligence",
            name="Communication Intelligence Agent",
            description="Drafts personalized recruiter cold emails, LinkedIn connection requests, follow-up notes, and salary negotiation scripts.",
            icon="Send"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[Any] = None) -> Dict[str, Any]:
        comm_type = inputs.get("type", "cold_email")
        company_name = inputs.get("company_name", "") or (memory.company_name if memory else "") or "Tech Global"
        recipient_role = inputs.get("recipient_role", "Engineering Manager")
        target_role = memory.get_target_role() if memory else "Software Engineer"
        candidate_skills = memory.get_candidate_skills() if memory else ["Next.js", "FastAPI", "Python"]

        reasoning_steps = [
            f"Tailored outreach messaging strategy for recipient '{recipient_role}' at '{company_name}'",
            "Structured high-conversion value proposition using candidate's actual skill stack",
            "Generated professional multi-channel communication templates"
        ]

        skills_str = ", ".join(candidate_skills[:3]) if candidate_skills else "Full Stack Software Engineering"

        dynamic_data = {
            "subject_line": f"{target_role} with {skills_str} experience - Excited about {company_name}'s Engineering Team",
            "body_text": f"Hi {recipient_role},\n\nI’ve been following {company_name}’s engineering work with great interest. As a {target_role} specializing in {skills_str}, I recently built high-throughput web applications with sub-100ms API response times.\n\nI’d love to connect for 10 minutes to learn more about upcoming engineering initiatives on your team.\n\nBest regards,\nCandidate",
            "linkedin_inmail": f"Hi! Inspired by {company_name}'s engineering vision. I'm a {target_role} skilled in {skills_str} eager to contribute to high-impact projects. Would love to connect!",
            "follow_up_note": f"Hi {recipient_role},\n\nFollowing up on my previous message regarding the {target_role} role at {company_name}. I recently published an open-source project showcasing microservice performance optimizations and would love to connect when convenient!",
            "salary_negotiation_script": f"Thank you so much for extending this offer to join {company_name}! Based on my technical skillset in {skills_str} and market benchmark data for this role, I was hoping we could explore aligning base compensation to $X. I am extremely enthusiastic about joining the team.",
            "pro_tips": [
                "Keep cold emails under 150 words for 3x higher response rates",
                "Send emails on Tuesday or Thursday mornings between 8:00 AM - 9:30 AM local time"
            ]
        }

        system_prompt = (
            "You are an Executive Tech Recruiter & Communication Strategist. Return JSON with keys: "
            "'subject_line' (str), 'body_text' (str), 'linkedin_inmail' (str), 'follow_up_note' (str), "
            "'salary_negotiation_script' (str), 'pro_tips' (list)."
        )

        user_prompt = f"Type: {comm_type}, Company: {company_name}, Recipient: {recipient_role}, Role: {target_role}\nDynamic Data:\n{dynamic_data}"
        llm_response = await self.call_llm(system_prompt, user_prompt)

        output = self.parse_json_safely(llm_response, dynamic_data)

        if memory:
            memory.communication_templates = output
            memory.log_step(self.agent_id, "Completed dynamic Communication Template generation", {"company": company_name})

        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
