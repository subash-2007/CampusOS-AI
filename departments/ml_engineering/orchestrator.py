from app.agents.base_agent import BaseAgent
from departments.ml_engineering.deterministic import MLEngineeringScorerAgent
from departments.ml_engineering.reasoning import StrategicMLNarrativeAgent, MLRetrainingPlannerAgent
from departments.ml_engineering.schemas import MLEngineeringOrchestratorReport, ReasoningMLPipelineResult

class MLEngineeringOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for ML Engineering Department."""
    def __init__(self):
        super().__init__(agent_id="ml_engineering_orchestrator", name="ML Engineering Master Orchestrator",
                         description="Coordinates all 9 ML engineering sub-agents.", icon="Activity")
        self.scorer = MLEngineeringScorerAgent()
        self.narrative_agent = StrategicMLNarrativeAgent()
        self.retraining_planner = MLRetrainingPlannerAgent()

    async def run_pipeline(self, train_loss: float = 0.042, f1: float = 0.94) -> MLEngineeringOrchestratorReport:
        steps = ["Step 1: Running deterministic ML Engineering pipeline (training loss, F1 accuracy, feature audit, versioning, inference throughput, fairness)."]
        det = self.scorer.run(train_loss, f1)
        steps.append("Step 2: Executing Strategic ML Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing ML Retraining Planner Agent.")
        retraining = await self.retraining_planner.plan_retraining(det)
        steps.append("Step 4: Compiling ML Engineering Master Report.")
        tier = "PRODUCTION ML PIPELINE" if det.ml_engineering_score >= 85 else "EXPERIMENTAL PIPELINE"
        return MLEngineeringOrchestratorReport(
            ml_tier=tier, ml_engineering_score=det.ml_engineering_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningMLPipelineResult(narrative=narrative, retraining_plan=retraining, reasoning_steps=steps),
            reasoning_steps=steps
        )
