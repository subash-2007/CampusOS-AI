from app.agents.base_agent import BaseAgent
from departments.student_financial_aid_intelligence.deterministic import StudentFinancialAidScorerAgent
from departments.student_financial_aid_intelligence.reasoning import StrategicFinancialAidNarrativeAgent, FinancialAidOptimizationPlannerAgent
from departments.student_financial_aid_intelligence.schemas import StudentFinancialAidOrchestratorReport, ReasoningFinancialAidResult

class StudentFinancialAidOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Student Financial Aid Intelligence Department."""
    def __init__(self):
        super().__init__(agent_id="student_financial_aid_orchestrator", name="Student Financial Aid Intelligence Master Orchestrator",
                         description="Coordinates all 9 financial aid sub-agents.", icon="DollarSign")
        self.scorer = StudentFinancialAidScorerAgent()
        self.narrative_agent = StrategicFinancialAidNarrativeAgent()
        self.optimization_planner = FinancialAidOptimizationPlannerAgent()

    async def run_pipeline(self, matches: int = 480) -> StudentFinancialAidOrchestratorReport:
        steps = ["Step 1: Running deterministic Financial Aid pipeline (scholarship match, FAFSA compliance, loan burden, disbursement, work-study, emergency grants)."]
        det = self.scorer.run(matches)
        steps.append("Step 2: Executing Strategic Financial Aid Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Financial Aid Optimization Planner Agent.")
        optimization = await self.optimization_planner.plan_optimization(det)
        steps.append("Step 4: Compiling Student Financial Aid Intelligence Master Report.")
        tier = "EQUITABLE FINANCIAL AID PLATFORM" if det.financial_aid_score >= 85 else "STANDARD FINANCIAL AID"
        return StudentFinancialAidOrchestratorReport(
            financial_aid_tier=tier, financial_aid_score=det.financial_aid_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningFinancialAidResult(narrative=narrative, optimization_plan=optimization, reasoning_steps=steps),
            reasoning_steps=steps
        )
