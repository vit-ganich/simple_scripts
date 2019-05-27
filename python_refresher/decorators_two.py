import functools


def my_decorator(func):
    @functools.wraps(func)
    def wrapper():
        print("Start decorating")
        func()
        print("Finish decorating")
    return wrapper


@my_decorator
def my_func():
    print("I'm a function")


my_func()

##


def decorator_with_args(flag):
    def my_inner_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("In the decprator")
            if flag:
                print("Runnung func")
                func(*args, **kwargs)
            else:
                print("Nor running flag")
            print("After")
        return wrapper
    return my_inner_decorator


@decorator_with_args(False)
def my_func_two():
    print("Hello")

my_func_two()


def decorator_with_foo_parameters(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("I'm a decorator")
        return func(*args, **kwargs)
    return wrapper


@decorator_with_foo_parameters
def my_new_foo(x, y):
    print("I'm a foo")
    return x * y


y = my_new_foo(100, 0.1)
print(y)

