from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.job_intelligence.schemas import (
    IdealCandidateProfile, InterviewFocusStrategy, ReasoningJobPipelineResult, DeterministicJobPipelineResult
)

class IdealCandidateProfilerAgent(BaseAgent):
    """Agent 8: Synthesizes ideal candidate profile and success factors."""
    def __init__(self):
        super().__init__(
            agent_id="ideal_candidate_profiler",
            name="Ideal Candidate Profiler Agent",
            description="Synthesizes ideal candidate persona, experience baseline, and success factors.",
            icon="UserCheck"
        )

    async def profile(self, jd_text: str, det_result: DeterministicJobPipelineResult) -> IdealCandidateProfile:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Executive Technical Recruiter",
            domain_focus="Ideal candidate persona formulation and core hiring criteria."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"seniority": det_result.seniority.seniority_level, "years": det_result.seniority.years_experience_required},
            extra_context=f"Tech languages: {', '.join(det_result.tech_stack.languages)}"
        )
        
        fallback = {
            "ideal_background": f"Strong engineering background with {det_result.seniority.years_experience_required}+ years of experience in distributed backend systems.",
            "key_success_factors": [
                "Proven mastery of modern web frameworks and database optimization",
                "Demonstrated ownership of cloud-native microservices"
            ],
            "must_have_skills": det_result.tech_stack.languages + det_result.tech_stack.frameworks
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="ideal_candidate_profile", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return IdealCandidateProfile(
                ideal_background=parsed.get("ideal_background", fallback["ideal_background"]),
                key_success_factors=parsed.get("key_success_factors", fallback["key_success_factors"]),
                must_have_skills=parsed.get("must_have_skills", fallback["must_have_skills"])
            )
        except Exception:
            return IdealCandidateProfile(**fallback)

class InterviewFocusStrategistAgent(BaseAgent):
    """Agent 9: Identifies primary interview evaluation topics and technical focus areas."""
    def __init__(self):
        super().__init__(
            agent_id="interview_focus_strategist",
            name="Interview Focus Strategist Agent",
            description="Identifies technical and behavioral interview evaluation criteria.",
            icon="Compass"
        )

    async def strategize(self, jd_text: str, det_result: DeterministicJobPipelineResult) -> InterviewFocusStrategy:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Engineering Hiring Committee Lead",
            domain_focus="Technical assessment design and interview evaluation rubric."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"complexity_tags": det_result.complexity.domain_tags}
        )
        
        fallback = {
            "technical_eval_focus": [
                "System architecture & concurrency under high load",
                "Database indexing and API latency optimization"
            ],
            "behavioral_eval_focus": [
                "Cross-functional communication & technical trade-off decisions",
                "Incident management & post-mortem analysis"
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="interview_focus", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return InterviewFocusStrategy(
                technical_eval_focus=parsed.get("technical_eval_focus", fallback["technical_eval_focus"]),
                behavioral_eval_focus=parsed.get("behavioral_eval_focus", fallback["behavioral_eval_focus"])
            )
        except Exception:
            return InterviewFocusStrategy(**fallback)
