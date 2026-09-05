from pydantic import BaseModel, Field
from typing import List, Optional

class SceneSchema(BaseModel):
    """
    Structured definition of a single video scene.
    """
    id: str = Field(..., description="Stable unique identifier for the scene, e.g., 'scene_001'")
    title: str = Field(..., description="Title of the scene")
    duration: int = Field(..., description="Duration of the scene in seconds")
    description: str = Field(..., description="What happens in the scene")
    camera: str = Field(..., description="Camera angles, lens, and movement")
    lighting: str = Field(..., description="Lighting setup and mood")
    environment: str = Field(..., description="Setting and environment description")
    style: str = Field(..., description="Visual cinematic style")
    characters: List[str] = Field(default_factory=list, description="List of character IDs present in this scene")
    video_prompt: Optional[str] = Field(None, description="The final comprehensive cinematic video generation prompt")

class StoryboardSchema(BaseModel):
    """
    The full sequence of scenes making up the video.
    """
    scenes: List[SceneSchema] = Field(..., description="List of all scenes in chronological order")
