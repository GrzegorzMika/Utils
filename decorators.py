from functools import wraps


def timer(function):
    import time

    @wraps(function)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time() - start
        print('{} ran in {} s'.format(function.__name__, end))
        return result

    return wrapper
