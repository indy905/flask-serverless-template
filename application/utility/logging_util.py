from functools import wraps
import logging

from application.common import CONSTANTS


def exception_logging(f):
    """
    try-except 구문으로 자동으로 예외를 잡아서 로깅한다.
    사용법 : 어노테이션 @exception_logging 형태로 메소드 위에 추가
    :param original_function: 원래 동작해야할 함수(어노테이션으로 자동 입력)
    :return:
    """
    logger = logging.getLogger("M:" + f.__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(CONSTANTS.LOGGING_FORMAT)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            if __debug__:
                logger.info("START: {}".format(f.__name__))

            result = f(*args, **kwargs)

            if __debug__:
                logger.info("END: {}".format(f.__name__))

            return result
        except Exception as e:
            if logger:
                logger.exception(e.__str__)
            raise

    return wrapper


class Logger(object):
    """
    공용으로 사용할 로깅 인스턴스를 반환해주는 클래스
    사용법 :
    def __init__(self):
        self.logger = Logger.get_logger(self)
        self.logger.info("message")
    """

    @staticmethod
    def get_logger(obj):
        """
        클래스를 넣어서 로깅 인스턴스를 생성하여 전달한다.
        :param obj: 클래스 객체
        :return: 로깅 인스턴스
        """
        logger = logging.getLogger("C:" + obj.__class__.__name__)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter(CONSTANTS.LOGGING_FORMAT)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
        return logger

    @staticmethod
    def get_default_logger(name: str):
        """
        기본 로깅 인스턴스를 생성하여 전달한다.
        :return: 로깅 인스턴스
        """
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter(CONSTANTS.LOGGING_FORMAT)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
        return logger
