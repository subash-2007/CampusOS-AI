# Department 001: Resume Intelligence (`resume_intelligence`)

## Overview
The **Resume Intelligence Department** is the Gold Standard reference implementation of CampusOS AI department architecture. It provides a production-grade multi-agent pipeline designed to parse, audit, benchmark, and enhance professional resumes.

---

## Internal 10-Agent Architecture

```
                                 ┌────────────────────────────────────────────────────────┐
                                 │                ResumeOrchestratorAgent                 │
                                 └───────────────────────────┬────────────────────────────┘
                                                             │
                                ┌────────────────────────────┴───────────────────────────┐
                                │                                                        │
                   ┌────────────▼──────────────┐                           ┌─────────────▼─────────────┐
                   │   Deterministic Pipeline  │                           │     Reasoning Pipeline    │
                   └────────────┬──────────────┘                           └─────────────┬─────────────┘
                                │                                                        │
         ┌──────────────────────┼──────────────────────┐                    ┌────────────┴────────────┐
         │                      │                      │                    │                         │
┌────────▼────────┐    ┌────────▼────────┐    ┌────────▼────────┐  ┌────────▼────────┐        ┌────────▼────────┐
│  ResumeParser   │    │ContactExtractor │    │ SectionAuditor  │  │ ImpactEvaluator │        │ ResumeEnhancer  │
└─────────────────┘    └─────────────────┘    └─────────────────┘  └─────────────────┘        └─────────────────┘
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ActionVerbAnalyzer│   │ DateGapDetector │    │BulletPointAuditor│
└─────────────────┘    └─────────────────┘    └─────────────────┘
                       ┌─────────────────┐
                       │ATSKeywordMatcher│
                       └─────────────────┘
```

### Deterministic Agents (7)
1. **ResumeParserAgent**: Coordinates rule-based extractors and computes parsing confidence score.
2. **ContactExtractorAgent**: Regex extraction of emails, phone numbers, and URLs.
3. **SectionAuditorAgent**: Audits presence of standard resume sections (Education, Experience, Skills, Projects, etc.).
4. **ActionVerbAnalyzerAgent**: Audits action verb usage, diversity, and verb density score.
5. **DateGapDetectorAgent**: Scans employment timelines for potential multi-year career gaps.
6. **BulletPointAuditorAgent**: Measures metric quantification rate across bullet points.
7. **ATSKeywordMatcherAgent**: Calculates keyword overlap percentage and missing skills against target Job Description.

### Reasoning Agents (2)
8. **ImpactEvaluatorAgent**: LLM-driven qualitative analysis of resume narrative, impact, and leadership signals.
9. **ResumeEnhancerAgent**: Formulates actionable bullet point rewrites and keyword optimization strategies.

### Orchestrator Agent (1)
10. **ResumeOrchestratorAgent**: End-to-end master orchestrator uniting deterministic calculations and LLM reasoning steps into a cohesive report.

---

## File Structure

- `schemas.py`: Pydantic data models for deterministic metrics, reasoning results, and orchestrator report.
- `deterministic.py`: Implementation of 7 rule-based deterministic agents.
- `reasoning.py`: Implementation of 2 LLM reasoning agents.
- `orchestrator.py`: Implementation of Master Orchestrator Agent.
- `README.md`: Technical documentation.
- `tests/test_resume_intelligence.py`: Comprehensive PyTest unit & integration tests.

---

## Usage Example

```python
import asyncio
from departments.resume_intelligence.orchestrator import ResumeOrchestratorAgent

async def main():
    orchestrator = ResumeOrchestratorAgent()
    sample_resume = """
    Alex Mercer
    Email: alex.mercer@example.com | Phone: (555) 019-2834
    GitHub: https://github.com/alexmercer
    
    EXPERIENCE
    Senior Software Engineer | Tech Corp | 2021 - 2024
    - Spearheaded microservice migration to FastAPI, reducing latency by 40%.
    - Built React dashboard for 50,000 active users.
    
    SKILLS
    Python, FastAPI, React, PostgreSQL, Docker
    """
    
    report = await orchestrator.run_pipeline(
        resume_text=sample_resume,
        target_keywords=["Python", "FastAPI", "React", "Docker", "Kubernetes", "AWS"]
    )
    
    print(f"Overall Score: {report.overall_score}/100")
    print(f"Confidence Score: {report.confidence_score}")
    print(f"ATS Match: {report.deterministic_analysis.ats_match.match_percentage}%")

if __name__ == "__main__":
    asyncio.run(main())
```
