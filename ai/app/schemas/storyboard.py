from pydantic import BaseModel, Field
from typing import List, Optional

class SceneSchema(BaseModel):
    """
    Structured definition of a single video scene.
    """
    id: str = Field(..., description="Stable unique identifier for the scene, e.g., 'scene_001'")
    scene_number: int = Field(..., description="Chronological number of the scene")
    title: str = Field(..., description="Title of the scene")
    duration: int = Field(..., description="Duration of the scene in seconds")
    description: str = Field(..., description="What happens in the scene")
    camera: str = Field(..., description="Camera angles, lens, and movement")
    lighting: str = Field(..., description="Lighting setup and mood")
    environment: str = Field(..., description="Setting and environment description")
    characters: List[str] = Field(default_factory=list, description="List of character IDs present in this scene")
    emotional_tone: Optional[str] = Field(None, description="The emotional tone of the scene")
    video_prompt: Optional[str] = Field(None, description="The final comprehensive cinematic video generation prompt")

class StoryboardResponseSchema(BaseModel):
    """
    The full storyboard response from the LLM.
    """
    task: str = Field("generate_storyboard", description="The task being performed")
    title: str = Field(..., description="Title of the storyboard/video")
    duration: int = Field(..., description="Total duration in seconds")
    style: str = Field(..., description="Visual cinematic style")
    aspect_ratio: str = Field("16:9", description="Video aspect ratio")
    characters: List[dict] = Field(default_factory=list, description="Characters involved in this storyboard")
    scenes: List[SceneSchema] = Field(..., description="List of all scenes in chronological order")
