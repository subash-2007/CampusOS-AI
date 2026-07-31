from app.agents.base_agent import BaseAgent
from departments.nlp_intelligence.deterministic import NLPCapabilityScorerAgent
from departments.nlp_intelligence.reasoning import StrategicNLPNarrativeAgent, NLPEnhancementPlannerAgent
from departments.nlp_intelligence.schemas import NLPIntelligenceOrchestratorReport, ReasoningNLPPipelineResult

class NLPIntelligenceOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for NLP Intelligence Department."""
    def __init__(self):
        super().__init__(agent_id="nlp_intelligence_orchestrator", name="NLP Intelligence Master Orchestrator",
                         description="Coordinates all 9 NLP intelligence sub-agents.", icon="Brain")
        self.scorer = NLPCapabilityScorerAgent()
        self.narrative_agent = StrategicNLPNarrativeAgent()
        self.enhancement_planner = NLPEnhancementPlannerAgent()

    async def run_pipeline(self, clf_acc: float = 0.96, ner_f1: float = 0.92) -> NLPIntelligenceOrchestratorReport:
        steps = ["Step 1: Running deterministic NLP pipeline (classification, sentiment, NER, similarity, language detection, summarization)."]
        det = self.scorer.run(clf_acc, ner_f1)
        steps.append("Step 2: Executing Strategic NLP Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing NLP Enhancement Planner Agent.")
        enhancement = await self.enhancement_planner.plan_enhancement(det)
        steps.append("Step 4: Compiling NLP Intelligence Master Report.")
        tier = "ADVANCED NLP CAPABILITY" if det.nlp_capability_score >= 85 else "STANDARD NLP"
        return NLPIntelligenceOrchestratorReport(
            nlp_tier=tier, nlp_capability_score=det.nlp_capability_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningNLPPipelineResult(narrative=narrative, enhancement_plan=enhancement, reasoning_steps=steps),
            reasoning_steps=steps
        )
