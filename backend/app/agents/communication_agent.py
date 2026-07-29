from typing import Dict, Any
from app.agents.base_agent import BaseAgent

class CommunicationAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="communication_intelligence",
            name="Communication Intelligence Agent",
            description="Drafts personalized recruiter cold emails, LinkedIn connection requests, follow-up notes, and salary negotiation scripts.",
            icon="Send"
        )

    async def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        comm_type = inputs.get("type", "cold_email")
        company_name = inputs.get("company_name", "Tech Global")
        recipient_role = inputs.get("recipient_role", "Engineering Manager")
        key_highlights = inputs.get("key_highlights", "Full Stack Software Engineer skilled in Next.js, FastAPI, and Cloud Architecture")

        reasoning_steps = [
            f"Tailored outreach messaging strategy for target recipient '{recipient_role}' at '{company_name}'",
            "Structured high-conversion value proposition & call-to-action",
            "Generated professional communication templates across multi-channel touchpoints"
        ]

        system_prompt = (
            "You are an Executive Tech Recruiter & Communication Strategist. Return JSON with keys: "
            "'subject_line' (str), 'body_text' (str), 'linkedin_inmail' (str), "
            "'follow_up_note' (str), 'salary_negotiation_script' (str), 'pro_tips' (list)."
        )

        user_prompt = f"Type: {comm_type}, Company: {company_name}, Recipient: {recipient_role}, Highlights: {key_highlights}"
        llm_response = await self.call_llm(system_prompt, user_prompt)

        fallback = {
            "subject_line": f"Full-Stack Engineer with Next.js/FastAPI experience - Passionate about {company_name}'s Engineering Growth",
            "body_text": f"Hi {recipient_role},\n\nI’ve been following {company_name}’s impressive engineering work, particularly your focus on scalable web products. As a Software Engineer specializing in Next.js, TypeScript, and FastAPI backends, I recently built a full-stack platform processing concurrent data with 99.8% uptime.\n\nI’d love to briefly connect for 10 minutes to learn more about upcoming engineering initiatives on your team.\n\nBest regards,\nCandidate",
            "linkedin_inmail": f"Hi! Inspired by {company_name}'s tech stack. I'm a Full Stack Engineer (Next.js/FastAPI/Python) eager to contribute to high-impact projects. Would love to connect!",
            "follow_up_note": f"Hi {recipient_role},\n\nFollowing up on my previous message. I recently published an open-source project showcasing microservice architecture and wanted to share a quick link. Looking forward to connecting when convenient!",
            "salary_negotiation_script": f"Thank you so much for extending this offer to join {company_name}! Based on my full-stack skillset and market benchmark data for this role, I was hoping we could explore aligning the base compensation to $X. I am extremely enthusiastic about joining the team.",
            "pro_tips": [
                "Keep cold emails under 150 words for 3x higher response rates",
                "Send emails on Tuesday or Thursday mornings between 8:00 AM - 9:30 AM local time"
            ]
        }

        output = self.parse_json_safely(llm_response, fallback)
        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
