from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.alumni_network_intelligence.schemas import (
    StrategicAlumniOutreachNarrative, OutreachIntroScript, ReasoningAlumniPipelineResult, DeterministicAlumniPipelineResult
)

class StrategicAlumniOutreachNarrativeAgent(BaseAgent):
    """Agent 8: Formulates strategic alumni networking narratives and target outreach profiles."""
    def __init__(self):
        super().__init__(
            agent_id="strategic_alumni_outreach_narrative",
            name="Strategic Alumni Outreach Narrative Agent",
            description="Evaluates alumni network strength and maps optimal outreach connection paths.",
            icon="UserPlus"
        )

    async def evaluate(self, company_name: str, det_result: DeterministicAlumniPipelineResult) -> StrategicAlumniOutreachNarrative:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="University Alumni Network Strategist",
            domain_focus="Alumni network leverage, referral path mapping, and warm outreach strategy."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"company_name": company_name, "matching_alumni": det_result.matches.matching_alumni_count}
        )
        
        fallback = {
            "alumni_networking_strategy": f"Found {det_result.matches.matching_alumni_count} alumni at {company_name}. Target senior alumni for informational interviews to establish warm referral rapport.",
            "target_alumni_profiles": [
                f"Senior Engineering Manager at {company_name} (Shared University Alum)",
                f"Staff Backend Engineer at {company_name} (Shared Major Alum)"
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="alumni_narrative", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicAlumniOutreachNarrative(
                alumni_networking_strategy=parsed.get("alumni_networking_strategy", fallback["alumni_networking_strategy"]),
                target_alumni_profiles=parsed.get("target_alumni_profiles", fallback["target_alumni_profiles"])
            )
        except Exception:
            return StrategicAlumniOutreachNarrative(**fallback)

class OutreachIntroScriptGeneratorAgent(BaseAgent):
    """Agent 9: Generates personalized alumni LinkedIn & email introduction messages."""
    def __init__(self):
        super().__init__(
            agent_id="outreach_intro_script_generator",
            name="Outreach Intro Script Generator Agent",
            description="Generates warm, high-converting alumni outreach connection messages.",
            icon="Send"
        )

    async def generate_script(self, company_name: str, det_result: DeterministicAlumniPipelineResult) -> OutreachIntroScript:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Alumni Outreach Specialist",
            domain_focus="LinkedIn connection request messaging and warm alumni referral scripts."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"referral_likelihood": det_result.referral.referral_likelihood_score}
        )
        
        fallback = {
            "personalized_alumni_outreach_draft": f"Hi [Name],\n\nI noticed we both graduated from {det_result.overlap.shared_universities[0] if det_result.overlap.shared_universities else 'Stanford'}! I'm currently preparing for backend roles at {company_name} and would love to ask a couple of quick questions about your experience on the team.\n\nBest,\nAlex",
            "warm_intro_talking_points": [
                "Reference shared university degree background in subject line",
                "Keep initial message under 75 words asking for a 15-min chat"
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="alumni_script", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return OutreachIntroScript(
                personalized_alumni_outreach_draft=parsed.get("personalized_alumni_outreach_draft", fallback["personalized_alumni_outreach_draft"]),
                warm_intro_talking_points=parsed.get("warm_intro_talking_points", fallback["warm_intro_talking_points"])
            )
        except Exception:
            return OutreachIntroScript(**fallback)
