from typing import Dict, List, Any

class ScoringEngine:
    """
    Enterprise scoring utilities for calculating normalized scores, confidence indices, and metric weights.
    """
    @staticmethod
    def calculate_weighted_score(metrics: Dict[str, float], weights: Dict[str, float]) -> float:
        """Calculates a weighted average score from normalized metrics (0.0 - 100.0)."""
        total_weight = sum(weights.values())
        if total_weight == 0:
            return 0.0
        weighted_sum = sum(metrics.get(key, 0.0) * weight for key, weight in weights.items())
        return round(weighted_sum / total_weight, 2)

    @staticmethod
    def calculate_confidence_score(present_fields: int, total_expected_fields: int) -> float:
        """Calculates parsing confidence score between 0.0 and 1.0."""
        if total_expected_fields == 0:
            return 0.0
        ratio = present_fields / total_expected_fields
        return round(min(max(ratio, 0.0), 1.0), 2)
