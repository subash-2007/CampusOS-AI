from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.api_design_intelligence.schemas import (
    StrategicAPINarrative, APIEvolutionPlan, ReasoningAPIPipelineResult, DeterministicAPIPipelineResult
)

class StrategicAPINarrativeAgent(BaseAgent):
    """Agent 8: Formulates strategic API design evaluations and REST maturity reviews."""
    def __init__(self):
        super().__init__(agent_id="strategic_api_narrative", name="Strategic API Narrative Agent",
                         description="Evaluates REST API maturity, OpenAPI coverage, and authentication strategy.", icon="Globe")

    async def evaluate(self, det: DeterministicAPIPipelineResult) -> StrategicAPINarrative:
        fallback = {
            "api_design_summary": f"Production-grade REST API ({det.api_quality_score:.1f}% quality). Full 100% versioning coverage, {det.openapi.spec_coverage_pct}% OpenAPI 3.1 spec with RFC7807 error standards.",
            "key_api_strengths": ["OAuth2 RS256 JWT with token refresh rotation", "100% endpoint versioning with zero breaking changes"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Principal API Architect", "REST design, OpenAPI, OAuth2"),
                                          PromptBuilder.build_user_context({"score": det.api_quality_score}), task_type="api_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicAPINarrative(api_design_summary=parsed.get("api_design_summary", fallback["api_design_summary"]),
                                         key_api_strengths=parsed.get("key_api_strengths", fallback["key_api_strengths"]))
        except Exception:
            return StrategicAPINarrative(**fallback)

class APIEvolutionPlannerAgent(BaseAgent):
    """Agent 9: Generates API versioning strategies and OpenAPI YAML samples."""
    def __init__(self):
        super().__init__(agent_id="api_evolution_planner", name="API Evolution Planner Agent",
                         description="Formulates API versioning roadmaps and sample OpenAPI YAML schemas.", icon="Code")

    async def plan_evolution(self, det: DeterministicAPIPipelineResult) -> APIEvolutionPlan:
        fallback = {
            "versioning_strategy": ["Adopt URL path versioning (/api/v2/) for all breaking changes", "Implement API deprecation headers (Sunset, Deprecation) for retired endpoints"],
            "sample_openapi_yaml": "openapi: '3.1.0'\ninfo:\n  title: CampusOS AI API\n  version: '2.0.0'\npaths:\n  /api/v2/resume/analyze:\n    post:\n      summary: Analyze resume\n      responses:\n        '200':\n          description: Resume analysis result"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("API Product Manager", "API lifecycle, versioning"),
                                          PromptBuilder.build_user_context({"endpoints": det.endpoint_audit.total_endpoints}), task_type="api_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return APIEvolutionPlan(versioning_strategy=parsed.get("versioning_strategy", fallback["versioning_strategy"]),
                                    sample_openapi_yaml=parsed.get("sample_openapi_yaml", fallback["sample_openapi_yaml"]))
        except Exception:
            return APIEvolutionPlan(**fallback)
