from flask import request

from application.utility.logging_util import Logger

logger = Logger.get_default_logger('request_input_converter')


def extract_class_json(class_):
    def wrap(f):
        def decorator(*args, **kwargs):
            try:
                obj = class_(**request.get_json(force=True))
            except TypeError as e:
                raise e
            else:
                return f(obj, *args, **kwargs)
        return decorator
    return wrap
