from fastapi import HTTPException, status
from src.config.constants import PRIVILEGED_ROLES
from src.models.user import User
from src.models.todo import Todo

def ensure_can_access_todo(user: User, todo: Todo) -> None:
    if user.role not in PRIVILEGED_ROLES and todo.owner_id != user.id:
        # 404 avoids revealing another user's todo exists.
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
