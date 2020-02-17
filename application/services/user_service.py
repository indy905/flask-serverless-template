from pynamodb.exceptions import DoesNotExist

from application.exceptions.already_user_exists_exception import AlreadyUserExistsException
from application.exceptions.user_not_found_exception import UserNotFoundException
from application.models.dao.users.user_model import UserModel
from application.models.dtos.users.create_user_dto import CreateUserDto
from application.models.types.role_type import RoleType
from application.utility.logging_util import Logger


class UserService:
    def __init__(self):
        self.logger = Logger.get_logger(self)

    def get_user(self, user_id: str):
        try:
            user = UserModel.get(user_id)
        except DoesNotExist as e:
            raise UserNotFoundException(user_id)
        else:
            return user.to_dict()

    def create_user(self, user_dto: CreateUserDto):
        try:
            user = UserModel.get(user_dto.id.data)
        except DoesNotExist as e:
            create_user = UserModel(id=user_dto.id.data, name=user_dto.name.data, role=RoleType(user_dto.role.data))
            create_user.save()
            return create_user.to_dict()
        else:
            raise AlreadyUserExistsException(user_dto.id)

    def delete_user(self, user_id: str):
        try:
            user = UserModel.get(user_id)
        except DoesNotExist as e:
            raise UserNotFoundException(user_id)
        else:
            return user.delete()

