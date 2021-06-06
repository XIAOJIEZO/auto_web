import logging
import time
import os


def logger():
    logger = logging.getLogger('logger')
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        if not os.path.exists("logs"): os.makedirs("logs")

        sh = logging.StreamHandler()
        fh = logging.FileHandler(filename='logs/' + time.strftime("%Y-%m-%d", time.localtime()) + '.log',
                                 encoding='utf8')
        # 日志输出格式
        formatter = logging.Formatter(
            fmt='{"time":"%(asctime)s", "level":"%(levelname)s", "func":"%(funcName)s", "line":"%(lineno)d", "msg":"%(message)s"}',
            datefmt="%Y-%m-%d %H:%M:%S")

        sh.setFormatter(formatter)
        fh.setFormatter(formatter)

        logger.addHandler(sh)
        logger.addHandler(fh)
    return logger
