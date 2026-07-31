from app.agents.base_agent import BaseAgent
from departments.campus_childcare_services.deterministic import CampusChildcareServicesScorerAgent
from departments.campus_childcare_services.reasoning import StrategicChildcareNarrativeAgent, FamilySupportPlannerAgent
from departments.campus_childcare_services.schemas import CampusChildcareServicesOrchestratorReport, ReasoningChildcarePipelineResult

class CampusChildcareServicesOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Campus Childcare & Family Services Department."""
    def __init__(self):
        super().__init__(agent_id="campus_childcare_services_orchestrator", name="Campus Childcare & Family Services Master Orchestrator",
                         description="Coordinates all 9 campus childcare & family services sub-agents.", icon="Heart")
        self.scorer = CampusChildcareServicesScorerAgent()
        self.narrative_agent = StrategicChildcareNarrativeAgent()
        self.family_planner = FamilySupportPlannerAgent()

    async def run_pipeline(self, children: int = 340) -> CampusChildcareServicesOrchestratorReport:
        steps = ["Step 1: Running deterministic Childcare pipeline (enrollment, subsidies, licensing, retention, infrastructure, after-school care)."]
        det = self.scorer.run(children)
        steps.append("Step 2: Executing Strategic Childcare Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Family Support Planner Agent.")
        family_plan = await self.family_planner.plan_family_support(det)
        steps.append("Step 4: Compiling Campus Childcare & Family Services Master Report.")
        tier = "GOLD-STANDARD FAMILY-FRIENDLY CAMPUS" if det.childcare_score >= 90 else "STANDARD CHILDCARE PROGRAM"
        return CampusChildcareServicesOrchestratorReport(
            family_support_tier=tier, childcare_score=det.childcare_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningChildcarePipelineResult(narrative=narrative, family_support_plan=family_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
