import re
import math
from typing import Dict, Any, List
from app.nlp.skill_extractor import extract_skills_from_text, extract_key_phrases

def compute_cosine_similarity(text1: str, text2: str) -> float:
    """Computes TF-IDF Cosine Similarity between two text documents."""
    if not text1.strip() or not text2.strip():
        return 0.0

    try:
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity
        
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform([text1, text2])
        sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        return float(sim)
    except Exception:
        # Fallback term frequency vector similarity
        def tokenize(txt):
            return re.findall(r'\w+', txt.lower())
        
        words1 = tokenize(text1)
        words2 = tokenize(text2)
        vocab = set(words1 + words2)
        if not vocab:
            return 0.0

        v1 = [words1.count(w) for w in vocab]
        v2 = [words2.count(w) for w in vocab]
        
        dot_product = sum(a * b for a, b in zip(v1, v2))
        mag1 = math.sqrt(sum(a * a for a in v1))
        mag2 = math.sqrt(sum(b * b for b in v2))
        
        if mag1 == 0 or mag2 == 0:
            return 0.0
        return dot_product / (mag1 * mag2)

def compute_ats_optimization(resume_text: str, job_description_text: str) -> Dict[str, Any]:
    """Dynamically analyzes resume against job description using TF-IDF and skill set matching."""
    if not job_description_text.strip():
        job_description_text = "Software Engineer role requiring Python, TypeScript, REST APIs, Git, database management, testing, and team collaboration."

    # Extract dynamic skills
    candidate_skills = set(extract_skills_from_text(resume_text))
    required_skills = set(extract_skills_from_text(job_description_text))
    
    # If no skills found in JD, pull key phrases
    if not required_skills:
        phrases = extract_key_phrases(job_description_text, 10)
        required_skills = set(phrases)

    matched_skills = sorted(list(candidate_skills.intersection(required_skills)))
    missing_skills = sorted(list(required_skills.difference(candidate_skills)))

    # Compute metric components
    cosine_sim = compute_cosine_similarity(resume_text, job_description_text)
    
    jaccard_ratio = 0.0
    if required_skills:
        jaccard_ratio = len(matched_skills) / len(required_skills)

    # Weighted ATS score calculation: 60% Skill Overlap + 40% TF-IDF Cosine Similarity
    raw_score = (jaccard_ratio * 65.0) + (cosine_sim * 35.0)
    # Give base baseline for any non-empty resume
    ats_score = int(min(100, max(25, round(raw_score if candidate_skills else raw_score + 20))))

    if ats_score >= 80:
        ats_compatibility = "High (90%+ ATS Pass Probability)"
    elif ats_score >= 60:
        ats_compatibility = "Moderate (70%+ ATS Pass Probability)"
    else:
        ats_compatibility = "Low (Needs Optimization)"

    # Dynamic Formatting & Structure Warnings
    formatting_warnings = []
    if len(resume_text.splitlines()) < 15:
        formatting_warnings.append("Resume length appears concise. Ensure all relevant experience and project details are expanded.")
    if "education" not in resume_text.lower():
        formatting_warnings.append("Education section not explicitly detected. Add a clear 'EDUCATION' section header.")
    if "skills" not in resume_text.lower():
        formatting_warnings.append("Dedicated 'SKILLS' header not detected. Group technical skills under a prominent header for ATS parser safety.")

    # Dynamic Bullet Point Optimizations based on actual missing skills
    bullet_optimizations = []
    if missing_skills:
        top_missing = missing_skills[:2]
        bullet_optimizations.append({
            "original": "Worked on core project features and integration.",
            "optimized": f"Architected high-throughput services incorporating {top_missing[0]}, increasing system reliability and developer efficiency."
        })
        if len(top_missing) > 1:
            bullet_optimizations.append({
                "original": "Assisted with application deployment and testing.",
                "optimized": f"Engineered automated deployment pipelines using {top_missing[1]}, reducing release latency by 35%."
            })
    else:
        bullet_optimizations.append({
            "original": "Built application features and maintained codebase.",
            "optimized": "Engineered scalable application features using industry best practices, improving performance and user retention by 30%."
        })

    return {
        "match_score": ats_score,
        "cosine_similarity": round(cosine_sim, 3),
        "jaccard_ratio": round(jaccard_ratio, 3),
        "ats_compatibility": ats_compatibility,
        "matched_keywords": matched_skills,
        "missing_keywords": missing_skills,
        "formatting_warnings": formatting_warnings,
        "bullet_optimizations": bullet_optimizations
    }
