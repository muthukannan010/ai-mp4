from pydantic import BaseModel, Field
from typing import Optional

class CharacterSchema(BaseModel):
    """
    Structured definition of a character to ensure consistency across scenes.
    """
    id: str = Field(..., description="Stable unique identifier for the character, e.g., 'character_001'")
    name: str = Field(..., description="Name of the character")
    description: str = Field(..., description="Brief overview of the character's role")
    appearance: str = Field(..., description="Physical appearance details")
    age: Optional[str] = Field(None, description="Approximate age")
    gender: Optional[str] = Field(None, description="Gender identity")
    clothing: str = Field(..., description="Default clothing or style")
    personality: str = Field(..., description="Personality traits and behavior")
