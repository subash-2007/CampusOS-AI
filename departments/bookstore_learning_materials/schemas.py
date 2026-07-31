from typing import List
from pydantic import BaseModel

class TextbookAdoptionDeadlineAudit(BaseModel):
    courses_with_textbook_adoptions_logged: int = 2850
    faculty_adoption_deadline_compliance_pct: float = 96.4
    inclusive_access_courses_count: int = 1420

class OpenEducationalResourcesMetric(BaseModel):
    oer_courses_adopted: int = 680
    student_cost_savings_oer_usd: float = 1850000.0
    zero_textbook_cost_sections: int = 840

class DigitalAccessCodeFulfillmentMetric(BaseModel):
    digital_access_codes_issued: int = 18400
    instant_day_one_access_pct: float = 98.8
    digital_code_support_tickets: int = 42

class UsedTextbookBuybackAudit(BaseModel):
    textbooks_rented_annual: int = 8400
    buyback_payout_to_students_usd: float = 420000.0
    textbook_rental_savings_usd: float = 850000.0

class CampusMerchandiseStoreMetric(BaseModel):
    apparel_merchandise_sales_usd: float = 2400000.0
    licensing_royalty_revenue_usd: float = 380000.0

class AffordableLearningMaterialsGrantAudit(BaseModel):
    affordability_grants_awarded_usd: float = 250000.0
    faculty_grant_recipients_count: int = 45

class DeterministicBookstorePipelineResult(BaseModel):
    adoptions: TextbookAdoptionDeadlineAudit
    oer: OpenEducationalResourcesMetric
    digital_access: DigitalAccessCodeFulfillmentMetric
    buyback: UsedTextbookBuybackAudit
    merchandise: CampusMerchandiseStoreMetric
    grants: AffordableLearningMaterialsGrantAudit
    bookstore_score: float
    confidence_score: float

class StrategicBookstoreNarrative(BaseModel):
    bookstore_summary: str
    key_bookstore_strengths: List[str]

class AffordableLearningPlan(BaseModel):
    affordability_actions: List[str]
    sample_inclusive_access_contract: str

class ReasoningBookstorePipelineResult(BaseModel):
    narrative: StrategicBookstoreNarrative
    affordability_plan: AffordableLearningPlan
    reasoning_steps: List[str]

class BookstoreLearningMaterialsOrchestratorReport(BaseModel):
    department: str = "Campus Bookstore & Learning Materials"
    department_id: str = "dept_071"
    bookstore_tier: str = "AFFORDABLE LEARNING EXCELLENCE CENTER"
    bookstore_score: float
    confidence_score: float
    deterministic_analysis: DeterministicBookstorePipelineResult
    reasoning_analysis: ReasoningBookstorePipelineResult
    reasoning_steps: List[str]
