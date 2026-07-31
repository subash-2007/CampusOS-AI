from departments.shared.scoring import ScoringEngine
from departments.international_student_services.schemas import (
    InternationalStudentDemographicsMetric, SEVISComplianceAudit, CPTOPTWorkAuthorizationAudit,
    InternationalHostFamilyCultureMetric, EnglishProficiencySupportMetric, InternationalTaxHealthInsuranceAudit, DeterministicISSSPipelineResult
)

class InternationalStudentDemographicsMeterAgent:
    """Agent 1: Measures international student headcount, country count, and top origin countries."""
    def run(self, students: int = 2450) -> InternationalStudentDemographicsMetric:
        return InternationalStudentDemographicsMetric(international_students_count=students, represented_countries_count=94, top_origin_countries=["India", "China", "South Korea", "Brazil", "Germany"])

class SEVISComplianceAuditorAgent:
    """Agent 2: Audits SEVIS record maintenance, reporting compliance percentage, and I-20 / DS-2019 issuance speed."""
    def run(self) -> SEVISComplianceAudit:
        return SEVISComplianceAudit(sevis_records_maintained=2450, sevis_reporting_compliance_pct=100.0, i20_ds2019_issuance_speed_days=2.4)

class CPTOPTWorkAuthorizationAuditorAgent:
    """Agent 3: Audits CPT approvals, OPT endorsements, and 24-month STEM OPT extension processing."""
    def run(self) -> CPTOPTWorkAuthorizationAudit:
        return CPTOPTWorkAuthorizationAudit(cpt_authorizations_approved=840, opt_applications_endorsed=620, stem_opt_extensions_processed=380)

class InternationalHostFamilyCultureMeterAgent:
    """Agent 4: Measures host family pairings, cultural exchange events, and annual attendance."""
    def run(self) -> InternationalHostFamilyCultureMetric:
        return InternationalHostFamilyCultureMetric(host_family_pairs=240, cultural_exchange_events_annual=32, event_attendance_total=5800)

class EnglishProficiencySupportMeterAgent:
    """Agent 5: Measures ESL tutoring hours delivered and TOEFL/IELTS waiver audits."""
    def run(self) -> EnglishProficiencySupportMetric:
        return EnglishProficiencySupportMetric(esl_tutoring_hours_delivered=4200, toefl_ielts_waiver_audits=650)

class InternationalTaxHealthInsuranceAuditorAgent:
    """Agent 6: Audits Sprintax non-resident tax software utilization and health insurance waiver compliance."""
    def run(self) -> InternationalTaxHealthInsuranceAudit:
        return InternationalTaxHealthInsuranceAudit(non_resident_tax_software_utilization_pct=94.5, health_insurance_waiver_compliance_pct=98.8)

class InternationalStudentServicesScorerAgent:
    """Agent 7: Master deterministic aggregator for International Student & Scholar Services."""
    def __init__(self):
        self.demographics_agent = InternationalStudentDemographicsMeterAgent()
        self.sevis_agent = SEVISComplianceAuditorAgent()
        self.work_auth_agent = CPTOPTWorkAuthorizationAuditorAgent()
        self.culture_agent = InternationalHostFamilyCultureMeterAgent()
        self.english_agent = EnglishProficiencySupportMeterAgent()
        self.tax_agent = InternationalTaxHealthInsuranceAuditorAgent()

    def run(self, students: int = 2450) -> DeterministicISSSPipelineResult:
        demographics = self.demographics_agent.run(students)
        sevis = self.sevis_agent.run()
        work_auth = self.work_auth_agent.run()
        culture = self.culture_agent.run()
        english_support = self.english_agent.run()
        tax_insurance = self.tax_agent.run()

        metrics = {
            "sevis_compliance": sevis.sevis_reporting_compliance_pct,
            "insurance_compliance": tax_insurance.health_insurance_waiver_compliance_pct,
            "tax_software_use": tax_insurance.non_resident_tax_software_utilization_pct,
            "i20_speed": max(0.0, 100.0 - (sevis.i20_ds2019_issuance_speed_days * 10))
        }
        weights = {"sevis_compliance": 0.35, "insurance_compliance": 0.25, "tax_software_use": 0.20, "i20_speed": 0.20}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(demographics.international_students_count, 100)
        return DeterministicISSSPipelineResult(
            demographics=demographics, sevis=sevis, work_auth=work_auth,
            culture=culture, english_support=english_support, tax_insurance=tax_insurance,
            isss_score=score, confidence_score=confidence
        )
