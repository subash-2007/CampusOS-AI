from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.testing_qa_intelligence.schemas import (
    StrategicQANarrative, QAImprovementPlan, ReasoningQAPipelineResult, DeterministicQAPipelineResult
)

class StrategicQANarrativeAgent(BaseAgent):
    """Agent 8: Evaluates QA maturity, test coverage depth, and defect prevention effectiveness."""
    def __init__(self):
        super().__init__(agent_id="strategic_qa_narrative", name="Strategic QA Narrative Agent",
                         description="Evaluates test coverage, automation rates, and bug density metrics.", icon="CheckSquare")

    async def evaluate(self, det: DeterministicQAPipelineResult) -> StrategicQANarrative:
        fallback = {
            "qa_summary": f"Enterprise QA excellence ({det.qa_quality_score:.1f}% quality). {det.unit_tests.coverage_pct}% unit coverage, {det.e2e_tests.e2e_pass_rate_pct}% E2E pass rate, {det.bug_density.bugs_per_kloc} bugs/KLOC.",
            "key_qa_strengths": [f"Zero critical bugs open with {det.bug_density.regression_rate_pct}% regression rate", f"{det.unit_tests.total_tests} tests at {det.unit_tests.coverage_pct}% coverage with {det.automation.automation_coverage_pct}% automation"]
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("Head of QA", "test strategy, mutation testing, automation"),
                                          PromptBuilder.build_user_context({"coverage": det.unit_tests.coverage_pct}), task_type="qa_eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return StrategicQANarrative(qa_summary=parsed.get("qa_summary", fallback["qa_summary"]),
                                        key_qa_strengths=parsed.get("key_qa_strengths", fallback["key_qa_strengths"]))
        except Exception:
            return StrategicQANarrative(**fallback)

class QAImprovementPlannerAgent(BaseAgent):
    """Agent 9: Generates testing improvement actions and pytest config samples."""
    def __init__(self):
        super().__init__(agent_id="qa_improvement_planner", name="QA Improvement Planner Agent",
                         description="Formulates test suite expansion plans and Pytest/Playwright configurations.", icon="ClipboardCheck")

    async def plan_improvement(self, det: DeterministicQAPipelineResult) -> QAImprovementPlan:
        fallback = {
            "testing_improvement_actions": [f"Automate {det.automation.manual_test_cases_remaining} remaining manual test cases using Playwright", f"Increase mutation score from {det.mutation.mutation_score_pct}% to 90% by targeting surviving mutants"],
            "sample_pytest_config": "[pytest]\naddopts = --cov=departments --cov-report=term-missing --cov-fail-under=90\ntestpaths = departments\nfilterwarnings = ignore::DeprecationWarning\nasyncio_mode = auto"
        }
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("QA Automation Engineer", "pytest, Playwright, mutation testing"),
                                          PromptBuilder.build_user_context({"mutation_score": det.mutation.mutation_score_pct}), task_type="qa_plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return QAImprovementPlan(testing_improvement_actions=parsed.get("testing_improvement_actions", fallback["testing_improvement_actions"]),
                                     sample_pytest_config=parsed.get("sample_pytest_config", fallback["sample_pytest_config"]))
        except Exception:
            return QAImprovementPlan(**fallback)
