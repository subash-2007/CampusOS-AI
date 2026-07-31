from app.agents.base_agent import BaseAgent
from departments.privacy_data_governance.deterministic import PrivacyComplianceScorerAgent
from departments.privacy_data_governance.reasoning import StrategicPrivacyNarrativeAgent, PrivacyRoadmapPlannerAgent
from departments.privacy_data_governance.schemas import PrivacyDataGovernanceOrchestratorReport, ReasoningPrivacyPipelineResult

class PrivacyDataGovernanceOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Privacy & Data Governance Department."""
    def __init__(self):
        super().__init__(agent_id="privacy_data_governance_orchestrator", name="Privacy & Data Governance Master Orchestrator",
                         description="Coordinates all 9 privacy and data governance sub-agents.", icon="ShieldCheck")
        self.scorer = PrivacyComplianceScorerAgent()
        self.narrative_agent = StrategicPrivacyNarrativeAgent()
        self.roadmap_planner = PrivacyRoadmapPlannerAgent()

    async def run_pipeline(self) -> PrivacyDataGovernanceOrchestratorReport:
        steps = ["Step 1: Running deterministic Privacy pipeline (GDPR, retention, consent, encryption, breach detection, lineage)."]
        det = self.scorer.run()
        steps.append("Step 2: Executing Strategic Privacy Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Privacy Roadmap Planner Agent.")
        roadmap = await self.roadmap_planner.plan_roadmap(det)
        steps.append("Step 4: Compiling Privacy & Data Governance Master Report.")
        tier = "FULL GDPR COMPLIANCE" if det.privacy_compliance_score >= 90 else "PARTIAL COMPLIANCE"
        return PrivacyDataGovernanceOrchestratorReport(
            privacy_tier=tier, privacy_compliance_score=det.privacy_compliance_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningPrivacyPipelineResult(narrative=narrative, roadmap=roadmap, reasoning_steps=steps),
            reasoning_steps=steps
        )
