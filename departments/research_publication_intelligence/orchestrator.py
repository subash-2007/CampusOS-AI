from app.agents.base_agent import BaseAgent
from departments.research_publication_intelligence.deterministic import ResearchExcellenceScorerAgent
from departments.research_publication_intelligence.reasoning import StrategicResearchNarrativeAgent, CommercializationPlannerAgent
from departments.research_publication_intelligence.schemas import ResearchPublicationOrchestratorReport, ReasoningResearchPipelineResult

class ResearchPublicationOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Research & Publication Intelligence Department."""
    def __init__(self):
        super().__init__(agent_id="research_publication_orchestrator", name="Research & Publication Intelligence Master Orchestrator",
                         description="Coordinates all 9 research and publication sub-agents.", icon="BookOpen")
        self.scorer = ResearchExcellenceScorerAgent()
        self.narrative_agent = StrategicResearchNarrativeAgent()
        self.commercialization_planner = CommercializationPlannerAgent()

    async def run_pipeline(self, papers: int = 340) -> ResearchPublicationOrchestratorReport:
        steps = ["Step 1: Running deterministic Research pipeline (publications, citation impact, grants, patents, open access, co-authorship)."]
        det = self.scorer.run(papers)
        steps.append("Step 2: Executing Strategic Research Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Commercialization Planner Agent.")
        commercialization = await self.commercialization_planner.plan_commercialization(det)
        steps.append("Step 4: Compiling Research & Publication Intelligence Master Report.")
        tier = "HIGH IMPACT RESEARCH INSTITUTION" if det.research_excellence_score >= 80 else "STANDARD RESEARCH INSTITUTION"
        return ResearchPublicationOrchestratorReport(
            research_tier=tier, research_excellence_score=det.research_excellence_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningResearchPipelineResult(narrative=narrative, commercialization_plan=commercialization, reasoning_steps=steps),
            reasoning_steps=steps
        )
