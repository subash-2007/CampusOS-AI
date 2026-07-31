from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.student_athletics_recreation.schemas import (
    StrategicAthleticsNarrative, CampusAthleticsPlan, ReasoningAthleticsPipelineResult, DeterministicAthleticsPipelineResult
)

class StrategicAthleticsNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates NCAA APR academic excellence, NIL compliance governance, and student rec center engagement."""
    def __init__(self):
        super().__init__(agent_id="strategic_athletics_narrative", name="Strategic Athletics Narrative Agent",
                         description="Evaluates NCAA APR scores, athletic graduation rates, NIL deal compliance, and sports medicine protocols.", icon="Activity")

    async def evaluate(self, det: DeterministicAthleticsPipelineResult) -> StrategicAthleticsNarrative:
        fallback = {
            "athletics_summary": f"NCAA championship excellence program ({det.athletics_score:.1f}% score). Supporting {det.headcount.ncaa_student_athletes_count} varsity athletes across {det.headcount.varsity_teams_count} teams, {det.ncaa_apr.ncaa_apr_score_avg:.0f} average NCAA APR score, {det.scholarships_nil.nil_compliance_rate_pct}% NIL compliance.",
            "key_athletics_strengths": [f"${det.scholarships_nil.athletic_scholarships_awarded_usd/1e6:.1f}M in athletic scholarships awarded with {det.scholarships_nil.nil_compliance_disclosures_processed} NIL disclosures verified", f"{det.rec_center.rec_center_annual_swipes:,} annual rec center visits with {det.headcount.club_intramural_participants:,} intramural participants"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Director of Intercollegiate Athletics & Recreation", "NCAA compliance, APR, NIL regulations, sports medicine, student recreation"),
                                          PromptBuilder.build_user_context({"score": det.athletics_score}), task_type="athletics_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicAthleticsNarrative(athletics_summary=parsed.get("athletics_summary", fallback["athletics_summary"]),
                                             key_athletics_strengths=parsed.get("key_athletics_strengths", fallback["key_athletics_strengths"]))
        except Exception:
            return StrategicAthleticsNarrative(**fallback)

class CampusAthleticsPlannerAgent(BaseAgent):
    """Agent 9: Generates NIL disclosure workflows and student-athlete academic tutoring schedules."""
    def __init__(self):
        super().__init__(agent_id="campus_athletics_planner", name="Campus Athletics Planner Agent",
                         description="Formulates NIL compliance review systems, sports performance nutrition programs, and intramural league expansions.", icon="ShieldCheck")

    async def plan_athletics(self, det: DeterministicAthleticsPipelineResult) -> CampusAthleticsPlan:
        fallback = {
            "athletics_program_actions": ["Implement AI Automated NIL Contract Compliance Scanner to protect student eligibility", "Expand Student Rec Center 24/7 Access with smart biometric entry kiosks"],
            "sample_nil_disclosure_schema": '{\n  "athlete_id": "ath_10942",\n  "sport": "Men\'s Basketball",\n  "brand_sponsor": "Local Tech Solutions LLC",\n  "compensation_usd": 15000.0,\n  "activity_type": "Social Media Endorsement & Youth Camp Appearance",\n  "compliance_status": "APPROVED BY ATHLETIC COMPLIANCE OFFICE",\n  "conflict_check": "Zero institutional conflict with official athletic sponsors"\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Athletic Compliance Officer", "NIL disclosure, NCAA APR, student-athlete welfare"),
                                          PromptBuilder.build_user_context({"athletes": det.headcount.ncaa_student_athletes_count}), task_type="athletics_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return CampusAthleticsPlan(athletics_program_actions=parsed.get("athletics_program_actions", fallback["athletics_program_actions"]),
                                       sample_nil_disclosure_schema=parsed.get("sample_nil_disclosure_schema", fallback["sample_nil_disclosure_schema"]))
        except Exception:
            return CampusAthleticsPlan(**fallback)
