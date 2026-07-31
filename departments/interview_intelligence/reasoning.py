from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.interview_intelligence.schemas import (
    STARResponseGuide, MockSimulationStrategy, ReasoningInterviewPipelineResult, DeterministicInterviewPipelineResult
)

class STARResponseCoachAgent(BaseAgent):
    """Agent 8: Coaches candidates on structuring high-impact STAR responses."""
    def __init__(self):
        super().__init__(
            agent_id="star_response_coach",
            name="STAR Response Coach Agent",
            description="Coaches candidates on structuring metric-driven STAR behavioral answers.",
            icon="MessageSquare"
        )

    async def coach(self, target_role: str, det_result: DeterministicInterviewPipelineResult) -> STARResponseGuide:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Principal Interview Coach & Ex-FAANG Recruiter",
            domain_focus="Behavioral STAR method answer optimization and executive presentation."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"target_role": target_role, "behavioral_questions_count": len(det_result.behavioral_questions.star_questions)}
        )
        
        fallback = {
            "situation_tips": "Set the context in 2-3 sentences. Clearly state company scale, tech stack, and business problem.",
            "task_tips": "Define your exact individual responsibility and architectural ownership.",
            "action_tips": "Detail 3 concrete engineering steps YOU executed (e.g. refactored queries, introduced caching).",
            "result_tips": "Always conclude with 2+ quantifiable metrics (e.g. 40% latency drop, $50k cost savings)."
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="star_coaching", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return STARResponseGuide(
                situation_tips=parsed.get("situation_tips", fallback["situation_tips"]),
                task_tips=parsed.get("task_tips", fallback["task_tips"]),
                action_tips=parsed.get("action_tips", fallback["action_tips"]),
                result_tips=parsed.get("result_tips", fallback["result_tips"])
            )
        except Exception:
            return STARResponseGuide(**fallback)

class MockSimulationStrategistAgent(BaseAgent):
    """Agent 9: Designs end-to-end mock interview simulation strategies."""
    def __init__(self):
        super().__init__(
            agent_id="mock_simulation_strategist",
            name="Mock Simulation Strategist Agent",
            description="Designs timed mock interview simulations and critical pitfall mitigation plans.",
            icon="PlayCircle"
        )

    async def plan(self, target_role: str, det_result: DeterministicInterviewPipelineResult) -> MockSimulationStrategy:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Lead Technical Interviewer",
            domain_focus="Mock interview simulation design and live coding performance optimization."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"estimated_rounds": det_result.duration.estimated_rounds}
        )
        
        fallback = {
            "mock_session_plan": [
                "Round 1 (45 min): Live Data Structures & Algorithms coding challenge",
                "Round 2 (60 min): System Architecture & Scalability design prompt",
                "Round 3 (45 min): STAR Behavioral & Leadership experience deep-dive"
            ],
            "critical_pitfalls_to_avoid": [
                "Jumping straight into code without clarifying input boundaries & edge cases",
                "Failing to quantify impact metrics in behavioral STAR answers",
                "Over-engineering simple solutions without considering maintenance overhead"
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="mock_simulation_plan", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return MockSimulationStrategy(
                mock_session_plan=parsed.get("mock_session_plan", fallback["mock_session_plan"]),
                critical_pitfalls_to_avoid=parsed.get("critical_pitfalls_to_avoid", fallback["critical_pitfalls_to_avoid"])
            )
        except Exception:
            return MockSimulationStrategy(**fallback)
