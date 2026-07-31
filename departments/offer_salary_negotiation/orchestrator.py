from typing import Dict, Any, List, Optional
from app.agents.base_agent import BaseAgent
from departments.offer_salary_negotiation.deterministic import OfferScorerAgent
from departments.offer_salary_negotiation.reasoning import StrategicNegotiationNarrativeAgent, CounterOfferScriptGeneratorAgent
from departments.offer_salary_negotiation.schemas import (
    OfferSalaryOrchestratorReport, ReasoningOfferPipelineResult
)

class OfferSalaryOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator Agent for the Offer & Salary Negotiation Department."""
    def __init__(self):
        super().__init__(
            agent_id="offer_salary_orchestrator",
            name="Offer & Salary Negotiation Master Orchestrator",
            description="Coordinates all 9 sub-agents to deliver a unified Offer & Salary Negotiation Report.",
            icon="Briefcase"
        )
        self.scorer = OfferScorerAgent()
        self.narrative_agent = StrategicNegotiationNarrativeAgent()
        self.script_generator = CounterOfferScriptGeneratorAgent()

    async def run_pipeline(
        self,
        offered_base: int = 150000,
        signing_bonus: int = 20000,
        annual_equity: int = 50000
    ) -> OfferSalaryOrchestratorReport:
        reasoning_steps = []
        
        # Step 1: Execute Deterministic Pipeline
        reasoning_steps.append("Step 1: Running deterministic Offer & Salary Negotiation pipeline (Base salary benchmarking, Equity grant valuation, Signing bonus audit, Relocation perks metric, Total compensation calculation, Negotiation leverage scoring).")
        det_result = self.scorer.run(offered_base, signing_bonus, annual_equity)
        
        # Step 2: Execute Strategic Negotiation Narrative Agent
        reasoning_steps.append("Step 2: Executing Strategic Negotiation Narrative Agent to evaluate positioning and target counter-offer TC.")
        narrative = await self.narrative_agent.evaluate(det_result)
        
        # Step 3: Execute Counter Offer Script Generator Agent
        reasoning_steps.append("Step 3: Executing Counter Offer Script Generator Agent to produce email draft and talking points.")
        script = await self.script_generator.generate_script(det_result)
        
        # Step 4: Synthesize Report
        reasoning_steps.append("Step 4: Compiling Offer & Salary Negotiation Master Report.")
        reasoning_result = ReasoningOfferPipelineResult(
            narrative=narrative,
            counter_script=script,
            reasoning_steps=reasoning_steps
        )
        
        readiness_tier = "HIGH LEVERAGE" if det_result.leverage.leverage_score >= 80 else "MODERATE LEVERAGE"
        
        return OfferSalaryOrchestratorReport(
            negotiation_readiness_tier=readiness_tier,
            negotiation_upside_percentage=det_result.negotiation_upside_percentage,
            confidence_score=det_result.confidence_score,
            deterministic_analysis=det_result,
            reasoning_analysis=reasoning_result,
            reasoning_steps=reasoning_steps
        )
