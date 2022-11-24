import time
from functools import wraps


def timeit(**dkwargs):
    def decorator(function):
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = function(*args, **kwargs)
            duration = 1_000 * (time.perf_counter() - start)
            if "ret" in dkwargs and dkwargs["ret"] == "us":
                return duration * 1_000
            if "ret" in dkwargs and dkwargs["ret"] == "ms":
                return duration
            if "ret" in dkwargs and dkwargs["ret"] == "s":
                return duration / 1_000

            print(f"{function.__name__} [etime={duration:.3f}ms]")
            return result

        return wrapper

    return decorator
