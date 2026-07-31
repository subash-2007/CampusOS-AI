from app.agents.base_agent import BaseAgent
from departments.accessibility_inclusivity_intelligence.deterministic import AccessibilityScorerAgent
from departments.accessibility_inclusivity_intelligence.reasoning import StrategicA11yNarrativeAgent, A11yRemediationPlannerAgent
from departments.accessibility_inclusivity_intelligence.schemas import AccessibilityInclusivityOrchestratorReport, ReasoningA11yPipelineResult

class AccessibilityInclusivityOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Accessibility & Inclusivity Intelligence Department."""
    def __init__(self):
        super().__init__(agent_id="accessibility_inclusivity_orchestrator", name="Accessibility & Inclusivity Intelligence Master Orchestrator",
                         description="Coordinates all 9 accessibility and inclusivity sub-agents.", icon="Heart")
        self.scorer = AccessibilityScorerAgent()
        self.narrative_agent = StrategicA11yNarrativeAgent()
        self.remediation_planner = A11yRemediationPlannerAgent()

    async def run_pipeline(self, compliance_pct: float = 96.5) -> AccessibilityInclusivityOrchestratorReport:
        steps = ["Step 1: Running deterministic Accessibility pipeline (WCAG 2.1 AA, screen reader, contrast, keyboard, inclusive language, cognitive)."]
        det = self.scorer.run(compliance_pct)
        steps.append("Step 2: Executing Strategic Accessibility Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Accessibility Remediation Planner Agent.")
        remediation = await self.remediation_planner.plan_remediation(det)
        steps.append("Step 4: Compiling Accessibility & Inclusivity Intelligence Master Report.")
        tier = "WCAG 2.1 AA COMPLIANT" if det.a11y_score >= 90 else "PARTIAL ACCESSIBILITY"
        return AccessibilityInclusivityOrchestratorReport(
            a11y_tier=tier, a11y_score=det.a11y_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningA11yPipelineResult(narrative=narrative, remediation_plan=remediation, reasoning_steps=steps),
            reasoning_steps=steps
        )
