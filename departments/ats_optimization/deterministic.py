import re
from typing import List, Dict, Any
from departments.shared.keywords import KeywordMatcher
from departments.shared.scoring import ScoringEngine
from departments.ats_optimization.schemas import (
    KeywordMatchBreakdown, FormatCompatibilityResult, SectionHeaderAudit,
    ActionVerbDensityResult, QuantificationScore, FrequencyAnalysis, DeterministicATSPipelineResult
)

WEAK_PHRASES = {"responsible for", "assisted with", "helped out", "worked on", "duties included", "tasks were"}

class HardSkillMatcherAgent:
    """Agent 1: Audits technical hard skill keyword matches against Job Description."""
    def run(self, resume_text: str, hard_skills: List[str]) -> Dict[str, Any]:
        resume_words = KeywordMatcher.extract_words(resume_text)
        res = KeywordMatcher.calculate_overlap(resume_words, hard_skills)
        return res

class SoftSkillMatcherAgent:
    """Agent 2: Audits soft skill keyword presence (e.g. leadership, collaboration)."""
    def run(self, resume_text: str, soft_skills: List[str]) -> Dict[str, Any]:
        resume_words = KeywordMatcher.extract_words(resume_text)
        res = KeywordMatcher.calculate_overlap(resume_words, soft_skills)
        return res

class FormatCompatibilityAgent:
    """Agent 3: Checks resume format safety against standard ATS parser bugs."""
    def run(self, resume_text: str) -> FormatCompatibilityResult:
        issues = []
        if "\t" in resume_text:
            issues.append("Contains tab characters which may corrupt column alignment")
        if re.search(r'[^\x00-\x7F]+', resume_text):
            issues.append("Contains special non-ASCII unicode symbols that may crash legacy ATS scanners")
        score = 100.0 - (len(issues) * 20.0)
        return FormatCompatibilityResult(
            is_ats_parseable=len(issues) == 0,
            formatting_issues=issues,
            font_safety_score=max(score, 0.0)
        )

class SectionHeaderAuditorAgent:
    """Agent 4: Audits section header standardness."""
    def run(self, resume_text: str) -> SectionHeaderAudit:
        standard_headers = ["experience", "education", "skills", "projects", "summary", "certifications"]
        lower = resume_text.lower()
        found = [h.capitalize() for h in standard_headers if h in lower]
        return SectionHeaderAudit(
            standard_headers_count=len(found),
            non_standard_headers=[]
        )

class WeakPhraseDetectorAgent:
    """Agent 5: Flags weak phrases that decrease ATS impact."""
    def run(self, resume_text: str) -> ActionVerbDensityResult:
        lower = resume_text.lower()
        weak_count = sum(lower.count(phrase) for phrase in WEAK_PHRASES)
        strong_verbs = len(re.findall(r'\b(engineered|built|launched|spearheaded|architected|deployed|led|created|developed|optimized)\b', lower))
        return ActionVerbDensityResult(
            strong_action_verb_count=strong_verbs,
            weak_phrase_count=weak_count
        )

class QuantificationMeterAgent:
    """Agent 6: Measures quantification metric percentage."""
    def run(self, resume_text: str) -> QuantificationScore:
        bullets = [line for line in resume_text.split('\n') if line.strip().startswith(('-', '*', '•'))]
        if not bullets:
            bullets = [line for line in resume_text.split('\n') if len(line.strip()) > 30]
        total = max(len(bullets), 1)
        quantified = sum(1 for line in bullets if re.search(r'(\d+[\d,.]*\s*%|\$\s*\d+[\d,.]*|\b\d+[\d,.]*\s*(x|k|m|b|users)\b)', line, re.IGNORECASE))
        rate = round((quantified / total) * 100.0, 2)
        return QuantificationScore(quantified_bullets_percentage=rate)

class ATSScorerAgent:
    """Agent 7: Aggregates deterministic sub-agent results into master ATS score."""
    def __init__(self):
        self.hard_agent = HardSkillMatcherAgent()
        self.soft_agent = SoftSkillMatcherAgent()
        self.format_agent = FormatCompatibilityAgent()
        self.header_agent = SectionHeaderAuditorAgent()
        self.weak_agent = WeakPhraseDetectorAgent()
        self.quant_agent = QuantificationMeterAgent()

    def run(self, resume_text: str, target_hard_skills: List[str] = None, target_soft_skills: List[str] = None) -> DeterministicATSPipelineResult:
        if target_hard_skills is None:
            target_hard_skills = ["Python", "FastAPI", "Docker", "SQL", "Git"]
        if target_soft_skills is None:
            target_soft_skills = ["Leadership", "Communication", "Problem Solving"]

        hard = self.hard_agent.run(resume_text, target_hard_skills)
        soft = self.soft_agent.run(resume_text, target_soft_skills)
        fmt = self.format_agent.run(resume_text)
        hdr = self.header_agent.run(resume_text)
        weak = self.weak_agent.run(resume_text)
        quant = self.quant_agent.run(resume_text)

        kw_breakdown = KeywordMatchBreakdown(
            hard_skills_match=hard["match_percentage"],
            soft_skills_match=soft["match_percentage"],
            missing_critical_keywords=hard["missing"],
            present_critical_keywords=hard["matched"]
        )

        metrics = {
            "hard": hard["match_percentage"],
            "soft": soft["match_percentage"],
            "fmt": fmt.font_safety_score,
            "quant": quant.quantified_bullets_percentage
        }
        weights = {"hard": 0.50, "soft": 0.20, "fmt": 0.15, "quant": 0.15}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(hdr.standard_headers_count + (1 if fmt.is_ats_parseable else 0), 7)

        return DeterministicATSPipelineResult(
            keyword_match=kw_breakdown,
            format_compat=fmt,
            section_audit=hdr,
            verb_density=weak,
            quantification=quant,
            frequency=FrequencyAnalysis(keyword_frequencies={k: 1 for k in hard["matched"]}),
            overall_ats_score=score,
            confidence_score=confidence
        )
