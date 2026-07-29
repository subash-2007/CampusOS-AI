from app.nlp.text_parser import parse_document_input, fetch_url_text
from app.nlp.skill_extractor import extract_skills_from_text, extract_key_phrases
from app.nlp.tfidf_matcher import compute_ats_optimization, compute_cosine_similarity
from app.nlp.resume_parser import analyze_resume_dynamically

__all__ = [
    "parse_document_input",
    "fetch_url_text",
    "extract_skills_from_text",
    "extract_key_phrases",
    "compute_ats_optimization",
    "compute_cosine_similarity",
    "analyze_resume_dynamically"
]
