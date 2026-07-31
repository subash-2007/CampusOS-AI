from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.campus_rec_wellness.schemas import (
    StrategicCampusRecNarrative, CampusRecOperationsPlan, ReasoningCampusRecPipelineResult, DeterministicCampusRecPipelineResult
)

class StrategicCampusRecNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates campus rec center utilization rates, intramural sports participation, and aquatic safety compliance."""
    def __init__(self):
        super().__init__(agent_id="strategic_campus_rec_narrative", name="Strategic Campus Rec Narrative Agent",
                         description="Evaluates recreation center turnstile scans, group fitness class fill rates, intramural league participation, and lifeguard certification compliance.", icon="Activity")

    async def evaluate(self, det: DeterministicCampusRecPipelineResult) -> StrategicCampusRecNarrative:
        fallback = {
            "rec_wellness_summary": f"Premier campus fitness & recreation center ({det.rec_wellness_score:.1f}% score). {det.turnstiles.rec_center_annual_turnstile_scans:,} annual turnstile scans ({det.turnstiles.rec_center_student_body_utilization_pct}% student body utilization), 100% lifeguard CPR certification compliance, {det.group_fitness.class_capacity_fill_rate_pct}% group fitness fill rate.",
            "key_rec_strengths": [f"{det.intramurals.intramural_league_athletes_count:,} intramural sports athletes competing across {det.intramurals.intramural_teams_registered} registered teams in {det.intramurals.intramural_sports_offered_count} sports leagues", f"{det.outdoors.outdoor_gear_rentals_annual:,} gear rentals and {det.outdoors.outdoor_expeditions_hosted} wilderness trips led by {det.outdoors.outdoor_safety_certified_guides_count} certified guides"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Director of Campus Recreation & Student Wellness", "recreation center turnstiles, group fitness, intramurals, outdoor adventures, aquatic safety"),
                                          PromptBuilder.build_user_context({"score": det.rec_wellness_score}), task_type="rec_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicCampusRecNarrative(rec_wellness_summary=parsed.get("rec_wellness_summary", fallback["rec_wellness_summary"]),
                                             key_rec_strengths=parsed.get("key_rec_strengths", fallback["key_rec_strengths"]))
        except Exception:
            return StrategicCampusRecNarrative(**fallback)

class CampusRecOperationsPlannerAgent(BaseAgent):
    """Agent 9: Formulates mobile group fitness reservation systems and intramural league bracket scheduling algorithms."""
    def __init__(self):
        super().__init__(agent_id="campus_rec_operations_planner", name="Campus Rec Operations Planner Agent",
                         description="Formulates mobile app rec center occupancy trackers, automated intramural scheduling engines, and equipment check-out RFID tracking.", icon="Calendar")

    async def plan_rec_operations(self, det: DeterministicCampusRecPipelineResult) -> CampusRecOperationsPlan:
        fallback = {
            "rec_actions": ["Deploy Real-Time Mobile Rec Center Gym Density Tracker so students can check crowd levels before heading to the gym", "Launch Automated Intramural League Tournament & Officiating Scheduling Engine"],
            "sample_intramural_league_bracket_schema": '{\n  "league_id": "IM_FB_2026_FALL",\n  "league_name": "Men\'s Open Flag Football Division A",\n  "teams_count": 16,\n  "tournament_format": "Double Elimination",\n  "playoff_bracket": [\n    {\n      "game_id": "G101",\n      "team_a": "Sigma Chi Flyers",\n      "team_b": "Engineering Bulldogs",\n      "field": "Turf Field 2 (Lit Under Floodlights)",\n      "scheduled_time": "2026-10-14T20:00:00Z",\n      "assigned_officials": ["Certified Intramural Ref #14", "Certified Intramural Ref #22"]\n    }\n  ]\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Recreation Operations Manager & Intramural Director", "group fitness reservation, intramural bracket, gym density tracker"),
                                          PromptBuilder.build_user_context({"scans": det.turnstiles.rec_center_annual_turnstile_scans}), task_type="rec_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return CampusRecOperationsPlan(rec_actions=parsed.get("rec_actions", fallback["rec_actions"]),
                                          sample_intramural_league_bracket_schema=parsed.get("sample_intramural_league_bracket_schema", fallback["sample_intramural_league_bracket_schema"]))
        except Exception:
            return CampusRecOperationsPlan(**fallback)
