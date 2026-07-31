from typing import Dict, Any, List, Optional
from app.agents.base_agent import BaseAgent
from departments.peer_benchmarking.deterministic import PeerScorerAgent
from departments.peer_benchmarking.reasoning import StrategicPeerNarrativeAgent, PeerOutperformanceStrategistAgent
from departments.peer_benchmarking.schemas import (
    PeerBenchmarkingOrchestratorReport, ReasoningPeerPipelineResult
)

class PeerBenchmarkingOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator Agent for the Peer Benchmarking Department."""
    def __init__(self):
        super().__init__(
            agent_id="peer_benchmarking_orchestrator",
            name="Peer Benchmarking Master Orchestrator",
            description="Coordinates all 9 sub-agents to deliver a unified Peer Benchmark Report.",
            icon="BarChart2"
        )
        self.scorer = PeerScorerAgent()
        self.narrative_agent = StrategicPeerNarrativeAgent()
        self.strategist = PeerOutperformanceStrategistAgent()

    async def run_pipeline(self, user_skills: Optional[List[str]] = None) -> PeerBenchmarkingOrchestratorReport:
        reasoning_steps = []
        
        # Step 1: Execute Deterministic Pipeline
        reasoning_steps.append("Step 1: Running deterministic Peer Benchmarking pipeline (Cohort percentile scoring, Academic peer comparison, Skill density benchmarking, Experience velocity indexing, Open-source peer ranking, Certification rigor benchmarking).")
        det_result = self.scorer.run(user_skills)
        
        # Step 2: Execute Strategic Peer Narrative Agent
        reasoning_steps.append("Step 2: Executing Strategic Peer Narrative Agent to evaluate competitive positioning.")
        narrative = await self.narrative_agent.evaluate(det_result)
        
        # Step 3: Execute Peer Outperformance Strategist Agent
        reasoning_steps.append("Step 3: Executing Peer Outperformance Strategist Agent to formulate leverage recommendations.")
        strategy = await self.strategist.strategize(det_result)
        
        # Step 4: Synthesize Report
        reasoning_steps.append("Step 4: Compiling Peer Benchmarking Master Report.")
        reasoning_result = ReasoningPeerPipelineResult(
            narrative=narrative,
            strategy=strategy,
            reasoning_steps=reasoning_steps
        )
        
        return PeerBenchmarkingOrchestratorReport(
            cohort_tier=det_result.percentile.cohort_tier,
            composite_benchmark_score=det_result.composite_benchmark_score,
            confidence_score=det_result.confidence_score,
            deterministic_analysis=det_result,
            reasoning_analysis=reasoning_result,
            reasoning_steps=reasoning_steps
        )
