from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.career_roadmap.schemas import (
    StrategicCareerAdvice, LongTermCareerVision, ReasoningRoadmapPipelineResult, DeterministicRoadmapPipelineResult
)

class StrategicCareerAdvisorAgent(BaseAgent):
    """Agent 8: Formulates strategic networking advice and career positioning narrative."""
    def __init__(self):
        super().__init__(
            agent_id="strategic_career_advisor",
            name="Strategic Career Advisor Agent",
            description="Formulates high-level career positioning narratives and networking strategies.",
            icon="Compass"
        )

    async def advise(self, target_role: str, det_result: DeterministicRoadmapPipelineResult) -> StrategicCareerAdvice:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Executive Career Strategist & Tech Leadership Coach",
            domain_focus="Strategic career positioning, salary negotiation, and executive networking."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"target_role": target_role, "expected_salary_increase": f"{det_result.salary_trajectory.expected_increase_pct}%"}
        )
        
        fallback = {
            "executive_narrative": f"Positioning for {target_role} requires highlighting systemic engineering impact, architectural ownership, and cross-functional leadership.",
            "networking_strategy": [
                "Engage with Principal Engineers and Hiring Managers on LinkedIn via technical content breakdown",
                "Attend targeted engineering meetups and open-source hackathons"
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="career_advice", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicCareerAdvice(
                executive_narrative=parsed.get("executive_narrative", fallback["executive_narrative"]),
                networking_strategy=parsed.get("networking_strategy", fallback["networking_strategy"])
            )
        except Exception:
            return StrategicCareerAdvice(**fallback)

class LongTermVisionStrategistAgent(BaseAgent):
    """Agent 9: Formulates 5-year career vision and strategic career pivot milestones."""
    def __init__(self):
        super().__init__(
            agent_id="long_term_vision_strategist",
            name="Long Term Vision Strategist Agent",
            description="Formulates 5-year long-term career growth visions and strategic pivot milestones.",
            icon="Eye"
        )

    async def project_vision(self, target_role: str, det_result: DeterministicRoadmapPipelineResult) -> LongTermCareerVision:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Chief Technology Officer & Engineering Career Mentor",
            domain_focus="Long-term technology career planning and executive track progression."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"long_term_level": det_result.progression_path.long_term_level}
        )
        
        fallback = {
            "five_year_vision": f"Transition from Senior Engineering into {det_result.progression_path.long_term_level}, driving organizational technology strategy.",
            "key_career_pivots": [
                "Year 1-2: Master enterprise cloud architecture & lead core infrastructure initiatives",
                "Year 3-5: Pivot to Staff Engineer / Director of Engineering, driving platform scale"
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="long_term_vision", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return LongTermCareerVision(
                five_year_vision=parsed.get("five_year_vision", fallback["five_year_vision"]),
                key_career_pivots=parsed.get("key_career_pivots", fallback["key_career_pivots"])
            )
        except Exception:
            return LongTermCareerVision(**fallback)
