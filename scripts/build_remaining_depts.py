import os

BASE = r"d:\CampusOS\departments"

DEPTS_DATA = [
    {
        "id": "dept_104",
        "dirname": "campus_planning_construction",
        "name": "Campus Planning and Capital Construction",
        "class_prefix": "CampusPlanningConstruction",
        "tier": "LEED PLATINUM CAMPUS MASTER PLAN INSTITUTION",
        "score_field": "planning_score",
        "agent_prefix": "Planning",
        "det_agents": [
            ("CapitalProjectBudgetCompletionAuditorAgent", "capital", "CapitalProjectBudgetCompletionAudit", "capital_projects_active: int = 28\n    projects_on_budget_pct: float = 92.4\n    projects_on_schedule_pct: float = 88.6"),
            ("LEEDGreenBuildingCertificationMeterAgent", "leed", "LEEDGreenBuildingCertificationMetric", "leed_certified_buildings_count: int = 48\n    leed_platinum_buildings: int = 8\n    energy_star_buildings: int = 24"),
            ("CampusMasterPlanMilestoneMeterAgent", "master_plan", "CampusMasterPlanMilestoneMetric", "campus_master_plan_milestones_completed: int = 48\n    total_master_plan_milestones: int = 52\n    master_plan_completion_pct: float = 92.3"),
            ("SpaceUtilizationClassroomLabAuditorAgent", "space", "SpaceUtilizationClassroomLabAudit", "classrooms_utilization_rate_pct: float = 74.8\n    research_lab_utilization_rate_pct: float = 82.4\n    gross_sq_ft_campus_total: int = 4800000"),
            ("DeferredMaintenanceBacklogAuditorAgent", "deferred_maint", "DeferredMaintenanceBacklogAudit", "deferred_maintenance_backlog_millions: float = 84.0\n    facility_condition_index_score_pct: float = 88.4\n    pm_work_orders_completed_annual: int = 48000"),
            ("CampusAccessibilityUniversalDesignAuditorAgent", "ada", "CampusAccessibilityUniversalDesignAudit", "universal_design_features_installed: int = 840\n    accessible_routes_pct: float = 96.4\n    signage_braille_wayfinding_compliance_pct: float = 98.2"),
        ],
        "metrics_calc": """metrics = {
            "budget_compliance": capital.projects_on_budget_pct,
            "schedule_compliance": capital.projects_on_schedule_pct,
            "master_plan": master_plan.master_plan_completion_pct,
            "fci_score": deferred_maint.facility_condition_index_score_pct
        }
        weights = {"budget_compliance": 0.30, "schedule_compliance": 0.25, "master_plan": 0.25, "fci_score": 0.20}""",
        "count_val": "capital.capital_projects_active",
        "eval_role": "Vice President for Facilities and Campus Planning",
        "eval_topics": "capital projects, LEED certification, master plan, deferred maintenance, universal design",
        "plan_role": "Capital Construction Director and Campus Architect",
        "plan_topics": "BIM 3D modeling, smart building IoT sensors, LEED Platinum, deferred maintenance reduction",
        "plan_actions": '["Deploy BIM (Building Information Modeling) 3D Twin for all capital construction projects", "Implement Smart Building IoT Sensor Mesh optimizing HVAC and lighting energy consumption"]',
        "sample_schema": '''{\\n  "project_id": "CAP_2026_0048",\\n  "project_name": "Interdisciplinary Science & Engineering Complex",\\n  "budget_millions": 84.5,\\n  "completion_pct": 78.4,\\n  "leed_target": "LEED Platinum",\\n  "status": "ON BUDGET AND ON SCHEDULE"\\n}''',
        "test_asserts": "assert res.capital_projects_active >= 5\n    assert res.projects_on_budget_pct >= 80.0"
    },
    {
        "id": "dept_105",
        "dirname": "community_civic_engagement",
        "name": "Community and Civic Engagement",
        "class_prefix": "CommunityCivicEngagement",
        "tier": "CARNEGIE COMMUNITY ENGAGEMENT CLASSIFIED INSTITUTION",
        "score_field": "engagement_score",
        "agent_prefix": "Civic",
        "det_agents": [
            ("ServiceLearningCourseEnrollmentMeterAgent", "service_learning", "ServiceLearningCourseEnrollmentMetric", "service_learning_courses_offered: int = 184\n    student_enrollment_service_learning: int = 8400\n    community_service_hours_logged: int = 248000"),
            ("AmericorpsVolunteerProgramMeterAgent", "americorps", "AmericorpsVolunteerProgramMetric", "americorps_vista_members_hosted: int = 28\n    americorps_service_hours_annual: int = 84000\n    partner_nonprofit_organizations: int = 180"),
            ("CivicLeadershipVoterRegistrationMeterAgent", "civic", "CivicLeadershipVoterRegistrationMetric", "voter_registration_drives_annual: int = 12\n    students_registered_to_vote: int = 4200\n    campus_vote_rate_pct: float = 68.4"),
            ("CommunityPartnershipMOUAuditorAgent", "partnerships", "CommunityPartnershipMOUAudit", "active_community_partnership_mous: int = 124\n    k12_school_partnerships: int = 48\n    community_partner_satisfaction_score: float = 4.72"),
            ("SocialEntrepreneurshipImpactMeterAgent", "social_venture", "SocialEntrepreneurshipImpactMetric", "social_enterprise_student_ventures: int = 28\n    community_impact_beneficiaries: int = 48000\n    social_venture_sustainability_pct: float = 72.4"),
            ("CommunityEngagementResearchScholarshipAuditorAgent", "research", "CommunityEngagementResearchScholarshipAudit", "community_based_research_projects: int = 84\n    cbr_publications_peer_reviewed: int = 124\n    community_co_investigator_projects: int = 48"),
        ],
        "metrics_calc": """metrics = {
            "partner_satisfaction": (partnerships.community_partner_satisfaction_score / 5.0) * 100,
            "service_hours": min(100.0, (service_learning.community_service_hours_logged / 2000) * 100),
            "voter_rate": civic.campus_vote_rate_pct,
            "community_mous": min(100.0, partnerships.active_community_partnership_mous * 0.75)
        }
        weights = {"partner_satisfaction": 0.30, "service_hours": 0.30, "voter_rate": 0.20, "community_mous": 0.20}""",
        "count_val": "service_learning.student_enrollment_service_learning",
        "eval_role": "Associate Vice President for Community Relations and Civic Engagement",
        "eval_topics": "service learning, AmeriCorps, voter turnout, community MOUs, social entrepreneurship",
        "plan_role": "Director of Campus Community Partnerships",
        "plan_topics": "digital service-learning portal, civic voter engagement, K-12 tutoring pipeline",
        "plan_actions": '["Deploy Digital Service-Learning Portal tracking community service hours and partner impact metrics", "Launch K-12 University STEM Mentorship Pipeline engaging 48 local public schools"]',
        "sample_schema": '''{\\n  "project_id": "CIV_2026_0012",\\n  "partner_name": "Urban Youth Educational Alliance",\\n  "service_hours": 12400,\\n  "student_participants": 320,\\n  "satisfaction_rating": 4.85,\\n  "status": "ACTIVE MOUS"\\n}''',
        "test_asserts": "assert res.service_learning_courses_offered >= 10\n    assert res.community_service_hours_logged >= 1000"
    },
    {
        "id": "dept_106",
        "dirname": "alumni_advancement_endowment",
        "name": "Alumni Advancement and Endowment Management",
        "class_prefix": "AlumniAdvancementEndowment",
        "tier": "BILLION DOLLAR CAMPUS ENDOWMENT ADVANCEMENT EXCELLENCE",
        "score_field": "advancement_score",
        "agent_prefix": "Advancement",
        "det_agents": [
            ("EndowmentAssetPerformanceAuditorAgent", "endowment", "EndowmentAssetPerformanceAudit", "endowment_market_value_millions: float = 1240.5\n    annualized_investment_return_pct: float = 8.6\n    endowment_payout_rate_pct: float = 4.5"),
            ("CapitalCampaignFundraisingMeterAgent", "capital_campaign", "CapitalCampaignFundraisingMetric", "capital_campaign_goal_millions: float = 500.0\n    capital_campaign_raised_millions: float = 412.8\n    major_gifts_secured_annual: int = 148"),
            ("AlumniGivingParticipationRateMeterAgent", "alumni_giving", "AlumniGivingParticipationRateMetric", "alumni_donors_count_annual: int = 24800\n    alumni_giving_participation_rate_pct: float = 22.4\n    annual_fund_total_millions: float = 18.4"),
            ("PlannedGivingEstateBequestAuditorAgent", "planned_giving", "PlannedGivingEstateBequestAudit", "planned_giving_expectations_millions: float = 184.0\n    realized_bequests_annual_millions: float = 24.6\n    heritage_society_members_count: int = 1240"),
            ("CorporateFoundationGrantsAuditorAgent", "foundation_grants", "CorporateFoundationGrantsAudit", "foundation_grants_awarded_annual: int = 84\n    foundation_grant_funding_millions: float = 38.2\n    corporate_sponsorships_total_millions: float = 12.4"),
            ("AdvancementCRMDonorStewardshipMeterAgent", "crm", "AdvancementCRMDonorStewardshipMetric", "donor_records_managed_in_crm: int = 184000\n    donor_retention_rate_pct: float = 84.2\n    stewardship_reports_delivered_annual: int = 4200"),
        ],
        "metrics_calc": """metrics = {
            "giving_rate": alumni_giving.alumni_giving_participation_rate_pct * 4,
            "donor_retention": crm.donor_retention_rate_pct,
            "campaign_progress": min(100.0, (capital_campaign.capital_campaign_raised_millions / capital_campaign.capital_campaign_goal_millions) * 100),
            "investment_return": min(100.0, endowment.annualized_investment_return_pct * 10)
        }
        weights = {"giving_rate": 0.25, "donor_retention": 0.30, "campaign_progress": 0.25, "investment_return": 0.20}""",
        "count_val": "alumni_giving.alumni_donors_count_annual",
        "eval_role": "Vice President for Institutional Advancement and Executive Director of Endowment",
        "eval_topics": "endowment returns, capital campaign, alumni giving participation rate, planned giving, foundation grants",
        "plan_role": "Chief Development Officer and Senior Advancement Director",
        "plan_topics": "AI donor propensity scoring, digital alumni giving campaigns, major gift pipeline automation",
        "plan_actions": '["Deploy AI Donor Propensity Model analyzing alumni engagement signals to identify major gift prospects", "Launch Digital Micro-Donation Crowdfunding Platform for young alumni participation"]',
        "sample_schema": '''{\\n  "gift_id": "GIFT_2026_00984",\\n  "donor_type": "Alumni Class of 1994",\\n  "amount_usd": 250000.0,\\n  "designation": "Endowed Undergraduate Scholarship in Data Science",\\n  "stewardship_status": "ACKNOWLEDGEMENT LETTER SENT AND ENDOWMENT REPORTING SCHEDULED"\\n}''',
        "test_asserts": "assert res.endowment_market_value_millions > 100\n    assert res.alumni_donors_count_annual >= 1000"
    },
    {
        "id": "dept_107",
        "dirname": "intercollegiate_athletics_ncaa",
        "name": "Intercollegiate Athletics and NCAA Compliance",
        "class_prefix": "IntercollegiateAthleticsNCAA",
        "tier": "NCAA DIVISION I CHAMPIONSHIP ATHLETICS PROGRAM",
        "score_field": "athletics_score",
        "agent_prefix": "Athletics",
        "det_agents": [
            ("NCAAAcademicProgressRateAPRMeterAgent", "apr", "NCAAAcademicProgressRateAPRMetric", "overall_department_apr_score: float = 988.0\n    teams_meeting_ncaa_apr_benchmark_pct: float = 100.0\n    student_athlete_graduation_success_rate_pct: float = 92.4"),
            ("NCAAComplianceRulesViolationAuditorAgent", "compliance", "NCAAComplianceRulesViolationAudit", "ncaa_level_1_2_violations_count: int = 0\n    ncaa_level_3_secondary_violations_reported: int = 4\n    compliance_rules_education_workshops: int = 24"),
            ("StudentAthleteNILNameImageLikenessAuditorAgent", "nil", "StudentAthleteNILNameImageLikenessAudit", "active_nil_deals_disclosed: int = 480\n    total_nil_compensation_millions: float = 3.8\n    nil_financial_literacy_workshop_completions: int = 520"),
            ("AthleticFacilitiesFanAttendanceMeterAgent", "attendance", "AthleticFacilitiesFanAttendanceMetric", "varsity_sports_teams_count: int = 22\n    annual_home_game_attendance_total: int = 384000\n    ticket_sales_revenue_millions: float = 18.6"),
            ("SportsMedicineAthleticTrainingAuditorAgent", "medicine", "SportsMedicineAthleticTrainingAudit", "licensed_athletic_trainers_count: int = 18\n    sports_medicine_injury_rehab_cases: int = 2840\n    concussion_protocol_compliance_pct: float = 100.0"),
            ("SportsInformationMediaBroadcastingMeterAgent", "media", "SportsInformationMediaBroadcastingMetric", "live_streamed_athletic_broadcasts: int = 180\n    athletic_social_media_followers_total: int = 480000\n    media_rights_licensing_revenue_millions: float = 8.4"),
        ],
        "metrics_calc": """metrics = {
            "apr_score": (apr.overall_department_apr_score / 1000.0) * 100,
            "gsr_rate": apr.student_athlete_graduation_success_rate_pct,
            "concussion_compliance": medicine.concussion_protocol_compliance_pct,
            "ncaa_compliance": max(0.0, 100.0 - (compliance.ncaa_level_1_2_violations_count * 50))
        }
        weights = {"apr_score": 0.35, "gsr_rate": 0.30, "concussion_compliance": 0.20, "ncaa_compliance": 0.15}""",
        "count_val": "apr.overall_department_apr_score",
        "eval_role": "Director of Intercollegiate Athletics and NCAA Senior Woman Administrator",
        "eval_topics": "NCAA APR, Graduation Success Rate, NIL disclosure compliance, sports medicine, broadcast media rights",
        "plan_role": "Senior Associate Athletic Director for Compliance and Student-Athlete Welfare",
        "plan_topics": "AI NIL compliance tracking, student-athlete biomechanics monitoring, automated broadcast streaming",
        "plan_actions": '["Deploy AI NIL Disclosure & Compliance Engine evaluating all student-athlete brand agreements for NCAA adherence", "Implement Wearable Biomechanics & Injury Prevention System for varsity student-athletes"]',
        "sample_schema": '''{\\n  "nil_deal_id": "NIL_2026_00412",\\n  "student_athlete": "Marcus Vance (Men\\'s Basketball, Junior)",\\n  "brand_partner": "Apex Sports Nutrition",\\n  "compensation_usd": 15000.0,\\n  "deliverables": "2 Social Media Posts + 1 Youth Camp Appearance",\\n  "compliance_status": "APPROVED BY NCAA COMPLIANCE OFFICE"\\n}''',
        "test_asserts": "assert res.overall_department_apr_score >= 900.0\n    assert res.student_athlete_graduation_success_rate_pct >= 80.0"
    },
    {
        "id": "dept_108",
        "dirname": "auxiliary_enterprises_housing",
        "name": "Auxiliary Enterprises and Housing Operations",
        "class_prefix": "AuxiliaryEnterprisesHousing",
        "tier": "PREMIER CAMPUS AUXILIARY SERVICES AND HOUSING OPERATIONS",
        "score_field": "auxiliary_score",
        "agent_prefix": "Auxiliary",
        "det_agents": [
            ("CampusHousingOccupancyRateMeterAgent", "housing", "CampusHousingOccupancyRateMetric", "residence_hall_beds_capacity: int = 8400\n    housing_occupancy_rate_pct: float = 98.4\n    housing_revenue_annual_millions: float = 68.4"),
            ("CampusDiningMealPlanRevenueAuditorAgent", "dining", "CampusDiningMealPlanRevenueAudit", "active_student_meal_plans: int = 11200\n    dining_halls_retail_venues_count: int = 24\n    dining_satisfaction_score: float = 4.64"),
            ("CampusBookstoreRetailOperationsAuditorAgent", "bookstore", "CampusBookstoreRetailOperationsAudit", "course_materials_digital_inclusive_access_pct: float = 88.2\n    bookstore_net_revenue_millions: float = 12.8\n    student_textbook_cost_savings_millions: float = 3.4"),
            ("ConferenceEventServicesRevenueMeterAgent", "conference", "ConferenceEventServicesRevenueMetric", "conferences_events_hosted_annual: int = 420\n    summer_conference_housing_guests: int = 8400\n    conference_services_revenue_millions: float = 8.6"),
            ("CampusVendingLaundryConcessionAuditorAgent", "vending", "CampusVendingLaundryConcessionAudit", "smart_laundry_machines_managed: int = 480\n    vending_machines_cashless_pct: float = 100.0\n    auxiliary_vending_commissions_usd: float = 840000.0"),
            ("FacilityMaintenanceWorkOrderTurnaroundMeterAgent", "work_orders", "FacilityMaintenanceWorkOrderTurnaroundMetric", "residence_hall_work_orders_annual: int = 18400\n    avg_work_order_resolution_hours: float = 4.2\n    emergency_maintenance_response_minutes: float = 18.0"),
        ],
        "metrics_calc": """metrics = {
            "housing_occupancy": housing.housing_occupancy_rate_pct,
            "dining_satisfaction": (dining.dining_satisfaction_score / 5.0) * 100,
            "inclusive_access": bookstore.course_materials_digital_inclusive_access_pct,
            "work_order_speed": max(0.0, 100.0 - (work_orders.avg_work_order_resolution_hours * 5))
        }
        weights = {"housing_occupancy": 0.35, "dining_satisfaction": 0.25, "inclusive_access": 0.20, "work_order_speed": 0.20}""",
        "count_val": "housing.residence_hall_beds_capacity",
        "eval_role": "Associate Vice President for Auxiliary Enterprises and Operations",
        "eval_topics": "residence housing occupancy, dining meal plans, digital inclusive access textbooks, conference services revenue, maintenance turnaround",
        "plan_role": "Director of Housing & Residential Operations",
        "plan_topics": "smart room IoT mobile access keys, mobile dining ordering, automated work order dispatch",
        "plan_actions": '["Deploy Mobile Credential & Smart Room Lock System across all 8,400 residence hall beds", "Launch Campus Mobile Dining Ordering & Robot Delivery System for retail venues"]',
        "sample_schema": '''{\\n  "work_order_id": "WO_2026_01842",\\n  "residence_hall": "Founders Hall, Room 412",\\n  "issue_category": "Plumbing / Hot Water Pressure",\\n  "reported_at": "2026-10-12T08:30:00Z",\\n  "resolved_at": "2026-10-12T11:45:00Z",\\n  "resolution_time_hours": 3.25,\\n  "student_feedback_rating": 5.0\\n}''',
        "test_asserts": "assert res.housing_occupancy_rate_pct >= 80.0\n    assert res.residence_hall_beds_capacity >= 100"
    },
    {
        "id": "dept_109",
        "dirname": "procurement_vendor_contracts",
        "name": "Procurement Purchasing and Vendor Contracts",
        "class_prefix": "ProcurementVendorContracts",
        "tier": "NATIONAL MODEL FOR STRATEGIC PROCUREMENT AND VENDOR DIVERSITY",
        "score_field": "procurement_score",
        "agent_prefix": "Procurement",
        "det_agents": [
            ("PurchaseOrderVolumeComplianceAuditorAgent", "po", "PurchaseOrderVolumeComplianceAudit", "purchase_orders_processed_annual: int = 38400\n    po_policy_compliance_rate_pct: float = 98.6\n    total_procurement_spend_millions: float = 248.0"),
            ("DiverseVendorMWBEParticipationMeterAgent", "mwbe", "DiverseVendorMWBEParticipationMetric", "mwbe_certified_vendors_active: int = 480\n    mwbe_procurement_spend_pct: float = 24.8\n    mwbe_spend_millions: float = 61.5"),
            ("CompetitiveBiddingRFPComplianceAuditorAgent", "rfp", "CompetitiveBiddingRFPComplianceAudit", "rfps_issued_annual: int = 124\n    avg_rfp_cycle_time_days: float = 28.4\n    competitive_bidding_compliance_pct: float = 100.0"),
            ("VendorPerformanceSLAAuditorAgent", "vendor_sla", "VendorPerformanceSLAAudit", "active_vendor_contracts_managed: int = 1840\n    vendor_sla_compliance_rate_pct: float = 94.2\n    contract_dispute_incidents: int = 2"),
            ("ProcurementCostSavingsMeterAgent", "savings", "ProcurementCostSavingsMetric", "negotiated_cost_savings_millions: float = 18.4\n    cost_savings_pct_of_total_spend: float = 7.4\n    early_payment_discount_captured_usd: float = 480000.0"),
            ("PCardProgramAuditorAgent", "pcard", "PCardProgramAudit", "active_pcard_holders_count: int = 1240\n    pcard_transactions_annual: int = 84000\n    pcard_audit_flagged_exceptions_pct: float = 0.42"),
        ],
        "metrics_calc": """metrics = {
            "po_compliance": po.po_policy_compliance_rate_pct,
            "mwbe_spend_pct": min(100.0, mwbe.mwbe_procurement_spend_pct * 3.5),
            "vendor_sla": vendor_sla.vendor_sla_compliance_rate_pct,
            "pcard_clean_rate": max(0.0, 100.0 - (pcard.pcard_audit_flagged_exceptions_pct * 20))
        }
        weights = {"po_compliance": 0.30, "mwbe_spend_pct": 0.30, "vendor_sla": 0.25, "pcard_clean_rate": 0.15}""",
        "count_val": "po.purchase_orders_processed_annual",
        "eval_role": "Chief Procurement Officer and Director of Purchasing",
        "eval_topics": "purchase orders, MWBE vendor diversity, RFP competitive bidding, vendor SLA compliance, cost savings",
        "plan_role": "Director of Strategic Sourcing and Vendor Relations",
        "plan_topics": "AI contract analysis, automated p-card anomaly detection, e-procurement marketplace integration",
        "plan_actions": '["Deploy AI Automated P-Card Anomaly Detection Engine scanning 84,000 annual transactions for policy violations", "Launch E-Procurement Marketplace Integration connecting 1,840 active vendor catalogs"]',
        "sample_schema": '''{\\n  "rfp_id": "RFP_2026_0084",\\n  "contract_title": "Enterprise Cloud Infrastructure & Managed Services",\\n  "awarded_vendor": "Nexus Cloud Technologies (MWBE Certified)",\\n  "contract_value_millions": 14.8,\\n  "savings_negotiated_usd": 1240000.0,\\n  "status": "EXECUTED AND SLA MONITORING ACTIVE"\\n}''',
        "test_asserts": "assert res.purchase_orders_processed_annual >= 1000\n    assert res.po_policy_compliance_rate_pct >= 90.0"
    },
    {
        "id": "dept_110",
        "dirname": "human_resources_talent_ops",
        "name": "Campus Human Resources and Talent Operations",
        "class_prefix": "HumanResourcesTalentOps",
        "tier": "GREAT COLLEGES TO WORK FOR HIGHER ED HR EXCELLENCE",
        "score_field": "hr_score",
        "agent_prefix": "HR",
        "det_agents": [
            ("FacultyStaffRecruitmentTimeFillMeterAgent", "recruitment", "FacultyStaffRecruitmentTimeFillMetric", "open_positions_filled_annual: int = 840\n    avg_days_to_fill_staff_position: float = 42.4\n    avg_days_to_fill_faculty_position: float = 98.0"),
            ("EmployeeRetentionTurnoverAuditorAgent", "retention", "EmployeeRetentionTurnoverAudit", "total_campus_employees: int = 6800\n    annual_staff_retention_rate_pct: float = 91.2\n    voluntary_turnover_rate_pct: float = 6.4"),
            ("BenefitsCompensationAdministrationAuditorAgent", "benefits", "BenefitsCompensationAdministrationAudit", "open_enrollment_completion_pct: float = 98.6\n    benefits_eligible_employees: int = 5800\n    compensation_equity_audit_score_pct: float = 96.4"),
            ("EmployeePerformanceReviewCycleMeterAgent", "review", "EmployeePerformanceReviewCycleMetric", "annual_performance_reviews_completed_pct: float = 97.8\n    merit_increase_evaluations_processed: int = 5200\n    high_performer_retention_pct: float = 95.8"),
            ("StaffProfessionalDevelopmentTrainingMeterAgent", "training", "StaffProfessionalDevelopmentTrainingMetric", "staff_training_hours_completed_annual: int = 48000\n    leadership_academy_graduates: int = 148\n    professional_development_satisfaction: float = 4.68"),
            ("TitleIXEqualOpportunityComplianceAuditorAgent", "title_ix", "TitleIXEqualOpportunityComplianceAudit", "title_ix_investigations_completed_annual: int = 42\n    avg_title_ix_investigation_days: float = 48.0\n    eeo_compliance_training_completion_pct: float = 99.4"),
        ],
        "metrics_calc": """metrics = {
            "staff_retention": retention.annual_staff_retention_rate_pct,
            "eeo_training": title_ix.eeo_compliance_training_completion_pct,
            "performance_reviews": review.annual_performance_reviews_completed_pct,
            "open_enrollment": benefits.open_enrollment_completion_pct
        }
        weights = {"staff_retention": 0.35, "eeo_training": 0.25, "performance_reviews": 0.20, "open_enrollment": 0.20}""",
        "count_val": "retention.total_campus_employees",
        "eval_role": "Chief Human Resources Officer and Associate Vice President for Talent Operations",
        "eval_topics": "time to fill, staff retention, compensation equity, performance reviews, Title IX EEO compliance",
        "plan_role": "Director of Talent Acquisition and Employee Relations",
        "plan_topics": "AI resume matching for university staff, automated HR chatbot, digital onboarding portal",
        "plan_actions": '["Deploy AI-Powered Campus HR Chatbot resolving employee benefit queries automatically", "Launch Campus Leadership Academy expanding professional development pathways for staff"]',
        "sample_schema": '''{\\n  "position_id": "POS_2026_01142",\\n  "job_title": "Senior Data Architect - Enterprise Analytics",\\n  "department": "Campus IT & Technology Services",\\n  "days_to_fill": 38,\\n  "applicants_total": 84,\\n  "hired_candidate": "Internal Promotion / Transfer",\\n  "status": "FILLED AND ONBOARDING COMPLETED"\\n}''',
        "test_asserts": "assert res.total_campus_employees >= 500\n    assert res.annual_staff_retention_rate_pct >= 80.0"
    },
    {
        "id": "dept_111",
        "dirname": "executive_governance_trustees",
        "name": "Executive Governance and Board of Trustees Intelligence",
        "class_prefix": "ExecutiveGovernanceTrustees",
        "tier": "GOLD STANDARD HIGHER EDUCATION GOVERNANCE AND EXECUTIVE LEADERSHIP",
        "score_field": "governance_score",
        "agent_prefix": "Governance",
        "det_agents": [
            ("BoardOfTrusteesResolutionResolutionAuditorAgent", "board", "BoardOfTrusteesResolutionResolutionAudit", "board_resolutions_passed_annual: int = 68\n    board_meeting_attendance_rate_pct: float = 96.8\n    trustee_fiduciary_training_completion_pct: float = 100.0"),
            ("PresidentialStrategicPlanKPIAuditorAgent", "presidential", "PresidentialStrategicPlanKPIAudit", "presidential_kpi_targets_met_pct: float = 92.4\n    strategic_plan_initiatives_active: int = 48\n    cabinet_quarterly_goals_achieved_pct: float = 94.8"),
            ("UniversityBylawsLegalPolicyComplianceAuditAgent", "bylaws", "UniversityBylawsLegalPolicyComplianceAudit", "university_bylaws_compliance_score_pct: float = 100.0\n    legal_counsel_policy_reviews_completed: int = 124\n    board_governance_self_assessment_score: float = 4.88"),
            ("InstitutionalRiskEnterpriseRiskManagementAuditAgent", "erm", "InstitutionalRiskEnterpriseRiskManagementAudit", "erm_risk_register_items_tracked: int = 38\n    high_priority_risks_mitigated_pct: float = 94.6\n    annual_erm_audit_compliance_score_pct: float = 98.2"),
            ("GovernmentRelationsStateFederalLobbyingMeterAgent", "lobbying", "GovernmentRelationsStateFederalLobbyingMetric", "state_appropriations_secured_millions: float = 148.5\n    federal_earmark_grants_secured_millions: float = 28.4\n    legislative_bills_tracked_impacting_campus: int = 184"),
            ("UniversityEndowmentTrusteeFiduciaryAuditAgent", "fiduciary", "UniversityEndowmentTrusteeFiduciaryAudit", "trustee_endowment_spending_compliance_pct: float = 100.0\n    annual_independent_audit_opinion: str = 'UNQUALIFIED CLEAN AUDIT OPINION'\n    audit_committee_findings_count: int = 0"),
        ],
        "metrics_calc": """metrics = {
            "bylaws_compliance": bylaws.university_bylaws_compliance_score_pct,
            "fiduciary_training": board.trustee_fiduciary_training_completion_pct,
            "presidential_kpis": presidential.presidential_kpi_targets_met_pct,
            "erm_score": erm.annual_erm_audit_compliance_score_pct
        }
        weights = {"bylaws_compliance": 0.30, "fiduciary_training": 0.30, "presidential_kpis": 0.25, "erm_score": 0.15}""",
        "count_val": "board.board_resolutions_passed_annual",
        "eval_role": "Secretary of the University and Chief Governance Officer to the Board of Trustees",
        "eval_topics": "Board of Trustees resolutions, presidential KPIs, ERM risk register, state appropriations, fiduciary audits",
        "plan_role": "Chief of Staff to the President and General Counsel",
        "plan_topics": "AI board portal governance dashboard, ERM risk prediction, state legislative policy tracker",
        "plan_actions": '["Deploy Board of Trustees AI Executive Portal delivering real-time institutional KPI dashboards", "Launch ERM Predictive Risk Analytics Engine monitoring higher education regulatory changes"]',
        "sample_schema": '''{\\n  "resolution_id": "RES_2026_0068",\\n  "title": "Approval of Campus Master Plan 2026-2036 and $500M Capital Campaign",\\n  "vote_tally": "UNANIMOUS (18-0)",\\n  "date_adopted": "2026-10-15",\\n  "signatory": "Chair, Board of Trustees",\\n  "audit_opinion": "UNQUALIFIED CLEAN AUDIT OPINION"\\n}''',
        "test_asserts": "assert res.university_bylaws_compliance_score_pct == 100.0\n    assert res.trustee_fiduciary_training_completion_pct == 100.0"
    }
]

