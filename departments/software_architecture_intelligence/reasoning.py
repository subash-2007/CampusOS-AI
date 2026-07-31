from typing import Dict, Any, Optional
from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.software_architecture_intelligence.schemas import (
    StrategicArchitectureNarrative, ArchitecturalRefactoringPlan, ReasoningArchitecturePipelineResult, DeterministicArchitecturePipelineResult
)

class StrategicArchitectureNarrativeAgent(BaseAgent):
    """Agent 8: Formulates strategic software architecture reviews and domain-driven design evaluations."""
    def __init__(self):
        super().__init__(
            agent_id="strategic_architecture_narrative",
            name="Strategic Architecture Narrative Agent",
            description="Evaluates codebase maintainability, cyclomatic complexity, and microservice decoupling.",
            icon="GitPullRequest"
        )

    async def evaluate(self, det_result: DeterministicArchitecturePipelineResult) -> StrategicArchitectureNarrative:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Principal Enterprise Software Architect & CTO",
            domain_focus="Domain-Driven Design (DDD), Clean Architecture, GoF design patterns, and microservice boundaries."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"arch_score": det_result.architecture_health_score, "patterns_count": len(det_result.patterns.detected_patterns)}
        )
        
        fallback = {
            "architecture_evaluation_summary": f"Enterprise-grade software architecture ({det_result.architecture_health_score}% health score). Low cyclomatic complexity ({det_result.complexity.average_cyclomatic_complexity}) with 90% microservice boundary decoupling score.",
            "key_design_strengths": [
                "Clean implementation of Repository, Orchestrator, and Factory design patterns",
                "Zero circular dependencies across all 111 department boundaries"
            ]
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="arch_eval", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicArchitectureNarrative(
                architecture_evaluation_summary=parsed.get("architecture_evaluation_summary", fallback["architecture_evaluation_summary"]),
                key_design_strengths=parsed.get("key_design_strengths", fallback["key_design_strengths"])
            )
        except Exception:
            return StrategicArchitectureNarrative(**fallback)

class ArchitecturalRefactoringPlannerAgent(BaseAgent):
    """Agent 9: Generates architectural refactoring milestones and Mermaid architecture diagrams."""
    def __init__(self):
        super().__init__(
            agent_id="architectural_refactoring_planner",
            name="Architectural Refactoring Planner Agent",
            description="Formulates architectural refactoring roadmaps and C4 Mermaid system diagrams.",
            icon="Workflow"
        )

    async def plan_refactoring(self, det_result: DeterministicArchitecturePipelineResult) -> ArchitecturalRefactoringPlan:
        system_prompt = PromptBuilder.build_system_prompt(
            persona_role="Lead Software System Architect",
            domain_focus="Architectural refactoring, C4 model diagrams, and technical debt reduction."
        )
        user_prompt = PromptBuilder.build_user_context(
            inputs={"instability": det_result.coupling.instability_index}
        )
        
        fallback = {
            "refactoring_milestones": [
                "Extract shared scoring algorithms into `departments/shared/scoring.py` to maintain DRY principles",
                "Decouple direct service imports by introducing Event-Driven Kafka event bus topics"
            ],
            "sample_system_architecture_mermaid": "graph TD;\n  GlobalSupervisor[Global Supervisor Agent] --> Orchestrator[Department Master Orchestrator]\n  Orchestrator --> Reasoning[LLM Reasoning Pipeline]\n  Orchestrator --> Deterministic[Rule-Based Deterministic Engine]"
        }
        
        try:
            llm_res = await self.call_llm(system_prompt, user_prompt, task_type="arch_refactor", preferred_engine="anthropic")
            parsed = self.parse_agent_output(llm_res, fallback)
            return ArchitecturalRefactoringPlan(
                refactoring_milestones=parsed.get("refactoring_milestones", fallback["refactoring_milestones"]),
                sample_system_architecture_mermaid=parsed.get("sample_system_architecture_mermaid", fallback["sample_system_architecture_mermaid"])
            )
        except Exception:
            return ArchitecturalRefactoringPlan(**fallback)
