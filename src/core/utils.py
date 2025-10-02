from functools import wraps
from logging import Logger

import time
import logging as lg
import sys
import re


def setup_logger(name: str, level: int) -> lg.Logger:
    logger = lg.getLogger(name)
    logger.setLevel(level)

    formatter = lg.Formatter("[{levelname} - {name}]: {message}", style="{")
    stream_handler = lg.StreamHandler(stream=sys.stdout)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger


def infowrapper(logger: Logger):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            name = func.__name__
            start_time = time.time()

            logger.debug(f"Function {name} been started at {start_time:.4f}")

            result = func(*args, **kwargs)
            end_time = time.time()

            elapsed = end_time - start_time

            logger.debug(
                f"Func {name} finished at {end_time:.4f}. Elapsed: {elapsed:.4f}s"
            )

            return result

        return wrapper

    return decorator


def printf(string: str, end="\n") -> None:
    sys.stdout.write(string + end)
    sys.stdout.flush()


def touch(path: str) -> None:
    with open(path, mode="w", encoding="utf-8") as file:
        pass


def validate_semver(semver: str) -> bool:
    semver_pattern = re.compile(
        r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
        r"(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?"
        r"(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
    )

    return re.match(semver_pattern, semver) is not None
