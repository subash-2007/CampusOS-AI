import pytest, asyncio
from departments.bookstore_learning_materials.deterministic import (
    TextbookAdoptionDeadlineAuditorAgent, OpenEducationalResourcesMeterAgent, DigitalAccessCodeFulfillmentMeterAgent,
    UsedTextbookBuybackAuditorAgent, CampusMerchandiseStoreMeterAgent, AffordableLearningMaterialsGrantAuditorAgent, BookstoreLearningMaterialsScorerAgent
)
from departments.bookstore_learning_materials.orchestrator import BookstoreLearningMaterialsOrchestratorAgent

def test_textbook_adoption_deadline_auditor():
    res = TextbookAdoptionDeadlineAuditorAgent().run(2850)
    assert res.courses_with_textbook_adoptions_logged == 2850
    assert res.faculty_adoption_deadline_compliance_pct >= 90.0

def test_open_educational_resources_meter():
    res = OpenEducationalResourcesMeterAgent().run()
    assert res.student_cost_savings_oer_usd > 1000000.0

def test_digital_access_code_fulfillment_meter():
    res = DigitalAccessCodeFulfillmentMeterAgent().run()
    assert res.instant_day_one_access_pct >= 95.0

def test_used_textbook_buyback_auditor():
    res = UsedTextbookBuybackAuditorAgent().run()
    assert res.textbook_rental_savings_usd > 500000.0

def test_campus_merchandise_store_meter():
    res = CampusMerchandiseStoreMeterAgent().run()
    assert res.apparel_merchandise_sales_usd > 1000000.0

def test_affordable_learning_materials_grant_auditor():
    res = AffordableLearningMaterialsGrantAuditorAgent().run()
    assert res.affordability_grants_awarded_usd > 100000.0

def test_bookstore_learning_materials_scorer():
    res = BookstoreLearningMaterialsScorerAgent().run(2850)
    assert res.bookstore_score >= 88.0
    assert res.confidence_score >= 0.5

def test_bookstore_learning_materials_orchestrator():
    report = asyncio.run(BookstoreLearningMaterialsOrchestratorAgent().run_pipeline(2850))
    assert report.department == "Campus Bookstore & Learning Materials"
    assert report.department_id == "dept_071"
    assert report.bookstore_tier == "AFFORDABLE LEARNING EXCELLENCE CENTER"
    assert len(report.reasoning_steps) == 4
