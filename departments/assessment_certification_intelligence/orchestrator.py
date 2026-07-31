from app.agents.base_agent import BaseAgent
from departments.assessment_certification_intelligence.deterministic import AssessmentCertificationScorerAgent
from departments.assessment_certification_intelligence.reasoning import StrategicAssessmentNarrativeAgent, CertificationExpansionPlannerAgent
from departments.assessment_certification_intelligence.schemas import AssessmentCertificationOrchestratorReport, ReasoningAssessmentPipelineResult

class AssessmentCertificationOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Assessment & Certification Intelligence Department."""
    def __init__(self):
        super().__init__(agent_id="assessment_certification_orchestrator", name="Assessment & Certification Intelligence Master Orchestrator",
                         description="Coordinates all 9 assessment and certification sub-agents.", icon="Award")
        self.scorer = AssessmentCertificationScorerAgent()
        self.narrative_agent = StrategicAssessmentNarrativeAgent()
        self.expansion_planner = CertificationExpansionPlannerAgent()

    async def run_pipeline(self, total_certs: int = 1250) -> AssessmentCertificationOrchestratorReport:
        steps = ["Step 1: Running deterministic Assessment pipeline (validity, proctoring, verification, difficulty, issuance, taxonomy)."]
        det = self.scorer.run(total_certs)
        steps.append("Step 2: Executing Strategic Assessment Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Certification Expansion Planner Agent.")
        expansion = await self.expansion_planner.plan_expansion(det)
        steps.append("Step 4: Compiling Assessment & Certification Intelligence Master Report.")
        tier = "ENTERPRISE CERTIFICATION ENGINE" if det.assessment_health_score >= 85 else "STANDARD CERTIFICATION ENGINE"
        return AssessmentCertificationOrchestratorReport(
            assessment_tier=tier, assessment_health_score=det.assessment_health_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningAssessmentPipelineResult(narrative=narrative, expansion_plan=expansion, reasoning_steps=steps),
            reasoning_steps=steps
        )
