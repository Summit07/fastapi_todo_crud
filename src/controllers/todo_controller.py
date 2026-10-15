from sqlalchemy.orm import Session
from src.dto.todo_dto import TodoCreateDTO, TodoUpdateDTO, TodoResponseDTO
from src.models.user import User
from src.schemas.todo_schema import TodoCreateSchema, TodoUpdateSchema
from src.services import todo_service

def create(db: Session, user: User, data: TodoCreateDTO) -> TodoResponseDTO:
    schema = TodoCreateSchema(**data.model_dump())
    todo_schema = todo_service.create_todo(db, user, schema)
    return TodoResponseDTO.model_validate(todo_schema)

def list_all(db: Session, user: User) -> list[TodoResponseDTO]:
    todo_schemas = todo_service.list_todos(db, user)
    return [TodoResponseDTO.model_validate(item) for item in todo_schemas]

def get_one(db: Session, user: User, todo_id: int) -> TodoResponseDTO:
    todo_schema = todo_service.get_todo(db, user, todo_id)
    return TodoResponseDTO.model_validate(todo_schema)

def update(db: Session, user: User, todo_id: int, data: TodoUpdateDTO) -> TodoResponseDTO:
    schema = TodoUpdateSchema(**data.model_dump(exclude_unset=True))
    todo_schema = todo_service.update_todo(db, user, todo_id, schema)
    return TodoResponseDTO.model_validate(todo_schema)

def delete(db: Session, user: User, todo_id: int) -> None:
    todo_service.delete_todo(db, user, todo_id)
