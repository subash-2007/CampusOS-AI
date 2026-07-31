from app.agents.base_agent import BaseAgent
from departments.environmental_health_safety.deterministic import EnvironmentalHealthSafetyComplianceScorerAgent
from departments.environmental_health_safety.reasoning import StrategicEHSNarrativeAgent, EHSCompliancePlannerAgent
from departments.environmental_health_safety.schemas import EnvironmentalHealthSafetyOrchestratorReport, ReasoningEHSPipelineResult

class EnvironmentalHealthSafetyOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Environmental Health and Safety Compliance Department."""
    def __init__(self):
        super().__init__(agent_id="environmental_health_safety_orchestrator", name="Environmental Health and Safety Compliance Master Orchestrator",
                         description="Coordinates all 9 environmental health and safety compliance sub-agents.", icon="AlertCircle")
        self.scorer = EnvironmentalHealthSafetyComplianceScorerAgent()
        self.narrative_agent = StrategicEHSNarrativeAgent()
        self.ehs_planner = EHSCompliancePlannerAgent()

    async def run_pipeline(self) -> EnvironmentalHealthSafetyOrchestratorReport:
        steps = ["Step 1: Running deterministic EHS pipeline (chemical inventory, OSHA training, EPA wastewater, biosafety IBC, fire inspections, ADA accessibility)."]
        det = self.scorer.run()
        steps.append("Step 2: Executing Strategic EHS Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing EHS Compliance Planner Agent.")
        ehs_plan = await self.ehs_planner.plan_ehs_compliance(det)
        steps.append("Step 4: Compiling Environmental Health and Safety Compliance Master Report.")
        tier = "EPA AND OSHA MODEL COMPLIANCE INSTITUTION" if det.ehs_score >= 90 else "STANDARD EHS COMPLIANCE DEPARTMENT"
        return EnvironmentalHealthSafetyOrchestratorReport(
            ehs_tier=tier, ehs_score=det.ehs_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningEHSPipelineResult(narrative=narrative, ehs_plan=ehs_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
