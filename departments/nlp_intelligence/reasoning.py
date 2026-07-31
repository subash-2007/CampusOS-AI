from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.nlp_intelligence.schemas import (
    StrategicNLPNarrative, NLPEnhancementPlan, ReasoningNLPPipelineResult, DeterministicNLPPipelineResult
)

class StrategicNLPNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates NLP pipeline capability maturity and linguistic coverage."""
    def __init__(self):
        super().__init__(agent_id="strategic_nlp_narrative", name="Strategic NLP Narrative Agent",
                         description="Evaluates text classification, NER, sentiment, and multilingual capabilities.", icon="MessageSquare")

    async def evaluate(self, det: DeterministicNLPPipelineResult) -> StrategicNLPNarrative:
        fallback = {
            "nlp_pipeline_summary": f"Advanced NLP capability suite ({det.nlp_capability_score:.1f}% score). {det.classification.classifier_accuracy:.0%} classification accuracy with {det.language_detection.languages_supported} language support.",
            "key_nlp_strengths": [f"NER F1={det.ner.ner_f1_score} across {det.ner.entity_types_supported} entity types", f"{det.language_detection.languages_supported} languages with {det.language_detection.detection_accuracy:.0%} detection accuracy"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("NLP Research Scientist", "text classification, NER, multilingual"),
                                          PromptBuilder.build_user_context({"score": det.nlp_capability_score}), task_type="nlp_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicNLPNarrative(nlp_pipeline_summary=parsed.get("nlp_pipeline_summary", fallback["nlp_pipeline_summary"]),
                                         key_nlp_strengths=parsed.get("key_nlp_strengths", fallback["key_nlp_strengths"]))
        except Exception:
            return StrategicNLPNarrative(**fallback)

class NLPEnhancementPlannerAgent(BaseAgent):
    """Agent 9: Generates NLP model upgrade recommendations and pipeline configs."""
    def __init__(self):
        super().__init__(agent_id="nlp_enhancement_planner", name="NLP Enhancement Planner Agent",
                         description="Formulates NLP model upgrade roadmaps and spaCy/Transformers configs.", icon="FileText")

    async def plan_enhancement(self, det: DeterministicNLPPipelineResult) -> NLPEnhancementPlan:
        fallback = {
            "model_upgrade_recommendations": ["Upgrade NER model to fine-tuned BERT-large for specialized career entities", "Add multilingual embedding support using LaBSE for 109 language coverage"],
            "sample_nlp_pipeline_config": "nlp:\n  classification_model: text-embedding-3-large\n  ner_model: campusos-ner-bert-v2\n  sentiment_model: cardiffnlp/twitter-roberta-base-sentiment\n  language_detection: fasttext-lid-176"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("NLP Engineer", "Transformers, spaCy, multilingual models"),
                                          PromptBuilder.build_user_context({"langs": det.language_detection.languages_supported}), task_type="nlp_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return NLPEnhancementPlan(model_upgrade_recommendations=parsed.get("model_upgrade_recommendations", fallback["model_upgrade_recommendations"]),
                                      sample_nlp_pipeline_config=parsed.get("sample_nlp_pipeline_config", fallback["sample_nlp_pipeline_config"]))
        except Exception:
            return NLPEnhancementPlan(**fallback)
