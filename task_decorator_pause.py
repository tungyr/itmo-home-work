import time
from functools import wraps


def pause(second):
    def decorator(print_func):
        @wraps(print_func)
        def wrapper(*args, **kwargs):
            time.sleep(second)
            return print_func()
        return wrapper
    return decorator


@pause(2)
def print_func():
    print('Функция выполняется с задержкой 2 секунды!')
