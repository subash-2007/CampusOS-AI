from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.student_judicial_conduct.schemas import (
    StrategicJudicialNarrative, JudicialOperationsPlan, ReasoningJudicialPipelineResult, DeterministicJudicialPipelineResult
)

class StrategicJudicialNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates student conduct due process protections, academic integrity honor code enforcement, and restorative justice outcomes."""
    def __init__(self):
        super().__init__(agent_id="strategic_judicial_narrative", name="Strategic Judicial Narrative Agent",
                         description="Evaluates student conduct case resolution speed, due process compliance rates, restorative justice recidivism reduction, and Title IX referral protocols.", icon="Shield")

    async def evaluate(self, det: DeterministicJudicialPipelineResult) -> StrategicJudicialNarrative:
        fallback = {
            "judicial_summary": f"Model fair due-process conduct system ({det.judicial_score:.1f}% score). Adjudicating {det.cases.annual_conduct_cases_adjudicated:,} conduct cases ({det.resolution.avg_case_resolution_days:.1f}-day average resolution), 100% due process compliance rate, 100% Title IX procedural compliance.",
            "key_judicial_strengths": [f"{det.restorative_justice.restorative_justice_resolutions} restorative justice resolutions logging {det.restorative_justice.sanctioned_community_service_hours_logged:,} service hours with {det.restorative_justice.recidivism_reduction_rate_pct}% recidivism reduction rate", f"{det.academic_integrity.honor_code_pledge_compliance_pct}% Honor Code pledge compliance with low {det.academic_integrity.repeat_academic_violation_rate_pct}% repeat academic violation rate"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Director of Student Judicial Affairs & Code of Conduct Administrator", "due process, Honor Code academic integrity, restorative justice, Title IX compliance"),
                                          PromptBuilder.build_user_context({"score": det.judicial_score}), task_type="judicial_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicJudicialNarrative(judicial_summary=parsed.get("judicial_summary", fallback["judicial_summary"]),
                                             key_judicial_strengths=parsed.get("key_judicial_strengths", fallback["key_judicial_strengths"]))
        except Exception:
            return StrategicJudicialNarrative(**fallback)

class JudicialOperationsPlannerAgent(BaseAgent):
    """Agent 9: Formulates digital student conduct case management portals and restorative justice mediation frameworks."""
    def __init__(self):
        super().__init__(agent_id="judicial_operations_planner", name="Judicial Operations Planner Agent",
                         description="Formulates Maxient conduct case management workflows, AI academic plagiarism detection protocols, and student rights advocate training.", icon="FileText")

    async def plan_judicial_operations(self, det: DeterministicJudicialPipelineResult) -> JudicialOperationsPlan:
        fallback = {
            "judicial_actions": ["Deploy Smart Conduct Case Portal allowing students to view charges, request advisors, and submit hearing statements digitally", "Expand Restorative Justice Diversion Circle for first-time non-violent alcohol & noise infractions"],
            "sample_conduct_hearing_decision_schema": '{\n  "case_number": "COND_2026_0412",\n  "respondent_id": "stu_99182",\n  "alleged_violation": "Section 4.2: Academic Integrity (Unauthorized Collaboration)",\n  "hearing_date": "2026-10-10",\n  "adjudicator": "University Conduct Hearing Board (3 Faculty, 2 Students)",\n  "finding": "RESPONSIBLE FOR VIOLATION",\n  "sanctions": [\n    "1. Grade of F on Assignment 3 (Course Grade Recalculated)",\n    "2. Academic Integrity Ethics Module Completion (Deadline: 14 Days)",\n    "3. Conduct Probation through Spring Semester 2027"\n  ],\n  "appeal_rights": "Written appeal may be submitted to Vice President for Student Affairs within 5 business days"\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Student Conduct Case Manager & Hearing Officer", "conduct hearing decision, due process, Maxient workflow"),
                                          PromptBuilder.build_user_context({"cases": det.cases.annual_conduct_cases_adjudicated}), task_type="judicial_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return JudicialOperationsPlan(judicial_actions=parsed.get("judicial_actions", fallback["judicial_actions"]),
                                          sample_conduct_hearing_decision_schema=parsed.get("sample_conduct_hearing_decision_schema", fallback["sample_conduct_hearing_decision_schema"]))
        except Exception:
            return JudicialOperationsPlan(**fallback)
