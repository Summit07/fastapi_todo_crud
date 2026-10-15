# FastAPI Todo CRUD (SQLite + JWT + RBAC)

A layered FastAPI starter project. The router and controller communicate via DTOs (Data Transfer Objects), controllers map between DTOs and internal schemas, and services interact with database models using schemas. Clients never interact with the database schemas directly.

## Features
- SQLite database using SQLAlchemy
- JWT access tokens and password hashing
- Roles: `Admin`, `users`, `superadmin`
- Todo CRUD endpoints
- `users` can manage their own todos; `Admin` and `superadmin` can manage todos across users
- Optional bootstrap superadmin from environment variables
- Layered `src/` package: `dto` (API request/response contracts), `controllers` (orchestration & DTO-to-schema mapping), `services` (business logic & DB operations using schemas), `schemas` (internal DB operation schemas), `models` (SQLAlchemy ORM), `routers` (HTTP endpoints), `middleware`, `config`, `utils`, `helpers`

## 1. Create and activate a virtual environment

Python 3.10+ recommended.

```bash
python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows PowerShell
# .\venv\Scripts\Activate.ps1
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` and set a long random `JWT_SECRET_KEY`. To create a first superadmin automatically, set `BOOTSTRAP_SUPERADMIN_EMAIL` and `BOOTSTRAP_SUPERADMIN_PASSWORD` before the first run. Leave them blank if not needed.

## 3. Run the API

From the project root:

```bash
uvicorn src.main:app --reload
```

- Swagger UI: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/health

The SQLite file `todo.db` is created automatically in the project root.

## Authentication flow
1. `POST /api/v1/auth/register` creates a regular `users` account. Public registration cannot assign privileged roles.
2. `POST /api/v1/auth/login` returns a bearer access token.
3. In Swagger, click **Authorize** and enter the token (or `Bearer <token>` if prompted).
4. Send `Authorization: Bearer <token>` with protected requests.

## Endpoints

| Method | Path | Auth | Description |
|---|---|---|---|
| POST | `/api/v1/auth/register` | No | Register regular user |
| POST | `/api/v1/auth/login` | No | Login and get JWT |
| GET | `/api/v1/auth/me` | Yes | Current user |
| POST | `/api/v1/todos/` | Yes | Create todo |
| GET | `/api/v1/todos/` | Yes | List todos (own for `users`, all for Admin/superadmin) |
| GET | `/api/v1/todos/{todo_id}` | Yes | Get one todo, with role-based access |
| PUT | `/api/v1/todos/{todo_id}` | Yes | Update todo |
| DELETE | `/api/v1/todos/{todo_id}` | Yes | Delete todo |

Todo body example:
```json
{
  "title": "Learn FastAPI",
  "description": "Build a layered CRUD API",
  "completed": false
}
```

Registration body:
```json
{
  "email": "person@example.com",
  "password": "change-this-password"
}
```

Login uses the same email/password shape.

## Role notes
- Role strings are exactly `Admin`, `users`, and `superadmin`.
- New public registrations always receive `users`.
- Only a trusted operator should set privileged roles in the database or bootstrap the first superadmin.
- `Admin` and `superadmin` can view/update/delete any todo; regular users can access only their own.
- This is a learning starter, not a production-hardened identity system. Add migrations, refresh-token/revocation strategy, rate limits, and stronger operational controls before production.
