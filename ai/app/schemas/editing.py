from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class EditActionSchema(BaseModel):
    """
    Structured output for identifying user edits via natural language.
    E.g. User says "Make scene 3 more emotional"
    """
    task: str = Field(..., description="The task being performed, e.g. 'modify_scene'")
    action: str = Field(..., description="Type of action, e.g., 'modify_scene', 'modify_character'")
    scene_id: Optional[str] = Field(None, description="ID of the scene being modified (if applicable)")
    character_id: Optional[str] = Field(None, description="ID of the character being modified (if applicable)")
    changes: Dict[str, Any] = Field(..., description="Key-value pairs representing the specific fields that are changing")
    affected_scenes: List[str] = Field(default_factory=list, description="List of scene IDs that are indirectly affected by this change and need regeneration")
    requires_regeneration: bool = Field(True, description="Whether the affected scenes require re-generation of their video prompts")
    explanation: str = Field(..., description="Explanation of what was updated and why")
