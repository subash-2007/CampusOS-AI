from typing import Dict, Any
from app.agents.base_agent import BaseAgent

class InterviewAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="interview_intelligence",
            name="Interview Intelligence Agent",
            description="Generates custom technical & behavioral interview questions, evaluates STAR responses, and runs mock practice sessions.",
            icon="MessageSquare"
        )

    async def run(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        target_role = inputs.get("target_role", "") or inputs.get("prompt", "") or "Full Stack Developer"

        reasoning_steps = [
            "Generated role-specific technical & behavioral interview questions",
            "Structured model answers using STAR framework (Situation, Task, Action, Result)",
            "Prepared real-time practice evaluation criteria"
        ]

        system_prompt = (
            "You are an Interview Intelligence Coach. Create tailored interview questions and answers. Return JSON with keys: "
            "'technical_questions' (list of dicts with 'question', 'category', 'difficulty', 'model_answer', 'key_concepts'), "
            "'behavioral_questions' (list of dicts with 'question', 'star_breakdown', 'pro_tips'), "
            "'mock_scenario' (dict with 'role', 'interviewer_persona', 'initial_prompt')."
        )

        user_prompt = f"Role: {target_role}\nInputs: {inputs}"
        llm_response = await self.call_llm(system_prompt, user_prompt)

        fallback = {
            "technical_questions": [
                {
                    "question": "How does React's Virtual DOM reconciliation process work, and how do key props prevent re-rendering issues?",
                    "category": "Frontend Architecture",
                    "difficulty": "Medium",
                    "model_answer": "React creates a lightweight in-memory representation of the real DOM. During state changes, React runs a diffing algorithm (Reconciliation) between the new Virtual DOM and previous snapshot. Keys allow React to track list items across updates efficiently without re-mounting identical DOM nodes.",
                    "key_concepts": ["Virtual DOM", "Diffing Algorithm", "Keys", "Component Lifecycle"]
                },
                {
                    "question": "Explain the difference between synchronous and asynchronous database queries in FastAPI using Motor/AsyncIO.",
                    "category": "Backend Systems",
                    "difficulty": "Medium",
                    "model_answer": "Synchronous queries block the main event loop thread while waiting for I/O operations, preventing other requests from processing. Asynchronous queries using `await` yield control back to Python's event loop, allowing hundreds of concurrent requests to execute on a single process thread.",
                    "key_concepts": ["Event Loop", "Non-blocking I/O", "Async/Await", "Concurrency"]
                }
            ],
            "behavioral_questions": [
                {
                    "question": "Tell me about a time you encountered a severe production bug or critical project blocker right before a deadline. How did you handle it?",
                    "star_breakdown": {
                        "Situation": "3 hours prior to campus project demo, API latency spiked to 4 seconds.",
                        "Task": "Identify root cause and restore sub-200ms response time immediately.",
                        "Action": "Profiled DB queries using logging, discovered unindexed MongoDB collection lookup, added compound index.",
                        "Result": "Reduced latency to 85ms and successfully delivered project on time with 100% uptime."
                    },
                    "pro_tips": "Focus 60% of your answer on the Action and measurable Result steps."
                }
            ],
            "mock_scenario": {
                "role": target_role,
                "interviewer_persona": "Senior Lead Engineer focusing on technical depth and problem-solving clarity",
                "initial_prompt": "Welcome! To start off, could you walk me through the architecture of a full-stack project you recently built and what key technical decisions you made?"
            }
        }

        output = self.parse_json_safely(llm_response, fallback)
        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
