from app.agents.base_agent import BaseAgent
from departments.student_legal_advocacy.deterministic import StudentLegalAdvocacyScorerAgent
from departments.student_legal_advocacy.reasoning import StrategicLegalNarrativeAgent, LegalAdvocacyPlannerAgent
from departments.student_legal_advocacy.schemas import StudentLegalAdvocacyOrchestratorReport, ReasoningLegalPipelineResult

class StudentLegalAdvocacyOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Student Legal & Advocacy Services Department."""
    def __init__(self):
        super().__init__(agent_id="student_legal_advocacy_orchestrator", name="Student Legal & Advocacy Services Master Orchestrator",
                         description="Coordinates all 9 student legal & advocacy sub-agents.", icon="Shield")
        self.scorer = StudentLegalAdvocacyScorerAgent()
        self.narrative_agent = StrategicLegalNarrativeAgent()
        self.advocacy_planner = LegalAdvocacyPlannerAgent()

    async def run_pipeline(self, consultations: int = 1420) -> StudentLegalAdvocacyOrchestratorReport:
        steps = ["Step 1: Running deterministic Legal Advocacy pipeline (consultations, housing disputes, immigration support, consumer debt, conduct representation, literacy workshops)."]
        det = self.scorer.run(consultations)
        steps.append("Step 2: Executing Strategic Legal Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Legal Advocacy Planner Agent.")
        advocacy_plan = await self.advocacy_planner.plan_advocacy(det)
        steps.append("Step 4: Compiling Student Legal & Advocacy Services Master Report.")
        tier = "COMPREHENSIVE STUDENT LEGAL DEFENSE" if det.legal_advocacy_score >= 90 else "STANDARD STUDENT LEGAL AID"
        return StudentLegalAdvocacyOrchestratorReport(
            advocacy_tier=tier, legal_advocacy_score=det.legal_advocacy_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningLegalPipelineResult(narrative=narrative, advocacy_plan=advocacy_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
