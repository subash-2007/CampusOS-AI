from app.agents.base_agent import BaseAgent
from departments.financial_aid_scholarships.deterministic import FinancialAidScholarshipsScorerAgent
from departments.financial_aid_scholarships.reasoning import StrategicFinancialAidNarrativeAgent, FinancialAidOperationsPlannerAgent
from departments.financial_aid_scholarships.schemas import FinancialAidScholarshipsOrchestratorReport, ReasoningFinancialAidPipelineResult

class FinancialAidScholarshipsOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Financial Aid & Scholarships Department."""
    def __init__(self):
        super().__init__(agent_id="financial_aid_scholarships_orchestrator", name="Financial Aid & Scholarships Master Orchestrator",
                         description="Coordinates all 9 financial aid & scholarships sub-agents.", icon="DollarSign")
        self.scorer = FinancialAidScholarshipsScorerAgent()
        self.narrative_agent = StrategicFinancialAidNarrativeAgent()
        self.aid_planner = FinancialAidOperationsPlannerAgent()

    async def run_pipeline(self, apps: int = 16800) -> FinancialAidScholarshipsOrchestratorReport:
        steps = ["Step 1: Running deterministic Financial Aid pipeline (FAFSA processing, scholarships, Title IV federal loans, SAP standards, emergency aid, loan default rate)."]
        det = self.scorer.run(apps)
        steps.append("Step 2: Executing Strategic Financial Aid Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Financial Aid Operations Planner Agent.")
        aid_plan = await self.aid_planner.plan_financial_aid(det)
        steps.append("Step 4: Compiling Financial Aid & Scholarships Master Report.")
        tier = "MODEL STUDENT FINANCIAL AID PROGRAM" if det.financial_aid_score >= 90 else "STANDARD FINANCIAL AID OFFICE"
        return FinancialAidScholarshipsOrchestratorReport(
            financial_aid_tier=tier, financial_aid_score=det.financial_aid_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningFinancialAidPipelineResult(narrative=narrative, aid_plan=aid_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
