import logging
from typing import Dict, Any, List, Optional
from datetime import datetime, timezone

from app.agents.base_agent import BaseAgent
from app.agents.shared_memory import SharedMemory
from app.nlp import parse_document_input, fetch_url_text

logger = logging.getLogger("CampusOS.SupervisorAgent")

class SupervisorAgent(BaseAgent):
    """Central Supervisor Agent (Career Intelligence Manager) orchestrating autonomous multi-agent pipelines."""
    def __init__(self):
        super().__init__(
            agent_id="supervisor_agent",
            name="Supervisor Agent (Career Intelligence Manager)",
            description="Central intelligence manager orchestrating task planning, agent delegation, shared memory context, and aggregated report synthesis.",
            icon="Brain"
        )

    async def run_supervisor_pipeline(
        self,
        resume_filename: Optional[str] = None,
        resume_bytes: Optional[bytes] = None,
        resume_text: Optional[str] = None,
        job_filename: Optional[str] = None,
        job_bytes: Optional[bytes] = None,
        job_text: Optional[str] = None,
        job_url: Optional[str] = None,
        career_goal: Optional[str] = None,
        target_role: Optional[str] = None,
        experience_level: Optional[str] = None,
        company_name: Optional[str] = None
    ) -> Dict[str, Any]:
        """Main multi-agent execution pipeline orchestrating sub-agent tasks and shared memory context."""
        memory = SharedMemory()

        # Step 1: Parse and resolve raw input text
        resolved_resume_text = parse_document_input(resume_filename, resume_bytes, resume_text)
        
        resolved_job_text = ""
        if job_url:
            resolved_job_text = await fetch_url_text(job_url)
        if not resolved_job_text:
            resolved_job_text = parse_document_input(job_filename, job_bytes, job_text)

        memory.resume_text = resolved_resume_text
        memory.job_description_text = resolved_job_text
        memory.target_role = target_role or "Software Engineer"
        memory.career_goal = career_goal or f"Land a role as {memory.target_role}"
        memory.experience_level = experience_level or "Entry Level / Student"
        memory.company_name = company_name or "Target Enterprise"

        memory.log_step(self.agent_id, "Supervisor received user inputs and created execution plan", {
            "has_resume": bool(resolved_resume_text),
            "has_jd": bool(resolved_job_text),
            "target_role": memory.target_role
        })

        # Step 2: Task Execution Plan
        tasks = [
            ("Task 1: Analyze Resume", "resume_intelligence", {"resume_text": resolved_resume_text}),
            ("Task 2: Deconstruct Job Requirements", "job_intelligence", {"job_description_text": resolved_job_text, "target_role": memory.target_role}),
            ("Task 3: Calculate ATS Compatibility & Keyword Overlap", "ats_optimization", {"resume_text": resolved_resume_text, "job_description_text": resolved_job_text}),
            ("Task 4: Identify Skill Gaps & Prioritized Learning", "skill_gap_intelligence", {"resume_text": resolved_resume_text, "job_description_text": resolved_job_text, "target_role": memory.target_role}),
            ("Task 5: Research Target Company & Interview Loop", "company_intelligence", {"company_name": memory.company_name, "job_description_text": resolved_job_text}),
            ("Task 6: Generate Personalized Technical/Behavioral Q&A", "interview_intelligence", {"target_role": memory.target_role}),
            ("Task 7: Build 30-60-90 Day Strategic Career Roadmap", "career_roadmap", {"target_role": memory.target_role}),
            ("Task 8: Audit GitHub/Portfolio & Build Production README", "portfolio_intelligence", {"target_role": memory.target_role}),
            ("Task 9: Generate Recruiter Outreach & Negotiation Templates", "communication_intelligence", {"company_name": memory.company_name, "recipient_role": "Engineering Manager"}),
            ("Task 10: Aggregate Overall Readiness Analytics", "career_analytics", {})
        ]

        # Step 3: Sequential Agent Execution passing Shared Memory Context
        from app.agents import agent_registry

        for task_title, sub_agent_id, sub_inputs in tasks:
            sub_agent = agent_registry.get_agent(sub_agent_id)
            if sub_agent:
                memory.log_step(self.agent_id, f"Delegating to {sub_agent.name}: {task_title}")
                await sub_agent.run(sub_inputs, memory=memory)

        # Step 4: Aggregate Deterministic Career Intelligence Report
        now = datetime.now(timezone.utc).isoformat()
        report_id = f"REP-{int(datetime.now().timestamp())}"

        aggregated_report = {
            "report_id": report_id,
            "generated_at": now,
            "candidate_profile": {
                "target_role": memory.target_role,
                "career_goal": memory.career_goal,
                "experience_level": memory.experience_level,
                "company_name": memory.company_name,
                "extracted_skills": memory.get_candidate_skills()
            },
            "overall_readiness_score": memory.career_roadmap.get("output", {}).get("overall_readiness", memory.ats_optimization.get("match_score", 78)),
            "resume_intelligence": memory.resume_analysis,
            "ats_optimization": memory.ats_optimization,
            "job_intelligence": memory.job_analysis,
            "company_intelligence": memory.company_intelligence,
            "skill_gap_analysis": memory.skill_gap_analysis,
            "interview_preparation": memory.interview_prep,
            "career_roadmap": memory.career_roadmap,
            "portfolio_intelligence": memory.portfolio_recommendations,
            "communication_templates": memory.communication_templates,
            "execution_trace": memory.execution_log
        }

        # Step 5: Optional LLM Enhancement for Human-Friendly Summary Formatting
        system_prompt = (
            "You are the Master Supervisor Agent formatting a final Career Intelligence Report. "
            "Enhance the aggregated report prose while preserving all calculated scores and keyword arrays exactly."
        )
        user_prompt = f"Aggregated Report Data:\n{aggregated_report}"
        llm_response = await self.call_llm(system_prompt, user_prompt)

        final_report = self.parse_json_safely(llm_response, aggregated_report)

        # Enforce exact dynamic scores from shared memory
        final_report["report_id"] = report_id
        final_report["generated_at"] = now
        final_report["candidate_profile"] = aggregated_report["candidate_profile"]
        final_report["overall_readiness_score"] = memory.ats_optimization.get("match_score", 80)
        final_report["resume_intelligence"] = memory.resume_analysis
        final_report["ats_optimization"] = memory.ats_optimization
        final_report["job_intelligence"] = memory.job_analysis
        final_report["company_intelligence"] = memory.company_intelligence
        final_report["skill_gap_analysis"] = memory.skill_gap_analysis
        final_report["interview_preparation"] = memory.interview_prep
        final_report["career_roadmap"] = memory.career_roadmap
        final_report["portfolio_intelligence"] = memory.portfolio_recommendations
        final_report["communication_templates"] = memory.communication_templates
        final_report["execution_trace"] = memory.execution_log

        return final_report

supervisor_agent = SupervisorAgent()
