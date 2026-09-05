from abc import ABC, abstractmethod
from typing import Dict, Any, Optional

class LLMProvider(ABC):
    """
    Abstract base class for LLM providers (e.g., local vLLM, OpenAI, Hugging Face).
    Ensures the AI system is not tightly coupled to a single model.
    """
    
    @abstractmethod
    def generate_structured(self, prompt: str, schema: Any, system_prompt: Optional[str] = None) -> Dict[str, Any]:
        """
        Generate a structured JSON output conforming to the provided Pydantic schema.
        """
        pass

    @abstractmethod
    def generate_text(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """
        Generate free-form text.
        """
        pass
