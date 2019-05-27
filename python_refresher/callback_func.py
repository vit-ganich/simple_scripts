"""Difference between lambda and callback functions.
A lambda is a function without a name.
A callback is a function that is called after something happens.
They are entirely different concepts.for example, a lambda can be used as acallback.

Here's an example of a callback:
"""


def add_two(x, y):
    print(x + y)


def do_something(callback):
    print("I'm doing stuff!")
    callback(10, 20)


do_something(add_two)


# Similarly, it could be a lambda function:


def do_something(callback):
    print("I'm doing stuff!")
    callback(10, 20)


do_something(lambda x, y: x + y)
