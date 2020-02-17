from enum import Enum


class RoleType(str, Enum):
    ADMIN = 'ADMIN'
    WRITE = 'WRITE'
    READ = 'READ'
