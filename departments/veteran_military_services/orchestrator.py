from app.agents.base_agent import BaseAgent
from departments.veteran_military_services.deterministic import VeteranMilitaryServicesScorerAgent
from departments.veteran_military_services.reasoning import StrategicVeteranNarrativeAgent, VeteranTransitionPlannerAgent
from departments.veteran_military_services.schemas import VeteranMilitaryServicesOrchestratorReport, ReasoningVeteranServicesPipelineResult

class VeteranMilitaryServicesOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Veteran & Military Student Services Department."""
    def __init__(self):
        super().__init__(agent_id="veteran_military_services_orchestrator", name="Veteran & Military Student Services Master Orchestrator",
                         description="Coordinates all 9 veteran & military services sub-agents.", icon="Award")
        self.scorer = VeteranMilitaryServicesScorerAgent()
        self.narrative_agent = StrategicVeteranNarrativeAgent()
        self.transition_planner = VeteranTransitionPlannerAgent()

    async def run_pipeline(self, veterans: int = 680) -> VeteranMilitaryServicesOrchestratorReport:
        steps = ["Step 1: Running deterministic Veteran Services pipeline (enrollment, GI Bill, Yellow Ribbon, JST transcripts, Veteran Resource Center, outcomes)."]
        det = self.scorer.run(veterans)
        steps.append("Step 2: Executing Strategic Veteran Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Veteran Transition Planner Agent.")
        transition = await self.transition_planner.plan_transition(det)
        steps.append("Step 4: Compiling Veteran & Military Student Services Master Report.")
        tier = "MILITARY FRIENDLY TOP-TEN CAMPUS" if det.veteran_services_score >= 88 else "STANDARD MILITARY STUDENT PROGRAM"
        return VeteranMilitaryServicesOrchestratorReport(
            military_friendly_tier=tier, veteran_services_score=det.veteran_services_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningVeteranServicesPipelineResult(narrative=narrative, transition_plan=transition, reasoning_steps=steps),
            reasoning_steps=steps
        )
