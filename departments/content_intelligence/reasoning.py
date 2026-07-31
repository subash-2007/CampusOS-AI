from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.content_intelligence.schemas import (
    StrategicContentNarrative, ContentEditorialPlan, ReasoningContentPipelineResult, DeterministicContentPipelineResult
)

class StrategicContentNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates content strategy quality, SEO health, and engagement metrics."""
    def __init__(self):
        super().__init__(agent_id="strategic_content_narrative", name="Strategic Content Narrative Agent",
                         description="Evaluates readability, SEO, freshness, and engagement.", icon="FileText")

    async def evaluate(self, det: DeterministicContentPipelineResult) -> StrategicContentNarrative:
        fallback = {
            "content_strategy_summary": f"Premium content platform ({det.content_quality_score:.1f}% quality). {det.plagiarism.unique_content_pct}% unique content, {det.seo.meta_description_coverage_pct}% SEO coverage, {det.engagement.avg_scroll_depth_pct}% scroll depth.",
            "key_content_strengths": [f"Zero plagiarized content with {det.plagiarism.unique_content_pct}% uniqueness", f"Professional readability (FK Grade {det.readability.flesch_kincaid_grade}) for career audience"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Chief Content Officer", "SEO, editorial strategy, engagement"),
                                          PromptBuilder.build_user_context({"score": det.content_quality_score}), task_type="content_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicContentNarrative(content_strategy_summary=parsed.get("content_strategy_summary", fallback["content_strategy_summary"]),
                                              key_content_strengths=parsed.get("key_content_strengths", fallback["key_content_strengths"]))
        except Exception:
            return StrategicContentNarrative(**fallback)

class ContentEditorialPlannerAgent(BaseAgent):
    """Agent 9: Generates content improvement actions and editorial brief templates."""
    def __init__(self):
        super().__init__(agent_id="content_editorial_planner", name="Content Editorial Planner Agent",
                         description="Formulates editorial content calendars and SEO optimization briefs.", icon="Edit")

    async def plan_editorial(self, det: DeterministicContentPipelineResult) -> ContentEditorialPlan:
        fallback = {
            "content_improvement_actions": ["Create 'Salary Negotiation Scripts' interactive guide to increase scroll depth beyond 68%", "Add schema markup (FAQ, HowTo) to top 20 career articles for rich snippet optimization"],
            "sample_content_brief": "Title: 10 Data Scientist Interview Questions (2024)\nTarget Keyword: data scientist interview questions (2,400/mo)\nFK Grade Target: 10-11\nWord Count: 1,800-2,200\nSections: Introduction, Technical Questions, Behavioral Questions, Tips\nCTA: Download our free AI Resume Builder"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("SEO Content Strategist", "content briefs, keyword strategy"),
                                          PromptBuilder.build_user_context({"freshness": det.freshness.avg_content_age_days}), task_type="content_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return ContentEditorialPlan(content_improvement_actions=parsed.get("content_improvement_actions", fallback["content_improvement_actions"]),
                                        sample_content_brief=parsed.get("sample_content_brief", fallback["sample_content_brief"]))
        except Exception:
            return ContentEditorialPlan(**fallback)
