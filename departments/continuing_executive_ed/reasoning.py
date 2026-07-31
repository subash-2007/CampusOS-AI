from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.continuing_executive_ed.schemas import (
    StrategicExecEdNarrative, ExecEdPortfolioPlan, ReasoningExecEdPipelineResult, DeterministicExecEdPipelineResult
)

class StrategicExecEdNarrativeAgent(BaseAgent):
    """Agent 8: Evaluates B2B executive education growth, certificate ROI, and NPS sentiment."""
    def __init__(self):
        super().__init__(agent_id="strategic_exec_ed_narrative", name="Strategic Exec Ed Narrative Agent",
                         description="Evaluates corporate client retention, executive NPS, and non-degree certificate career impact.", icon="Briefcase")

    async def evaluate(self, det: DeterministicExecEdPipelineResult) -> StrategicExecEdNarrative:
        fallback = {
            "exec_ed_summary": f"Premier enterprise executive academy ({det.exec_ed_score:.1f}% score). {det.enrollment.executive_learners_count:,} executive learners, ${det.revenue.b2b_corporate_revenue_usd/1e6:.1f}M B2B revenue across {det.revenue.enterprise_client_count} enterprise clients, {det.nps.executive_nps_score} NPS score.",
            "key_exec_ed_strengths": [f"{det.revenue.repeat_contract_rate_pct}% repeat enterprise client contract rate", f"{det.promotions.learners_promoted_within_1_year_pct}% of executive learners promoted within 1 year with an average {det.promotions.avg_salary_increase_pct}% salary boost"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Dean of Executive Education", "B2B corporate training, executive certificates, leadership development"),
                                          PromptBuilder.build_user_context({"score": det.exec_ed_score}), task_type="exec_ed_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicExecEdNarrative(exec_ed_summary=parsed.get("exec_ed_summary", fallback["exec_ed_summary"]),
                                          key_exec_ed_strengths=parsed.get("key_exec_ed_strengths", fallback["key_exec_ed_strengths"]))
        except Exception:
            return StrategicExecEdNarrative(**fallback)

class ExecEdPortfolioPlannerAgent(BaseAgent):
    """Agent 9: Generates custom enterprise cohort proposals and micro-credential stackable certificates."""
    def __init__(self):
        super().__init__(agent_id="exec_ed_portfolio_planner", name="Exec Ed Portfolio Planner Agent",
                         description="Formulates AI leadership certificates, corporate custom programs, and stackable executive badges.", icon="TrendingUp")

    async def plan_portfolio(self, det: DeterministicExecEdPipelineResult) -> ExecEdPortfolioPlan:
        fallback = {
            "portfolio_actions": ["Launch Executive AI Governance & Strategy Certificate for Fortune 500 C-Suite leaders", "Expand Micro-Credential Stacking enabling 3 executive certificates to count toward Executive MBA"],
            "sample_corporate_cohort_contract": "CUSTOM EXECUTIVE EDUCATION MASTER SERVICES AGREEMENT\nClient: Global Tech Enterprise Inc.\nScope: AI Transformation & Executive Leadership Masterclass\nParticipants: 50 Senior Vice Presidents & Directors\nDuration: 6 Months (Hybrid On-Campus & Online synchronous)\nTotal Fee: $450,000 USD\nDeliverables: Customized Capstone Projects, CEU Certificates, Digital Badges"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Executive Education Business Director", "corporate custom cohorts, micro-credentials, executive MBA stacking"),
                                          PromptBuilder.build_user_context({"clients": det.revenue.enterprise_client_count}), task_type="exec_ed_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return ExecEdPortfolioPlan(portfolio_actions=parsed.get("portfolio_actions", fallback["portfolio_actions"]),
                                       sample_corporate_cohort_contract=parsed.get("sample_corporate_cohort_contract", fallback["sample_corporate_cohort_contract"]))
        except Exception:
            return ExecEdPortfolioPlan(**fallback)
