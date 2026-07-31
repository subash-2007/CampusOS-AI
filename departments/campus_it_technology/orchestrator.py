from app.agents.base_agent import BaseAgent
from departments.campus_it_technology.deterministic import CampusITTechnologyScorerAgent
from departments.campus_it_technology.reasoning import StrategicITNarrativeAgent, ITOperationsPlannerAgent
from departments.campus_it_technology.schemas import CampusITTechnologyOrchestratorReport, ReasoningITPipelineResult

class CampusITTechnologyOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Campus IT & Technology Services Department."""
    def __init__(self):
        super().__init__(agent_id="campus_it_technology_orchestrator", name="Campus IT & Technology Services Master Orchestrator",
                         description="Coordinates all 9 campus IT & technology services sub-agents.", icon="Server")
        self.scorer = CampusITTechnologyScorerAgent()
        self.narrative_agent = StrategicITNarrativeAgent()
        self.it_planner = ITOperationsPlannerAgent()

    async def run_pipeline(self, access_points: int = 3800) -> CampusITTechnologyOrchestratorReport:
        steps = ["Step 1: Running deterministic IT pipeline (network uptime, helpdesk, SOC cybersecurity, software licensing, AV technology, DRP)."]
        det = self.scorer.run(access_points)
        steps.append("Step 2: Executing Strategic IT Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing IT Operations Planner Agent.")
        it_plan = await self.it_planner.plan_it_operations(det)
        steps.append("Step 4: Compiling Campus IT & Technology Services Master Report.")
        tier = "AWARD-WINNING DIGITAL CAMPUS TECHNOLOGY INFRASTRUCTURE" if det.it_score >= 90 else "STANDARD CAMPUS IT DEPARTMENT"
        return CampusITTechnologyOrchestratorReport(
            it_tier=tier, it_score=det.it_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningITPipelineResult(narrative=narrative, it_plan=it_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
