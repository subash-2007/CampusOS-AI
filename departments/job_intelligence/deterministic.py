import re
from typing import List, Dict, Any
from departments.shared.keywords import KeywordMatcher
from departments.shared.scoring import ScoringEngine
from departments.job_intelligence.schemas import (
    TechStackExtraction, SenioritySignal, ResponsibilityBreakdown,
    SalaryBenchmarkResult, WorkModelResult, DomainComplexityResult, DeterministicJobPipelineResult
)

KNOWN_LANGUAGES = {"python", "javascript", "typescript", "java", "c++", "go", "rust", "sql"}
KNOWN_FRAMEWORKS = {"react", "next.js", "fastapi", "django", "node.js", "express", "spring"}
KNOWN_DATABASES = {"postgresql", "mongodb", "redis", "mysql", "dynamodb"}
KNOWN_CLOUD = {"aws", "gcp", "azure", "docker", "kubernetes", "terraform"}

class TechStackExtractorAgent:
    """Agent 1: Extracts technical stack from Job Description."""
    def run(self, jd_text: str) -> TechStackExtraction:
        words = set(KeywordMatcher.extract_words(jd_text))
        return TechStackExtraction(
            languages=sorted(list(words.intersection(KNOWN_LANGUAGES))),
            frameworks=sorted(list(words.intersection(KNOWN_FRAMEWORKS))),
            databases=sorted(list(words.intersection(KNOWN_DATABASES))),
            cloud_tools=sorted(list(words.intersection(KNOWN_CLOUD)))
        )

class SeniorityClassifierAgent:
    """Agent 2: Classifies seniority level and required years of experience."""
    def run(self, jd_text: str) -> SenioritySignal:
        lower = jd_text.lower()
        years_match = re.search(r'(\d+)\+?\s*years', lower)
        years = int(years_match.group(1)) if years_match else 3
        
        if "principal" in lower or "staff" in lower or years >= 8:
            level = "Principal / Staff"
        elif "senior" in lower or years >= 5:
            level = "Senior"
        elif "junior" in lower or "entry" in lower or years <= 2:
            level = "Junior / Entry"
        else:
            level = "Mid-Level"
            
        mgmt = "manage" in lower or "lead" in lower or "director" in lower
        return SenioritySignal(seniority_level=level, years_experience_required=years, is_management_role=mgmt)

class ResponsibilityParserAgent:
    """Agent 3: Parses job responsibilities."""
    def run(self, jd_text: str) -> ResponsibilityBreakdown:
        lines = [line.strip() for line in jd_text.split('\n') if line.strip().startswith(('-', '*', '•'))]
        if not lines:
            lines = [line.strip() for line in jd_text.split('\n') if len(line.strip()) > 25][:5]
        return ResponsibilityBreakdown(
            core_responsibilities=lines[:3],
            secondary_duties=lines[3:6]
        )

class SalaryBenchmarkAgent:
    """Agent 4: Estimates compensation benchmarks."""
    def run(self, jd_text: str) -> SalaryBenchmarkResult:
        match = re.search(r'\$(\d{2,3}),?(\d{3})\s*-\s*\$(\d{2,3}),?(\d{3})', jd_text)
        if match:
            min_sal = int(match.group(1) + match.group(2))
            max_sal = int(match.group(3) + match.group(4))
            return SalaryBenchmarkResult(estimated_min_salary=min_sal, estimated_max_salary=max_sal, currency="USD")
        return SalaryBenchmarkResult(estimated_min_salary=110000, estimated_max_salary=150000, currency="USD")

class WorkModelExtractorAgent:
    """Agent 5: Identifies work model (Remote, Hybrid, On-Site)."""
    def run(self, jd_text: str) -> WorkModelResult:
        lower = jd_text.lower()
        if "remote" in lower:
            model = "Remote"
        elif "hybrid" in lower:
            model = "Hybrid"
        else:
            model = "On-Site"
        return WorkModelResult(work_model=model, location="United States")

class DomainComplexityAgent:
    """Agent 6: Assesses domain complexity score."""
    def run(self, jd_text: str) -> DomainComplexityResult:
        lower = jd_text.lower()
        tags = []
        if "distributed" in lower or "microservices" in lower:
            tags.append("Distributed Systems")
        if "ai" in lower or "machine learning" in lower:
            tags.append("AI / ML")
        if "cloud" in lower or "aws" in lower:
            tags.append("Cloud Architecture")
        score = min(50.0 + len(tags) * 15.0, 100.0)
        return DomainComplexityResult(complexity_score=score, domain_tags=tags)

class JobScorerAgent:
    """Agent 7: Master deterministic aggregator for Job Intelligence."""
    def __init__(self):
        self.tech_agent = TechStackExtractorAgent()
        self.seniority_agent = SeniorityClassifierAgent()
        self.resp_agent = ResponsibilityParserAgent()
        self.salary_agent = SalaryBenchmarkAgent()
        self.work_agent = WorkModelExtractorAgent()
        self.complexity_agent = DomainComplexityAgent()

    def run(self, jd_text: str) -> DeterministicJobPipelineResult:
        tech = self.tech_agent.run(jd_text)
        sen = self.seniority_agent.run(jd_text)
        resp = self.resp_agent.run(jd_text)
        sal = self.salary_agent.run(jd_text)
        wm = self.work_agent.run(jd_text)
        comp = self.complexity_agent.run(jd_text)
        
        confidence = ScoringEngine.calculate_confidence_score(
            len(tech.languages) + len(tech.frameworks) + (1 if resp.core_responsibilities else 0), 6
        )
        return DeterministicJobPipelineResult(
            tech_stack=tech,
            seniority=sen,
            responsibilities=resp,
            salary=sal,
            work_model=wm,
            complexity=comp,
            confidence_score=confidence
        )
