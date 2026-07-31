from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.student_government_leadership.schemas import (
    StrategicSGANarrative, StudentGovernancePlan, ReasoningSGAPipelineResult, DeterministicSGAPipelineResult
)

class StrategicSGANarrativeAgent(BaseAgent):
    """Agent 8: Evaluates student government elections turnout, activity fee fiscal transparency, and legislative impact."""
    def __init__(self):
        super().__init__(agent_id="strategic_sga_narrative", name="Strategic SGA Narrative Agent",
                         description="Evaluates SGA election voter turnout, Student Senate bill adoption, activity fee budget allocation, and leadership certificates.", icon="Award")

    async def evaluate(self, det: DeterministicSGAPipelineResult) -> StrategicSGANarrative:
        fallback = {
            "sga_summary": f"High-engagement student democracy ({det.sga_score:.1f}% score). {det.elections.student_voters_count:,} student voters ({det.elections.sga_election_voter_turnout_pct:.1f}% turnout), ${det.budget.sga_activity_fee_budget_usd/1e6:.1f}M in student activity fee budget allocated with {det.budget.budget_disbursement_transparency_pct}% transparency, {det.senate.administration_adoption_rate_pct}% Senate bill adoption rate.",
            "key_sga_strengths": [f"{det.senate.resolutions_passed} Student Senate resolutions passed across {det.senate.senate_bills_introduced} bills introduced", f"${det.budget.sga_activity_fee_budget_usd:,.0f} activity fee budget distributed across {det.budget.club_funding_grants_disbursed} student organization grants"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Director of Student Government & Leadership Development", "SGA elections, student activity fee budget, Student Senate legislation, town halls"),
                                          PromptBuilder.build_user_context({"score": det.sga_score}), task_type="sga_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicSGANarrative(sga_summary=parsed.get("sga_summary", fallback["sga_summary"]),
                                        key_sga_strengths=parsed.get("key_sga_strengths", fallback["key_sga_strengths"]))
        except Exception:
            return StrategicSGANarrative(**fallback)

class StudentGovernancePlannerAgent(BaseAgent):
    """Agent 9: Formulates student legislative tracking portals and digital SGA election voting systems."""
    def __init__(self):
        super().__init__(agent_id="student_governance_planner", name="Student Governance Planner Agent",
                         description="Formulates mobile election voting apps, transparent activity fee tracking ledgers, and student leadership certificate roadmaps.", icon="FileText")

    async def plan_governance(self, det: DeterministicSGAPipelineResult) -> StudentGovernancePlan:
        fallback = {
            "governance_actions": ["Deploy One-Click Blockchain Election Voting System to boost student turnout over 50%", "Launch Public Open-Ledger SGA Budget Portal tracking all student club grant expenditures"],
            "sample_sga_bill_schema": '{\n  "bill_id": "SSB_2026_14",\n  "bill_title": "Campus Mental Health Days Act",\n  "sponsor": "Senator Maria Rodriguez (College of Arts & Sciences)",\n  "summary": "Establishes 2 mandatory campus wellness days per semester with no academic assignments due",\n  "senate_vote": "PASSED (34 Ayes, 2 Nays, 1 Abstention)",\n  "administration_status": "APPROVED BY UNIVERSITY PRESIDENT & FACULTY SENATE"\n}'
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("SGA Advisor & Student Advocacy Specialist", "SGA elections, Student Senate bills, activity fee budget"),
                                          PromptBuilder.build_user_context({"voters": det.elections.student_voters_count}), task_type="sga_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StudentGovernancePlan(governance_actions=parsed.get("governance_actions", fallback["governance_actions"]),
                                        sample_sga_bill_schema=parsed.get("sample_sga_bill_schema", fallback["sample_sga_bill_schema"]))
        except Exception:
            return StudentGovernancePlan(**fallback)
