from collections import namedtuple
from functools import wraps


def return_namedtuple(*items):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(items, tuple):
                Ntuple = namedtuple(func.__name__, items)
                n_tuple = Ntuple(*result)
                return n_tuple
            return result
        return wrapper
    return decorator
