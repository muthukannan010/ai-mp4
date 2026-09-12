from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class ChatRequestSchema(BaseModel):
    """
    Request payload sent from the frontend to the backend for chat interactions.
    """
    project_id: str = Field(..., description="ID of the current project")
    message: str = Field(..., description="User's natural language request")
    task: str = Field(..., description="Inferred or explicitly stated task type (e.g. 'modify_scene')")
    selected_scene_id: Optional[str] = Field(None, description="Currently selected scene ID context")
    selected_character_id: Optional[str] = Field(None, description="Currently selected character ID context")

class ChatResponseSchema(BaseModel):
    """
    Response payload sent from the backend to the frontend.
    """
    task: str = Field(..., description="The task that was executed")
    result: Dict[str, Any] = Field(..., description="The structured result data, payload depends on the task")
    error: Optional[str] = Field(None, description="Error message if the request failed")
