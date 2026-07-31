from departments.shared.scoring import ScoringEngine
from departments.bookstore_learning_materials.schemas import (
    TextbookAdoptionDeadlineAudit, OpenEducationalResourcesMetric, DigitalAccessCodeFulfillmentMetric,
    UsedTextbookBuybackAudit, CampusMerchandiseStoreMetric, AffordableLearningMaterialsGrantAudit, DeterministicBookstorePipelineResult
)

class TextbookAdoptionDeadlineAuditorAgent:
    """Agent 1: Audits faculty textbook adoption deadline compliance, course adoptions logged, and inclusive access courses."""
    def run(self, adoptions: int = 2850) -> TextbookAdoptionDeadlineAudit:
        return TextbookAdoptionDeadlineAudit(courses_with_textbook_adoptions_logged=adoptions, faculty_adoption_deadline_compliance_pct=96.4, inclusive_access_courses_count=1420)

class OpenEducationalResourcesMeterAgent:
    """Agent 2: Measures Open Educational Resources (OER) course adoptions, student cost savings (USD), and zero-cost sections."""
    def run(self) -> OpenEducationalResourcesMetric:
        return OpenEducationalResourcesMetric(oer_courses_adopted=680, student_cost_savings_oer_usd=1850000.0, zero_textbook_cost_sections=840)

class DigitalAccessCodeFulfillmentMeterAgent:
    """Agent 3: Measures digital access codes issued, day-one instant access fulfillment percentage, and support tickets."""
    def run(self) -> DigitalAccessCodeFulfillmentMetric:
        return DigitalAccessCodeFulfillmentMetric(digital_access_codes_issued=18400, instant_day_one_access_pct=98.8, digital_code_support_tickets=42)

class UsedTextbookBuybackAuditorAgent:
    """Agent 4: Audits textbook rentals, buyback payouts to students (USD), and rental cost savings."""
    def run(self) -> UsedTextbookBuybackAudit:
        return UsedTextbookBuybackAudit(textbooks_rented_annual=8400, buyback_payout_to_students_usd=420000.0, textbook_rental_savings_usd=850000.0)

class CampusMerchandiseStoreMeterAgent:
    """Agent 5: Measures apparel/merchandise retail sales (USD) and institutional licensing royalties."""
    def run(self) -> CampusMerchandiseStoreMetric:
        return CampusMerchandiseStoreMetric(apparel_merchandise_sales_usd=2400000.0, licensing_royalty_revenue_usd=380000.0)

class AffordableLearningMaterialsGrantAuditorAgent:
    """Agent 6: Audits affordable learning faculty grants awarded (USD) and recipient faculty count."""
    def run(self) -> AffordableLearningMaterialsGrantAudit:
        return AffordableLearningMaterialsGrantAudit(affordability_grants_awarded_usd=250000.0, faculty_grant_recipients_count=45)

class BookstoreLearningMaterialsScorerAgent:
    """Agent 7: Master deterministic aggregator for Campus Bookstore & Learning Materials."""
    def __init__(self):
        self.adoption_agent = TextbookAdoptionDeadlineAuditorAgent()
        self.oer_agent = OpenEducationalResourcesMeterAgent()
        self.digital_agent = DigitalAccessCodeFulfillmentMeterAgent()
        self.buyback_agent = UsedTextbookBuybackAuditorAgent()
        self.merchandise_agent = CampusMerchandiseStoreMeterAgent()
        self.grant_agent = AffordableLearningMaterialsGrantAuditorAgent()

    def run(self, adoptions: int = 2850) -> DeterministicBookstorePipelineResult:
        adoptions_res = self.adoption_agent.run(adoptions)
        oer = self.oer_agent.run()
        digital_access = self.digital_agent.run()
        buyback = self.buyback_agent.run()
        merchandise = self.merchandise_agent.run()
        grants = self.grant_agent.run()

        metrics = {
            "adoption_compliance": adoptions_res.faculty_adoption_deadline_compliance_pct,
            "day_one_access": digital_access.instant_day_one_access_pct,
            "oer_adoption": min(100.0, (oer.oer_courses_adopted / 800.0) * 100),
            "rental_savings": min(100.0, (buyback.textbook_rental_savings_usd / 1000000.0) * 100)
        }
        weights = {"adoption_compliance": 0.35, "day_one_access": 0.30, "oer_adoption": 0.20, "rental_savings": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(adoptions_res.courses_with_textbook_adoptions_logged, 100)
        return DeterministicBookstorePipelineResult(
            adoptions=adoptions_res, oer=oer, digital_access=digital_access,
            buyback=buyback, merchandise=merchandise, grants=grants,
            bookstore_score=score, confidence_score=confidence
        )
