from typing import Dict, Any, List, Optional
from app.agents.base_agent import BaseAgent
from departments.software_architecture_intelligence.deterministic import ArchitectureScorerAgent
from departments.software_architecture_intelligence.reasoning import StrategicArchitectureNarrativeAgent, ArchitecturalRefactoringPlannerAgent
from departments.software_architecture_intelligence.schemas import (
    SoftwareArchitectureOrchestratorReport, ReasoningArchitecturePipelineResult
)

class SoftwareArchitectureOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator Agent for the Software Architecture Intelligence Department."""
    def __init__(self):
        super().__init__(
            agent_id="software_architecture_orchestrator",
            name="Software Architecture Intelligence Master Orchestrator",
            description="Coordinates all 9 sub-agents to deliver a unified Software Architecture Report.",
            icon="Layers"
        )
        self.scorer = ArchitectureScorerAgent()
        self.narrative_agent = StrategicArchitectureNarrativeAgent()
        self.refactoring_planner = ArchitecturalRefactoringPlannerAgent()

    async def run_pipeline(self, complexity: float = 3.2, dup_pct: float = 1.2) -> SoftwareArchitectureOrchestratorReport:
        reasoning_steps = []
        
        # Step 1: Execute Deterministic Pipeline
        reasoning_steps.append("Step 1: Running deterministic Software Architecture Intelligence pipeline (Cyclomatic complexity metering, Afferent/efferent coupling auditing, GoF design pattern coverage identification, Microservice boundary decoupling evaluation, AST code duplication index metering, System scalability QPS benchmarking).")
        det_result = self.scorer.run(complexity, dup_pct)
        
        # Step 2: Execute Strategic Architecture Narrative Agent
        reasoning_steps.append("Step 2: Executing Strategic Architecture Narrative Agent to evaluate system design strengths.")
        narrative = await self.narrative_agent.evaluate(det_result)
        
        # Step 3: Execute Architectural Refactoring Planner Agent
        reasoning_steps.append("Step 3: Executing Architectural Refactoring Planner Agent to formulate refactoring roadmap and Mermaid diagrams.")
        refactoring_plan = await self.refactoring_planner.plan_refactoring(det_result)
        
        # Step 4: Synthesize Report
        reasoning_steps.append("Step 4: Compiling Software Architecture Intelligence Master Report.")
        reasoning_result = ReasoningArchitecturePipelineResult(
            narrative=narrative,
            refactoring_plan=refactoring_plan,
            reasoning_steps=reasoning_steps
        )
        
        tier = "ENTERPRISE ARCHITECTURE" if det_result.architecture_health_score >= 85 else "MODULAR CODEBASE"
        
        return SoftwareArchitectureOrchestratorReport(
            architecture_tier=tier,
            architecture_health_score=det_result.architecture_health_score,
            confidence_score=det_result.confidence_score,
            deterministic_analysis=det_result,
            reasoning_analysis=reasoning_result,
            reasoning_steps=reasoning_steps
        )
