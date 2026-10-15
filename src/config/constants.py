from enum import Enum

class Role(str, Enum):
    ADMIN = "Admin"
    USER = "users"
    SUPERADMIN = "superadmin"

PRIVILEGED_ROLES = {Role.ADMIN.value, Role.SUPERADMIN.value}
