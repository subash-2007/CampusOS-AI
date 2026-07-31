import re
from typing import List, Dict, Any
from departments.shared.validators import DataValidator
from departments.shared.keywords import KeywordMatcher
from departments.shared.scoring import ScoringEngine
from departments.resume_intelligence.schemas import (
    ContactInfo, ActionVerbAudit, ATSMatchResult, DateGapResult, BulletPointAudit, DeterministicPipelineResult
)

# Standard Strong Resume Action Verbs
STRONG_ACTION_VERBS = {
    "accelerated", "achieved", "architected", "built", "engineered", "created",
    "developed", "deployed", "designed", "decreased", "expanded", "headed",
    "implemented", "improved", "increased", "launched", "lead", "led", "managed",
    "optimized", "orchestrated", "reduced", "spearheaded", "scaled", "transformed"
}

STANDARD_SECTIONS = {"education", "experience", "skills", "projects", "certifications", "summary"}

class ContactExtractorAgent:
    """Agent 1: Extracts email, phone, and links deterministically using regex."""
    def run(self, text: str) -> ContactInfo:
        emails = DataValidator.validate_email(text)
        phones = DataValidator.validate_phone(text)
        links = re.findall(r'https?://[^\s,]+', text)
        return ContactInfo(
            emails=list(set(emails)),
            phones=list(set(phones)),
            links=list(set(links))
        )

class SectionAuditorAgent:
    """Agent 2: Identifies structural resume sections."""
    def run(self, text: str) -> List[str]:
        lower_text = text.lower()
        return [sec.capitalize() for sec in STANDARD_SECTIONS if sec in lower_text]

class ActionVerbAnalyzerAgent:
    """Agent 3: Analyzes action verb presence and verb density score."""
    def run(self, text: str) -> ActionVerbAudit:
        words = KeywordMatcher.extract_words(text)
        verbs_found = sorted(list(set(w for w in words if w in STRONG_ACTION_VERBS)))
        total_words = max(len(words), 1)
        density = round((len(verbs_found) / total_words) * 100, 2)
        return ActionVerbAudit(action_verbs_found=verbs_found, verb_density_score=density)

class DateGapDetectorAgent:
    """Agent 4: Scans for potential employment date gaps."""
    def run(self, text: str) -> DateGapResult:
        years = [int(y) for y in re.findall(r'\b(20[0-2][0-9]|19[8-9][0-9])\b', text)]
        years = sorted(list(set(years)))
        gaps = []
        if len(years) > 1:
            for i in range(len(years) - 1):
                if years[i+1] - years[i] > 2:
                    gaps.append(f"Potential gap detected between {years[i]} and {years[i+1]}")
        return DateGapResult(has_gaps=len(gaps) > 0, gaps_detected=gaps)

class BulletPointAuditorAgent:
    """Agent 5: Evaluates bullet points and metric quantification rate."""
    def run(self, text: str) -> BulletPointAudit:
        raw_lines = [line.strip() for line in text.split('\n') if line.strip()]
        lines = [line for line in raw_lines if line.startswith(('-', '*', '•')) or re.match(r'^\d+\.', line)]
        if not lines:
            lines = [line for line in raw_lines if len(line) > 35 and not line.isupper() and not '@' in line and not '|' in line]
        
        total = len(lines)
        metric_regex = r'(\d+[\d,.]*\s*%|\$\s*\d+[\d,.]*|\b\d+[\d,.]*\s*(x|k|m|b|gb|tb|users|clients|events|ms|s|\+)\b)'
        with_metrics = sum(1 for line in lines if re.search(metric_regex, line, re.IGNORECASE))
        rate = round((with_metrics / max(total, 1)) * 100, 2)
        return BulletPointAudit(total_bullets=total, bullets_with_metrics=with_metrics, quantification_rate=rate)

class ATSKeywordMatcherAgent:
    """Agent 6: Measures ATS keyword overlap against Target Job Description."""
    def run(self, resume_text: str, target_keywords: List[str]) -> ATSMatchResult:
        resume_words = KeywordMatcher.extract_words(resume_text)
        res = KeywordMatcher.calculate_overlap(resume_words, target_keywords)
        return ATSMatchResult(
            match_percentage=res["match_percentage"],
            matched_keywords=res["matched"],
            missing_keywords=res["missing"]
        )

class ResumeParserAgent:
    """Agent 7: Aggregates deterministic pipeline agents and calculates confidence score."""
    def __init__(self):
        self.contact_agent = ContactExtractorAgent()
        self.section_agent = SectionAuditorAgent()
        self.verb_agent = ActionVerbAnalyzerAgent()
        self.date_agent = DateGapDetectorAgent()
        self.bullet_agent = BulletPointAuditorAgent()
        self.ats_agent = ATSKeywordMatcherAgent()

    def run(self, resume_text: str, target_keywords: List[str] = None) -> DeterministicPipelineResult:
        if target_keywords is None:
            target_keywords = ["Python", "FastAPI", "React", "Docker", "SQL", "Git"]
            
        contact = self.contact_agent.run(resume_text)
        sections = self.section_agent.run(resume_text)
        verbs = self.verb_agent.run(resume_text)
        date_gaps = self.date_agent.run(resume_text)
        bullets = self.bullet_agent.run(resume_text)
        ats = self.ats_agent.run(resume_text, target_keywords)
        
        # Calculate Parsing Confidence Score
        present_count = len(sections) + (1 if contact.emails else 0) + (1 if contact.phones else 0)
        confidence = ScoringEngine.calculate_confidence_score(present_count, len(STANDARD_SECTIONS) + 2)
        
        return DeterministicPipelineResult(
            contact=contact,
            sections_found=sections,
            action_verbs=verbs,
            ats_match=ats,
            date_gaps=date_gaps,
            bullet_audit=bullets,
            confidence_score=confidence
        )
