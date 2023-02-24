from logging import Formatter, getLogger, Logger, StreamHandler, DEBUG, INFO
import sys


# ref: https://hackers-high.com/python/logging-overview/
log_level = INFO
handler = StreamHandler(sys.stdout)
handler.setLevel(log_level)
# fmt = Formatter(
#     "%(asctime)s - %(name)s - %(levelname)s - %(message)s", "%Y-%m-%dT%H:%M:%S"
# )
fmt = Formatter("%(message)s", "%Y-%m-%dT%H:%M:%S")
handler.setFormatter(fmt)


def create_logger(name: str, level: int = INFO) -> Logger:
    logger = getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    logger.propagate = False

    # if logger.hasHandlers():
    #     logger.handlers.clear()

    return logger
