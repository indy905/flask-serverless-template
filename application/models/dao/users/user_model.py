import os

from pynamodb.attributes import UnicodeAttribute

from application.models.dao.base.base_model import BaseModel
from application.models.types.role_type import RoleType
from application.models.types.enum_unicode_attribute import EnumUnicodeAttribute

USER_TABLE_NAME = os.getenv('USER_TABLE', 'flask-serverless-user-dev')


class UserModel(BaseModel):
    class Meta:
        table_name = USER_TABLE_NAME
        region = 'ap-northeast-2'
        abstract = False

    id = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute(null=True)
    role = EnumUnicodeAttribute(RoleType, null=True)
