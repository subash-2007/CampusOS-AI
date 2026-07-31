"""
Script to generate departments 101-111 for CampusOS AI.
Run from d:\CampusOS with PYTHONPATH set.
"""
import os

DEPT_BASE = r"d:\CampusOS\departments"

DEPARTMENTS = [
    {
        "id": "dept_101", "dirname": "global_engagement_partnerships",
        "name": "Global Engagement & International Partnerships",
        "tier_name": "WORLD-CLASS GLOBAL ENGAGEMENT INSTITUTION",
        "score_field": "global_score",
        "agents": [
            ("InternationalStudentEnrollmentMeterAgent", "int_students: int = 3840", "int_students", "InternationalStudentEnrollmentMetric", "students_enrolled_from_international_countries: int = 3840\n    visa_sponsorship_active_count: int = 3680\n    international_student_avg_gpa: float = 3.62"),
            ("StudyAbroadParticipationMeterAgent", "", "", "StudyAbroadParticipationMetric", "students_studying_abroad_annual: int = 1840\n    semester_programs_pct: float = 58.4\n    stem_study_abroad_participants: int = 480"),
            ("GlobalMOUPartnershipAgreementAuditAgent", "", "", "GlobalMOUPartnershipAgreementAudit", "active_bilateral_mou_agreements: int = 184\n    joint_degree_programs_operational: int = 12\n    dual_diploma_enrollments: int = 84"),
            ("ELIProgramEnglishLanguageAuditAgent", "", "", "ELIProgramEnglishLanguageAudit", "eli_program_enrollment: int = 480\n    toefl_ielts_success_rate_pct: float = 92.4\n    eli_graduate_persistence_pct: float = 88.6"),
            ("InternationalFacultyExchangeMeterAgent", "", "", "InternationalFacultyExchangeMetric", "visiting_international_scholars_hosted: int = 84\n    outbound_faculty_sabbaticals: int = 28\n    joint_research_publications: int = 184"),
            ("CulturalExchangeLanguageProgramMeterAgent", "", "", "CulturalExchangeLanguageProgramMetric", "international_cultural_events_annual: int = 124\n    language_exchange_pairs_active: int = 380\n    global_festival_attendance: int = 8400"),
        ],
        "scoring": {"intl_enrollment": "min(100.0, (det.intl_students.students_enrolled_from_international_countries / 30) * 100)", "mou_agreements": "min(100.0, det.mou.active_bilateral_mou_agreements * 0.5)", "study_abroad": "min(100.0, (det.study_abroad.students_studying_abroad_annual / 18) * 100)", "eli_success": "det.eli.toefl_ielts_success_rate_pct"},
        "weights": {"intl_enrollment": 0.30, "mou_agreements": 0.25, "study_abroad": 0.25, "eli_success": 0.20},
    },
    {
        "id": "dept_102", "dirname": "campus_safety_security",
        "name": "Campus Safety & Security Operations",
        "tier_name": "NATIONALLY ACCREDITED CAMPUS PUBLIC SAFETY DEPARTMENT",
        "score_field": "safety_score",
        "agents": [
            ("CampusPolicePatrolResponseMeterAgent", "", "", "CampusPolicePatrolResponseMetric", "sworn_campus_officers_count: int = 84\n    avg_emergency_response_time_minutes: float = 3.8\n    clery_act_incidents_reported_annual: int = 284"),
            ("CrimePreventionAwarenessProgramMeterAgent", "", "", "CrimePreventionAwarenessProgramMetric", "rad_self_defense_workshop_participants: int = 1840\n    crime_prevention_programs_offered: int = 48\n    bystander_intervention_completions: int = 4200"),
            ("CampusCCTVAccessControlAuditorAgent", "", "", "CampusCCTVAccessControlAudit", "cctv_cameras_operational: int = 2840\n    blue_light_station_uptime_pct: float = 99.97\n    access_control_doors_managed: int = 4800"),
            ("EmergencyMassNotificationAuditorAgent", "", "", "EmergencyMassNotificationAudit", "mass_notification_tests_annual: int = 4\n    avg_notification_delivery_seconds: float = 28.0\n    opt_in_enrollment_rate_pct: float = 94.8"),
            ("CampusParkingCitationEnforcementMeterAgent", "", "", "CampusParkingCitationEnforcementMetric", "registered_parking_permits_issued: int = 8400\n    parking_citations_issued_annual: int = 12400\n    parking_appeal_success_rate_pct: float = 18.4"),
            ("SafetyEscortNightRideServiceMeterAgent", "", "", "SafetyEscortNightRideServiceMetric", "safe_walk_escort_requests_fulfilled: int = 4200\n    night_ride_shuttle_trips_annual: int = 18400\n    escort_service_satisfaction_score: float = 4.82"),
        ],
        "scoring": {"blue_light_uptime": "det.cctv.blue_light_station_uptime_pct", "notification_speed": "max(0.0, 100.0 - (det.notification.avg_notification_delivery_seconds * 0.5))", "response_speed": "max(0.0, 100.0 - (det.patrol.avg_emergency_response_time_minutes * 5))", "escort_satisfaction": "(det.escort.escort_service_satisfaction_score / 5.0) * 100"},
        "weights": {"blue_light_uptime": 0.35, "notification_speed": 0.25, "response_speed": 0.25, "escort_satisfaction": 0.15},
    },
    {
        "id": "dept_103", "dirname": "environmental_health_safety",
        "name": "Environmental Health & Safety Compliance",
        "tier_name": "EPA & OSHA MODEL COMPLIANCE INSTITUTION",
        "score_field": "ehs_score",
        "agents": [
            ("LaboratoryChemicalInventoryAuditorAgent", "", "", "LaboratoryChemicalInventoryAudit", "chemical_inventory_items_managed: int = 48000\n    properly_labeled_containers_pct: float = 99.2\n    expired_chemicals_disposed_annual: int = 1240"),
            ("OccupationalSafetyOSHATrainingMeterAgent", "", "", "OccupationalSafetyOSHATrainingMetric", "osha_training_completions_annual: int = 4200\n    lab_safety_certifications_annual: int = 1840\n    safety_incident_rate_per_100_workers: float = 0.84"),
            ("EnvironmentalPermitWastewaterAuditorAgent", "", "", "EnvironmentalPermitWastewaterAudit", "epa_permits_in_compliance: int = 48\n    stormwater_inspections_annual: int = 12\n    wastewater_discharge_violations: int = 0"),
            ("RadiationBiosafetyIBCComplianceAuditorAgent", "", "", "RadiationBiosafetyIBCComplianceAudit", "ibc_protocol_approvals_annual: int = 184\n    radiation_license_reviews_completed: int = 28\n    bsl2_lab_audits_completed: int = 48"),
            ("FireLifeSafetySystemInspectionMeterAgent", "", "", "FireLifeSafetySystemInspectionMetric", "fire_suppression_inspections_completed: int = 840\n    emergency_exit_lighting_inspections: int = 2840\n    fire_drills_per_building_annual: float = 2.0"),
            ("ADAFacilitiesAccessibilityAuditorAgent", "", "", "ADAFacilitiesAccessibilityAudit", "ada_compliance_inspections_completed: int = 380\n    barrier_removal_projects_annual: int = 48\n    transition_plan_completion_pct: float = 94.8"),
        ],
        "scoring": {"chemical_labeling": "det.chemicals.properly_labeled_containers_pct", "wastewater_compliance": "max(0.0, 100.0 - (det.wastewater.wastewater_discharge_violations * 20))", "ada_completion": "det.ada.transition_plan_completion_pct", "fire_inspection": "min(100.0, (det.fire.fire_suppression_inspections_completed / 8) * 100)"},
        "weights": {"chemical_labeling": 0.30, "wastewater_compliance": 0.35, "ada_completion": 0.20, "fire_inspection": 0.15},
    },
    {
        "id": "dept_104", "dirname": "campus_planning_construction",
        "name": "Campus Planning & Capital Construction",
        "tier_name": "LEED PLATINUM CAMPUS MASTER PLAN INSTITUTION",
        "score_field": "planning_score",
        "agents": [
            ("CapitalProjectBudgetCompletionAuditorAgent", "", "", "CapitalProjectBudgetCompletionAudit", "capital_projects_active: int = 28\n    projects_on_budget_pct: float = 92.4\n    projects_on_schedule_pct: float = 88.6"),
            ("LEEDGreenBuildingCertificationMeterAgent", "", "", "LEEDGreenBuildingCertificationMetric", "leed_certified_buildings_count: int = 48\n    leed_platinum_buildings: int = 8\n    energy_star_buildings: int = 24"),
            ("CampusMasterPlanMilestoneMeterAgent", "", "", "CampusMasterPlanMilestoneMetric", "campus_master_plan_milestones_completed: int = 48\n    total_master_plan_milestones: int = 52\n    master_plan_completion_pct: float = 92.3"),
            ("SpaceUtilizationClassroomLabAuditorAgent", "", "", "SpaceUtilizationClassroomLabAudit", "classrooms_utilization_rate_pct: float = 74.8\n    research_lab_utilization_rate_pct: float = 82.4\n    gross_sq_ft_campus_total: int = 4800000"),
            ("DeferredMaintenanceBacklogAuditorAgent", "", "", "DeferredMaintenanceBacklogAudit", "deferred_maintenance_backlog_millions: float = 84.0\n    facility_condition_index_score_pct: float = 88.4\n    pm_work_orders_completed_annual: int = 48000"),
            ("CampusAccessibilityUniversalDesignAuditAgent", "", "", "CampusAccessibilityUniversalDesignAudit", "universal_design_features_installed: int = 840\n    accessible_routes_pct: float = 96.4\n    signage_braille_wayfinding_compliance_pct: float = 98.2"),
        ],
        "scoring": {"budget_compliance": "det.capital.projects_on_budget_pct", "schedule_compliance": "det.capital.projects_on_schedule_pct", "master_plan": "det.master_plan.master_plan_completion_pct", "fci_score": "det.deferred_maint.facility_condition_index_score_pct"},
        "weights": {"budget_compliance": 0.30, "schedule_compliance": 0.25, "master_plan": 0.25, "fci_score": 0.20},
    },
    {
        "id": "dept_105", "dirname": "community_civic_engagement",
        "name": "Community & Civic Engagement",
        "tier_name": "CARNEGIE COMMUNITY ENGAGEMENT CLASSIFIED INSTITUTION",
        "score_field": "engagement_score",
        "agents": [
            ("ServiceLearningCourseEnrollmentMeterAgent", "", "", "ServiceLearningCourseEnrollmentMetric", "service_learning_courses_offered: int = 184\n    student_enrollment_service_learning: int = 8400\n    community_service_hours_logged: int = 248000"),
            ("AmericorpsVolunteerProgramMeterAgent", "", "", "AmericorpsVolunteerProgramMetric", "americorps_vista_members_hosted: int = 28\n    americorps_service_hours_annual: int = 84000\n    partner_nonprofit_organizations: int = 180"),
            ("CivicLeadershipVoterRegistrationMeterAgent", "", "", "CivicLeadershipVoterRegistrationMetric", "voter_registration_drives_annual: int = 12\n    students_registered_to_vote: int = 4200\n    campus_vote_rate_pct: float = 68.4"),
            ("CommunityPartnershipMOUAuditAgent", "", "", "CommunityPartnershipMOUAudit", "active_community_partnership_mous: int = 124\n    k12_school_partnerships: int = 48\n    community_partner_satisfaction_score: float = 4.72"),
            ("SocialEntrepreneurshipImpactMeterAgent", "", "", "SocialEntrepreneurshipImpactMetric", "social_enterprise_student_ventures: int = 28\n    community_impact_beneficiaries: int = 48000\n    social_venture_sustainability_pct: float = 72.4"),
            ("CommunityEngagementResearchScholarshipAuditAgent", "", "", "CommunityEngagementResearchScholarshipAudit", "community_based_research_projects: int = 84\n    cbr_publications_peer_reviewed: int = 124\n    community_co_investigator_projects: int = 48"),
        ],
        "scoring": {"partner_satisfaction": "(det.partnerships.community_partner_satisfaction_score / 5.0) * 100", "service_hours": "min(100.0, (det.service_learning.community_service_hours_logged / 2000) * 100)", "voter_rate": "det.civic.campus_vote_rate_pct", "community_mous": "min(100.0, det.partnerships.active_community_partnership_mous * 0.75)"},
        "weights": {"partner_satisfaction": 0.30, "service_hours": 0.30, "voter_rate": 0.20, "community_mous": 0.20},
    },
]

for d in DEPARTMENTS:
    path = os.path.join(DEPT_BASE, d["dirname"])
    os.makedirs(os.path.join(path, "tests"), exist_ok=True)
    # Write __init__.py
    with open(os.path.join(path, "__init__.py"), "w") as f:
        f.write(f'"""{d["id"]} - {d["name"]} Department"""\nfrom app.agents.base_agent import BaseAgent\n')
    with open(os.path.join(path, "tests", "__init__.py"), "w") as f:
        f.write(f'"""{d["id"]} tests init"""')
    print(f"Created scaffold for {d['id']} {d['dirname']}")

print("All scaffolds created.")
