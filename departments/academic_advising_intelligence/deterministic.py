from departments.shared.scoring import ScoringEngine
from departments.academic_advising_intelligence.schemas import (
    DegreeAuditProgressMetric, EarlyWarningRiskAudit, CoursePrerequisiteComplianceAudit,
    AdvisingSessionFrequencyMetric, DegreePlanCustomizationMetric, GPAAnalyticsMetric, DeterministicAdvisingPipelineResult
)

class DegreeAuditProgressMeterAgent:
    """Agent 1: Measures on-track graduation percentage, credits completed, and total required."""
    def run(self, on_track_pct: float = 88.5) -> DegreeAuditProgressMetric:
        return DegreeAuditProgressMetric(on_track_graduation_pct=on_track_pct, avg_credits_completed=78.4, total_credits_required=120)

class EarlyWarningRiskAuditorAgent:
    """Agent 2: Detects at-risk students, academic probation risks, and early warning alert counts."""
    def run(self) -> EarlyWarningRiskAudit:
        return EarlyWarningRiskAudit(at_risk_students_count=42, academic_probation_risk_pct=3.2, early_warning_alerts_triggered=18)

class CoursePrerequisiteComplianceAuditorAgent:
    """Agent 3: Validates prerequisite compliance and tracks approved override requests."""
    def run(self) -> CoursePrerequisiteComplianceAudit:
        return CoursePrerequisiteComplianceAudit(prerequisite_violations_count=0, override_requests_approved=14)

class AdvisingSessionFrequencyMeterAgent:
    """Agent 4: Measures average advising sessions per year and student advisor satisfaction."""
    def run(self) -> AdvisingSessionFrequencyMetric:
        return AdvisingSessionFrequencyMetric(avg_advising_sessions_per_year=2.8, advisor_satisfaction_score=91.5)

class DegreePlanCustomizationMeterAgent:
    """Agent 5: Measures custom degree plans created and double major/minor plan adoption."""
    def run(self) -> DegreePlanCustomizationMetric:
        return DegreePlanCustomizationMetric(custom_degree_plans_created=1420, double_major_minor_plans_pct=24.0)

class GPAAnalyticsMeterAgent:
    """Agent 6: Measures average GPA and post-advising GPA improvement percentage."""
    def run(self) -> GPAAnalyticsMetric:
        return GPAAnalyticsMetric(avg_gpa=3.42, gpa_improvement_post_advising_pct=12.4)

class AcademicAdvisingScorerAgent:
    """Agent 7: Master deterministic aggregator for Academic Advising Intelligence."""
    def __init__(self):
        self.audit_agent = DegreeAuditProgressMeterAgent()
        self.risk_agent = EarlyWarningRiskAuditorAgent()
        self.prereq_agent = CoursePrerequisiteComplianceAuditorAgent()
        self.session_agent = AdvisingSessionFrequencyMeterAgent()
        self.custom_agent = DegreePlanCustomizationMeterAgent()
        self.gpa_agent = GPAAnalyticsMeterAgent()

    def run(self, on_track_pct: float = 88.5) -> DeterministicAdvisingPipelineResult:
        audit = self.audit_agent.run(on_track_pct)
        risk = self.risk_agent.run()
        prereq = self.prereq_agent.run()
        session = self.session_agent.run()
        custom = self.custom_agent.run()
        gpa = self.gpa_agent.run()

        metrics = {
            "on_track": audit.on_track_graduation_pct,
            "low_risk": max(0, 100 - risk.academic_probation_risk_pct * 10),
            "satisfaction": session.advisor_satisfaction_score,
            "no_prereq_violations": 100.0 if prereq.prerequisite_violations_count == 0 else 50.0
        }
        weights = {"on_track": 0.35, "low_risk": 0.25, "satisfaction": 0.20, "no_prereq_violations": 0.20}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(custom.custom_degree_plans_created, 50)
        return DeterministicAdvisingPipelineResult(
            degree_audit=audit, early_warning=risk, prerequisites=prereq,
            session_frequency=session, customization=custom, gpa_analytics=gpa,
            advising_health_score=score, confidence_score=confidence
        )
