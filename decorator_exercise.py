# Author: Jose Angel Garcia Gomez
# Date: 17-04-2023
# Description: Decorator exercise


from typing import Callable


def star(func: Callable) -> Callable:
    """A decorator that prints 15 * before and after the function call"""
    # TODO(students): implement this function
    def inner(*args):
        print("***************")
        func(*args)
        print("***************")
    return inner


def reverse_first_arg_string(func: Callable) -> Callable:
    """A decorator that reverses the first argument of the function call"""
    # TODO(students): implement this function
    def inner(msg1, *args):
        msg1 = msg1[::-1]
        func(msg1, *args)
    return inner


@star
@reverse_first_arg_string
def printer(*args):
    print(*args)


if __name__ == '__main__':
    printer("i love python", "1234", "abcd")
"""
Desired Behavior:

INPUT:
printer("i love python", "1234", "abcd")

OUTPUT:
***************
nohtyp evol i 1234
***************

"""
