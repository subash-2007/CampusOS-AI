from app.agents.base_agent import BaseAgent
from departments.institutional_research_accreditation.deterministic import InstitutionalResearchAccreditationScorerAgent
from departments.institutional_research_accreditation.reasoning import StrategicResearchNarrativeAgent, AccreditationCompliancePlannerAgent
from departments.institutional_research_accreditation.schemas import InstitutionalResearchAccreditationOrchestratorReport, ReasoningResearchPipelineResult

class InstitutionalResearchAccreditationOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Institutional Research & Accreditation Department."""
    def __init__(self):
        super().__init__(agent_id="institutional_research_accreditation_orchestrator", name="Institutional Research & Accreditation Master Orchestrator",
                         description="Coordinates all 9 institutional research & accreditation sub-agents.", icon="Award")
        self.scorer = InstitutionalResearchAccreditationScorerAgent()
        self.narrative_agent = StrategicResearchNarrativeAgent()
        self.accreditation_planner = AccreditationCompliancePlannerAgent()

    async def run_pipeline(self) -> InstitutionalResearchAccreditationOrchestratorReport:
        steps = ["Step 1: Running deterministic Accreditation pipeline (IPEDS, SACSCOC, graduation/retention rates, SLO assessment, faculty credentials, institutional effectiveness)."]
        det = self.scorer.run()
        steps.append("Step 2: Executing Strategic Research Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Accreditation Compliance Planner Agent.")
        accreditation_plan = await self.accreditation_planner.plan_accreditation(det)
        steps.append("Step 4: Compiling Institutional Research & Accreditation Master Report.")
        tier = "GOLD STANDARD ACCREDITED INSTITUTION" if det.research_score >= 90 else "STANDARD ACCREDITED INSTITUTION"
        return InstitutionalResearchAccreditationOrchestratorReport(
            accreditation_tier=tier, research_score=det.research_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningResearchPipelineResult(narrative=narrative, accreditation_plan=accreditation_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
