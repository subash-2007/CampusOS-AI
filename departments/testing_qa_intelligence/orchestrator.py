from app.agents.base_agent import BaseAgent
from departments.testing_qa_intelligence.deterministic import QAQualityScorerAgent
from departments.testing_qa_intelligence.reasoning import StrategicQANarrativeAgent, QAImprovementPlannerAgent
from departments.testing_qa_intelligence.schemas import TestingQAOrchestratorReport, ReasoningQAPipelineResult

class TestingQAOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Testing & QA Intelligence Department."""
    def __init__(self):
        super().__init__(agent_id="testing_qa_orchestrator", name="Testing & QA Intelligence Master Orchestrator",
                         description="Coordinates all 9 testing and QA sub-agents.", icon="TestTube")
        self.scorer = QAQualityScorerAgent()
        self.narrative_agent = StrategicQANarrativeAgent()
        self.improvement_planner = QAImprovementPlannerAgent()

    async def run_pipeline(self, coverage: float = 94.0) -> TestingQAOrchestratorReport:
        steps = ["Step 1: Running deterministic QA pipeline (unit coverage, integration, E2E, bug density, automation, mutation testing)."]
        det = self.scorer.run(coverage)
        steps.append("Step 2: Executing Strategic QA Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing QA Improvement Planner Agent.")
        improvement = await self.improvement_planner.plan_improvement(det)
        steps.append("Step 4: Compiling Testing & QA Intelligence Master Report.")
        tier = "ENTERPRISE QA EXCELLENCE" if det.qa_quality_score >= 85 else "STANDARD QA"
        return TestingQAOrchestratorReport(
            qa_tier=tier, qa_quality_score=det.qa_quality_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningQAPipelineResult(narrative=narrative, improvement_plan=improvement, reasoning_steps=steps),
            reasoning_steps=steps
        )
