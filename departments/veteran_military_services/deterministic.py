from departments.shared.scoring import ScoringEngine
from departments.veteran_military_services.schemas import (
    VeteranStudentEnrollmentMetric, GIBillDisbursementAudit, YellowRibbonProgramAudit,
    MilitaryJointServicesTranscriptAudit, VeteranResourceCenterMetric, VeteranGraduationEmploymentMetric, DeterministicVeteranServicesPipelineResult
)

class VeteranStudentEnrollmentMeterAgent:
    """Agent 1: Measures veteran student headcount, active duty military, and military dependent students."""
    def run(self, veterans: int = 680) -> VeteranStudentEnrollmentMetric:
        return VeteranStudentEnrollmentMetric(veteran_students_count=veterans, active_duty_military_count=140, military_dependents_count=320)

class GIBillDisbursementAuditorAgent:
    """Agent 2: Audits GI Bill certifications processed, certification speed (days), and compliance percentage."""
    def run(self) -> GIBillDisbursementAudit:
        return GIBillDisbursementAudit(gi_bill_certifications_processed=1140, avg_certification_speed_days=1.8, gi_bill_compliance_pct=100.0)

class YellowRibbonProgramAuditorAgent:
    """Agent 3: Audits Yellow Ribbon institutional match funding (USD) and recipient student count."""
    def run(self) -> YellowRibbonProgramAudit:
        return YellowRibbonProgramAudit(yellow_ribbon_funding_usd=650000.0, yellow_ribbon_recipients_count=145)

class MilitaryJointServicesTranscriptAuditorAgent:
    """Agent 4: Audits Military Joint Services Transcript (JST) evaluations and credits awarded."""
    def run(self) -> MilitaryJointServicesTranscriptAudit:
        return MilitaryJointServicesTranscriptAudit(jst_transcripts_evaluated=420, military_credits_awarded_avg=18.4)

class VeteranResourceCenterMeterAgent:
    """Agent 5: Measures Veteran Resource Center annual visits and peer veteran mentorship pairings."""
    def run(self) -> VeteranResourceCenterMetric:
        return VeteranResourceCenterMetric(vrc_lounge_visits_annual=8400, peer_veteran_mentorship_pairs=180)

class VeteranGraduationEmploymentMeterAgent:
    """Agent 6: Measures veteran student retention percentage and 6-month career placement rate."""
    def run(self) -> VeteranGraduationEmploymentMetric:
        return VeteranGraduationEmploymentMetric(veteran_retention_rate_pct=94.2, veteran_career_placement_rate_pct=92.8)

class VeteranMilitaryServicesScorerAgent:
    """Agent 7: Master deterministic aggregator for Veteran & Military Student Services."""
    def __init__(self):
        self.enrollment_agent = VeteranStudentEnrollmentMeterAgent()
        self.gi_bill_agent = GIBillDisbursementAuditorAgent()
        self.yellow_ribbon_agent = YellowRibbonProgramAuditorAgent()
        self.jst_agent = MilitaryJointServicesTranscriptAuditorAgent()
        self.vrc_agent = VeteranResourceCenterMeterAgent()
        self.outcomes_agent = VeteranGraduationEmploymentMeterAgent()

    def run(self, veterans: int = 680) -> DeterministicVeteranServicesPipelineResult:
        enrollment = self.enrollment_agent.run(veterans)
        gi_bill = self.gi_bill_agent.run()
        yellow_ribbon = self.yellow_ribbon_agent.run()
        jst = self.jst_agent.run()
        vrc = self.vrc_agent.run()
        outcomes = self.outcomes_agent.run()

        metrics = {
            "gi_compliance": gi_bill.gi_bill_compliance_pct,
            "veteran_retention": outcomes.veteran_retention_rate_pct,
            "career_placement": outcomes.veteran_career_placement_rate_pct,
            "certification_speed": max(0.0, 100.0 - (gi_bill.avg_certification_speed_days * 10))
        }
        weights = {"gi_compliance": 0.35, "veteran_retention": 0.25, "career_placement": 0.25, "certification_speed": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(enrollment.veteran_students_count, 50)
        return DeterministicVeteranServicesPipelineResult(
            enrollment=enrollment, gi_bill=gi_bill, yellow_ribbon=yellow_ribbon,
            jst=jst, vrc=vrc, outcomes=outcomes,
            veteran_services_score=score, confidence_score=confidence
        )
