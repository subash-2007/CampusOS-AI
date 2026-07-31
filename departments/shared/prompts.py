from typing import Dict, Any

class PromptBuilder:
    """
    Structured prompt templates builder for LLM agent context synthesis.
    """
    @staticmethod
    def build_system_prompt(persona_role: str, domain_focus: str) -> str:
        return (
            f"You are an expert AI Agent operating as {persona_role}.\n"
            f"Your domain focus is: {domain_focus}.\n"
            "Provide rigorous, actionable, objective, and structured evaluation step by step. "
            "Return output strictly conforming to expected schema standards."
        )

    @staticmethod
    def build_user_context(inputs: Dict[str, Any], extra_context: str = "") -> str:
        formatted_inputs = "\n".join(f"- {k}: {v}" for k, v in inputs.items())
        context = f"=== TASK INPUT CONTEXT ===\n{formatted_inputs}\n"
        if extra_context:
            context += f"\n=== ADDITIONAL DOMAIN CONTEXT ===\n{extra_context}\n"
        return context
