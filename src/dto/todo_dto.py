from pydantic import BaseModel, Field, ConfigDict

class TodoCreateDTO(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str | None = None
    completed: bool = False

class TodoUpdateDTO(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    description: str | None = None
    completed: bool | None = None

class TodoResponseDTO(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: bool
    owner_id: int
    model_config = ConfigDict(from_attributes=True)

# Aliases for backward compatibility
TodoCreate = TodoCreateDTO
TodoUpdate = TodoUpdateDTO
TodoResponse = TodoResponseDTO

