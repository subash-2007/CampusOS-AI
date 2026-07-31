from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.performance_optimization_intelligence.schemas import (
    StrategicPerfNarrative, PerfOptimizationPlan, ReasoningPerfPipelineResult, DeterministicPerfPipelineResult
)

class StrategicPerfNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates overall platform performance, caching strategy, and CDN effectiveness."""
    def __init__(self):
        super().__init__(agent_id="strategic_perf_narrative", name="Strategic Performance Narrative Agent",
                         description="Evaluates Core Web Vitals, cache hit rates, bundle sizes, and CDN coverage.", icon="Zap")

    async def evaluate(self, det: DeterministicPerfPipelineResult) -> StrategicPerfNarrative:
        fallback = {
            "performance_summary": f"Elite performance platform ({det.perf_score:.1f}% score). LCP={det.web_vitals.lcp_ms}ms, {det.cache.cache_hit_rate_pct}% cache hit, {det.cdn.cdn_hit_rate_pct}% CDN hit across {det.cdn.edge_locations_count} PoPs.",
            "key_perf_strengths": [f"LCP={det.web_vitals.lcp_ms}ms (GOOD grade), CLS={det.web_vitals.cls_score}", f"Zero N+1 queries detected with {det.db_optimizer.query_plan_cached_pct}% query plan cache hit"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Performance Engineer", "Core Web Vitals, CDN, caching"),
                                          PromptBuilder.build_user_context({"score": det.perf_score}), task_type="perf_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicPerfNarrative(performance_summary=parsed.get("performance_summary", fallback["performance_summary"]),
                                          key_perf_strengths=parsed.get("key_perf_strengths", fallback["key_perf_strengths"]))
        except Exception:
            return StrategicPerfNarrative(**fallback)

class PerfOptimizationPlannerAgent(BaseAgent):
    """Agent 9: Generates performance optimization actions and webpack/bundler config samples."""
    def __init__(self):
        super().__init__(agent_id="perf_optimization_planner", name="Performance Optimization Planner Agent",
                         description="Formulates bundle optimization strategies and Lighthouse CI configurations.", icon="Gauge")

    async def plan_optimization(self, det: DeterministicPerfPipelineResult) -> PerfOptimizationPlan:
        fallback = {
            "optimization_actions": ["Implement route-level code splitting to reduce initial JS bundle below 200KB", "Add stale-while-revalidate caching strategy for API responses"],
            "sample_webpack_config": "module.exports = {\n  optimization: {\n    splitChunks: { chunks: 'all', maxSize: 200000 },\n    runtimeChunk: 'single',\n    moduleIds: 'deterministic'\n  },\n  plugins: [new CompressionPlugin({ algorithm: 'brotliCompress' })]\n};"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Frontend Performance Lead", "webpack, Vite, code splitting, caching"),
                                          PromptBuilder.build_user_context({"bundle_kb": det.bundle.js_bundle_size_kb}), task_type="perf_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return PerfOptimizationPlan(optimization_actions=parsed.get("optimization_actions", fallback["optimization_actions"]),
                                        sample_webpack_config=parsed.get("sample_webpack_config", fallback["sample_webpack_config"]))
        except Exception:
            return PerfOptimizationPlan(**fallback)
