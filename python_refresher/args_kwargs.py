def long_method(arg1, arg2, arg3, arg4, arg5):
    return arg1 + arg2 + arg3 + arg4 + arg5


def short_method(*args):
    return sum(args)


def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

what_are_kwargs(33, 55, "ddd")

what_are_kwargs(333, 444, name='Vitali', location='Minsk')
