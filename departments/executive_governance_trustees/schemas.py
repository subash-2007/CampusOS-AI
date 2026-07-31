from typing import List
from pydantic import BaseModel

class BoardOfTrusteesResolutionResolutionAudit(BaseModel):
    board_resolutions_passed_annual: int = 68
    board_meeting_attendance_rate_pct: float = 96.8
    trustee_fiduciary_training_completion_pct: float = 100.0

class PresidentialStrategicPlanKPIAudit(BaseModel):
    presidential_kpi_targets_met_pct: float = 92.4
    strategic_plan_initiatives_active: int = 48
    cabinet_quarterly_goals_achieved_pct: float = 94.8

class UniversityBylawsLegalPolicyComplianceAudit(BaseModel):
    university_bylaws_compliance_score_pct: float = 100.0
    legal_counsel_policy_reviews_completed: int = 124
    board_governance_self_assessment_score: float = 4.88

class InstitutionalRiskEnterpriseRiskManagementAudit(BaseModel):
    erm_risk_register_items_tracked: int = 38
    high_priority_risks_mitigated_pct: float = 94.6
    annual_erm_audit_compliance_score_pct: float = 98.2

class GovernmentRelationsStateFederalLobbyingMetric(BaseModel):
    state_appropriations_secured_millions: float = 148.5
    federal_earmark_grants_secured_millions: float = 28.4
    legislative_bills_tracked_impacting_campus: int = 184

class UniversityEndowmentTrusteeFiduciaryAudit(BaseModel):
    trustee_endowment_spending_compliance_pct: float = 100.0
    annual_independent_audit_opinion: str = 'UNQUALIFIED CLEAN AUDIT OPINION'
    audit_committee_findings_count: int = 0

class DeterministicExecutiveGovernanceTrusteesPipelineResult(BaseModel):
    board: BoardOfTrusteesResolutionResolutionAudit
    presidential: PresidentialStrategicPlanKPIAudit
    bylaws: UniversityBylawsLegalPolicyComplianceAudit
    erm: InstitutionalRiskEnterpriseRiskManagementAudit
    lobbying: GovernmentRelationsStateFederalLobbyingMetric
    fiduciary: UniversityEndowmentTrusteeFiduciaryAudit
    governance_score: float
    confidence_score: float

class StrategicGovernanceNarrative(BaseModel):
    governance_summary: str
    key_governance_strengths: List[str]

class GovernanceOperationsPlan(BaseModel):
    governance_actions: List[str]
    sample_schema_data: str

class ReasoningGovernancePipelineResult(BaseModel):
    narrative: StrategicGovernanceNarrative
    plan: GovernanceOperationsPlan
    reasoning_steps: List[str]

class ExecutiveGovernanceTrusteesOrchestratorReport(BaseModel):
    department: str = "Executive Governance and Board of Trustees Intelligence"
    department_id: str = "dept_111"
    tier: str = "GOLD STANDARD HIGHER EDUCATION GOVERNANCE AND EXECUTIVE LEADERSHIP"
    governance_score: float
    confidence_score: float
    deterministic_analysis: DeterministicExecutiveGovernanceTrusteesPipelineResult
    reasoning_analysis: ReasoningGovernancePipelineResult
    reasoning_steps: List[str]
