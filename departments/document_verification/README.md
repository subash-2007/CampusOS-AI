# Department 011: Document Verification (`document_verification`)

## Overview
The **Document Verification Department** delivers an enterprise multi-agent pipeline designed to audit contact formatting, verify employment timeline continuity, validate academic credential standards, audit structural section integrity, flag duplicate entries, and run text sanity checks.

---

## Internal 10-Agent Architecture

### Deterministic Agents (7)
1. **ContactVerificationAgent**: Verifies email, phone number, and URL formatting.
2. **DateConsistencyAgent**: Scans for employment timeline gaps and date ordering.
3. **CredentialFormatAuditorAgent**: Audits academic degree names and credential standards.
4. **StructuralIntegrityAuditorAgent**: Audits presence of core resume sections.
5. **DuplicateEntryDetectorAgent**: Identifies repetitive bullet points or duplicate skill tags.
6. **TextSanityAuditorAgent**: Audits spelling sanity and common typo patterns.
7. **VerificationScorerAgent**: Master deterministic aggregator for verification scores.

### Reasoning Agents (2)
8. **VerificationAuditSummaryAgent**: Formulates overall audit summary and verification verdict.
9. **DocumentCorrectionGuideAgent**: Formulates step-by-step document correction guides.

### Orchestrator Agent (1)
10. **VerificationOrchestratorAgent**: Master Orchestrator Agent uniting verification checks and audit guidance.
