from pydantic import BaseModel, Field, ConfigDict

class TodoCreateSchema(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str | None = None
    completed: bool = False
    owner_id: int | None = None

class TodoUpdateSchema(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    description: str | None = None
    completed: bool | None = None

class TodoSchema(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: bool
    owner_id: int
    model_config = ConfigDict(from_attributes=True)

# Aliases
TodoInDBSchema = TodoSchema
TodoResponseSchema = TodoSchema
