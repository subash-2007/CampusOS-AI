from departments.shared.scoring import ScoringEngine
from departments.career_center_student_employment.schemas import (
    CampusCareerFairEmployerEngagementMetric, OnCampusStudentEmploymentPayrollAudit, CareerAdvisingAppointmentVolumeMetric,
    MockInterviewSkillVerificationAudit, OnCampusRecruitingOCRInterviewScheduleMetric, FirstDestinationCareerOutcomeAudit, DeterministicCareerCenterPipelineResult
)

class CampusCareerFairEmployerEngagementMeterAgent:
    """Agent 1: Measures annual career fairs hosted, participating employers count, and student attendees."""
    def run(self, employers: int = 680) -> CampusCareerFairEmployerEngagementMetric:
        return CampusCareerFairEmployerEngagementMetric(career_fairs_hosted_annual=12, participating_employers_count=employers, student_career_fair_attendees=14500)

class OnCampusStudentEmploymentPayrollAuditorAgent:
    """Agent 2: Audits on-campus student hires count, Federal Work-Study disbursed (USD), and payroll compliance score."""
    def run(self) -> OnCampusStudentEmploymentPayrollAudit:
        return OnCampusStudentEmploymentPayrollAudit(student_employees_hired_on_campus=4200, federal_work_study_fws_disbursed_usd=3800000.0, student_payroll_compliance_score_pct=100.0)

class CareerAdvisingAppointmentVolumeMeterAgent:
    """Agent 3: Measures 1-on-1 career coaching appointments, resume critique turnaround hours, and CSAT rating."""
    def run(self) -> CareerAdvisingAppointmentVolumeMetric:
        return CareerAdvisingAppointmentVolumeMetric(one_on_one_career_coaching_appointments=9400, resume_critique_turnaround_hours=18.5, advising_csat_score=4.88)

class MockInterviewSkillVerificationAuditorAgent:
    """Agent 4: Audits mock interviews conducted, AI interview portal users, and interview readiness score percentage."""
    def run(self) -> MockInterviewSkillVerificationAudit:
        return MockInterviewSkillVerificationAudit(mock_interviews_conducted=2800, ai_interview_prep_portal_active_users=6400, interview_readiness_score_pct=92.4)

class OnCampusRecruitingOCRInterviewScheduleMeterAgent:
    """Agent 5: Measures on-campus interviews conducted and employer job postings count on Handshake/CampusOS."""
    def run(self) -> OnCampusRecruitingOCRInterviewScheduleMetric:
        return OnCampusRecruitingOCRInterviewScheduleMetric(on_campus_interviews_conducted=1850, employer_job_postings_handshake=24500)

class FirstDestinationCareerOutcomeAuditorAgent:
    """Agent 6: Audits NACE first destination knowledge rate percentage, 6-month employment/grad school placement rate, and average starting salary (USD)."""
    def run(self) -> FirstDestinationCareerOutcomeAudit:
        return FirstDestinationCareerOutcomeAudit(first_destination_knowledge_rate_pct=88.5, employed_or_grad_school_at_6_months_pct=95.2, avg_starting_salary_usd=72400.0)

class CareerCenterStudentEmploymentScorerAgent:
    """Agent 7: Master deterministic aggregator for Career Center & Student Employment."""
    def __init__(self):
        self.fairs_agent = CampusCareerFairEmployerEngagementMeterAgent()
        self.employment_agent = OnCampusStudentEmploymentPayrollAuditorAgent()
        self.advising_agent = CareerAdvisingAppointmentVolumeMeterAgent()
        self.mock_interviews_agent = MockInterviewSkillVerificationAuditorAgent()
        self.recruiting_agent = OnCampusRecruitingOCRInterviewScheduleMeterAgent()
        self.outcomes_agent = FirstDestinationCareerOutcomeAuditorAgent()

    def run(self, employers: int = 680) -> DeterministicCareerCenterPipelineResult:
        fairs = self.fairs_agent.run(employers)
        employment = self.employment_agent.run()
        advising = self.advising_agent.run()
        mock_interviews = self.mock_interviews_agent.run()
        recruiting = self.recruiting_agent.run()
        outcomes = self.outcomes_agent.run()

        metrics = {
            "placement_rate": outcomes.employed_or_grad_school_at_6_months_pct,
            "payroll_compliance": employment.student_payroll_compliance_score_pct,
            "interview_readiness": mock_interviews.interview_readiness_score_pct,
            "advising_csat": (advising.advising_csat_score / 5.0) * 100
        }
        weights = {"placement_rate": 0.35, "payroll_compliance": 0.30, "interview_readiness": 0.20, "advising_csat": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(fairs.participating_employers_count, 100)
        return DeterministicCareerCenterPipelineResult(
            fairs=fairs, employment=employment, advising=advising,
            mock_interviews=mock_interviews, recruiting=recruiting, outcomes=outcomes,
            career_center_score=score, confidence_score=confidence
        )
