import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    ENV = 'development'
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    """
    개발 환경 관련 변수
    """
    ENV = 'development'
    DEBUG = True
    TESTING = True


class StagingConfig(Config):
    """
    Staging 관련 환경 변수
    """
    ENV = 'staging'
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    """
    Production 관련 환경 변수
    """
    ENV = 'production'
    DEBUG = False
    TESTING = False


config_by_name = dict(
    dev=DevelopmentConfig,
    staging=StagingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
