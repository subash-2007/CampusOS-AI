from typing import Dict, Any, List, Optional
from app.agents.base_agent import BaseAgent
from departments.alumni_network_intelligence.deterministic import AlumniScorerAgent
from departments.alumni_network_intelligence.reasoning import StrategicAlumniOutreachNarrativeAgent, OutreachIntroScriptGeneratorAgent
from departments.alumni_network_intelligence.schemas import (
    AlumniNetworkOrchestratorReport, ReasoningAlumniPipelineResult
)

class AlumniNetworkOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator Agent for the Alumni Network Intelligence Department."""
    def __init__(self):
        super().__init__(
            agent_id="alumni_network_orchestrator",
            name="Alumni Network Intelligence Master Orchestrator",
            description="Coordinates all 9 sub-agents to deliver a unified Alumni Network Report.",
            icon="Users"
        )
        self.scorer = AlumniScorerAgent()
        self.narrative_agent = StrategicAlumniOutreachNarrativeAgent()
        self.script_generator = OutreachIntroScriptGeneratorAgent()

    async def run_pipeline(
        self,
        company_name: str = "Google",
        university: str = "Stanford University"
    ) -> AlumniNetworkOrchestratorReport:
        reasoning_steps = []
        
        # Step 1: Execute Deterministic Pipeline
        reasoning_steps.append("Step 1: Running deterministic Alumni Network Intelligence pipeline (Alumni directory matching, Referral likelihood scoring, Shared background overlap detection, Outreach response rate metering, Alumni seniority distribution mapping, Geographic alumni density scoring).")
        det_result = self.scorer.run(company_name, university)
        
        # Step 2: Execute Strategic Alumni Outreach Narrative Agent
        reasoning_steps.append("Step 2: Executing Strategic Alumni Outreach Narrative Agent to map referral paths.")
        narrative = await self.narrative_agent.evaluate(company_name, det_result)
        
        # Step 3: Execute Outreach Intro Script Generator Agent
        reasoning_steps.append("Step 3: Executing Outreach Intro Script Generator Agent to generate warm introduction drafts.")
        script = await self.script_generator.generate_script(company_name, det_result)
        
        # Step 4: Synthesize Report
        reasoning_steps.append("Step 4: Compiling Alumni Network Intelligence Master Report.")
        reasoning_result = ReasoningAlumniPipelineResult(
            narrative=narrative,
            intro_script=script,
            reasoning_steps=reasoning_steps
        )
        
        strength_tier = "STRONG NETWORK" if det_result.alumni_network_power_score >= 80 else "MODERATE NETWORK"
        
        return AlumniNetworkOrchestratorReport(
            network_strength_tier=strength_tier,
            alumni_network_power_score=det_result.alumni_network_power_score,
            confidence_score=det_result.confidence_score,
            deterministic_analysis=det_result,
            reasoning_analysis=reasoning_result,
            reasoning_steps=reasoning_steps
        )
