import json
from http import HTTPStatus

from flask import jsonify, Blueprint, make_response

from application.exceptions.already_user_exists_exception import AlreadyUserExistsException
from application.exceptions.user_not_found_exception import UserNotFoundException
from application.models.dtos.users.create_user_dto import CreateUserDto
from application.services.user_service import UserService
from application.utility.logging_util import Logger
from application.utility.extract_class_json import extract_class_json

user_blueprint = Blueprint('user', __name__, url_prefix='/user')
user_logger = Logger.get_default_logger('USER_CONTROLLER')
user_service = UserService()


@user_blueprint.errorhandler(Exception)
def exception_handler(error):
    """
    Common exception handler for this controller
    :param error: Exception
    :return: Common exception response
    """
    if isinstance(error, AlreadyUserExistsException) \
            or isinstance(error, UserNotFoundException):
        user_logger.error(error.to_dict())
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
    else:
        user_logger.error(str(error))
        response = jsonify({"message": str(error)})
        response.status_code = int(HTTPStatus.INTERNAL_SERVER_ERROR.value)
    return response


@user_blueprint.route('/<id>/', methods=['GET'], endpoint='get_user')
@user_blueprint.route('/<id>', methods=['GET'], endpoint='get_user')
def get_user(id: str):
    """
    Get user
    :param id: user id
    :return: user json
    """
    # TODO: get user
    return make_response(json.dumps({}, ensure_ascii=False), 200)


@user_blueprint.route('/', methods=['POST'], endpoint='create_user')
@user_blueprint.route('', methods=['POST'], endpoint='create_user')
@extract_class_json(CreateUserDto)
def create_user(create_user_dto: CreateUserDto):
    """
    Create user
    :param create_user_dto:
    :return: user json
    """
    # TODO: create user
    return make_response(json.dumps({}, ensure_ascii=False), 200)


@user_blueprint.route('/<id>/', methods=['DELETE'], endpoint='delete_user')
@user_blueprint.route('/<id>', methods=['DELETE'], endpoint='delete_user')
def delete_user(id: str):
    """
    Delete user
    :param id: user id
    :return: delete success (200 OK) or not
    """
    # TODO: delete user
    return make_response(json.dumps({}, ensure_ascii=False), 200)
