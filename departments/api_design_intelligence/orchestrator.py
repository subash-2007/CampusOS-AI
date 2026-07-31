from app.agents.base_agent import BaseAgent
from departments.api_design_intelligence.deterministic import APIScorerAgent
from departments.api_design_intelligence.reasoning import StrategicAPINarrativeAgent, APIEvolutionPlannerAgent
from departments.api_design_intelligence.schemas import APIDesignOrchestratorReport, ReasoningAPIPipelineResult

class APIDesignOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for the API Design Intelligence Department."""
    def __init__(self):
        super().__init__(agent_id="api_design_orchestrator", name="API Design Intelligence Master Orchestrator",
                         description="Coordinates all 9 API design sub-agents.", icon="Zap")
        self.scorer = APIScorerAgent()
        self.narrative_agent = StrategicAPINarrativeAgent()
        self.evolution_planner = APIEvolutionPlannerAgent()

    async def run_pipeline(self, total_endpoints: int = 42, coverage: float = 98.0) -> APIDesignOrchestratorReport:
        steps = []
        steps.append("Step 1: Running deterministic API Design pipeline (REST endpoint audit, OpenAPI spec coverage, P99 latency, rate limiting, OAuth2 auth, RFC7807 error standards).")
        det = self.scorer.run(total_endpoints, coverage)
        steps.append("Step 2: Executing Strategic API Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing API Evolution Planner Agent.")
        evolution = await self.evolution_planner.plan_evolution(det)
        steps.append("Step 4: Compiling API Design Intelligence Master Report.")
        tier = "PRODUCTION GRADE API" if det.api_quality_score >= 85 else "FUNCTIONAL API"
        return APIDesignOrchestratorReport(
            api_tier=tier, api_quality_score=det.api_quality_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningAPIPipelineResult(narrative=narrative, evolution_plan=evolution, reasoning_steps=steps),
            reasoning_steps=steps
        )
