import os
import json
from typing import Dict, Any, Optional
from pydantic import BaseModel

from google import genai
from google.genai import types

from ai.app.models.provider import LLMProvider

class GeminiProvider(LLMProvider):
    def __init__(self, api_key: str = None, model_name: str = "gemini-2.5-flash"):
        key = api_key or os.environ.get("GEMINI_API_KEY")
        if not key:
            raise ValueError("GEMINI_API_KEY environment variable is not set. Please set it in your .env file.")
        self.client = genai.Client(api_key=key)
        self.model_name = model_name

    def generate_structured(self, prompt: str, schema: Any, system_prompt: Optional[str] = None) -> Dict[str, Any]:
        """
        Generates a structured JSON response using the specified Pydantic schema.
        """
        config_kwargs = {
            "response_mime_type": "application/json",
            "response_schema": schema,
            "temperature": 0.7,
        }
        if system_prompt:
            config_kwargs["system_instruction"] = system_prompt
            
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
            config=types.GenerateContentConfig(**config_kwargs)
        )
        
        # Parse the returned JSON text string into a dictionary
        try:
            return json.loads(response.text)
        except json.JSONDecodeError:
            print("Failed to parse JSON response:", response.text)
            return {"error": "Failed to generate structured response."}

    def generate_text(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """
        Generates a standard text response.
        """
        config_kwargs = {}
        if system_prompt:
            config_kwargs["system_instruction"] = system_prompt
            
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
            config=types.GenerateContentConfig(**config_kwargs) if config_kwargs else None
        )
        return response.text
