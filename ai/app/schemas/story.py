from pydantic import BaseModel, Field

class StorySchema(BaseModel):
    """
    Structured definition of the video's narrative and overall concept.
    """
    concept: str = Field(..., description="High-level concept or logline of the video")
    beginning: str = Field(..., description="Description of how the story begins")
    middle: str = Field(..., description="Description of the main conflict or action in the middle")
    ending: str = Field(..., description="Description of how the story concludes")
    setting: str = Field(..., description="The main setting or world where the story takes place")
    tone: str = Field(..., description="The emotional tone or mood of the story")

class GenerateStoryResponseSchema(BaseModel):
    """
    Response schema for story generation task.
    """
    task: str = Field("generate_story", description="The task being performed")
    story: StorySchema = Field(..., description="The generated story details")
