"""
로깅에 사용할 포맷
[2019-10-18 18:30:11,850][INFO][C:Class] - message
[2019-10-18 18:30:11,850][ERROR][M:Method] - message
"""
LOGGING_FORMAT = '[%(asctime)s][%(levelname)s][%(name)s] - %(message)s'
