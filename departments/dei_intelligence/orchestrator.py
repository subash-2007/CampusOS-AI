from app.agents.base_agent import BaseAgent
from departments.dei_intelligence.deterministic import DiversityEquityInclusionScorerAgent
from departments.dei_intelligence.reasoning import StrategicDEINarrativeAgent, DEIActionPlannerAgent
from departments.dei_intelligence.schemas import DiversityEquityInclusionOrchestratorReport, ReasoningDEIPipelineResult

class DiversityEquityInclusionOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Diversity Equity & Inclusion Department."""
    def __init__(self):
        super().__init__(agent_id="dei_intelligence_orchestrator", name="Diversity Equity & Inclusion Master Orchestrator",
                         description="Coordinates all 9 diversity equity & inclusion sub-agents.", icon="Users")
        self.scorer = DiversityEquityInclusionScorerAgent()
        self.narrative_agent = StrategicDEINarrativeAgent()
        self.dei_planner = DEIActionPlannerAgent()

    async def run_pipeline(self, urm_pct: float = 34.8) -> DiversityEquityInclusionOrchestratorReport:
        steps = ["Step 1: Running deterministic DEI pipeline (demographics, faculty diversity, cultural centers, inclusive curriculum, bias response, scholarships)."]
        det = self.scorer.run(urm_pct)
        steps.append("Step 2: Executing Strategic DEI Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing DEI Action Planner Agent.")
        action_plan = await self.dei_planner.plan_dei(det)
        steps.append("Step 4: Compiling Diversity Equity & Inclusion Master Report.")
        tier = "NATIONAL MODEL FOR INCLUSIVE EXCELLENCE" if det.dei_score >= 90 else "STANDARD DEI PROGRAM"
        return DiversityEquityInclusionOrchestratorReport(
            dei_tier=tier, dei_score=det.dei_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningDEIPipelineResult(narrative=narrative, action_plan=action_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
