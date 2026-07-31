from departments.shared.scoring import ScoringEngine
from departments.executive_governance_trustees.schemas import (BoardOfTrusteesResolutionResolutionAudit, PresidentialStrategicPlanKPIAudit, UniversityBylawsLegalPolicyComplianceAudit, InstitutionalRiskEnterpriseRiskManagementAudit, GovernmentRelationsStateFederalLobbyingMetric, UniversityEndowmentTrusteeFiduciaryAudit, DeterministicExecutiveGovernanceTrusteesPipelineResult)

class BoardOfTrusteesResolutionResolutionAuditorAgent:
    """Agent 1: Evaluates BoardOfTrusteesResolutionResolutionAudit."""
    def run(self) -> BoardOfTrusteesResolutionResolutionAudit:
        return BoardOfTrusteesResolutionResolutionAudit()

class PresidentialStrategicPlanKPIAuditorAgent:
    """Agent 2: Evaluates PresidentialStrategicPlanKPIAudit."""
    def run(self) -> PresidentialStrategicPlanKPIAudit:
        return PresidentialStrategicPlanKPIAudit()

class UniversityBylawsLegalPolicyComplianceAuditAgent:
    """Agent 3: Evaluates UniversityBylawsLegalPolicyComplianceAudit."""
    def run(self) -> UniversityBylawsLegalPolicyComplianceAudit:
        return UniversityBylawsLegalPolicyComplianceAudit()

class InstitutionalRiskEnterpriseRiskManagementAuditAgent:
    """Agent 4: Evaluates InstitutionalRiskEnterpriseRiskManagementAudit."""
    def run(self) -> InstitutionalRiskEnterpriseRiskManagementAudit:
        return InstitutionalRiskEnterpriseRiskManagementAudit()

class GovernmentRelationsStateFederalLobbyingMeterAgent:
    """Agent 5: Evaluates GovernmentRelationsStateFederalLobbyingMetric."""
    def run(self) -> GovernmentRelationsStateFederalLobbyingMetric:
        return GovernmentRelationsStateFederalLobbyingMetric()

class UniversityEndowmentTrusteeFiduciaryAuditAgent:
    """Agent 6: Evaluates UniversityEndowmentTrusteeFiduciaryAudit."""
    def run(self) -> UniversityEndowmentTrusteeFiduciaryAudit:
        return UniversityEndowmentTrusteeFiduciaryAudit()

class ExecutiveGovernanceTrusteesScorerAgent:
    """Agent 7: Master deterministic aggregator for Executive Governance and Board of Trustees Intelligence."""
    def __init__(self):
        self.board_agent = BoardOfTrusteesResolutionResolutionAuditorAgent()
        self.presidential_agent = PresidentialStrategicPlanKPIAuditorAgent()
        self.bylaws_agent = UniversityBylawsLegalPolicyComplianceAuditAgent()
        self.erm_agent = InstitutionalRiskEnterpriseRiskManagementAuditAgent()
        self.lobbying_agent = GovernmentRelationsStateFederalLobbyingMeterAgent()
        self.fiduciary_agent = UniversityEndowmentTrusteeFiduciaryAuditAgent()

    def run(self) -> DeterministicExecutiveGovernanceTrusteesPipelineResult:
        board = self.board_agent.run()
        presidential = self.presidential_agent.run()
        bylaws = self.bylaws_agent.run()
        erm = self.erm_agent.run()
        lobbying = self.lobbying_agent.run()
        fiduciary = self.fiduciary_agent.run()
        metrics = {
            "bylaws_compliance": bylaws.university_bylaws_compliance_score_pct,
            "fiduciary_training": board.trustee_fiduciary_training_completion_pct,
            "presidential_kpis": presidential.presidential_kpi_targets_met_pct,
            "erm_score": erm.annual_erm_audit_compliance_score_pct
        }
        weights = {"bylaws_compliance": 0.30, "fiduciary_training": 0.30, "presidential_kpis": 0.25, "erm_score": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(board.board_resolutions_passed_annual, 10)
        return DeterministicExecutiveGovernanceTrusteesPipelineResult(
            board=board,
            presidential=presidential,
            bylaws=bylaws,
            erm=erm,
            lobbying=lobbying,
            fiduciary=fiduciary,
            governance_score=score, confidence_score=confidence
        )
