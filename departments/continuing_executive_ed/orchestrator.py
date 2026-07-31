from app.agents.base_agent import BaseAgent
from departments.continuing_executive_ed.deterministic import ContinuingExecutiveEdScorerAgent
from departments.continuing_executive_ed.reasoning import StrategicExecEdNarrativeAgent, ExecEdPortfolioPlannerAgent
from departments.continuing_executive_ed.schemas import ContinuingExecutiveEdOrchestratorReport, ReasoningExecEdPipelineResult

class ContinuingExecutiveEdOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Continuing Education & Executive Ed Department."""
    def __init__(self):
        super().__init__(agent_id="continuing_executive_ed_orchestrator", name="Continuing Education & Executive Ed Master Orchestrator",
                         description="Coordinates all 9 continuing & executive ed sub-agents.", icon="Briefcase")
        self.scorer = ContinuingExecutiveEdScorerAgent()
        self.narrative_agent = StrategicExecEdNarrativeAgent()
        self.portfolio_planner = ExecEdPortfolioPlannerAgent()

    async def run_pipeline(self, learners: int = 1850) -> ContinuingExecutiveEdOrchestratorReport:
        steps = ["Step 1: Running deterministic Executive Ed pipeline (enrollment, certificates, B2B revenue, CEUs, NPS, career promotions)."]
        det = self.scorer.run(learners)
        steps.append("Step 2: Executing Strategic Exec Ed Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Exec Ed Portfolio Planner Agent.")
        portfolio = await self.portfolio_planner.plan_portfolio(det)
        steps.append("Step 4: Compiling Continuing Education & Executive Ed Master Report.")
        tier = "PREMIER ENTERPRISE EXECUTIVE ACADEMY" if det.exec_ed_score >= 85 else "GROWING EXECUTIVE EDUCATION CENTER"
        return ContinuingExecutiveEdOrchestratorReport(
            exec_ed_tier=tier, exec_ed_score=det.exec_ed_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningExecEdPipelineResult(narrative=narrative, portfolio_plan=portfolio, reasoning_steps=steps),
            reasoning_steps=steps
        )
