from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.memory_personalization.schemas import (
    PersonalizationSynthesis, AdaptiveLearningPath, ReasoningMemoryPipelineResult, DeterministicMemoryPipelineResult
)

class PersonalizationSynthesizerAgent(BaseAgent):
    """Agent 8: Synthesizes cross-session memory context into personalized advice."""
    def __init__(self):
        super().__init__(
            agent_id="personalization_synthesizer",
            name="Personalization Synthesizer Agent",
            description="Synthesizes cross-session user memory into highly tailored career guidance.",
            icon="UserCheck"
        )

    async def synthesize(self, det_result: DeterministicMemoryPipelineResult) -> PersonalizationSynthesis:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Personal AI Career Steward",
            domain_focus="Cross-session context synthesis and hyper-personalized recommendations."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"persona": det_result.persona.persona_archetype, "target_roles": det_result.preferences.target_roles}
        )
        
        fallback = {
            "tailored_advice": f"As a {det_result.persona.persona_archetype}, focus your preparation on deepening mastery in {', '.join(det_result.skill_trajectory.in_progress_skills[:2])}.",
            "recommended_next_actions": [
                "Execute Mock System Design simulation tailored to senior backend roles",
                "Update portfolio README with high-concurrency microservice metrics"
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="personalization_synth", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return PersonalizationSynthesis(
                tailored_advice=parsed.get("tailored_advice", fallback["tailored_advice"]),
                recommended_next_actions=parsed.get("recommended_next_actions", fallback["recommended_next_actions"])
            )
        except Exception:
            return PersonalizationSynthesis(**fallback)

class AdaptiveLearningPathAgent(BaseAgent):
    """Agent 9: Adapts learning paths dynamically based on user progress velocity."""
    def __init__(self):
        super().__init__(
            agent_id="adaptive_learning_path_agent",
            name="Adaptive Learning Path Agent",
            description="Adapts career milestones dynamically based on user progress and skill acquisition velocity.",
            icon="Activity"
        )

    async def adapt(self, det_result: DeterministicMemoryPipelineResult) -> AdaptiveLearningPath:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Adaptive Learning Architect",
            domain_focus="Dynamic milestone adjustment and learning velocity optimization."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"retention_score": det_result.retention.retention_score}
        )
        
        fallback = {
            "adapted_milestones": [
                f"Accelerate {skill} mastery phase based on past fast completion rates" for skill in det_result.skill_trajectory.in_progress_skills[:2]
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="adaptive_path", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return AdaptiveLearningPath(
                adapted_milestones=parsed.get("adapted_milestones", fallback["adapted_milestones"])
            )
        except Exception:
            return AdaptiveLearningPath(**fallback)
