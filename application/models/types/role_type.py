from enum import Enum


class RoleType(str, Enum):
    # 0: admin, 1: write, 2: read
    ADMIN = '0'
    WRITE = '1'
    READ = '2'
