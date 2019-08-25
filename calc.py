import functools as ft


def add(*args):
    """Adding list of values"""
    return sum(args)


def mul(*args):
    return ft.reduce(lambda a, b: a*b, args)


def div(x, y):
    return x // y


def sub(x, y):
    return x - y


print(add(1, 2, 4))
print(sub(75, 90))
print(mul(1, 2, 4))
