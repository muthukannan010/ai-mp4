from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class EditActionSchema(BaseModel):
    """
    Structured output for identifying user edits via natural language.
    E.g. User says "Make scene 3 more emotional"
    """
    action: str = Field(..., description="Type of action, e.g., 'modify_scene', 'modify_character', 'add_scene'")
    target_id: Optional[str] = Field(None, description="ID of the scene or character being modified (if applicable)")
    changes: Dict[str, Any] = Field(..., description="Key-value pairs representing the specific fields that are changing")
    affected_scenes: List[str] = Field(default_factory=list, description="List of scene IDs that are indirectly affected by this change and need regeneration")
    regenerate: bool = Field(True, description="Whether the affected scenes require re-generation of their video prompts")
