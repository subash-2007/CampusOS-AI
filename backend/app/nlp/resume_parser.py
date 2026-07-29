import re
from typing import Dict, Any, List

ACTION_VERBS = {
    "built", "developed", "architected", "engineered", "designed", "implemented",
    "scaled", "optimized", "spearheaded", "automated", "created", "led", "managed",
    "deployed", "integrated", "launched", "reduced", "increased", "accelerated",
    "refactored", "orchestrated", "transformed", "migrated", "improved"
}

SECTION_HEADERS = [
    "education", "experience", "work experience", "employment", "projects",
    "technical skills", "skills", "certifications", "achievements", "summary", "objective"
]

def analyze_resume_dynamically(resume_text: str) -> Dict[str, Any]:
    """Dynamically parses resume structure, metrics, action verbs, and quality scores."""
    if not resume_text:
        return {
            "overall_score": 65,
            "impact_score": 60,
            "credibility_index": 70,
            "ats_readiness": 65,
            "strengths": ["Clear document format"],
            "weaknesses": ["Provide more detailed experience bullets"],
            "suggestions": ["Include technical project descriptions and quantitative metrics"]
        }

    lower_text = resume_text.lower()
    words = re.findall(r'\b[a-zA-Z0-9+#.-]+\b', lower_text)
    word_count = len(words)

    # 1. Section Header Detection
    detected_sections = []
    for header in SECTION_HEADERS:
        if header in lower_text:
            detected_sections.append(header.title())
    section_count = len(set(detected_sections))

    # 2. Metric & Action Verb Extraction
    metrics = re.findall(r'\b\d+(?:[\.,]\d+)?%?\b', resume_text)
    metric_count = len(metrics)

    found_action_verbs = [w for w in words if w in ACTION_VERBS]
    action_verb_count = len(set(found_action_verbs))

    # 3. Dynamic Score Calculation
    formatting_score = min(96, max(52, 58 + (section_count * 7)))
    impact_score = min(95, max(48, 52 + (metric_count * 4) + (action_verb_count * 3)))
    credibility_index = min(98, max(55, 62 + (15 if word_count > 150 else 5) + (15 if section_count >= 3 else 5)))
    ats_readiness = min(95, max(50, round((formatting_score * 0.5) + (impact_score * 0.5))))
    overall_score = min(98, max(52, round((formatting_score * 0.35) + (impact_score * 0.35) + (credibility_index * 0.30))))

    # 4. Dynamic Strengths & Weaknesses Synthesis
    strengths = []
    if section_count >= 3:
        strengths.append(f"Structured layout with {section_count} clear section headers")
    if action_verb_count > 3:
        strengths.append(f"Strong action verb usage ({', '.join(list(set(found_action_verbs))[:3])})")
    if metric_count > 2:
        strengths.append(f"Includes quantitative impact metrics ({metric_count} measurable numbers/percentages found)")
    if not strengths:
        strengths.append("Readable plain text layout")

    weaknesses = []
    if metric_count <= 2:
        weaknesses.append("Low quantitative metric density (few percentages or measurable numbers)")
    if action_verb_count <= 3:
        weaknesses.append("Bullet points could use stronger technical action verbs")
    if section_count < 4:
        weaknesses.append("Missing dedicated section headers (e.g., Projects, Certifications)")

    suggestions = [
        "Incorporate quantitative metrics into experience bullet points (e.g. 'Improved latency by 25%')",
        "Add a dedicated Projects section highlighting technical tech stack details",
        "Align technical skill keywords with target job descriptions"
    ]

    return {
        "overall_score": overall_score,
        "impact_score": impact_score,
        "credibility_index": credibility_index,
        "ats_readiness": ats_readiness,
        "word_count": word_count,
        "detected_sections": detected_sections,
        "metric_count": metric_count,
        "action_verb_count": action_verb_count,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "suggestions": suggestions
    }
