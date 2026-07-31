from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.transfer_student_intelligence.schemas import (
    StrategicTransferNarrative, TransferPathwayPlan, ReasoningTransferPipelineResult, DeterministicTransferPipelineResult
)

class StrategicTransferNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates community college transfer pathways, credit transfer speed, and academic outcomes."""
    def __init__(self):
        super().__init__(agent_id="strategic_transfer_narrative", name="Strategic Transfer Narrative Agent",
                         description="Evaluates articulation agreement coverage, transcript evaluation speed, and transfer graduation rates.", icon="GitPullRequest")

    async def evaluate(self, det: DeterministicTransferPipelineResult) -> StrategicTransferNarrative:
        fallback = {
            "transfer_summary": f"High-efficiency transfer articulation pathway ({det.transfer_intelligence_score:.1f}% score). {det.agreements.active_articulation_agreements} articulation agreements across {det.agreements.feeder_community_colleges} community colleges, {det.evaluations.avg_evaluation_turnaround_days:.1f}-day evaluation turnaround, {det.graduation.four_year_transfer_grad_rate_pct}% 4-year transfer graduation rate.",
            "key_transfer_strengths": [f"{det.evaluations.accepted_credit_transfer_pct}% of transfer credit applications accepted with automated equivalency rules", f"{det.gpa_stability.gpa_retention_stability_pct}% post-transfer GPA retention stability (average 1st-year GPA: {det.gpa_stability.post_transfer_first_year_gpa})"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Director of Transfer Articulation & Credit", "community college transfer, credit equivalency, articulation agreements"),
                                          PromptBuilder.build_user_context({"score": det.transfer_intelligence_score}), task_type="transfer_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicTransferNarrative(transfer_summary=parsed.get("transfer_summary", fallback["transfer_summary"]),
                                            key_transfer_strengths=parsed.get("key_transfer_strengths", fallback["key_transfer_strengths"]))
        except Exception:
            return StrategicTransferNarrative(**fallback)

class TransferPathwayPlannerAgent(BaseAgent):
    """Agent 9: Formulates community college 2+2 articulation roadmaps and instant transcript evaluation APIs."""
    def __init__(self):
        super().__init__(agent_id="transfer_pathway_planner", name="Transfer Pathway Planner Agent",
                         description="Formulates community college 2+2 course maps, reverse transfer degree audits, and merit aid programs.", icon="Share2")

    async def plan_pathways(self, det: DeterministicTransferPipelineResult) -> TransferPathwayPlan:
        fallback = {
            "pathway_actions": ["Expand Reverse Transfer Degree Audits to return associate degrees to community college partners automatically", "Deploy AI Instant Transcript Evaluation Engine to reduce turnaround under 24 hours"],
            "sample_articulation_agreement_json": '{\n  "partner_institution": "State Community College",\n  "pathway_code": "AS_CS_TO_BS_CS",\n  "guaranteed_transfer_credits": 60,\n  "required_gpa": 2.75,\n  "mapped_courses": [\n    {\n      "cc_course": "CS101 Intro to Java",\n      "university_course": "CS1101 Object Oriented Design",\n      "credits": 4\n    }\n  ]\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Transfer Operations Specialist", "2+2 articulation, transcript evaluation, reverse transfer"),
                                          PromptBuilder.build_user_context({"agreements": det.agreements.active_articulation_agreements}), task_type="transfer_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return TransferPathwayPlan(pathway_actions=parsed.get("pathway_actions", fallback["pathway_actions"]),
                                       sample_articulation_agreement_json=parsed.get("sample_articulation_agreement_json", fallback["sample_articulation_agreement_json"]))
        except Exception:
            return TransferPathwayPlan(**fallback)
