import functools


def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start decorating")
        value = func(*args, **kwargs)

        value *= 100
        print(f"After decorating: {value}")
        return value
    return wrapper


@decorator
def my_foo(value: int) -> int:
    print(f"Initial value: {value}")
    return value


def foo(x: int) -> int:
    return x * x
