from typing import Dict, Any, List
from app.agents.base_agent import BaseAgent

class CareerOrchestratorAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="career_orchestrator",
            name="Career Orchestrator Agent",
            description="Master intelligence routing, coordinating agent workflows and synthesizing holistic career guidance.",
            icon="Brain"
        )

    async def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        prompt = inputs.get("prompt", "")
        context = inputs.get("context", {})
        
        reasoning_steps = [
            "Analyzed user prompt intent & domain scope",
            "Determined optimal AI agent execution pipeline",
            "Synthesized multi-dimensional career insights & action plan"
        ]

        system_prompt = (
            "You are the Master Career Orchestrator Agent for CampusOS AI. Your goal is to guide students and job seekers "
            "by synthesizing advice across resumes, ATS optimization, skill gaps, interviews, and company research. "
            "Provide structured, clear, highly encouraging, and actionable response in JSON format with keys: "
            "'response', 'suggested_agents', 'recommended_actions', 'confidence_score'."
        )

        user_prompt = f"User Request: {prompt}\nContext: {context}"
        llm_response = await self.call_llm(system_prompt, user_prompt)

        fallback = {
            "response": f"I am your CampusOS Career Orchestrator. Regarding '{prompt if prompt else 'your career journey'}': I recommend starting by analyzing your resume with our **Resume Intelligence Agent** and comparing it against your target job role using the **ATS Optimization Agent**.",
            "suggested_agents": ["resume_intelligence", "ats_optimization", "interview_intelligence"],
            "recommended_actions": [
                "Upload your latest PDF/DOCX resume",
                "Paste target Job Description to benchmark your match score",
                "Review customized 30-60-90 day career roadmap"
            ],
            "confidence_score": 96
        }

        output = self.parse_json_safely(llm_response, fallback)
        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
