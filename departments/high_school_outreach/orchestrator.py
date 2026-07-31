from app.agents.base_agent import BaseAgent
from departments.high_school_outreach.deterministic import HighSchoolOutreachScorerAgent
from departments.high_school_outreach.reasoning import StrategicOutreachNarrativeAgent, OutreachExpansionPlannerAgent
from departments.high_school_outreach.schemas import HighSchoolOutreachOrchestratorReport, ReasoningOutreachPipelineResult

class HighSchoolOutreachOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for High School & K-12 Outreach Department."""
    def __init__(self):
        super().__init__(agent_id="high_school_outreach_orchestrator", name="High School & K-12 Outreach Master Orchestrator",
                         description="Coordinates all 9 K-12 outreach sub-agents.", icon="Compass")
        self.scorer = HighSchoolOutreachScorerAgent()
        self.narrative_agent = StrategicOutreachNarrativeAgent()
        self.expansion_planner = OutreachExpansionPlannerAgent()

    async def run_pipeline(self, schools: int = 184) -> HighSchoolOutreachOrchestratorReport:
        steps = ["Step 1: Running deterministic High School Outreach pipeline (partnerships, STEM programs, dual enrollment, campus tours, counselor portal, scholarships)."]
        det = self.scorer.run(schools)
        steps.append("Step 2: Executing Strategic Outreach Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Outreach Expansion Planner Agent.")
        expansion = await self.expansion_planner.plan_expansion(det)
        steps.append("Step 4: Compiling High School & K-12 Outreach Master Report.")
        tier = "STRATEGIC PIPELINE FEEDER" if det.outreach_health_score >= 80 else "GROWING OUTREACH PIPELINE"
        return HighSchoolOutreachOrchestratorReport(
            outreach_tier=tier, outreach_health_score=det.outreach_health_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningOutreachPipelineResult(narrative=narrative, expansion_plan=expansion, reasoning_steps=steps),
            reasoning_steps=steps
        )
