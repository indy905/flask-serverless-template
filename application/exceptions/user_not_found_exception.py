class UserNotFoundException(Exception):
    """
    User를 찾을 수 없을 경우 예외
    """
    status_code = 404

    def __init__(self, user, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = "'{0}' is not found. Check user name or id.".format(user)
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv
