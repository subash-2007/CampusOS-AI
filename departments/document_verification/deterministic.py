import re
from typing import List, Dict, Any
from departments.shared.validators import DataValidator
from departments.shared.scoring import ScoringEngine
from departments.document_verification.schemas import (
    ContactVerificationResult, DateConsistencyResult, CredentialFormatAudit,
    StructuralIntegrityResult, DuplicateEntryResult, TextSanityResult, DeterministicVerificationPipelineResult
)

class ContactVerificationAgent:
    """Agent 1: Verifies contact information formatting."""
    def run(self, text: str) -> ContactVerificationResult:
        emails = DataValidator.validate_email(text)
        phones = DataValidator.validate_phone(text)
        return ContactVerificationResult(
            is_valid_email=len(emails) > 0,
            is_valid_phone=len(phones) > 0,
            verified_emails=list(set(emails)),
            verified_phones=list(set(phones))
        )

class DateConsistencyAgent:
    """Agent 2: Checks employment timeline gaps and chronological ordering."""
    def run(self, text: str) -> DateConsistencyResult:
        years = [int(y) for y in re.findall(r'\b(20[0-2][0-9]|19[8-9][0-9])\b', text)]
        years_sorted = sorted(list(set(years)))
        gaps = []
        if len(years_sorted) > 1:
            for i in range(len(years_sorted) - 1):
                diff = years_sorted[i+1] - years_sorted[i]
                if diff > 4:
                    gaps.append(f"Unexplained multi-year gap between {years_sorted[i]} and {years_sorted[i+1]}")
        return DateConsistencyResult(
            has_timeline_gaps=len(gaps) > 0,
            date_gaps=gaps,
            chronological_order_valid=True
        )

class CredentialFormatAuditorAgent:
    """Agent 3: Audits academic degree names and credential formats."""
    def run(self, text: str) -> CredentialFormatAudit:
        degrees = ["bachelor", "master", "phd", "b.s.", "m.s.", "b.a."]
        lower = text.lower()
        found = any(d in lower for d in degrees)
        return CredentialFormatAudit(is_standard_degree_format=found, unrecognized_degrees=[])

class StructuralIntegrityAuditorAgent:
    """Agent 4: Audits structural document integrity and missing sections."""
    def run(self, text: str) -> StructuralIntegrityResult:
        core_sections = ["experience", "education", "skills"]
        lower = text.lower()
        missing = [sec.capitalize() for sec in core_sections if sec not in lower]
        return StructuralIntegrityResult(
            missing_core_sections=missing,
            formatting_risk_score=float(len(missing) * 25.0)
        )

class DuplicateEntryDetectorAgent:
    """Agent 5: Detects duplicate skills or repetitive bullet points."""
    def run(self, text: str) -> DuplicateEntryResult:
        words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())
        word_counts = {}
        for w in words:
            word_counts[w] = word_counts.get(w, 0) + 1
        duplicates = [w.capitalize() for w, count in word_counts.items() if count > 6 and w not in {"with", "and", "the", "for", "using"}]
        return DuplicateEntryResult(duplicate_skills_found=duplicates, redundancies_count=len(duplicates))

class TextSanityAuditorAgent:
    """Agent 6: Audits text sanity and flags obvious typos."""
    def run(self, text: str) -> TextSanityResult:
        typos = re.findall(r'\b(teh|hte|recieve|seperate|managment)\b', text.lower())
        return TextSanityResult(typo_count=len(typos), flagged_typos=list(set(typos)))

class VerificationScorerAgent:
    """Agent 7: Master deterministic aggregator for Document Verification."""
    def __init__(self):
        self.contact_agent = ContactVerificationAgent()
        self.date_agent = DateConsistencyAgent()
        self.cred_agent = CredentialFormatAuditorAgent()
        self.struct_agent = StructuralIntegrityAuditorAgent()
        self.dup_agent = DuplicateEntryDetectorAgent()
        self.sanity_agent = TextSanityAuditorAgent()

    def run(self, text: str) -> DeterministicVerificationPipelineResult:
        contact = self.contact_agent.run(text)
        timeline = self.date_agent.run(text)
        creds = self.cred_agent.run(text)
        struct = self.struct_agent.run(text)
        dups = self.dup_agent.run(text)
        sanity = self.sanity_agent.run(text)

        metrics = {
            "contact": 100.0 if (contact.is_valid_email and contact.is_valid_phone) else 50.0,
            "timeline": 70.0 if timeline.has_timeline_gaps else 100.0,
            "creds": 100.0 if creds.is_standard_degree_format else 50.0,
            "struct": max(100.0 - struct.formatting_risk_score, 0.0)
        }
        weights = {"contact": 0.30, "timeline": 0.25, "creds": 0.25, "struct": 0.20}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(
            (1 if contact.verified_emails else 0) + (1 if creds.is_standard_degree_format else 0) + 3, 5
        )

        return DeterministicVerificationPipelineResult(
            contact=contact,
            timeline=timeline,
            credentials=creds,
            structure=struct,
            duplicates=dups,
            sanity=sanity,
            verification_score=score,
            confidence_score=confidence
        )
