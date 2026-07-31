from typing import Dict, Any, List, Optional
from app.agents.base_agent import BaseAgent
from departments.cybersecurity_compliance.deterministic import CybersecurityScorerAgent
from departments.cybersecurity_compliance.reasoning import StrategicSecurityNarrativeAgent, ThreatMitigationPlannerAgent
from departments.cybersecurity_compliance.schemas import (
    CybersecurityComplianceOrchestratorReport, ReasoningSecurityPipelineResult
)

class CybersecurityComplianceOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator Agent for the Cybersecurity & Compliance Department."""
    def __init__(self):
        super().__init__(
            agent_id="cybersecurity_compliance_orchestrator",
            name="Cybersecurity & Compliance Master Orchestrator",
            description="Coordinates all 9 sub-agents to deliver a unified Cybersecurity Report.",
            icon="Key"
        )
        self.scorer = CybersecurityScorerAgent()
        self.narrative_agent = StrategicSecurityNarrativeAgent()
        self.mitigation_planner = ThreatMitigationPlannerAgent()

    async def run_pipeline(self, critical_vulnerabilities: int = 0) -> CybersecurityComplianceOrchestratorReport:
        reasoning_steps = []
        
        # Step 1: Execute Deterministic Pipeline
        reasoning_steps.append("Step 1: Running deterministic Cybersecurity & Compliance pipeline (Vulnerability scan metering, SOC2 compliance auditing, Encryption strength verification, IAM least-privilege metering, Incident response MTTD/MTTR auditing, GDPR compliance verification).")
        det_result = self.scorer.run(critical_vulnerabilities)
        
        # Step 2: Execute Strategic Security Narrative Agent
        reasoning_steps.append("Step 2: Executing Strategic Security Narrative Agent to analyze CISO security posture.")
        narrative = await self.narrative_agent.evaluate(det_result)
        
        # Step 3: Execute Threat Mitigation Planner Agent
        reasoning_steps.append("Step 3: Executing Threat Mitigation Planner Agent to formulate Zero-Trust playbooks.")
        mitigation = await self.mitigation_planner.plan_mitigation(det_result)
        
        # Step 4: Synthesize Report
        reasoning_steps.append("Step 4: Compiling Cybersecurity & Compliance Master Report.")
        reasoning_result = ReasoningSecurityPipelineResult(
            narrative=narrative,
            mitigation_plan=mitigation,
            reasoning_steps=reasoning_steps
        )
        
        tier = "ENTERPRISE HARDENED" if det_result.cybersecurity_posture_score >= 85 else "MODERATE RISK"
        
        return CybersecurityComplianceOrchestratorReport(
            security_tier=tier,
            cybersecurity_posture_score=det_result.cybersecurity_posture_score,
            confidence_score=det_result.confidence_score,
            deterministic_analysis=det_result,
            reasoning_analysis=reasoning_result,
            reasoning_steps=reasoning_steps
        )
