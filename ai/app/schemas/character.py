from pydantic import BaseModel, Field
from typing import List

class CharacterSchema(BaseModel):
    """
    Structured definition of a character to ensure consistency across scenes.
    """
    id: str = Field(..., description="Stable unique identifier for the character, e.g., 'character_001'")
    name: str = Field(..., description="Name of the character")
    description: str = Field(..., description="Brief overview of the character's role")
    appearance: str = Field(..., description="Physical appearance details")
    clothing: str = Field(..., description="Default clothing or style")
    personality: str = Field(..., description="Personality traits and behavior")

class GenerateCharactersResponseSchema(BaseModel):
    """
    Response schema for character generation task.
    """
    task: str = Field("generate_characters", description="The task being performed")
    characters: List[CharacterSchema] = Field(..., description="List of characters generated")
