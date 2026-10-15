from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from src.config.constants import PRIVILEGED_ROLES
from src.models.todo import Todo
from src.models.user import User
from src.schemas.todo_schema import TodoCreateSchema, TodoUpdateSchema, TodoSchema
from src.helpers.permissions import ensure_can_access_todo

def _get_todo_model(db: Session, user: User, todo_id: int) -> Todo:
    todo = db.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    ensure_can_access_todo(user, todo)
    return todo

def create_todo(db: Session, user: User, data: TodoCreateSchema) -> TodoSchema:
    todo = Todo(
        title=data.title,
        description=data.description,
        completed=data.completed,
        owner_id=user.id,
    )
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return TodoSchema.model_validate(todo)

def list_todos(db: Session, user: User) -> list[TodoSchema]:
    query = select(Todo).order_by(Todo.id.desc())
    if user.role not in PRIVILEGED_ROLES:
        query = query.where(Todo.owner_id == user.id)
    todos = list(db.scalars(query).all())
    return [TodoSchema.model_validate(todo) for todo in todos]

def get_todo(db: Session, user: User, todo_id: int) -> TodoSchema:
    todo = _get_todo_model(db, user, todo_id)
    return TodoSchema.model_validate(todo)

def update_todo(db: Session, user: User, todo_id: int, data: TodoUpdateSchema) -> TodoSchema:
    todo = _get_todo_model(db, user, todo_id)
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(todo, key, value)
    db.commit()
    db.refresh(todo)
    return TodoSchema.model_validate(todo)

def delete_todo(db: Session, user: User, todo_id: int) -> None:
    todo = _get_todo_model(db, user, todo_id)
    db.delete(todo)
    db.commit()
