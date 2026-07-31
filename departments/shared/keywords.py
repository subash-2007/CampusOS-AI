import re
from typing import List, Set, Dict, Any

class KeywordMatcher:
    """
    High-performance keyword matching and text overlap calculation utilities.
    """
    @staticmethod
    def extract_words(text: str) -> List[str]:
        """Extract clean alphanumeric tokens from text."""
        return re.findall(r'\b[a-zA-Z0-9+#.-]+\b', text.lower())

    @staticmethod
    def calculate_overlap(source_keywords: List[str], target_keywords: List[str]) -> Dict[str, Any]:
        """Calculates keyword match percentage and identifies missing keywords."""
        source_set = set(k.lower() for k in source_keywords)
        target_set = set(k.lower() for k in target_keywords)
        if not target_set:
            return {"match_percentage": 0.0, "matched": [], "missing": []}
        
        matched = list(source_set.intersection(target_set))
        missing = list(target_set.difference(source_set))
        percentage = (len(matched) / len(target_set)) * 100.0
        
        return {
            "match_percentage": round(percentage, 2),
            "matched": sorted(matched),
            "missing": sorted(missing)
        }
