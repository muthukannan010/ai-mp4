import sys
import os
from fastapi import APIRouter

# Temporarily add the root to sys.path to import from ai module
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
sys.path.append(project_root)

from ai.app.schemas.chat import ChatRequestSchema, ChatResponseSchema
from ai.app.models.gemini_provider import GeminiProvider

router = APIRouter()

# Initialize the Gemini provider (Assuming GEMINI_API_KEY is in environment)
try:
    llm_provider = GeminiProvider()
except ValueError as e:
    print(f"Warning: {e}")
    llm_provider = None

@router.post("/", response_model=ChatResponseSchema)
async def process_chat(request: ChatRequestSchema):
    if not llm_provider:
        return ChatResponseSchema(
            task=request.task,
            result={"reply": "Error: GEMINI_API_KEY is not configured in the backend's .env file."},
            error="API key missing"
        )
        
    system_prompt = (
        "You are CineAI Director, an expert AI assistant for a film studio application. "
        "Your job is to help the user brainstorm ideas, create storyboards, characters, and scenes. "
        "Always be helpful, creative, cinematic, and concise in your responses."
    )
    
    try:
        # Ask Gemini to generate a response to the user's prompt
        ai_reply = llm_provider.generate_text(prompt=request.message, system_prompt=system_prompt)
        
        return ChatResponseSchema(
            task=request.task,
            result={"reply": ai_reply},
            error=None
        )
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return ChatResponseSchema(
            task=request.task,
            result={},
            error=f"Failed to generate response: {str(e)}"
        )
