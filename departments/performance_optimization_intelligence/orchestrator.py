from app.agents.base_agent import BaseAgent
from departments.performance_optimization_intelligence.deterministic import PerformanceScorerAgent
from departments.performance_optimization_intelligence.reasoning import StrategicPerfNarrativeAgent, PerfOptimizationPlannerAgent
from departments.performance_optimization_intelligence.schemas import PerformanceOptimizationOrchestratorReport, ReasoningPerfPipelineResult

class PerformanceOptimizationOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Performance Optimization Intelligence Department."""
    def __init__(self):
        super().__init__(agent_id="performance_optimization_orchestrator", name="Performance Optimization Intelligence Master Orchestrator",
                         description="Coordinates all 9 performance optimization sub-agents.", icon="Zap")
        self.scorer = PerformanceScorerAgent()
        self.narrative_agent = StrategicPerfNarrativeAgent()
        self.optimization_planner = PerfOptimizationPlannerAgent()

    async def run_pipeline(self, lcp: float = 1200.0) -> PerformanceOptimizationOrchestratorReport:
        steps = ["Step 1: Running deterministic Performance pipeline (Core Web Vitals, cache hit, bundle size, CDN, DB optimizer, memory leaks)."]
        det = self.scorer.run(lcp)
        steps.append("Step 2: Executing Strategic Performance Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Performance Optimization Planner Agent.")
        optimization = await self.optimization_planner.plan_optimization(det)
        steps.append("Step 4: Compiling Performance Optimization Intelligence Master Report.")
        tier = "ELITE PERFORMANCE" if det.perf_score >= 85 else "STANDARD PERFORMANCE"
        return PerformanceOptimizationOrchestratorReport(
            perf_tier=tier, perf_score=det.perf_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningPerfPipelineResult(narrative=narrative, optimization_plan=optimization, reasoning_steps=steps),
            reasoning_steps=steps
        )
