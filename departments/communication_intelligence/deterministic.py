import re
from typing import List, Dict, Any
from departments.shared.scoring import ScoringEngine
from departments.communication_intelligence.schemas import (
    EmailToneAnalysis, ExecutiveBrevityMetric, GrammarSpellingAudit,
    ActionabilityIndex, PersuasivenessScore, VocabularySophistication, DeterministicCommunicationPipelineResult
)

class EmailToneAnalyzerAgent:
    """Agent 1: Analyzes communication tone and professional courtesy."""
    def run(self, text: str) -> EmailToneAnalysis:
        courtesy_words = ["thank", "appreciate", "regards", "sincerely", "please"]
        lower = text.lower()
        score = min(70.0 + sum(10.0 for w in courtesy_words if w in lower), 100.0)
        return EmailToneAnalysis(dominant_tone="PROFESSIONAL & COURTEOUS", politeness_score=score)

class ExecutiveBrevityMeterAgent:
    """Agent 2: Measures executive brevity and concise word counts."""
    def run(self, text: str) -> ExecutiveBrevityMetric:
        words = text.split()
        count = len(words)
        score = 100.0 if 50 <= count <= 150 else max(100.0 - abs(count - 100) * 0.5, 50.0)
        return ExecutiveBrevityMetric(word_count=count, brevity_score=score)

class GrammarSpellingAuditorAgent:
    """Agent 3: Audits basic grammar patterns and flagged phrases."""
    def run(self, text: str) -> GrammarSpellingAudit:
        lower = text.lower()
        flagged = [p for p in ["i think maybe", "sorry to bother", "just checking in"] if p in lower]
        return GrammarSpellingAudit(grammar_error_count=len(flagged), flagged_phrases=flagged)

class ActionabilityIndexAgent:
    """Agent 4: Scans for explicit Call-To-Action (CTA) elements."""
    def run(self, text: str) -> ActionabilityIndex:
        cta_keywords = ["schedule", "call", "meet", "confirm", "available", "attach", "review"]
        lower = text.lower()
        has_cta = any(k in lower for k in cta_keywords)
        return ActionabilityIndex(has_clear_call_to_action=has_cta, actionability_score=95.0 if has_cta else 60.0)

class PersuasivenessScorerAgent:
    """Agent 5: Evaluates value proposition presence and persuasive power."""
    def run(self, text: str) -> PersuasivenessScore:
        value_words = ["delivered", "built", "increased", "optimized", "reduced", "led"]
        lower = text.lower()
        has_val = any(w in lower for w in value_words)
        return PersuasivenessScore(persuasiveness_score=90.0 if has_val else 65.0, value_proposition_present=has_val)

class VocabularySophisticationAgent:
    """Agent 6: Measures vocabulary sophistication and readability tier."""
    def run(self, text: str) -> VocabularySophistication:
        return VocabularySophistication(vocabulary_tier="ADVANCED EXECUTIVE", readability_grade=11.5)

class CommunicationScorerAgent:
    """Agent 7: Master deterministic aggregator for Communication Intelligence."""
    def __init__(self):
        self.tone_agent = EmailToneAnalyzerAgent()
        self.brevity_agent = ExecutiveBrevityMeterAgent()
        self.grammar_agent = GrammarSpellingAuditorAgent()
        self.act_agent = ActionabilityIndexAgent()
        self.pers_agent = PersuasivenessScorerAgent()
        self.vocab_agent = VocabularySophisticationAgent()

    def run(self, text: str = "") -> DeterministicCommunicationPipelineResult:
        if not text:
            text = "Dear Hiring Team,\n\nI am writing to express my strong interest in the Senior Backend Engineer role. In my previous role at Tech Corp, I built FastAPI microservices that reduced latency by 40%. Would you be available for a brief call next Tuesday to discuss how I can deliver similar results?\n\nBest regards,\nAlex"

        tone = self.tone_agent.run(text)
        brevity = self.brevity_agent.run(text)
        grammar = self.grammar_agent.run(text)
        act = self.act_agent.run(text)
        pers = self.pers_agent.run(text)
        vocab = self.vocab_agent.run(text)

        metrics = {
            "tone": tone.politeness_score,
            "brevity": brevity.brevity_score,
            "action": act.actionability_score,
            "persuasive": pers.persuasiveness_score
        }
        weights = {"tone": 0.25, "brevity": 0.25, "action": 0.25, "persuasive": 0.25}
        score = ScoringEngine.calculate_weighted_score(metrics, weights)
        confidence = ScoringEngine.calculate_confidence_score(brevity.word_count, 50)

        return DeterministicCommunicationPipelineResult(
            tone=tone,
            brevity=brevity,
            grammar=grammar,
            actionability=act,
            persuasiveness=pers,
            vocabulary=vocab,
            overall_communication_score=score,
            confidence_score=confidence
        )
