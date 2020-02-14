class AlreadyUserExistsException(Exception):
    """
    User가 이미 존재할 경우 예외
    """
    status_code = 403

    def __init__(self, user, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = "'{0}' is already exists.".format(user)
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv
