from app.agents.base_agent import BaseAgent
from departments.disability_services_accommodations.deterministic import DisabilityServicesAccommodationsScorerAgent
from departments.disability_services_accommodations.reasoning import StrategicDisabilityServicesNarrativeAgent, AccommodationPlannerAgent
from departments.disability_services_accommodations.schemas import DisabilityServicesAccommodationsOrchestratorReport, ReasoningDisabilityServicesPipelineResult

class DisabilityServicesAccommodationsOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Disability Services & Accommodations Department."""
    def __init__(self):
        super().__init__(agent_id="disability_services_accommodations_orchestrator", name="Disability Services & Accommodations Master Orchestrator",
                         description="Coordinates all 9 disability services & accommodations sub-agents.", icon="CheckCircle")
        self.scorer = DisabilityServicesAccommodationsScorerAgent()
        self.narrative_agent = StrategicDisabilityServicesNarrativeAgent()
        self.accommodation_planner = AccommodationPlannerAgent()

    async def run_pipeline(self, registered: int = 1420) -> DisabilityServicesAccommodationsOrchestratorReport:
        steps = ["Step 1: Running deterministic Disability Services pipeline (registrations, exam proctoring, assistive tech, physical accessibility, digital materials, grants)."]
        det = self.scorer.run(registered)
        steps.append("Step 2: Executing Strategic Disability Services Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Accommodation Planner Agent.")
        accommodations = await self.accommodation_planner.plan_accommodations(det)
        steps.append("Step 4: Compiling Disability Services & Accommodations Master Report.")
        tier = "UNIVERSAL ACCESSIBILITY EXCELLENCE" if det.disability_services_score >= 90 else "STANDARD DISABILITY SERVICES"
        return DisabilityServicesAccommodationsOrchestratorReport(
            accessibility_tier=tier, disability_services_score=det.disability_services_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningDisabilityServicesPipelineResult(narrative=narrative, accommodation_plan=accommodations, reasoning_steps=steps),
            reasoning_steps=steps
        )
