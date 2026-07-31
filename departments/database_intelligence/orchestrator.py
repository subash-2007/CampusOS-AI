from app.agents.base_agent import BaseAgent
from departments.database_intelligence.deterministic import DatabaseScorerAgent
from departments.database_intelligence.reasoning import StrategicDBNarrativeAgent, DBOptimizationPlannerAgent
from departments.database_intelligence.schemas import DatabaseIntelligenceOrchestratorReport, ReasoningDBPipelineResult

class DatabaseIntelligenceOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Database Intelligence Department."""
    def __init__(self):
        super().__init__(agent_id="database_intelligence_orchestrator", name="Database Intelligence Master Orchestrator",
                         description="Coordinates all 9 database intelligence sub-agents.", icon="Database")
        self.scorer = DatabaseScorerAgent()
        self.narrative_agent = StrategicDBNarrativeAgent()
        self.optimization_planner = DBOptimizationPlannerAgent()

    async def run_pipeline(self, avg_ms: float = 8.5, coverage: float = 95.0) -> DatabaseIntelligenceOrchestratorReport:
        steps = ["Step 1: Running deterministic DB pipeline (query perf, index coverage, normalization, pool, integrity, backup)."]
        det = self.scorer.run(avg_ms, coverage)
        steps.append("Step 2: Executing Strategic DB Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing DB Optimization Planner Agent.")
        optimization = await self.optimization_planner.plan_optimization(det)
        steps.append("Step 4: Compiling Database Intelligence Master Report.")
        tier = "HIGH PERFORMANCE DATABASE" if det.db_health_score >= 85 else "FUNCTIONAL DATABASE"
        return DatabaseIntelligenceOrchestratorReport(
            db_tier=tier, db_health_score=det.db_health_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningDBPipelineResult(narrative=narrative, optimization_plan=optimization, reasoning_steps=steps),
            reasoning_steps=steps
        )
