from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.student_disability_access.schemas import (
    StrategicDisabilityNarrative, DisabilityAccessPlan, ReasoningDisabilityPipelineResult, DeterministicDisabilityPipelineResult
)

class StrategicDisabilityNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates student disability accommodation fulfillment, WCAG 2.1 AA digital accessibility, and CART live captioning coverage."""
    def __init__(self):
        super().__init__(agent_id="strategic_disability_narrative", name="Strategic Disability Narrative Agent",
                         description="Evaluates academic accommodation plan turnaround, testing center proctoring fulfillment, Canvas WCAG compliance, and physical ADA accessibility.", icon="CheckSquare")

    async def evaluate(self, det: DeterministicDisabilityPipelineResult) -> StrategicDisabilityNarrative:
        fallback = {
            "disability_summary": f"National model for universal accessibility ({det.disability_access_score:.1f}% score). Supporting {det.accommodations.students_registered_with_disability_office:,} registered students across {det.accommodations.active_academic_accommodation_plans:,} active accommodation plans ({det.accommodations.accommodation_plan_processing_days_avg:.1f}-day average turn), 100% live captioning fulfillment.",
            "key_disability_strengths": [f"{det.testing_center.exam_accommodation_fulfillment_rate_pct}% exam accommodation fulfillment across {det.testing_center.accommodated_exams_proctored_annual:,} proctored exams in {det.testing_center.distraction_reduced_testing_booths} dedicated testing booths", f"{det.digital_accessibility.wcag_21_aa_compliance_score_pct}% WCAG 2.1 AA digital compliance across {det.digital_accessibility.canvas_lms_courses_scanned_for_wcag:,} scanned Canvas LMS courses"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Director of Disability Resources & Universal Accessibility", "academic accommodations, WCAG 2.1 AA, CART captioning, ADA physical access, testing center proctoring"),
                                          PromptBuilder.build_user_context({"score": det.disability_access_score}), task_type="disability_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicDisabilityNarrative(disability_summary=parsed.get("disability_summary", fallback["disability_summary"]),
                                               key_disability_strengths=parsed.get("key_disability_strengths", fallback["key_disability_strengths"]))
        except Exception:
            return StrategicDisabilityNarrative(**fallback)

class DisabilityAccessPlannerAgent(BaseAgent):
    """Agent 9: Formulates automated faculty accommodation letter generation and AI-powered live lecture captioning systems."""
    def __init__(self):
        super().__init__(agent_id="disability_access_planner", name="Disability Access Planner Agent",
                         description="Formulates digital accommodation portals, automated screen-reader document converters, and barrier-free physical campus navigation maps.", icon="Layers")

    async def plan_disability_access(self, det: DeterministicDisabilityPipelineResult) -> DisabilityAccessPlan:
        fallback = {
            "disability_actions": ["Deploy Smart One-Click Accommodation Letter Portal transmitting approved accommodations to faculty LMS automatically", "Launch Real-Time AI CART Speech-to-Text Live Captioning for all university lectures"],
            "sample_accommodation_letter_schema": '{\n  "student_id": "stu_99182",\n  "academic_term": "Fall 2026",\n  "course": "CS 401: Advanced Data Structures",\n  "instructor": "Dr. Alan Turing",\n  "approved_accommodations": [\n    "1. 1.5x Extended Time on All In-Class Quizzes & Examinations",\n    "2. Distraction-Reduced Testing Environment at Accessibility Center",\n    "3. Permission to Record Class Lectures via Glean Assistive App",\n    "4. Accessible Digital Copies of All Course Slides & PDFs (Screen-Reader Compatible)"\n  ],\n  "letter_status": "OFFICIALLY DELIVERED TO INSTRUCTOR LMS PORTAL & ACKNOWLEDGED"\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Disability Access Specialist & Assistive Tech Manager", "accommodation letter, CART captioning, WCAG 2.1 AA"),
                                          PromptBuilder.build_user_context({"students": det.accommodations.students_registered_with_disability_office}), task_type="disability_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return DisabilityAccessPlan(disability_actions=parsed.get("disability_actions", fallback["disability_actions"]),
                                        sample_accommodation_letter_schema=parsed.get("sample_accommodation_letter_schema", fallback["sample_accommodation_letter_schema"]))
        except Exception:
            return DisabilityAccessPlan(**fallback)
