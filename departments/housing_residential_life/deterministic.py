from departments.shared.scoring import ScoringEngine
from departments.housing_residential_life.schemas import (
    HousingOccupancyCapacityMetric, RoommateMatchingSatisfactionAudit, ResidentAdvisorStaffingRatioAudit,
    LivingLearningCommunityEngagementMetric, FacilitiesWorkOrderResolutionAudit, MoveInOutCheckinCheckoutMetric, DeterministicHousingPipelineResult
)

class HousingOccupancyCapacityMeterAgent:
    """Agent 1: Measures total residence hall beds, occupied beds, and occupancy rate percentage."""
    def run(self, beds: int = 9500) -> HousingOccupancyCapacityMetric:
        return HousingOccupancyCapacityMetric(total_residence_hall_beds=beds, occupied_beds_count=9320, housing_occupancy_rate_pct=98.1)

class RoommateMatchingSatisfactionAuditorAgent:
    """Agent 2: Audits roommate pairings created, conflict transfer requests, and satisfaction rate percentage."""
    def run(self) -> RoommateMatchingSatisfactionAudit:
        return RoommateMatchingSatisfactionAudit(roommate_pairings_created=4200, roommate_conflict_transfer_requests=84, roommate_satisfaction_rate_pct=98.0)

class ResidentAdvisorStaffingRatioAuditorAgent:
    """Agent 3: Audits active resident advisors count, RA-to-resident ratio, and training completion percentage."""
    def run(self) -> ResidentAdvisorStaffingRatioAudit:
        return ResidentAdvisorStaffingRatioAudit(resident_advisors_active=180, ra_to_resident_ratio=51.7, ra_training_completion_pct=100.0)

class LivingLearningCommunityEngagementMeterAgent:
    """Agent 4: Measures active living-learning communities, enrolled residents, and first-year retention rate."""
    def run(self) -> LivingLearningCommunityEngagementMetric:
        return LivingLearningCommunityEngagementMetric(active_living_learning_communities=14, llc_enrolled_residents=1850, llc_first_year_retention_rate_pct=94.2)

class FacilitiesWorkOrderResolutionAuditorAgent:
    """Agent 5: Audits maintenance work orders annual volume, 24-hour resolution percentage, and average resolution time."""
    def run(self) -> FacilitiesWorkOrderResolutionAudit:
        return FacilitiesWorkOrderResolutionAudit(maintenance_work_orders_annual=8400, work_orders_resolved_in_24h_pct=96.5, avg_resolution_time_hours=14.2)

class MoveInOutCheckinCheckoutMeterAgent:
    """Agent 6: Measures digital move-in check-ins completed and average check-in time (mins)."""
    def run(self) -> MoveInOutCheckinCheckoutMetric:
        return MoveInOutCheckinCheckoutMetric(move_in_digital_checkins_completed=4200, avg_move_in_checkin_minutes=3.8)

class StudentHousingResidentialLifeScorerAgent:
    """Agent 7: Master deterministic aggregator for Student Housing & Residential Life."""
    def __init__(self):
        self.occupancy_agent = HousingOccupancyCapacityMeterAgent()
        self.roommates_agent = RoommateMatchingSatisfactionAuditorAgent()
        self.staffing_agent = ResidentAdvisorStaffingRatioAuditorAgent()
        self.llc_agent = LivingLearningCommunityEngagementMeterAgent()
        self.facilities_agent = FacilitiesWorkOrderResolutionAuditorAgent()
        self.move_in_agent = MoveInOutCheckinCheckoutMeterAgent()

    def run(self, beds: int = 9500) -> DeterministicHousingPipelineResult:
        occupancy = self.occupancy_agent.run(beds)
        roommates = self.roommates_agent.run()
        staffing = self.staffing_agent.run()
        llc = self.llc_agent.run()
        facilities = self.facilities_agent.run()
        move_in = self.move_in_agent.run()

        metrics = {
            "ra_training": staffing.ra_training_completion_pct,
            "roommate_satisfaction": roommates.roommate_satisfaction_rate_pct,
            "occupancy_rate": occupancy.housing_occupancy_rate_pct,
            "work_order_resolution": facilities.work_orders_resolved_in_24h_pct
        }
        weights = {"ra_training": 0.35, "roommate_satisfaction": 0.30, "occupancy_rate": 0.20, "work_order_resolution": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(occupancy.occupied_beds_count, 500)
        return DeterministicHousingPipelineResult(
            occupancy=occupancy, roommates=roommates, staffing=staffing,
            llc=llc, facilities=facilities, move_in=move_in,
            housing_score=score, confidence_score=confidence
        )
