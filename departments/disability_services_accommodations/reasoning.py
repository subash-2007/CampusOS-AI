from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.disability_services_accommodations.schemas import (
    StrategicDisabilityServicesNarrative, AccommodationPlan, ReasoningDisabilityServicesPipelineResult, DeterministicDisabilityServicesPipelineResult
)

class StrategicDisabilityServicesNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates ADA Title II & III compliance, physical/digital accessibility, and exam proctoring SLAs."""
    def __init__(self):
        super().__init__(agent_id="strategic_disability_services_narrative", name="Strategic Disability Services Narrative Agent",
                         description="Evaluates student accommodation fulfillment, ADA compliance, assistive technology adoption, and digital material accessibility.", icon="CheckCircle")

    async def evaluate(self, det: DeterministicDisabilityServicesPipelineResult) -> StrategicDisabilityServicesNarrative:
        fallback = {
            "services_summary": f"Universal accessibility excellence ({det.disability_services_score:.1f}% score). {det.registrations.registered_students_count:,} registered students receiving accommodations, {det.exam_proctoring.proctoring_sla_fulfillment_pct}% proctoring SLA fulfillment across {det.exam_proctoring.extended_time_exams_proctored:,} exams, {det.physical_accessibility.wheelchair_accessible_routes_pct}% physical route accessibility.",
            "key_accessibility_strengths": [f"{det.digital_materials.captioned_video_lecture_pct}% of video lectures fully closed-captioned", f"{det.digital_materials.accessible_pdf_conversion_count:,} digital course PDFs converted to screen-reader accessible formats"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Director of Student Disability Resources", "ADA compliance, exam accommodations, assistive technology, digital accessibility"),
                                          PromptBuilder.build_user_context({"score": det.disability_services_score}), task_type="disability_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicDisabilityServicesNarrative(services_summary=parsed.get("services_summary", fallback["services_summary"]),
                                                       key_accessibility_strengths=parsed.get("key_accessibility_strengths", fallback["key_accessibility_strengths"]))
        except Exception:
            return StrategicDisabilityServicesNarrative(**fallback)

class AccommodationPlannerAgent(BaseAgent):
    """Agent 9: Generates personalized academic accommodation letters and campus accessibility improvement blueprints."""
    def __init__(self):
        super().__init__(agent_id="accommodation_planner", name="Accommodation Planner Agent",
                         description="Formulates student accommodation notifications, tactile map upgrades, and digital accessibility scanning routines.", icon="FileText")

    async def plan_accommodations(self, det: DeterministicDisabilityServicesPipelineResult) -> AccommodationPlan:
        fallback = {
            "accessibility_actions": ["Deploy AI Auto-Captioning Verification Engine for all live-streamed lectures", "Install Tactile Braille Wayfinding Signs and Bluetooth Beacons across all campus academic halls"],
            "sample_accommodation_letter_template": "OFFICIAL STUDENT ACCOMMODATION LETTER\nStudent ID: std_88192\nIssued By: Office of Disability Services & Accommodations\nEffective Dates: 2026-08-25 to 2027-05-31\nApproved Accommodations:\n  1. Testing: 1.5x extended time on all timed exams/quizzes in quiet testing room\n  2. Course Materials: Digital screen-reader accessible PDFs provided 5 days prior to class\n  3. Note-Taking: Access to peer note-taker or Glean audio recording software\n  4. Attendance: Flexibility with attendance during acute disability flare-ups"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Disability Specialist & Advocate", "accommodation letters, ADA accommodations, universal design for learning"),
                                          PromptBuilder.build_user_context({"students": det.registrations.registered_students_count}), task_type="disability_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return AccommodationPlan(accessibility_actions=parsed.get("accessibility_actions", fallback["accessibility_actions"]),
                                     sample_accommodation_letter_template=parsed.get("sample_accommodation_letter_template", fallback["sample_accommodation_letter_template"]))
        except Exception:
            return AccommodationPlan(**fallback)
