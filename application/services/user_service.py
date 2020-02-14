from application.models.dtos.users.create_user_dto import CreateUserDto
from application.utility.logging_util import Logger


class UserService:
    def __init__(self):
        self.logger = Logger.get_logger(self)

    def get_user(self, user_id: str):
        pass

    def create_user(self, user_dto: CreateUserDto):
        pass

    def delete_user(self, user_id: str):
        pass