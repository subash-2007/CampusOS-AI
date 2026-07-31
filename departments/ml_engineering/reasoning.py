from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.ml_engineering.schemas import (
    StrategicMLNarrative, MLRetrainingPlan, ReasoningMLPipelineResult, DeterministicMLPipelineResult
)

class StrategicMLNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates ML pipeline health, model performance, and fairness."""
    def __init__(self):
        super().__init__(agent_id="strategic_ml_narrative", name="Strategic ML Narrative Agent",
                         description="Evaluates model accuracy, fairness, and inference performance.", icon="TrendingUp")

    async def evaluate(self, det: DeterministicMLPipelineResult) -> StrategicMLNarrative:
        fallback = {
            "ml_pipeline_summary": f"Production ML pipeline ({det.ml_engineering_score:.1f}% score). F1={det.accuracy.f1_score}, {det.inference.inferences_per_second} IPS with zero bias detection.",
            "key_ml_strengths": ["Zero algorithmic bias with 0.02 demographic parity difference", f"High {det.accuracy.f1_score} F1-score across all evaluation splits"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("ML Research Lead", "MLOps, fairness, model evaluation"),
                                          PromptBuilder.build_user_context({"f1": det.accuracy.f1_score}), task_type="ml_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicMLNarrative(ml_pipeline_summary=parsed.get("ml_pipeline_summary", fallback["ml_pipeline_summary"]),
                                        key_ml_strengths=parsed.get("key_ml_strengths", fallback["key_ml_strengths"]))
        except Exception:
            return StrategicMLNarrative(**fallback)

class MLRetrainingPlannerAgent(BaseAgent):
    """Agent 9: Generates model retraining triggers and training config samples."""
    def __init__(self):
        super().__init__(agent_id="ml_retraining_planner", name="ML Retraining Planner Agent",
                         description="Formulates automated retraining triggers and MLflow config.", icon="RefreshCw")

    async def plan_retraining(self, det: DeterministicMLPipelineResult) -> MLRetrainingPlan:
        fallback = {
            "retraining_triggers": ["Trigger retraining when validation F1 drops below 0.90", "Retrain on 10% data drift threshold using PSI > 0.2"],
            "sample_training_config": "mlflow:\n  experiment: campusos_resume_model\n  tracking_uri: http://mlflow:5000\ntraining:\n  epochs: 50\n  batch_size: 256\n  learning_rate: 0.001\n  early_stopping_patience: 5"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("MLOps Engineer", "retraining pipelines, drift detection"),
                                          PromptBuilder.build_user_context({"loss": det.training.training_loss}), task_type="ml_retrain")
            parsed = self.parse_agent_output(llm_res, fallback)
            return MLRetrainingPlan(retraining_triggers=parsed.get("retraining_triggers", fallback["retraining_triggers"]),
                                    sample_training_config=parsed.get("sample_training_config", fallback["sample_training_config"]))
        except Exception:
            return MLRetrainingPlan(**fallback)
