from wtforms import StringField, validators, Form


class CreateUserDto(Form):
    id = StringField('id', [validators.DataRequired(), validators.Length(min=2, max=30, message='Id length 2 to 30.')])
    name = StringField('name', [validators.DataRequired()])
    role = StringField('role', [validators.DataRequired(),
                                validators.AnyOf(message='Role is one of ADMIN, READ, WRITE.',
                                                 values=['ADMIN', 'READ', 'WRITE'])])
