from typing import Dict, Any, List, Optional
from app.agents.base_agent import BaseAgent
from departments.ui_ux_design_intelligence.deterministic import DesignScorerAgent
from departments.ui_ux_design_intelligence.reasoning import StrategicDesignNarrativeAgent, DesignSystemAuditPlannerAgent
from departments.ui_ux_design_intelligence.schemas import (
    UIUXDesignOrchestratorReport, ReasoningDesignPipelineResult
)

class UIUXDesignOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator Agent for the UI/UX Design Intelligence Department."""
    def __init__(self):
        super().__init__(
            agent_id="ui_ux_design_orchestrator",
            name="UI/UX Design Intelligence Master Orchestrator",
            description="Coordinates all 9 sub-agents to deliver a unified UI/UX Design Report.",
            icon="Layout"
        )
        self.scorer = DesignScorerAgent()
        self.narrative_agent = StrategicDesignNarrativeAgent()
        self.audit_planner = DesignSystemAuditPlannerAgent()

    async def run_pipeline(self, contrast: float = 7.5, token_pct: float = 94.0) -> UIUXDesignOrchestratorReport:
        reasoning_steps = []
        
        # Step 1: Execute Deterministic Pipeline
        reasoning_steps.append("Step 1: Running deterministic UI/UX Design Intelligence pipeline (WCAG 2.1 AAA accessibility contrast auditing, Design system token coverage metering, Usability task success rate evaluation, User flow friction index scoring, Typography 8-point grid alignment auditing, Micro-animation 60 FPS performance metering).")
        det_result = self.scorer.run(contrast, token_pct)
        
        # Step 2: Execute Strategic Design Narrative Agent
        reasoning_steps.append("Step 2: Executing Strategic Design Narrative Agent to evaluate design aesthetics highlights.")
        narrative = await self.narrative_agent.evaluate(det_result)
        
        # Step 3: Execute Design System Audit Planner Agent
        reasoning_steps.append("Step 3: Executing Design System Audit Planner Agent to formulate Figma token sync recommendations.")
        audit_plan = await self.audit_planner.plan_audit(det_result)
        
        # Step 4: Synthesize Report
        reasoning_steps.append("Step 4: Compiling UI/UX Design Intelligence Master Report.")
        reasoning_result = ReasoningDesignPipelineResult(
            narrative=narrative,
            audit_plan=audit_plan,
            reasoning_steps=reasoning_steps
        )
        
        tier = "PREMIUM AAA DESIGN" if det_result.design_quality_score >= 85 else "STANDARD UI"
        
        return UIUXDesignOrchestratorReport(
            design_tier=tier,
            design_quality_score=det_result.design_quality_score,
            confidence_score=det_result.confidence_score,
            deterministic_analysis=det_result,
            reasoning_analysis=reasoning_result,
            reasoning_steps=reasoning_steps
        )
