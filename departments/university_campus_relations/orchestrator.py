from app.agents.base_agent import BaseAgent
from departments.university_campus_relations.deterministic import UniversityCampusRelationsScorerAgent
from departments.university_campus_relations.reasoning import StrategicCampusNarrativeAgent, CampusRelationsPlannerAgent
from departments.university_campus_relations.schemas import UniversityCampusRelationsOrchestratorReport, ReasoningCampusPipelineResult

class UniversityCampusRelationsOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for University & Campus Relations Department."""
    def __init__(self):
        super().__init__(agent_id="university_campus_relations_orchestrator", name="University & Campus Relations Master Orchestrator",
                         description="Coordinates all 9 university and campus relations sub-agents.", icon="Landmark")
        self.scorer = UniversityCampusRelationsScorerAgent()
        self.narrative_agent = StrategicCampusNarrativeAgent()
        self.relations_planner = CampusRelationsPlannerAgent()

    async def run_pipeline(self, universities: int = 142) -> UniversityCampusRelationsOrchestratorReport:
        steps = ["Step 1: Running deterministic Campus pipeline (partner count, career fairs, placement rate, MOU status, student engagement, faculty collaboration)."]
        det = self.scorer.run(universities)
        steps.append("Step 2: Executing Strategic Campus Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Campus Relations Planner Agent.")
        relations = await self.relations_planner.plan_relations(det)
        steps.append("Step 4: Compiling University & Campus Relations Master Report.")
        tier = "STRATEGIC ACADEMIC PARTNER" if det.campus_relations_score >= 85 else "STANDARD ACADEMIC PARTNER"
        return UniversityCampusRelationsOrchestratorReport(
            campus_tier=tier, campus_relations_score=det.campus_relations_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningCampusPipelineResult(narrative=narrative, relations_plan=relations, reasoning_steps=steps),
            reasoning_steps=steps
        )
