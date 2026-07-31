from departments.shared.scoring import ScoringEngine
from departments.student_legal_advocacy.schemas import (
    StudentLegalConsultationMetric, LandlordTenantDisputeAudit, StudentImmigrationLegalSupportAudit,
    ConsumerDebtFinancialLegalMetric, StudentRightsConductRepresentationAudit, LegalLiteracyWorkshopMetric, DeterministicLegalPipelineResult
)

class StudentLegalConsultationMeterAgent:
    """Agent 1: Measures legal consultations conducted, licensed staff attorneys, and confidentiality compliance."""
    def run(self, consultations: int = 1420) -> StudentLegalConsultationMetric:
        return StudentLegalConsultationMetric(legal_consultations_conducted=consultations, licensed_attorneys_on_staff=4, confidentiality_compliance_pct=100.0)

class LandlordTenantDisputeAuditorAgent:
    """Agent 2: Audits off-campus lease reviews, security deposit recovery (USD), and tenant dispute resolution rate."""
    def run(self) -> LandlordTenantDisputeAudit:
        return LandlordTenantDisputeAudit(off_campus_lease_reviews_completed=850, security_deposit_recovery_usd=142000.0, tenant_dispute_resolution_pct=94.5)

class StudentImmigrationLegalSupportAuditorAgent:
    """Agent 3: Audits immigration legal consultations and visa assistance case volume."""
    def run(self) -> StudentImmigrationLegalSupportAudit:
        return StudentImmigrationLegalSupportAudit(immigration_legal_consultations=480, dca_tps_visa_assistance_cases=120)

class ConsumerDebtFinancialLegalMeterAgent:
    """Agent 4: Measures identity theft consumer cases and debt collection dispute resolutions."""
    def run(self) -> ConsumerDebtFinancialLegalMetric:
        return ConsumerDebtFinancialLegalMetric(identity_theft_consumer_cases=85, debt_collection_dispute_resolutions=64)

class StudentRightsConductRepresentationAuditorAgent:
    """Agent 5: Audits conduct hearing advisor representation count and due process compliance percentage."""
    def run(self) -> StudentRightsConductRepresentationAudit:
        return StudentRightsConductRepresentationAudit(university_conduct_hearing_advisors=210, due_process_compliance_pct=100.0)

class LegalLiteracyWorkshopMeterAgent:
    """Agent 6: Measures 'Know Your Rights' workshops hosted, attendees total, and satisfaction rating."""
    def run(self) -> LegalLiteracyWorkshopMetric:
        return LegalLiteracyWorkshopMetric(know_your_rights_workshops_hosted=24, workshop_attendees_total=3200, student_satisfaction_rating=4.85)

class StudentLegalAdvocacyScorerAgent:
    """Agent 7: Master deterministic aggregator for Student Legal & Advocacy Services."""
    def __init__(self):
        self.consultation_agent = StudentLegalConsultationMeterAgent()
        self.housing_agent = LandlordTenantDisputeAuditorAgent()
        self.immigration_agent = StudentImmigrationLegalSupportAuditorAgent()
        self.consumer_agent = ConsumerDebtFinancialLegalMeterAgent()
        self.conduct_agent = StudentRightsConductRepresentationAuditorAgent()
        self.workshop_agent = LegalLiteracyWorkshopMeterAgent()

    def run(self, consultations: int = 1420) -> DeterministicLegalPipelineResult:
        consultation_res = self.consultation_agent.run(consultations)
        housing_disputes = self.housing_agent.run()
        immigration_support = self.immigration_agent.run()
        consumer_debt = self.consumer_agent.run()
        conduct_representation = self.conduct_agent.run()
        literacy_workshops = self.workshop_agent.run()

        metrics = {
            "confidentiality": consultation_res.confidentiality_compliance_pct,
            "due_process": conduct_representation.due_process_compliance_pct,
            "dispute_resolution": housing_disputes.tenant_dispute_resolution_pct,
            "workshop_satisfaction": (literacy_workshops.student_satisfaction_rating / 5.0) * 100
        }
        weights = {"confidentiality": 0.35, "due_process": 0.30, "dispute_resolution": 0.20, "workshop_satisfaction": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(consultation_res.legal_consultations_conducted, 100)
        return DeterministicLegalPipelineResult(
            consultations=consultation_res, housing_disputes=housing_disputes,
            immigration_support=immigration_support, consumer_debt=consumer_debt,
            conduct_representation=conduct_representation, literacy_workshops=literacy_workshops,
            legal_advocacy_score=score, confidence_score=confidence
        )