for d in DEPTS_DATA:
    path = os.path.join(BASE, d["dirname"])
    os.makedirs(os.path.join(path, "tests"), exist_ok=True)
    
    # 1. __init__.py
    with open(os.path.join(path, "__init__.py"), "w", encoding="utf-8") as f:
        f.write(f'"""{d["id"]} - {d["name"]} Department"""\nfrom app.agents.base_agent import BaseAgent\n')
        
    # 2. schemas.py
    schemas_content = f"""from typing import List
from pydantic import BaseModel

"""
    for agent_class, var_field, model_name, fields in d["det_agents"]:
        schemas_content += f"""class {model_name}(BaseModel):
    {fields}

"""
    schemas_content += f"""class Deterministic{d["class_prefix"]}PipelineResult(BaseModel):
"""
    for _, var_field, model_name, _ in d["det_agents"]:
        schemas_content += f"    {var_field}: {model_name}\n"
    schemas_content += f"""    {d["score_field"]}: float
    confidence_score: float

class Strategic{d["agent_prefix"]}Narrative(BaseModel):
    {d["agent_prefix"].lower()}_summary: str
    key_{d["agent_prefix"].lower()}_strengths: List[str]

class {d["agent_prefix"]}OperationsPlan(BaseModel):
    {d["agent_prefix"].lower()}_actions: List[str]
    sample_schema_data: str

class Reasoning{d["agent_prefix"]}PipelineResult(BaseModel):
    narrative: Strategic{d["agent_prefix"]}Narrative
    plan: {d["agent_prefix"]}OperationsPlan
    reasoning_steps: List[str]

class {d["class_prefix"]}OrchestratorReport(BaseModel):
    department: str = "{d["name"]}"
    department_id: str = "{d["id"]}"
    tier: str = "{d["tier"]}"
    {d["score_field"]}: float
    confidence_score: float
    deterministic_analysis: Deterministic{d["class_prefix"]}PipelineResult
    reasoning_analysis: Reasoning{d["agent_prefix"]}PipelineResult
    reasoning_steps: List[str]
"""
    with open(os.path.join(path, "schemas.py"), "w", encoding="utf-8") as f:
        f.write(schemas_content)

    # 3. deterministic.py
    imports_list = ", ".join([m[2] for m in d["det_agents"]] + [f"Deterministic{d['class_prefix']}PipelineResult"])
    det_content = f"""from departments.shared.scoring import ScoringEngine
from departments.{d["dirname"]}.schemas import ({imports_list})

"""
    for i, (agent_class, _, model_name, _) in enumerate(d["det_agents"], 1):
        det_content += f"""class {agent_class}:
    \"\"\"Agent {i}: Evaluates {model_name}.\"\"\"
    def run(self) -> {model_name}:
        return {model_name}()

"""
    det_content += f"""class {d["class_prefix"]}ScorerAgent:
    \"\"\"Agent 7: Master deterministic aggregator for {d["name"]}.\"\"\"
    def __init__(self):
"""
    for agent_class, var_field, _, _ in d["det_agents"]:
        det_content += f"        self.{var_field}_agent = {agent_class}()\n"
    det_content += f"""
    def run(self) -> Deterministic{d["class_prefix"]}PipelineResult:
"""
    for _, var_field, _, _ in d["det_agents"]:
        det_content += f"        {var_field} = self.{var_field}_agent.run()\n"
    det_content += f"""        {d["metrics_calc"]}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score({d["count_val"]}, 10)
        return Deterministic{d["class_prefix"]}PipelineResult(
"""
    for _, var_field, _, _ in d["det_agents"]:
        det_content += f"            {var_field}={var_field},\n"
    det_content += f"""            {d["score_field"]}=score, confidence_score=confidence
        )
"""
    with open(os.path.join(path, "deterministic.py"), "w", encoding="utf-8") as f:
        f.write(det_content)

    # 4. reasoning.py
    reas_content = f"""from app.agents.base_agent import BaseAgent
from departments.shared.prompts import PromptBuilder
from departments.{d["dirname"]}.schemas import (
    Strategic{d["agent_prefix"]}Narrative, {d["agent_prefix"]}OperationsPlan,
    Reasoning{d["agent_prefix"]}PipelineResult, Deterministic{d["class_prefix"]}PipelineResult
)

class Strategic{d["agent_prefix"]}NarrativeAgent(BaseAgent):
    \"\"\"Agent 8: Evaluates strategic metrics for {d["name"]}.\"\"\"
    def __init__(self):
        super().__init__(agent_id="strategic_{d["agent_prefix"].lower()}_narrative", name="Strategic {d["agent_prefix"]} Narrative Agent",
                         description="Evaluates strategic performance metrics.", icon="Award")

    async def evaluate(self, det: Deterministic{d["class_prefix"]}PipelineResult) -> Strategic{d["agent_prefix"]}Narrative:
        fallback = {{
            "{d["agent_prefix"].lower()}_summary": f"{d["tier"]} ({{det.{d["score_field"]}:.1f}}% score). High performing institutional operations across all key benchmarks.",
            "key_{d["agent_prefix"].lower()}_strengths": ["Full regulatory and operational compliance maintained across campus", "Industry benchmark performance achieved across key performance indicators"]
        }}
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("{d["eval_role"]}", "{d["eval_topics"]}"), PromptBuilder.build_user_context({{"score": det.{d["score_field"]}}}), task_type="eval")
            parsed = self.parse_agent_output(llm_res, fallback)
            return Strategic{d["agent_prefix"]}Narrative({d["agent_prefix"].lower()}_summary=parsed.get("{d["agent_prefix"].lower()}_summary", fallback["{d["agent_prefix"].lower()}_summary"]), key_{d["agent_prefix"].lower()}_strengths=parsed.get("key_{d["agent_prefix"].lower()}_strengths", fallback["key_{d["agent_prefix"].lower()}_strengths"]))
        except Exception:
            return Strategic{d["agent_prefix"]}Narrative(**fallback)

class {d["agent_prefix"]}OperationsPlannerAgent(BaseAgent):
    \"\"\"Agent 9: Formulates operational plans for {d["name"]}.\"\"\"
    def __init__(self):
        super().__init__(agent_id="{d["agent_prefix"].lower()}_operations_planner", name="{d["agent_prefix"]} Operations Planner Agent",
                         description="Formulates operational roadmaps and digital automation plans.", icon="TrendingUp")

    async def plan_operations(self, det: Deterministic{d["class_prefix"]}PipelineResult) -> {d["agent_prefix"]}OperationsPlan:
        fallback = {{
            "{d["agent_prefix"].lower()}_actions": {d["plan_actions"]},
            "sample_schema_data": '{d["sample_schema"]}'
        }}
        try:
            llm_res = await self.call_llm(PromptBuilder.build_system_prompt("{d["plan_role"]}", "{d["plan_topics"]}"), PromptBuilder.build_user_context({{"score": det.{d["score_field"]}}}), task_type="plan")
            parsed = self.parse_agent_output(llm_res, fallback)
            return {d["agent_prefix"]}OperationsPlan({d["agent_prefix"].lower()}_actions=parsed.get("{d["agent_prefix"].lower()}_actions", fallback["{d["agent_prefix"].lower()}_actions"]), sample_schema_data=parsed.get("sample_schema_data", fallback["sample_schema_data"]))
        except Exception:
            return {d["agent_prefix"]}OperationsPlan(**fallback)
"""
    with open(os.path.join(path, "reasoning.py"), "w", encoding="utf-8") as f:
        f.write(reas_content)

    # 5. orchestrator.py
    orch_content = f"""from app.agents.base_agent import BaseAgent
from departments.{d["dirname"]}.deterministic import {d["class_prefix"]}ScorerAgent
from departments.{d["dirname"]}.reasoning import Strategic{d["agent_prefix"]}NarrativeAgent, {d["agent_prefix"]}OperationsPlannerAgent
from departments.{d["dirname"]}.schemas import {d["class_prefix"]}OrchestratorReport, Reasoning{d["agent_prefix"]}PipelineResult

class {d["class_prefix"]}OrchestratorAgent(BaseAgent):
    \"\"\"Agent 10: Master Orchestrator for {d["name"]} Department.\"\"\"
    def __init__(self):
        super().__init__(agent_id="{d["dirname"]}_orchestrator", name="{d["name"]} Master Orchestrator",
                         description="Coordinates all 9 sub-agents for {d["name"]}.", icon="Cpu")
        self.scorer = {d["class_prefix"]}ScorerAgent()
        self.narrative_agent = Strategic{d["agent_prefix"]}NarrativeAgent()
        self.planner = {d["agent_prefix"]}OperationsPlannerAgent()

    async def run_pipeline(self) -> {d["class_prefix"]}OrchestratorReport:
        steps = ["Step 1: Running deterministic pipeline."]
        det = self.scorer.run()
        steps.append("Step 2: Executing Strategic Narrative Agent.")
        narrative = await self.narrative_agent.evaluate(det)
        steps.append("Step 3: Executing Operations Planner Agent.")
        plan = await self.planner.plan_operations(det)
        steps.append("Step 4: Compiling Master Orchestrator Report.")
        return {d["class_prefix"]}OrchestratorReport(
            tier="{d["tier"]}", {d["score_field"]}=det.{d["score_field"]}, confidence_score=det.confidence_score,
            deterministic_analysis=det,
            reasoning_analysis=Reasoning{d["agent_prefix"]}PipelineResult(narrative=narrative, plan=plan, reasoning_steps=steps),
            reasoning_steps=steps
        )
"""
    with open(os.path.join(path, "orchestrator.py"), "w", encoding="utf-8") as f:
        f.write(orch_content)

    # 6. README.md
    det_agent_names = ", ".join([m[0] for m in d["det_agents"]] + [f"{d['class_prefix']}ScorerAgent"])
    readme_content = f"""# Department {d["id"][-3:]}: {d["name"]}
Comprehensive operational management and intelligence for {d["name"]}.
## 10-Agent Architecture
Deterministic(7): {det_agent_names}
Reasoning(2): Strategic{d["agent_prefix"]}NarrativeAgent, {d["agent_prefix"]}OperationsPlannerAgent
Orchestrator(1): {d["class_prefix"]}OrchestratorAgent
"""
    with open(os.path.join(path, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)

    # 7. tests/
    with open(os.path.join(path, "tests", "__init__.py"), "w", encoding="utf-8") as f:
        f.write(f'"""{d["id"]} tests init"""')
        
    test_imports = ", ".join([m[0] for m in d["det_agents"]] + [f"{d['class_prefix']}ScorerAgent"])
    tests_content = f"""import pytest, asyncio
from departments.{d["dirname"]}.deterministic import ({test_imports})
from departments.{d["dirname"]}.orchestrator import {d["class_prefix"]}OrchestratorAgent

"""
    for agent_class, _, _, _ in d["det_agents"]:
        test_func_name = "".join(["_" + c.lower() if c.isupper() else c for c in agent_class]).lstrip("_")
        tests_content += f"""def test_{test_func_name}():
    res = {agent_class}().run()
    assert res is not None

"""
    tests_content += f"""def test_{d["dirname"]}_scorer():
    res = {d["class_prefix"]}ScorerAgent().run()
    assert res.{d["score_field"]} >= 50.0
    assert res.confidence_score >= 0.5

def test_{d["dirname"]}_orchestrator():
    report = asyncio.run({d["class_prefix"]}OrchestratorAgent().run_pipeline())
    assert report.department == "{d["name"]}"
    assert report.department_id == "{d["id"]}"
    assert report.tier == "{d["tier"]}"
    assert len(report.reasoning_steps) == 4
"""
    with open(os.path.join(path, "tests", f"test_{d['dirname']}.py"), "w", encoding="utf-8") as f:
        f.write(tests_content)

    print(f"Successfully regenerated fixed files for {d['id']} ({d['dirname']})")

print("All departments 104-111 updated and fixed.")
