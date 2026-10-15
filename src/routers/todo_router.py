from fastapi import APIRouter, Response, status
from src.middleware.auth_middleware import CurrentUser, DbSession
from src.controllers import todo_controller
from src.dto.todo_dto import TodoCreateDTO, TodoUpdateDTO, TodoResponseDTO

router = APIRouter(prefix="/todos", tags=["todos"])

@router.post("/", response_model=TodoResponseDTO, status_code=status.HTTP_201_CREATED)
def create_todo(data: TodoCreateDTO, db: DbSession, user: CurrentUser):
    return todo_controller.create(db, user, data)

@router.get("/", response_model=list[TodoResponseDTO])
def list_todos(db: DbSession, user: CurrentUser):
    return todo_controller.list_all(db, user)

@router.get("/{todo_id}", response_model=TodoResponseDTO)
def get_todo(todo_id: int, db: DbSession, user: CurrentUser):
    return todo_controller.get_one(db, user, todo_id)

@router.put("/{todo_id}", response_model=TodoResponseDTO)
def update_todo(todo_id: int, data: TodoUpdateDTO, db: DbSession, user: CurrentUser):
    return todo_controller.update(db, user, todo_id, data)

@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: DbSession, user: CurrentUser):
    todo_controller.delete(db, user, todo_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
