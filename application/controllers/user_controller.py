import json
from http import HTTPStatus

from flask import jsonify, Blueprint, make_response

from application.exceptions.already_user_exists_exception import AlreadyUserExistsException
from application.exceptions.form_validation_exception import FormValidationException
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
            or isinstance(error, UserNotFoundException) \
            or isinstance(error, FormValidationException):
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
    result = user_service.get_user(user_id=id)
    return make_response(json.dumps(result, ensure_ascii=False), 200)


@user_blueprint.route('/', methods=['POST'], endpoint='create_user')
@user_blueprint.route('', methods=['POST'], endpoint='create_user')
@extract_class_json(CreateUserDto)
def create_user(create_user_dto: CreateUserDto):
    """
    Create user
    :param create_user_dto:
    :return: user json
    """
    if not create_user_dto.validate():
        raise FormValidationException(create_user_dto.errors)
    result = user_service.create_user(create_user_dto)
    return make_response(json.dumps(result, ensure_ascii=False), 200)


@user_blueprint.route('/<id>/', methods=['DELETE'], endpoint='delete_user')
@user_blueprint.route('/<id>', methods=['DELETE'], endpoint='delete_user')
def delete_user(id: str):
    """
    Delete user
    :param id: user id
    :return: delete success (200 OK) or not
    """
    result = user_service.delete_user(user_id=id)
    return make_response(json.dumps(result, ensure_ascii=False), 200)
