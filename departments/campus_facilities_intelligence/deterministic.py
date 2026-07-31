from departments.shared.scoring import ScoringEngine
from departments.campus_facilities_intelligence.schemas import (
    HousingOccupancyMetric, MaintenanceTicketResolutionMetric, CampusEnergySustainabilityAudit,
    FacilityBookingUtilizationMetric, CampusSafetyAudit, DiningFacilityQualityAudit, DeterministicFacilitiesPipelineResult
)

class HousingOccupancyMeterAgent:
    """Agent 1: Measures housing bed capacity, occupied beds, and occupancy rate percentage."""
    def run(self, capacity: int = 4500) -> HousingOccupancyMetric:
        occupied = 4320
        return HousingOccupancyMetric(total_bed_capacity=capacity, occupied_beds_count=occupied, occupancy_rate_pct=(occupied / capacity) * 100)

class MaintenanceTicketResolutionMeterAgent:
    """Agent 2: Measures average resolution hours, urgent SLA compliance, and open ticket counts."""
    def run(self) -> MaintenanceTicketResolutionMetric:
        return MaintenanceTicketResolutionMetric(avg_maintenance_resolution_hours=14.5, urgent_maintenance_sla_compliance_pct=98.2, open_tickets_count=24)

class CampusEnergySustainabilityAuditorAgent:
    """Agent 3: Audits renewable energy share, LEED certified building count, and carbon reduction."""
    def run(self) -> CampusEnergySustainabilityAudit:
        return CampusEnergySustainabilityAudit(renewable_energy_share_pct=42.0, leed_certified_buildings_count=14, carbon_footprint_reduction_pct=18.5)

class FacilityBookingUtilizationMeterAgent:
    """Agent 4: Measures study room and lab space booking utilization rates."""
    def run(self) -> FacilityBookingUtilizationMetric:
        return FacilityBookingUtilizationMetric(study_room_booking_utilization_pct=84.0, lab_space_utilization_pct=76.5)

class CampusSafetyAuditorAgent:
    """Agent 5: Audits keycard access points, emergency call box compliance, and safety incident rates."""
    def run(self) -> CampusSafetyAudit:
        return CampusSafetyAudit(keycard_access_points_active=420, emergency_call_box_compliance_pct=100.0, safety_incident_rate_per_1k=0.4)

class DiningFacilityQualityAuditorAgent:
    """Agent 6: Audits dining hall customer satisfaction and dietary restriction option counts."""
    def run(self) -> DiningFacilityQualityAudit:
        return DiningFacilityQualityAudit(dining_hall_csat_pct=91.0, dietary_restriction_options_count=18)

class CampusFacilitiesScorerAgent:
    """Agent 7: Master deterministic aggregator for Campus Housing & Facilities Intelligence."""
    def __init__(self):
        self.occupancy_agent = HousingOccupancyMeterAgent()
        self.maintenance_agent = MaintenanceTicketResolutionMeterAgent()
        self.sustainability_agent = CampusEnergySustainabilityAuditorAgent()
        self.utilization_agent = FacilityBookingUtilizationMeterAgent()
        self.safety_agent = CampusSafetyAuditorAgent()
        self.dining_agent = DiningFacilityQualityAuditorAgent()

    def run(self, capacity: int = 4500) -> DeterministicFacilitiesPipelineResult:
        occupancy = self.occupancy_agent.run(capacity)
        maintenance = self.maintenance_agent.run()
        sustainability = self.sustainability_agent.run()
        utilization = self.utilization_agent.run()
        safety = self.safety_agent.run()
        dining = self.dining_agent.run()

        metrics = {
            "occupancy": occupancy.occupancy_rate_pct,
            "maintenance_sla": maintenance.urgent_maintenance_sla_compliance_pct,
            "safety": safety.emergency_call_box_compliance_pct,
            "dining_csat": dining.dining_hall_csat_pct
        }
        weights = {"occupancy": 0.30, "maintenance_sla": 0.30, "safety": 0.20, "dining_csat": 0.20}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(sustainability.leed_certified_buildings_count, 5)
        return DeterministicFacilitiesPipelineResult(
            occupancy=occupancy, maintenance=maintenance, sustainability=sustainability,
            utilization=utilization, safety=safety, dining=dining,
            facilities_health_score=score, confidence_score=confidence
        )
