from departments.shared.scoring import ScoringEngine
from departments.residential_housing_operations.schemas import (
    KeycardAccessSecurityAudit, ResidenceHallHousekeepingSanitationAudit, HVACUtilityEnergyConsumptionMetric,
    ResidenceHallLaundryMachineStatusMetric, MailroomPackageLockerFulfillmentMetric, SummerConferenceHousingTurnaroundAudit, DeterministicResidentialHousingPipelineResult
)

class KeycardAccessSecurityAuditorAgent:
    """Agent 1: Audits electronic keycard doors managed, access control uptime percentage, and tailgating incidents."""
    def run(self, doors: int = 4800) -> KeycardAccessSecurityAudit:
        return KeycardAccessSecurityAudit(electronic_keycard_doors_managed=doors, access_control_uptime_pct=99.99, unauthorized_tailgating_incidents=4)

class ResidenceHallHousekeepingSanitationAuditorAgent:
    """Agent 2: Audits common areas cleaned, daily sanitation inspection score percentage, and custodial staffing fulfillment."""
    def run(self) -> ResidenceHallHousekeepingSanitationAudit:
        return ResidenceHallHousekeepingSanitationAudit(residence_hall_common_areas_cleaned=340, daily_sanitation_inspection_score_pct=98.6, custodial_staffing_fulfillment_pct=96.5)

class HVACUtilityEnergyConsumptionMeterAgent:
    """Agent 3: Measures smart thermostat coverage percentage, HVAC emergency repairs, and building energy efficiency score."""
    def run(self) -> HVACUtilityEnergyConsumptionMetric:
        return HVACUtilityEnergyConsumptionMetric(smart_thermostat_coverage_pct=92.4, hvac_emergency_repairs_annual=24, building_energy_efficiency_score=91.8)

class ResidenceHallLaundryMachineStatusMeterAgent:
    """Agent 4: Measures campus laundry machines count, machine uptime percentage, and mobile laundry app users."""
    def run(self) -> ResidenceHallLaundryMachineStatusMetric:
        return ResidenceHallLaundryMachineStatusMetric(campus_laundry_machines_managed=380, laundry_machine_uptime_pct=97.8, mobile_laundry_app_active_users=8400)

class MailroomPackageLockerFulfillmentMeterAgent:
    """Agent 5: Measures annual student packages processed, smart locker pickup time (hours), and misplacement rate percentage."""
    def run(self) -> MailroomPackageLockerFulfillmentMetric:
        return MailroomPackageLockerFulfillmentMetric(student_packages_processed_annual=145000, smart_locker_pickup_time_avg_hours=3.2, package_misplacement_rate_pct=0.05)

class SummerConferenceHousingTurnaroundAuditorAgent:
    """Agent 6: Audits summer conference rooms prepared and room turnaround cleaning speed (hours)."""
    def run(self) -> SummerConferenceHousingTurnaroundAudit:
        return SummerConferenceHousingTurnaroundAudit(summer_conference_rooms_prepared=3200, room_turnaround_cleaning_speed_hours=4.0)

class ResidentialHousingOperationsScorerAgent:
    """Agent 7: Master deterministic aggregator for Residential Housing Operations."""
    def __init__(self):
        self.security_agent = KeycardAccessSecurityAuditorAgent()
        self.housekeeping_agent = ResidenceHallHousekeepingSanitationAuditorAgent()
        self.hvac_agent = HVACUtilityEnergyConsumptionMeterAgent()
        self.laundry_agent = ResidenceHallLaundryMachineStatusMeterAgent()
        self.mailroom_agent = MailroomPackageLockerFulfillmentMeterAgent()
        self.summer_housing_agent = SummerConferenceHousingTurnaroundAuditorAgent()

    def run(self, doors: int = 4800) -> DeterministicResidentialHousingPipelineResult:
        security = self.security_agent.run(doors)
        housekeeping = self.housekeeping_agent.run()
        hvac = self.hvac_agent.run()
        laundry = self.laundry_agent.run()
        mailroom = self.mailroom_agent.run()
        summer_housing = self.summer_housing_agent.run()

        metrics = {
            "access_uptime": security.access_control_uptime_pct,
            "sanitation_score": housekeeping.daily_sanitation_inspection_score_pct,
            "laundry_uptime": laundry.laundry_machine_uptime_pct,
            "package_accuracy": max(0.0, 100.0 - (mailroom.package_misplacement_rate_pct * 100))
        }
        weights = {"access_uptime": 0.35, "sanitation_score": 0.30, "laundry_uptime": 0.20, "package_accuracy": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(security.electronic_keycard_doors_managed, 100)
        return DeterministicResidentialHousingPipelineResult(
            security=security, housekeeping=housekeeping, hvac=hvac,
            laundry=laundry, mailroom=mailroom, summer_housing=summer_housing,
            residential_housing_score=score, confidence_score=confidence
        )
