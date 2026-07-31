import pytest, asyncio
from departments.housing_residential_life.deterministic import (
    HousingOccupancyCapacityMeterAgent, RoommateMatchingSatisfactionAuditorAgent, ResidentAdvisorStaffingRatioAuditorAgent,
    LivingLearningCommunityEngagementMeterAgent, FacilitiesWorkOrderResolutionAuditorAgent, MoveInOutCheckinCheckoutMeterAgent, StudentHousingResidentialLifeScorerAgent
)
from departments.housing_residential_life.orchestrator import StudentHousingResidentialLifeOrchestratorAgent

def test_housing_occupancy_capacity_meter():
    res = HousingOccupancyCapacityMeterAgent().run(9500)
    assert res.total_residence_hall_beds == 9500
    assert res.housing_occupancy_rate_pct >= 90.0

def test_roommate_matching_satisfaction_auditor():
    res = RoommateMatchingSatisfactionAuditorAgent().run()
    assert res.roommate_satisfaction_rate_pct >= 90.0

def test_resident_advisor_staffing_ratio_auditor():
    res = ResidentAdvisorStaffingRatioAuditorAgent().run()
    assert res.ra_training_completion_pct == 100.0

def test_living_learning_community_engagement_meter():
    res = LivingLearningCommunityEngagementMeterAgent().run()
    assert res.llc_first_year_retention_rate_pct >= 90.0

def test_facilities_work_order_resolution_auditor():
    res = FacilitiesWorkOrderResolutionAuditorAgent().run()
    assert res.work_orders_resolved_in_24h_pct >= 90.0
    assert res.avg_resolution_time_hours <= 24.0

def test_move_in_out_checkin_checkout_meter():
    res = MoveInOutCheckinCheckoutMeterAgent().run()
    assert res.move_in_digital_checkins_completed >= 1000

def test_student_housing_residential_life_scorer():
    res = StudentHousingResidentialLifeScorerAgent().run(9500)
    assert res.housing_score >= 90.0
    assert res.confidence_score >= 0.5

def test_student_housing_residential_life_orchestrator():
    report = asyncio.run(StudentHousingResidentialLifeOrchestratorAgent().run_pipeline(9500))
    assert report.department == "Student Housing & Residential Life"
    assert report.department_id == "dept_083"
    assert report.housing_tier == "EXEMPLARY RESIDENTIAL COMMUNITY"
    assert len(report.reasoning_steps) == 4
