from functools import wraps
from time import time


def measure(func):
    "计算程序的运行时间"

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = int(round(time() * 1000))
        try:
            return func(*args, **kwargs)
        finally:
            end = int(round(time() * 1000)) - start
            print(f"Total execution time: {end if end > 0 else 0} ms")

    return wrapper
