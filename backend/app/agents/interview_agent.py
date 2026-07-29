from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent

class InterviewAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="interview_intelligence",
            name="Interview Intelligence Agent",
            description="Generates tailored technical and HR interview questions with sample STAR-method answers based on target role.",
            icon="MessageSquare"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[Any] = None) -> Dict[str, Any]:
        target_role = memory.target_role if memory else "Software Engineer"
        missing_skills = memory.get_missing_skills() if memory else []

        reasoning_steps = [
            "Analyzed candidate experience and target role requirements",
            "Synthesized technical and behavioral STAR interview questions with sample answers"
        ]

        dynamic_fallback = {
            "readiness_score": 80,
            "technical_questions": [
                {
                    "question": f"How do you design high-availability backend APIs for {target_role} applications?",
                    "sample_answer": "I use asynchronous frameworks like FastAPI, modular database pooling, redis caching, and horizontal pod scaling."
                },
                {
                    "question": "Walk me through how you optimize slow SQL/NoSQL database queries.",
                    "sample_answer": "I analyze query execution plans, create compound indexes, and implement query caching using Redis."
                },
                {
                    "question": "How do you manage state management in complex React applications?",
                    "sample_answer": "I leverage React Context for global state, custom hooks for reusable logic, and React Query for server-side state synchronization."
                }
            ],
            "hr_questions": [
                {
                    "question": "Tell me about a time you had to deliver a critical feature under tight deadlines.",
                    "sample_answer": "Situation: Tight product release. Task: Deliver core MVP API. Action: Prioritized essential endpoints and automated tests. Result: Launched on time."
                },
                {
                    "question": "How do you handle technical disagreements with team members during code reviews?",
                    "sample_answer": "I focus on empirical benchmark data, maintain open communication, and evaluate solutions based on scalability and maintainability."
                }
            ]
        }

        system_prompt = (
            "You are a Principal Software Engineering Interviewer. Generate 3 Technical and 2 HR interview questions with sample STAR answers. "
            "Return JSON ONLY with keys:\n"
            "- 'readiness_score': int (0-100)\n"
            "- 'technical_questions': list of 3 dicts with 'question' and 'sample_answer'\n"
            "- 'hr_questions': list of 2 dicts with 'question' and 'sample_answer'"
        )

        user_prompt = f"Target Role: {target_role}\nTarget Focus Areas / Gaps: {missing_skills}"
        llm_response = await self.call_llm(system_prompt, user_prompt)
        output = self.parse_json_safely(llm_response, dynamic_fallback)

        if memory:
            memory.interview_prep = output

        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
