from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.personal_branding_intelligence.schemas import (
    StrategicBrandNarrative, ContentCalendarStrategy, ReasoningBrandingPipelineResult, DeterministicBrandingPipelineResult
)

class StrategicBrandNarrativeAgent(BaseAgent):
    """Agent 8: Formulates personal brand positioning narratives and thought leadership pillars."""
    def __init__(self):
        super().__init__(
            agent_id="strategic_brand_narrative",
            name="Strategic Brand Narrative Agent",
            description="Evaluates personal brand positioning and establishes core thought leadership pillars.",
            icon="Award"
        )

    async def evaluate(self, det_result: DeterministicBrandingPipelineResult) -> StrategicBrandNarrative:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Personal Branding Executive Strategist",
            domain_focus="Executive brand positioning, thought leadership content pillars, and public presence strategy."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"brand_score": det_result.personal_brand_score, "headline_score": det_result.headline.headline_score}
        )
        
        fallback = {
            "personal_brand_positioning": f"Position candidate as a high-authority technical leader ({det_result.personal_brand_score}% brand score) specializing in cloud-native microservices.",
            "target_thought_leadership_topics": [
                "Scaling FastAPI Microservices to 10k+ QPS",
                "Zero-Downtime Database Migration Strategies",
                "Building Resilient Event-Driven Distributed Systems"
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="brand_narrative", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicBrandNarrative(
                personal_brand_positioning=parsed.get("personal_brand_positioning", fallback["personal_brand_positioning"]),
                target_thought_leadership_topics=parsed.get("target_thought_leadership_topics", fallback["target_thought_leadership_topics"])
            )
        except Exception:
            return StrategicBrandNarrative(**fallback)

class ContentCalendarStrategistAgent(BaseAgent):
    """Agent 9: Generates monthly technical content calendars and sample post drafts."""
    def __init__(self):
        super().__init__(
            agent_id="content_calendar_strategist",
            name="Content Calendar Strategist Agent",
            description="Generates high-engagement LinkedIn and technical blog content calendars.",
            icon="Calendar"
        )

    async def generate_calendar(self, det_result: DeterministicBrandingPipelineResult) -> ContentCalendarStrategy:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Technical Copywriter & Social Media Strategist",
            domain_focus="LinkedIn post drafting, technical blogging, and audience engagement strategy."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"posts_per_month": det_result.engagement.posts_per_month}
        )
        
        fallback = {
            "recommended_post_topics": [
                "Post 1: How we cut API response latency by 45% using FastAPI & Redis caching",
                "Post 2: 3 common architectural mistakes in microservice deployments",
                "Post 3: Why we migrated our CI/CD pipeline to GitHub Actions",
                "Post 4: Key lessons learned scaling Python services to production"
            ],
            "sample_linkedin_post_draft": "🚀 How we reduced API latency by 45% in production:\n\nWhen scaling our microservice architecture, DB query bottlenecks were slowing down customer checkout flows. Here is how we fixed it:\n\n1. Implemented Redis cache-aside pattern for hot read paths\n2. Optimized Gunicorn worker concurrency settings\n3. Added connection pooling to PostgreSQL\n\nResult: Latency dropped from 180ms to 99ms at 10k QPS.\n\nWhat caching strategy does your team use? Let's discuss in the comments below! 👇"
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="content_calendar", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return ContentCalendarStrategy(
                recommended_post_topics=parsed.get("recommended_post_topics", fallback["recommended_post_topics"]),
                sample_linkedin_post_draft=parsed.get("sample_linkedin_post_draft", fallback["sample_linkedin_post_draft"])
            )
        except Exception:
            return ContentCalendarStrategy(**fallback)
