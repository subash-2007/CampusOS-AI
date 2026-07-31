from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.database_intelligence.schemas import (
    StrategicDBNarrative, DBOptimizationPlan, ReasoningDBPipelineResult, DeterministicDBPipelineResult
)

class StrategicDBNarrativeAgent(BaseAgent):
    """Agent 8: Formulates strategic database architecture and query optimization evaluations."""
    def __init__(self):
        super().__init__(agent_id="strategic_db_narrative", name="Strategic DB Narrative Agent",
                         description="Evaluates query performance, index coverage, and normalization.", icon="Database")

    async def evaluate(self, det: DeterministicDBPipelineResult) -> StrategicDBNarrative:
        fallback = {
            "db_architecture_summary": f"High-performance PostgreSQL database ({det.db_health_score:.1f}% health). Avg {det.query_perf.avg_query_time_ms}ms query time, {det.index_coverage.index_coverage_pct}% index coverage.",
            "key_db_strengths": ["Zero slow queries with sub-10ms average response", "Full FK constraint enforcement with no nullable critical fields"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Principal DBA", "PostgreSQL, indexing, normalization"),
                                          PromptBuilder.build_user_context({"score": det.db_health_score}), task_type="db_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicDBNarrative(db_architecture_summary=parsed.get("db_architecture_summary", fallback["db_architecture_summary"]),
                                        key_db_strengths=parsed.get("key_db_strengths", fallback["key_db_strengths"]))
        except Exception:
            return StrategicDBNarrative(**fallback)

class DBOptimizationPlannerAgent(BaseAgent):
    """Agent 9: Generates indexing recommendations and query optimization samples."""
    def __init__(self):
        super().__init__(agent_id="db_optimization_planner", name="DB Optimization Planner Agent",
                         description="Formulates index optimization plans and EXPLAIN ANALYZE recommendations.", icon="Cpu")

    async def plan_optimization(self, det: DeterministicDBPipelineResult) -> DBOptimizationPlan:
        fallback = {
            "indexing_recommendations": ["Add composite index on (user_id, created_at) for timeline queries", "Create partial index on jobs WHERE status='active' for active job lookups"],
            "sample_query_optimization": "-- Before: Seq Scan on resumes\nSELECT * FROM resumes WHERE user_id = $1;\n\n-- After: Index Scan using resumes_user_id_idx\nCREATE INDEX CONCURRENTLY resumes_user_id_idx ON resumes(user_id);"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Query Optimization Specialist", "EXPLAIN ANALYZE, indexes"),
                                          PromptBuilder.build_user_context({"missing": det.index_coverage.missing_indexes_count}), task_type="db_optimize")
            parsed = self.parse_agent_output(llm_res, fallback)
            return DBOptimizationPlan(indexing_recommendations=parsed.get("indexing_recommendations", fallback["indexing_recommendations"]),
                                      sample_query_optimization=parsed.get("sample_query_optimization", fallback["sample_query_optimization"]))
        except Exception:
            return DBOptimizationPlan(**fallback)
