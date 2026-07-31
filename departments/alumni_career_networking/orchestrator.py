from app.agents.base_agent import BaseAgent
from departments.alumni_career_networking.deterministic import AlumniCareerNetworkingScorerAgent
from departments.alumni_career_networking.reasoning import StrategicAlumniCareerNarrativeAgent, AlumniCareerPlannerAgent
from departments.alumni_career_networking.schemas import AlumniCareerNetworkingOrchestratorReport, ReasoningAlumniCareerPipelineResult

class AlumniCareerNetworkingOrchestratorAgent(BaseAgent):
    """Agent 10: Master Orchestrator for Alumni Career Services & Networking Department."""
    def __init__(self):
        super().__init__(agent_id="alumni_career_networking_orchestrator", name="Alumni Career Services & Networking Master Orchestrator",
                         description="Coordinates all 9 alumni career services & networking sub-agents.", icon="Briefcase")
        self.scorer = AlumniCareerNetworkingScorerAgent()
        self.narrative_agent = StrategicAlumniCareerNarrativeAgent()
        self.career_planner = AlumniCareerPlannerAgent()

    async def run_pipeline(self, mentors: int = 8450) -> AlumniCareerNetworkingOrchestratorReport:
        steps = ["Step 1: Running deterministic Alumni Career pipeline (mentorship, coaching, chapters, job board, lifelong learning, directory)."]
        det = self.scorer.run(mentors)
        steps.append("Step 2: Executing Strategic Alumni Career Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Alumni Career Planner Agent.")
        alumni_career_plan = await self.career_planner.plan_alumni_career(det)
        steps.append("Step 4: Compiling Alumni Career Services & Networking Master Report.")
        tier = "GLOBAL ALUMNI CAREER POWERHOUSE" if det.alumni_career_score >= 90 else "STANDARD ALUMNI CAREER NETWORK"
        return AlumniCareerNetworkingOrchestratorReport(
            alumni_career_tier=tier, alumni_career_score=det.alumni_career_score, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=ReasoningAlumniCareerPipelineResult(narrative=narrative, alumni_career_plan=alumni_career_plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
