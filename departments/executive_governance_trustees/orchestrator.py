from app.agents.base_agent import BaseAgent
from departments.executive_governance_trustees.deterministic import ExecutiveGovernanceTrusteesScorerAgent
from departments.executive_governance_trustees.reasoning import StrategicGovernanceNarrativeAgent, GovernanceOperationsPlannerAgent
from departments.executive_governance_trustees.schemas import ExecutiveGovernanceTrusteesOrchestratorReport, ReasoningGovernancePipelineResult

class ExecutiveGovernanceTrusteesOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Executive Governance and Board of Trustees Intelligence Department."""
    def __init__(self):
        super().__init__(agent_id="executive_governance_trustees_orchestrator", name="Executive Governance and Board of Trustees Intelligence Master Orchestrator",
                         description="Coordinates all 9 sub-agents for Executive Governance and Board of Trustees Intelligence.", icon="Cpu")
        self.scorer = ExecutiveGovernanceTrusteesScorerAgent()
        self.narrative_agent = StrategicGovernanceNarrativeAgent()
        self.planner = GovernanceOperationsPlannerAgent()

    async def run_pipeline(self) -> ExecutiveGovernanceTrusteesOrchestratorReport:
        steps = ["Step 1: Running deterministic pipeline."]
        det = self.scorer.run()
        steps.append("Step 2: Executing Strategic Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Operations Planner Agent.")
        plan = await self.planner.plan_operations(det)
        steps.append("Step 4: Compiling Master Orchestrator Report.")
        return ExecutiveGovernanceTrusteesOrchestratorReport(
            tier="GOLD STANDARD HIGHER EDUCATION GOVERNANCE AND EXECUTIVE LEADERSHIP", governance_score=det.governance_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningGovernancePipelineResult(narrative=narrative, plan=plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
