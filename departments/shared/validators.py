import re
from typing import List, Dict, Any

class DataValidator:
    """
    Data validation routines for emails, phone numbers, timeline integrity, and string quality.
    """
    EMAIL_REGEX = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    PHONE_REGEX = r'(\+?\d{1,3}[\s-]?)?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}'

    @classmethod
    def validate_email(cls, text: str) -> List[str]:
        return re.findall(cls.EMAIL_REGEX, text)

    @classmethod
    def validate_phone(cls, text: str) -> List[str]:
        return re.findall(cls.PHONE_REGEX, text)

    @staticmethod
    def audit_text_length(text: str, min_words: int = 20) -> Dict[str, Any]:
        words = text.split()
        word_count = len(words)
        return {
            "word_count": word_count,
            "meets_minimum": word_count >= min_words
        }
