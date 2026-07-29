import re
from typing import Dict, Any, List
from app.nlp.skill_extractor import extract_skills_from_text

HIGH_IMPACT_VERBS = [
    "architected", "spearheaded", "engineered", "orchestrated", "developed",
    "optimized", "implemented", "designed", "deployed", "scaled", "automated",
    "reduced", "increased", "boosted", "built", "accelerated", "crafted"
]

def analyze_resume_dynamically(resume_text: str) -> Dict[str, Any]:
    """Dynamically parses and evaluates candidate resume text without static fallbacks."""
    if not resume_text.strip():
        return {
            "overall_score": 50,
            "impact_score": 45,
            "formatting_score": 60,
            "strengths": ["Document submitted"],
            "weaknesses": ["Empty or unreadable text"],
            "improvements": ["Upload a readable PDF/DOCX file"],
            "action_verb_rating": "Moderate",
            "extracted_skills": []
        }

    lines = [line.strip() for line in resume_text.splitlines() if line.strip()]
    text_lower = resume_text.lower()

    # Dynamic Skills Extraction
    extracted_skills = extract_skills_from_text(resume_text)

    # Detect Sections
    has_education = any(h in text_lower for h in ["education", "university", "bachelor", "master", "degree", "gpa"])
    has_experience = any(h in text_lower for h in ["experience", "employment", "work history", "intern", "engineer"])
    has_projects = any(h in text_lower for h in ["project", "github", "portfolio", "hackathon"])
    has_skills = any(h in text_lower for h in ["skill", "technologies", "languages", "frameworks"])

    # Count Quantitative Metrics (% numbers, $, ms, users)
    metrics_matches = re.findall(r'\b(?:\d+%\b|\$\d+|\d+\+|\d+ms\b|\d+k\b)', text_lower)
    metric_count = len(metrics_matches)

    # Count Action Verbs
    action_verb_count = sum(1 for verb in HIGH_IMPACT_VERBS if re.search(r'\b' + verb + r'\b', text_lower))

    # Calculate Scores Dynamically
    # 1. Formatting Score (30 pts max based on sections & structure)
    section_score = (has_education * 7) + (has_experience * 8) + (has_projects * 8) + (has_skills * 7)
    formatting_score = min(100, max(50, 60 + section_score))

    # 2. Impact Score (based on quantitative metrics + action verb density)
    impact_score = min(100, max(45, 50 + (metric_count * 5) + (action_verb_count * 4)))

    # 3. Overall Score
    skill_bonus = min(20, len(extracted_skills) * 2)
    overall_score = min(100, max(40, round((formatting_score * 0.4) + (impact_score * 0.4) + skill_bonus)))

    # Dynamic Strengths
    strengths: List[str] = []
    if extracted_skills:
        strengths.append(f"Identified {len(extracted_skills)} technical skills including {', '.join(extracted_skills[:4])}")
    if has_projects:
        strengths.append("Dedicated Projects section highlighting practical implementation experience")
    if metric_count > 0:
        strengths.append(f"Incorporates quantified impact metrics ({metric_count} metrics detected)")
    if action_verb_count >= 3:
        strengths.append("Uses active engineering verbs (e.g. Engineered, Developed, Optimized)")
    if not strengths:
        strengths.append("Clear document structure with readable text entries")

    # Dynamic Weaknesses & Improvement Areas
    weaknesses: List[str] = []
    improvements: List[str] = []

    if metric_count < 2:
        weaknesses.append("Resume bullet points lack quantified business/technical impact metrics (e.g. % speedup, user count)")
        improvements.append("Add STAR format metrics to bullet points (e.g. 'Optimized API latency by 35% across 10,000 requests')")

    if action_verb_count < 3:
        weaknesses.append("Bullet points could use stronger, high-impact technical action verbs")
        improvements.append("Elevate bullet openings using strong verbs: 'Architected', 'Spearheaded', 'Engineered'")

    if not has_skills or len(extracted_skills) < 5:
        weaknesses.append("Skill coverage appears narrow or unorganized under a clear header")
        improvements.append("Group your technical skills explicitly under languages, frameworks, databases, and tools headers")

    if not improvements:
        improvements.append("Tailor your summary section specifically to your target job role title")

    action_verb_rating = f"{'Strong' if action_verb_count >= 4 else 'Moderate'} ({action_verb_count} high-impact verbs detected)"

    return {
        "overall_score": overall_score,
        "impact_score": impact_score,
        "formatting_score": formatting_score,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "improvements": improvements,
        "action_verb_rating": action_verb_rating,
        "extracted_skills": extracted_skills,
        "metrics_count": metric_count
    }
