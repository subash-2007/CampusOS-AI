from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.research_publication_intelligence.schemas import (
    StrategicResearchNarrative, CommercializationPlan, ReasoningResearchPipelineResult, DeterministicResearchPipelineResult
)

class StrategicResearchNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates institutional research impact, citation metrics, and grant competitiveness."""
    def __init__(self):
        super().__init__(agent_id="strategic_research_narrative", name="Strategic Research Narrative Agent",
                         description="Evaluates publication output, citation h-index, grant win rates, and open access compliance.", icon="BookOpen")

    async def evaluate(self, det: DeterministicResearchPipelineResult) -> StrategicResearchNarrative:
        fallback = {
            "research_summary": f"High impact research institution ({det.research_excellence_score:.1f}% score). {det.publications.published_papers_total} papers published, {det.citation.total_citations_count:,} citations (h-index {det.citation.h_index_avg}), ${det.grants.active_grants_value_usd/1e6:.1f}M active grant funding.",
            "key_research_strengths": [f"{det.open_access.open_access_publications_pct}% open access compliance across {det.open_access.arxiv_biorxiv_preprints_count} preprint uploads", f"{det.patents.patents_granted_count} granted patents with {det.patents.tech_transfer_licensing_agreements} active commercial licensing agreements"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Vice President of Research", "grant funding, bibliometrics, h-index, tech transfer"),
                                          PromptBuilder.build_user_context({"score": det.research_excellence_score}), task_type="research_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicResearchNarrative(research_summary=parsed.get("research_summary", fallback["research_summary"]),
                                             key_research_strengths=parsed.get("key_research_strengths", fallback["key_research_strengths"]))
        except Exception:
            return StrategicResearchNarrative(**fallback)

class CommercializationPlannerAgent(BaseAgent):
    """Agent 9: Generates technology transfer commercialization roadmaps and research grant proposals."""
    def __init__(self):
        super().__init__(agent_id="commercialization_planner", name="Commercialization Planner Agent",
                         description="Formulates IP licensing strategies, university spin-off incubators, and NSF/NIH grant applications.", icon="Lightbulb")

    async def plan_commercialization(self, det: DeterministicResearchPipelineResult) -> CommercializationPlan:
        fallback = {
            "tech_transfer_actions": [f"File international PCT patent applications for {det.patents.patents_filed_count} disclosure filings in AI & Biotechnology", "Establish Campus IP Spin-Off Accelerator to support faculty entrepreneurs"],
            "sample_grant_proposal_summary": "PROJECT ABSTRACT\nTitle: Autonomous Multi-Agent AI Systems for Higher Education (NSF AI Institute)\nPrincipal Investigator: Dr. A. Vance\nRequested Budget: $2,500,000 over 36 months\nObjectives:\n  1. Develop deterministic verification pipelines for autonomous LLM agents\n  2. Evaluate student outcome improvement across 10,000 active learners\n  3. Publish open-access benchmarks and datasets on HuggingFace and arXiv"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Tech Transfer Director", "NSF/NIH grants, patent licensing, spin-offs"),
                                          PromptBuilder.build_user_context({"patents": det.patents.patents_granted_count}), task_type="research_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return CommercializationPlan(tech_transfer_actions=parsed.get("tech_transfer_actions", fallback["tech_transfer_actions"]),
                                        sample_grant_proposal_summary=parsed.get("sample_grant_proposal_summary", fallback["sample_grant_proposal_summary"]))
        except Exception:
            return CommercializationPlan(**fallback)
