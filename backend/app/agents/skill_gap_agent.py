from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from app.nlp import extract_skills_from_text

class SkillGapAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="skill_gap_intelligence",
            name="Skill Gap Intelligence Agent",
            description="Identifies missing technical and soft skills, generating a prioritized learning matrix and course recommendations.",
            icon="Zap"
        )

    async def run(self, inputs: Dict[str, Any], memory: Optional[Any] = None) -> Dict[str, Any]:
        resume_text = inputs.get("resume_text", "") or (memory.resume_text if memory else "")
        job_desc = inputs.get("job_description_text", "") or (memory.job_description_text if memory else "")
        target_role = inputs.get("target_role", "") or (memory.get_target_role() if memory else "Software Engineer")

        reasoning_steps = [
            "Audited current technical competencies from candidate resume",
            "Cross-referenced against target job requirements",
            "Calculated Readiness % and built prioritized dynamic learning pathway"
        ]

        candidate_skills = set(memory.get_candidate_skills() if memory else extract_skills_from_text(resume_text))
        required_skills = set(extract_skills_from_text(job_desc))

        missing_skills = list(required_skills.difference(candidate_skills))
        if not missing_skills:
            missing_skills = ["Cloud Deployment (AWS/Docker)", "System Design & Microservices", "CI/CD Automation"]

        # Readiness Calculation
        total_req = max(1, len(required_skills))
        matched_count = len(candidate_skills.intersection(required_skills))
        readiness_pct = int(round((matched_count / total_req) * 100)) if required_skills else 70
        readiness_pct = max(35, min(98, readiness_pct))

        critical_gaps = []
        for idx, skill in enumerate(missing_skills[:3]):
            urgency = "High" if idx == 0 else "Medium"
            critical_gaps.append({
                "skill": skill,
                "urgency": urgency,
                "reason": f"Required for {target_role} role requirements and technical screens."
            })

        secondary_gaps = []
        for skill in missing_skills[3:6]:
            secondary_gaps.append({
                "skill": skill,
                "urgency": "Low",
                "reason": "Secondary stack component for enhanced recruiter appeal."
            })

        learning_pathway = []
        for m_idx, gap in enumerate(critical_gaps):
            learning_pathway.append({
                "month": f"Month {m_idx + 1}",
                "topic": f"Mastering {gap['skill']}",
                "resource": f"Official {gap['skill']} Documentation & Production Labs",
                "estimated_hours": "8 - 12 hours"
            })

        dynamic_data = {
            "critical_gaps": critical_gaps,
            "secondary_gaps": secondary_gaps,
            "learning_pathway": learning_pathway,
            "overall_readiness_pct": readiness_pct
        }

        system_prompt = (
            "You are a Skill Gap Analyst. Evaluate skill gaps for target role and refine into JSON with keys: "
            "'critical_gaps' (list of dicts), 'secondary_gaps' (list of dicts), 'learning_pathway' (list of dicts), "
            "'overall_readiness_pct' (int)."
        )
        user_prompt = f"Candidate Skills: {candidate_skills}\nMissing Skills: {missing_skills}\nDynamic Data:\n{dynamic_data}"
        llm_response = await self.call_llm(system_prompt, user_prompt)

        output = self.parse_json_safely(llm_response, dynamic_data)
        output["overall_readiness_pct"] = readiness_pct
        output["critical_gaps"] = critical_gaps

        if memory:
            memory.skill_gap_analysis = output
            memory.log_step(self.agent_id, "Completed dynamic Skill Gap analysis", {"readiness": readiness_pct})

        return {
            "agent_id": self.agent_id,
            "agent_name": self.name,
            "reasoning_steps": reasoning_steps,
            "output": output
        }
