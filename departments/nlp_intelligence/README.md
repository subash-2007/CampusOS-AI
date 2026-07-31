# Department 034: NLP Intelligence (`nlp_intelligence`)
Text classification, sentiment analysis, NER F1, embedding similarity, multilingual detection, and ROUGE-L summarization scoring. Generates NLP model upgrade recommendations.
## 10-Agent Architecture
Deterministic(7): TextClassificationMeterAgent, SentimentAnalysisAuditorAgent, NERMeterAgent, TextSimilarityMeterAgent, LanguageDetectionAuditorAgent, TextSummarizationMeterAgent, NLPCapabilityScorerAgent
Reasoning(2): StrategicNLPNarrativeAgent, NLPEnhancementPlannerAgent
Orchestrator(1): NLPIntelligenceOrchestratorAgent
