from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent

class CareerRoadmapAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="career_roadmap",
            name="Career Roadmap Agent",
            description="Generates actionable 30-60-90 day strategic execution plans, skill milestones, and target role progression.",
            icon="Compass"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[Any] = None) -> Dict[str, Any]:
        target_role = inputs.get("target_role", "") or (memory.get_target_role() if memory else "Software Engineer")
        missing_skills = memory.get_missing_skills() if memory else []

        reasoning_steps = [
            f"Structured multi-phase career roadmap tailored for target role '{target_role}'",
            "Aligned learning milestones with candidate's identified skill gaps",
            "Calculated strategic deliverables & expected compensation trajectory"
        ]

        gap_1 = missing_skills[0] if missing_skills else "Cloud Deployment & Docker"
        gap_2 = missing_skills[1] if len(missing_skills) > 1 else "System Architecture & Caching"

        dynamic_milestones = [
            {
                "phase": "Days 1 - 30 (Month 1)",
                "title": f"Skill Gap Blitz: {gap_1}",
                "duration": "Month 1",
                "goals": [
                    f"Master core concepts and hands-on production labs for {gap_1}",
                    f"Incorporate {gap_1} into a full-stack portfolio project",
                    "Optimize resume bullet points to achieve 85%+ ATS match score"
                ],
                "deliverables": [
                    f"Published GitHub project repository utilizing {gap_1}",
                    "Validated ATS-compliant resume PDF",
                    "Completed 20 targeted data structure & system design problems"
                ],
                "key_metrics": "Resume ATS Score >= 85%, 1 deployed live project"
            },
            {
                "phase": "Days 31 - 60 (Month 2)",
                "title": f"Advanced Competency: {gap_2} & Recruiter Outreach",
                "duration": "Month 2",
                "goals": [
                    f"Build production integration involving {gap_2}",
                    "Launch targeted recruiter outreach campaign (15 personalized messages/week)",
                    "Conduct 5 mock technical interview practice sessions"
                ],
                "deliverables": [
                    "Deployed full-stack app with production CI/CD pipeline",
                    "30 customized cold emails/LinkedIn applications submitted",
                    "Refined STAR behavioral interview stories"
                ],
                "key_metrics": "5+ recruiter responses, 3 initial phone screens"
            },
            {
                "phase": "Days 61 - 90 (Month 3)",
                "title": "Interview Execution & Offer Negotiation",
                "duration": "Month 3",
                "goals": [
                    "Ace technical coding assessments and system architecture loops",
                    "Execute final round virtual/onsite interview loops",
                    "Negotiate compensation packages with industry benchmark data"
                ],
                "deliverables": [
                    "Completion of 3+ full interview loops",
                    "Offer evaluation matrix & counter-offer scripts",
                    f"Signed offer letter for target {target_role} position"
                ],
                "key_metrics": "1-2 formal job offers, successful contract execution"
            }
        ]

        dynamic_data = {
            "target_role": target_role,
            "career_trajectory": f"Junior {target_role} -> Senior {target_role} -> Technical Lead / Architect",
            "expected_salary_range": "$85,000 - $125,000 / year (Target Compensation)",
            "milestones": dynamic_milestones
        }

        system_prompt = (
            "You are a Strategic Career Roadmap Planner. Return JSON with keys: "
            "'target_role' (str), 'career_trajectory' (str), 'expected_salary_range' (str), "
            "'milestones' (list of dicts with 'phase', 'title', 'duration', 'goals', 'deliverables', 'key_metrics')."
        )
        user_prompt = f"Target Role: {target_role}\nMissing Skills: {missing_skills}\nDynamic Data:\n{dynamic_data}"
        llm_response = await self.call_llm(system_prompt, user_prompt)

        output = self.parse_json_safely(llm_response, dynamic_data)

        if memory:
            memory.career_roadmap = output
            memory.log_step(self.agent_id, "Completed dynamic Career Roadmap generation", {"milestones": len(output.get("milestones", []))})

        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
