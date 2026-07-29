from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from app.nlp import extract_skills_from_text

class InterviewAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="interview_intelligence",
            name="Interview Intelligence Agent",
            description="Generates custom technical & behavioral interview questions, evaluates STAR responses, and runs mock practice sessions.",
            icon="MessageSquare"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[Any] = None) -> Dict[str, Any]:
        target_role = inputs.get("target_role", "") or (memory.get_target_role() if memory else "Full Stack Software Engineer")
        candidate_skills = memory.get_candidate_skills() if memory else []
        missing_skills = memory.get_missing_skills() if memory else []

        reasoning_steps = [
            f"Generated role-specific technical & behavioral interview questions for '{target_role}'",
            "Synthesized model answers using STAR framework based on candidate's actual skills",
            "Prepared customized technical screening criteria"
        ]

        skill_1 = candidate_skills[0] if candidate_skills else "Python/TypeScript"
        skill_2 = candidate_skills[1] if len(candidate_skills) > 1 else "REST APIs"
        missing_1 = missing_skills[0] if missing_skills else "Docker/Cloud Infrastructure"

        dynamic_questions = [
            {
                "question": f"How do you optimize performance and manage state when building applications with {skill_1} and {skill_2}?",
                "category": f"{target_role} Architecture",
                "difficulty": "Medium",
                "model_answer": f"When building with {skill_1}, performance optimization involves minimizing blocking I/O, utilizing efficient data structures, and implementing caching layers. For {skill_2}, structuring clean modular endpoints prevents unnecessary database query overhead.",
                "key_concepts": [skill_1, skill_2, "Performance Optimization", "System Architecture"]
            },
            {
                "question": f"Have you used {missing_1} in production or personal projects? How would you integrate it into a microservices pipeline?",
                "category": "Cloud & Infrastructure",
                "difficulty": "Medium",
                "model_answer": f"Integrating {missing_1} ensures reproducible container environments and smooth CI/CD deployments. By defining declarative configuration scripts, services can auto-scale and maintain high availability.",
                "key_concepts": [missing_1, "CI/CD Pipelines", "Containerization", "Scalability"]
            }
        ]

        behavioral_questions = [
            {
                "question": f"Walk me through a complex technical challenge you faced while building a project involving {skill_1}. How did you resolve it?",
                "star_breakdown": {
                    "Situation": f"Spiked latency and unexpected API response failures during peak testing.",
                    "Task": "Identify root cause and restore sub-100ms response time immediately.",
                    "Action": f"Profiled application code, optimized queries, and refactored {skill_1} async functions.",
                    "Result": "Reduced latency by 45% and ensured stable 99.9% uptime."
                },
                "pro_tips": "Focus 60% of your response time on the specific Action and quantifiable Result steps."
            }
        ]

        dynamic_data = {
            "technical_questions": dynamic_questions,
            "behavioral_questions": behavioral_questions,
            "mock_scenario": {
                "role": target_role,
                "interviewer_persona": "Senior Lead Engineer focusing on technical depth and problem-solving clarity",
                "initial_prompt": f"Welcome! To start off, could you walk me through your experience with {skill_1} and how you structured your recent projects?"
            }
        }

        system_prompt = (
            "You are an Interview Intelligence Coach. Create tailored interview questions and answers in JSON format with keys: "
            "'technical_questions' (list of dicts), 'behavioral_questions' (list of dicts), 'mock_scenario' (dict)."
        )
        user_prompt = f"Candidate Skills: {candidate_skills}\nTarget Role: {target_role}\nMissing Skills: {missing_skills}\nDynamic Data:\n{dynamic_data}"
        llm_response = await self.call_llm(system_prompt, user_prompt)

        output = self.parse_json_safely(llm_response, dynamic_data)

        if memory:
            memory.interview_prep = output
            memory.log_step(self.agent_id, "Completed dynamic Interview Question generation", {"questions_count": len(output.get("technical_questions", []))})

        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
